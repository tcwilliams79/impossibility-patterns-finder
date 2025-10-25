# Contributing to the IPF Catalog

Thanks for helping grow the **Impossibility Patterns Finder (IPF)** catalog. This guide shows how to add a new entry and keep the repository consistent and valid.

## 1) What makes a good IPF entry?

Every entry should clearly state:
- **The limit** (formal statement) and a **plain-language** explanation
- **Assumptions** under which the limit holds
- At least one **typed escape hatch** explaining how the limit can be relaxed (and the **limitations** of that relaxation)
- **Primary evidence** (paper, book, official source; include DOI/URL)
- Optional: **typical traps**, **test procedure**, **related limits**, **tags**

Mechanism taxonomy (**S/C/R**) referenced in the README:
- **S** — *Self-reference / diagonalization*
- **C** — *Context / incompatibility*
- **R** — *Resource / monotonicity*
(Choose one that best characterizes the limit.)

## 2) Where to put files

- **Atomic limits:** `catalog/atomic/` (single-domain results, e.g., Halting Problem)
- **Compound limits:** `catalog/compound/` (cross-domain/trilemma-style)
- **Examples (templates):** `examples/` (e.g., `examples/minimal.json`)
- The JSON Schema lives at `schema/ipf-schema-v1.0.json`.

## 3) Create your entry (start from the template)

Copy the minimal template:

**macOS/Linux**

cp examples/minimal.json catalog/atomic/IPF-XXXXX.json

**Windows**

copy examples/minimal.json catalog/atomic/IPF-XXXXX.json

Fill in fields (use your own id, title, etc.). Keep domains specific (e.g., ["Information Theory"], ["Thermodynamics"]).

Field tips

id: Use a stable identifier (e.g., IPF-00012). If unsure, use a placeholder and we’ll renumber on merge.

mechanism: one of S, C, R.

escape_hatches[]: Include type, description, and limitations.

evidence[]: Prefer primary sources with DOI (type: "paper"). Add reputable secondary reviews as needed.

## 4) Validate locally

### Single file (original script):

**macOS/Linux**
python validation/validate.py catalog/atomic/IPF-XXXXX.json

**Windows**
python validation\validate.py catalog\atomic\IPF-XXXXX.json

Validate all (cross-platform runner):

**macOS/Linux**
python validation/validate_all.py --schema schema/ipf-schema-v1.0.json --dirs catalog examples

**Windows**
python validation\validate_all.py --schema schema\ipf-schema-v1.0.json --dirs catalog examples

You should see:

✓ All JSON documents validate against IPF Schema

## 5) Open a PR

Include in your PR:

The new JSON file under catalog/atomic or catalog/compound

A one-paragraph rationale (why this belongs; edge cases considered)

Any discussion about tricky choices (assumptions, mechanism type)

## 6) Review checklist (maintainers use this too)
- Clear formal and plain-language statements
- Explicit assumptions
- At least one escape hatch with limitations
- Mechanism ∈ {S, C, R}
- Primary evidence (DOI/URL) present; optional secondary sources
- Passes schema validation
- Reasonable domains and tags
- Cross-refs in related_limits if applicable

## 7) Style & licensing

JSON is UTF-8, 2-space indents, keys in snake_case where applicable.

Keep descriptions concise (plain-language ≤ 3 sentences).

Licensing: Code/schema under MIT; catalog/docs under CC BY 4.0. See LICENSE.

## 8) Questions?

Open an Issue or start a discussion in the repo. Thanks for contributing!
