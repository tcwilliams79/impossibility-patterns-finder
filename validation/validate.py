#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
import json, os, argparse, sys
from pathlib import Path
from datetime import date
from typing import Dict, Any, List
from jsonschema import Draft202012Validator

def looks_like_schema(doc: Any) -> bool:
    return isinstance(doc, dict) and "$schema" in doc and "properties" in doc

def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)

def gather_catalog_files(root: Path) -> List[Path]:
    files = []
    for p, dirs, fnames in os.walk(root):
        # never descend into a folder literally named 'schema'
        if os.path.basename(p).lower() == "schema":
            continue
        for fn in fnames:
            if fn.lower().endswith(".json"):
                files.append(Path(p) / fn)
    return sorted(files)

def validate_dates(entry):
    issues = []
    for fld in ("date_added", "last_reviewed"):
        if fld in entry:
            val = entry[fld]
            if not isinstance(val, str):
                issues.append(f"{fld} must be YYYY-MM-DD (string)")
                continue
            try:
                date.fromisoformat(val)
            except Exception:
                issues.append(f"{fld} not in YYYY-MM-DD format: {val}")
    return issues

def escape_hatch_mechanisms(entry):
    eh = entry.get("escape_hatches", [])
    if not isinstance(eh, list):
        return ["escape_hatches must be a list"]
    kinds = set()
    for item in eh:
        if isinstance(item, dict):
            kinds.add(item.get("kind") or item.get("type") or "unknown")
    issues = []
    if len(kinds) == 1 and len(eh) > 1:
        issues.append("All escape_hatches use same kind/type; consider diversity")
    return issues

def validate_quality(entry):
    issues = []
    q = entry.get("quality")
    if not isinstance(q, dict):
        return issues
    for fld in ("precision_target","recall_target","false_alarm_target"):
        if fld in q:
            v = q[fld]
            if not isinstance(v, (int, float)) or not (0.0 <= v <= 1.0):
                issues.append(f"quality.{fld} must be a number in [0,1]")
    return issues

def main():
    ap = argparse.ArgumentParser(description="Validate IPF catalog entries against schema")
    ap.add_argument("--schema", default="schema/ipf-schema-v1.0.json", help="Path to JSON Schema (default: schema/ipf-schema-v1.0.json)")
    ap.add_argument("--catalog", default="catalog", help="Path to catalog root (default: catalog)")
    ap.add_argument("--strict", action="store_true", help="Enable extra checks (dates, escape hatch diversity, quality bounds)")
    ap.add_argument("--json", action="store_true", help="Emit JSON summary to stdout (CI-friendly)")
    args = ap.parse_args()

    schema_path = Path(args.schema)
    if not schema_path.exists():
        # try common fallbacks without changing your structure
        for cand in [Path("ipf-schema-v1.0.json"), Path("../schema/ipf-schema-v1.0.json")]:
            if cand.exists():
                schema_path = cand
                break
    if not schema_path.exists():
        print(f"Schema not found: {args.schema}", file=sys.stderr)
        sys.exit(2)

    catalog_root = Path(args.catalog)
    if not catalog_root.exists():
        print(f"Catalog path not found: {args.catalog}", file=sys.stderr)
        sys.exit(2)

    with open(schema_path, "r", encoding="utf-8") as f:
        schema = json.load(f)
    validator = Draft202012Validator(schema)

    files = gather_catalog_files(catalog_root)
    total = 0
    invalid = 0
    results = []

    for path in files:
        try:
            with open(path, "r", encoding="utf-8") as f:
                doc = json.load(f)
        except Exception as e:
            invalid += 1
            total += 1
            results.append({"file": str(path), "valid": False, "errors": [f"JSON parse error: {e}"]})
            continue

        # Skip JSON Schema docs if they slipped into catalog
        if looks_like_schema(doc):
            # silently skip; it's not a catalog entry
            continue

        total += 1
        errs = [f"[{('/'.join(map(str,e.path)) or '(root)')}] {e.message}" for e in validator.iter_errors(doc)]

        if args.strict:
            errs.extend(validate_dates(doc))
            errs.extend(escape_hatch_mechanisms(doc))
            errs.extend(validate_quality(doc))
            lic = doc.get("_license")
            if lic != "CC-BY-4.0":
                errs.append("license must be 'CC-BY-4.0' for catalog entries")

        valid = len(errs) == 0
        if not valid:
            invalid += 1
        results.append({"file": str(path), "valid": valid, "errors": errs})

    summary = {"checked": total, "invalid": invalid, "valid": total - invalid, "results": results}

    if args.json:
        print(json.dumps(summary, indent=2))
    else:
        for r in results:
            status = "✅ VALID" if r["valid"] else "❌ INVALID"
            print(f"{status}  {r['file']}")
            if r["errors"]:
                for emsg in r["errors"]:
                    print(f"  - {emsg}")
        print(f"\nSummary: {summary['valid']} valid / {summary['checked']} checked; {summary['invalid']} invalid")

    sys.exit(0 if invalid == 0 else 1)

if __name__ == "__main__":
    main()
