#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# validation/validate.py — strict validator for IPF Schema v1.0
import argparse, json, sys, glob
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

def _collect(paths):
    files = []
    for p in paths:
        path = Path(p)
        if path.is_dir():
            files += [str(f) for f in path.rglob("*.json")]
        else:
            files += glob.glob(str(path))
    return sorted(set(files))

def main():
    ap = argparse.ArgumentParser(description="Validate IPF JSON against the schema.")
    ap.add_argument("targets", nargs="+", help="Files/dirs/globs (e.g., catalog examples/*.json)")
    ap.add_argument("--schema", default="schema/ipf-schema-v1.0.json", help="Path to JSON Schema")
    args = ap.parse_args()

    # Load & check schema
    try:
        with open(args.schema, "r", encoding="utf-8") as f:
            schema = json.load(f)
    except Exception as e:
        print(f"[SCHEMA ERROR] Failed to load schema: {args.schema}\n{e}", file=sys.stderr)
        return 2
    Draft202012Validator.check_schema(schema)
    validator = Draft202012Validator(schema, format_checker=FormatChecker())

    files = _collect(args.targets)
    if not files:
        print("[WARN] No JSON files matched the given targets.", file=sys.stderr)
        return 2

    bad = 0
    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                inst = json.load(f)
        except Exception as e:
            bad += 1
            print(f"[ERROR] {fp}: not valid JSON → {e}")
            continue

        errors = sorted(validator.iter_errors(inst), key=lambda e: e.path)
        if errors:
            bad += 1
            print(f"[FAIL] {fp}: {len(errors)} error(s)")
            for e in errors:
                loc = "$" + "".join([f"[{repr(p)}]" if isinstance(p,int) else f".{p}" for p in e.path])
                print(f"  - at {loc}: {e.message}")
                for sub in getattr(e, "context", []):
                    print(f"      ↳ {sub.message}")
        else:
            print(f"[OK] {fp}")

    if bad:
        print(f"\n{bad} file(s) failed validation.")
        return 1
    print("[OK] All files valid against IPF Schema")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
