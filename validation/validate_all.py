import argparse, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator as V, exceptions as js_exc

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--schema", default="schema/ipf-schema-v1.0.json")
    p.add_argument("--dirs", nargs="+", default=["catalog", "examples"])
    args = p.parse_args()

    schema_path = Path(args.schema)
    with schema_path.open(encoding="utf-8") as f:
        schema = json.load(f)
    validator = V(schema)

    json_files = []
    for d in args.dirs:
        root = Path(d)
        if root.exists():
            json_files += list(root.rglob("*.json"))

    errors = 0
    for jf in sorted(json_files):
        try:
            with jf.open(encoding="utf-8") as f:
                inst = json.load(f)
            for e in validator.iter_errors(inst):
                errors += 1
                print(f"[FAIL] {jf}: {e.message}")
        except js_exc.SchemaError as se:
            print(f"[SCHEMA ERROR] {se}", file=sys.stderr)
            return 2
        except Exception as ex:
            errors += 1
            print(f"[ERROR] {jf}: {ex}", file=sys.stderr)

    if errors:
        print(f"\n{errors} validation error(s).")
        return 1
    print("[OK] All JSON documents validate against IPF Schema")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
