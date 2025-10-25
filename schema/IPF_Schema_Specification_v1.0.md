# IPF Schema Specification v1.0

## Metadata

**Title:** Impossibility Patterns Finder Catalog Entry Schema
**Version:** 1.0
**Date:** 2025-10-19
**Author:** Thomas C. Williams
**License:** CC BY 4.0
**DOI:** [To be assigned by Zenodo]
**Related Work:** Williams (2025) IPF Concept Note v0.1, DOI: 10.5281/zenodo.17388374

## Abstract

This document specifies the JSON Schema for Impossibility Patterns Finder (IPF) catalog entries. The schema enables machine-readable, versioned documentation of theoretical limits across scientific domains, with typed relaxations following the SCR (Self-reference, Context, Resource) taxonomy.

## 1. Overview

### 1.1 Purpose

The IPF schema standardizes how impossibility results are documented, enabling:

- **Machine validation** of catalog entries for consistency
- **API integration** for automated barrier checking
- **Community contributions** with quality control
- **Cross-domain discovery** through structured metadata
- **Versioned evolution** with backward compatibility

### 1.2 Design Principles

1. **Completeness**: All information needed to understand and apply a limit
2. **Precision**: Formal statements alongside plain language
3. **Actionability**: Typed escape hatches enable systematic workarounds
4. **Traceability**: References support academic rigor
5. **Extensibility**: Optional fields for compound limits and cross-domain patterns

## 2. Schema Structure

### 2.1 Required Fields

Every catalog entry MUST include:

| Field | Type | Description |
|-------|------|-------------|
| `limit_id` | string | Unique identifier (format: `IPF-00001`) |
| `title` | string | Human-readable name (3-200 chars) |
| `domain` | array[string] | Scientific domains (≥1 entry) |
| `mechanism` | enum | SCR classification: `S`, `C`, or `R` |
| `formal_statement` | string | Precise mathematical/logical statement |
| `plain_language` | string | Non-technical explanation |
| `assumptions_scope` | array[string] | Conditions under which limit holds |
| `evidence_grade` | enum | `Theorem`, `Law`, `Principle`, `Conjecture`, `Empirical Regularity` |
| `typical_traps` | array[string] | Common misconceptions |
| `escape_hatches` | array[object] | Typed relaxations (structured) |
| `test_or_check` | string | Procedure to detect conflicts |
| `references` | array | Citations (string or structured) |
| `related_limits` | array[string] | Connected impossibility results |
| `version` | string | Entry version (format: `1.0`) |
| `date_added` | date | ISO 8601 format |
| `last_reviewed` | date | ISO 8601 format |
| `status` | enum | `active`, `deprecated`, `under_review`, `draft` |

### 2.2 Optional Fields

For compound or cross-domain limits:

| Field | Type | Description |
|-------|------|-------------|
| `evidence_basis` | string | Synthesis explanation for compound limits |
| `synthesis_components` | array[object] | Component limits that combine |
| `cross_domain_manifestations` | array[object] | Domain-specific instances |
| `notes` | string | Additional commentary |

### 2.3 Structured Sub-Objects

#### 2.3.1 Escape Hatch Object

```json
{
  "type": "Context|Resource|Self-reference",
  "description": "How to relax the constraint",
  "examples": ["Example 1", "Example 2"],
  "trade_offs": "Costs of this approach"
}
```

**Validation Rules:**
- `type` MUST match an SCR mechanism
- `examples` array MUST have ≥1 entry
- All fields REQUIRED

#### 2.3.2 Structured Reference Object

For compound limits, use structured references:

```json
{
  "key": "Author-YYYY",
  "citation": "Full bibliographic citation",
  "relevance": "How this supports the limit",
  "strength": "foundational|supporting|illustrative"
}
```

**Grading:**
- `foundational`: Proves the core result
- `supporting`: Provides context or related theory
- `illustrative`: Shows practical manifestation

#### 2.3.3 Synthesis Component Object

```json
{
  "limit_id": "IPF-00001 or canonical name",
  "role": "How this contributes to compound limit",
  "mechanism": "S|C|R"
}
```

## 3. Validation Rules

### 3.1 Identifier Format

- `limit_id`: MUST match regex `^IPF-[0-9]{5}$`
- IDs MUST be unique within catalog
- Sequential numbering recommended but not required

### 3.2 Evidence Grade Constraints

If `evidence_grade` is `"Principle"`:
- `evidence_basis` field REQUIRED
- `synthesis_components` SHOULD have ≥1 entry

### 3.3 Reference Consistency

- For atomic limits: simple string citations acceptable
- For compound limits: structured references RECOMMENDED
- All citations MUST be verifiable

### 3.4 Cross-Domain Entries

If `cross_domain_manifestations` present:
- Each manifestation MUST specify `domain`, `instance`, `analysis`
- References SHOULD be provided for each manifestation

## 4. Versioning Protocol

### 4.1 Schema Versioning

Schema uses semantic versioning: `MAJOR.MINOR.PATCH`

- **MAJOR**: Breaking changes (backward incompatible)
- **MINOR**: New optional fields (backward compatible)
- **PATCH**: Documentation or validation refinements

Current version: **1.0**

### 4.2 Entry Versioning

Each catalog entry has independent version:

- Increment on any content change
- Track `last_reviewed` date
- Maintain change log in repository

### 4.3 Deprecation

To deprecate an entry:
1. Set `status` to `"deprecated"`
2. Add `notes` explaining reason
3. Reference replacement entry if applicable
4. Maintain for ≥2 schema major versions

## 5. Quality Standards

### 5.1 Acceptance Criteria

New entries MUST:
- [ ] Validate against JSON Schema
- [ ] Provide ≥1 academic reference
- [ ] Include ≥2 escape hatches
- [ ] Have plain language explanation understandable to educated non-specialists
- [ ] Pass peer review by ≥1 domain expert

### 5.2 Withhold Rules

From IPF Concept Note evaluation plan:
- Withhold catalog release if >2 mislabeled entries per 10-item audit
- Flag entries with precision <0.70 or false-alarm rate >20%

## 6. Extension Points

### 6.1 Custom Fields

Implementers MAY add custom fields with prefix `x_`:

```json
{
  "limit_id": "IPF-00001",
  "x_custom_metadata": "Implementation-specific data"
}
```

Schema validation will ignore `x_` prefixed fields.

### 6.2 Domain-Specific Schemas

Domains MAY define stricter schemas that:
- Require specific domain values
- Add validation for domain-specific terminology
- Extend escape hatch types

Contact maintainers to register domain schemas.

## 7. Usage Examples

### 7.1 Minimal Valid Entry (Atomic Limit)

```json
{
  "limit_id": "IPF-00001",
  "title": "Halting Problem",
  "domain": ["Computation"],
  "mechanism": "S",
  "formal_statement": "No total computable procedure decides...",
  "plain_language": "No algorithm can always tell if any program will finish.",
  "assumptions_scope": ["Turing-equivalent computation"],
  "evidence_grade": "Theorem",
  "typical_traps": ["Believing perfect static analysis exists"],
  "escape_hatches": [{
    "type": "Context",
    "description": "Restrict language",
    "examples": ["Finite-state languages"],
    "trade_offs": "Reduced expressiveness"
  }],
  "test_or_check": "Look for reduction from undecidable problem",
  "references": ["Turing (1936)"],
  "related_limits": ["Rice's theorem"],
  "version": "1.0",
  "date_added": "2025-10-18",
  "last_reviewed": "2025-10-18",
  "status": "active"
}
```

### 7.2 Compound Limit with Structured References

See IPF-00011 in Appendix B of concept note for complete example.

## 8. Implementation Guidelines

### 8.1 Validation Tools

Reference implementations:

**Python:**
```python
import jsonschema
import json

with open('ipf-schema-v1.0.json') as f:
    schema = json.load(f)

with open('entry.json') as f:
    entry = json.load(f)

jsonschema.validate(instance=entry, schema=schema)
```

**JavaScript/Node.js:**
```javascript
const Ajv = require('ajv');
const ajv = new Ajv();

const schema = require('./ipf-schema-v1.0.json');
const validate = ajv.compile(schema);

const entry = require('./entry.json');
const valid = validate(entry);
if (!valid) console.log(validate.errors);
```

### 8.2 Catalog Organization

Recommended repository structure:

```
ipf-catalog/
├── schema/
│   ├── v1.0/
│   │   ├── catalog-entry.json
│   │   └── documentation.md
├── catalog/
│   ├── atomic/
│   │   ├── IPF-00001.json
│   │   ├── IPF-00002.json
│   │   └── ...
│   └── compound/
│       └── IPF-00011.json
├── validation/
│   ├── validate.py
│   └── validate.js
└── README.md
```

## 9. Governance

### 9.1 Schema Evolution

Changes to schema follow this process:

1. **Proposal**: Open issue with rationale
2. **Discussion**: Community feedback (≥2 weeks)
3. **Draft**: Create test implementation
4. **Validation**: Test with ≥10 existing entries
5. **Publication**: New schema version + migration guide
6. **Announcement**: Notify catalog maintainers

### 9.2 Entry Contributions

Community contributions welcome:

1. Fork repository
2. Add entry following schema
3. Validate with provided tools
4. Submit pull request with:
   - Entry JSON file
   - Evidence of peer review
   - Test cases for /barrier-check

Maintainers review within 30 days.

## 10. References

- JSON Schema specification: https://json-schema.org/
- Williams (2025). IPF Concept Note. DOI: 10.5281/zenodo.17388374
- Williams (2025). SCR Taxonomy. DOI: 10.5281/zenodo.17083195

## Appendix A: Complete Schema

See separate file: `catalog-entry.json`

## Appendix B: Validation Test Suite

[To be developed: Suite of valid/invalid entries for testing validators]

---

**Suggested Citation:**

Williams, Thomas C. 2025. Impossibility Patterns Finder Schema Specification v1.0. Zenodo. [DOI]

**License:** This specification is licensed under CC BY 4.0. Implementation code examples may use Apache 2.0 or MIT licenses.

**Contact:** [Your professional contact - consider creating ipf@yourdomain.com]

**Last Updated:** 2025-10-19
