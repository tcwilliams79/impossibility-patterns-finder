# IPF Catalog v1.0 - Seed Entries

## Overview

This directory contains the seed catalog for the Impossibility Patterns Finder (IPF) project, consisting of 11 validated entries spanning multiple scientific domains.

**Catalog Version:** 1.0  
**Schema Version:** 1.0  
**Publication Date:** 2025-10-19  
**Author:** Thomas C. Williams  
**License:** 
Schema & tools: MIT (see Section A in LICENSE)
Catalog & docs: CC BY 4.0 (see Section B in LICENSE)
**DOI:** [To be assigned]

## Contents

### Atomic Limits (10 entries)

Foundational impossibility results from single domains:

| ID | Title | Domain | Mechanism | Evidence |
|----|-------|--------|-----------|----------|
| IPF-00001 | Halting Problem | Computation | S | Theorem |
| IPF-00002 | Rice's Theorem | Computation | S | Theorem |
| IPF-00003 | No-Free-Lunch (Optimization) | Optimization/ML | C | Theorem |
| IPF-00004 | No-Free-Lunch (Learning) | ML/Statistics | C | Theorem |
| IPF-00005 | No-Cloning Theorem | Quantum Mechanics | C | Theorem |
| IPF-00006 | Heisenberg Uncertainty | Quantum Mechanics | C | Principle |
| IPF-00007 | Second Law (Entropy) | Thermodynamics | R | Law |
| IPF-00008 | Arrow's Impossibility | Social Choice | C | Theorem |
| IPF-00009 | Bias-Variance Tradeoff | ML/Statistics | R | Principle |
| IPF-00010 | Shannon Capacity | Information Theory | R | Theorem |

### Compound Limits (1 entry)

Cross-domain synthesis demonstrating advanced schema features:

| ID | Title | Domains | Mechanism | Evidence |
|----|-------|---------|-----------|----------|
| IPF-00011 | Coordination-Incentive-Trust Trilemma | Distributed Systems, Mechanism Design, Blockchain | C | Principle |

## Mechanism Distribution

The seed catalog demonstrates balanced coverage of the SCR taxonomy:

- **S (Self-reference):** 2 entries (20%)
- **C (Context/Incompatibility):** 6 entries (55%)
- **R (Resource/Monotonicity):** 3 entries (25%)

This distribution reflects that context incompatibilities are common across domains, while self-reference limits are primarily computational/logical, and resource limits span physical and information-theoretic domains.

## Validation

All entries have been validated against the IPF Schema v1.0 specification:

```bash
# Python validation
python validate.py IPF-00001.json
# Output: ✓ IPF-00001.json is valid

# Validate entire catalog
python validate.py *.json
```

## Quality Metrics

Each entry includes:

- ✓ Formal mathematical/logical statement
- ✓ Plain language explanation
- ✓ Explicit assumptions
- ✓ ≥2 typed escape hatches with SCR classification
- ✓ Academic references with full citations
- ✓ Typical traps (common misconceptions)
- ✓ Test procedure for conflict detection
- ✓ Related limits for cross-referencing

## Usage Examples

### API Integration

```python
import json

# Load a catalog entry
with open('IPF-00001.json') as f:
    halting_problem = json.load(f)

# Access structured data
print(halting_problem['title'])
print(halting_problem['mechanism'])  # 'S'
print(halting_problem['plain_language'])

# Iterate through escape hatches
for hatch in halting_problem['escape_hatches']:
    print(f"{hatch['type']}: {hatch['description']}")
```

### Barrier Check Example

```python
# Claim: "Perfect static analyzer for all Python programs"
claim = {
    "domains": ["Computation", "Programs"],
    "requires": ["Total correctness", "All programs"]
}

# Check against catalog
conflicts = check_barriers(claim, catalog=['IPF-00001.json', 'IPF-00002.json'])
# Returns: [IPF-00001 (Halting), IPF-00002 (Rice's theorem)]
```

## File Organization

```
catalog/
├── atomic/
│   ├── IPF-00001.json  # Halting Problem
│   ├── IPF-00002.json  # Rice's Theorem
│   ├── IPF-00003.json  # No-Free-Lunch (Optimization)
│   ├── IPF-00004.json  # No-Free-Lunch (Learning)
│   ├── IPF-00005.json  # No-Cloning Theorem
│   ├── IPF-00006.json  # Heisenberg Uncertainty
│   ├── IPF-00007.json  # Second Law
│   ├── IPF-00008.json  # Arrow's Impossibility
│   ├── IPF-00009.json  # Bias-Variance Tradeoff
│   └── IPF-00010.json  # Shannon Capacity
└── compound/
    └── IPF-00011.json  # Coordination-Incentive-Trust Trilemma
```

## Extending the Catalog

To contribute new entries:

1. **Follow the schema:** Validate against `ipf-schema-v1.0.json`
2. **Provide evidence:** Include academic references
3. **Type relaxations:** Use SCR mechanism types consistently
4. **Peer review:** Have ≥1 domain expert review before submission
5. **Submit PR:** Include entry JSON + validation results

See [CONTRIBUTING.md] for detailed guidelines.

## Key Design Decisions

### Why These 11?

The seed catalog was selected to:

1. **Span disciplines:** Computation, physics, statistics, economics, information theory
2. **Cover SCR spectrum:** Examples of S, C, and R mechanisms
3. **Mix evidence grades:** Theorems, laws, principles
4. **Show schema features:** Both atomic and compound entries
5. **Prove practical value:** Well-known results that appear in real research

### Structured Escape Hatches

Each entry provides typed relaxations showing:

- **What to change:** Self-reference structure, context, or resources
- **How to change it:** Concrete examples
- **Cost of change:** Trade-offs explicitly stated

This transforms "impossible" into "here's what you'd need to relax."

### Cross-Domain Synthesis

IPF-00011 demonstrates how the schema handles:

- Compound limits synthesized from multiple results
- Cross-domain manifestations (blockchain, auctions, databases)
- Graded references (foundational vs. illustrative)
- Evidence basis explaining the synthesis

## Citation

To cite the catalog:

**Individual Entry:**
```
Williams, Thomas C. 2025. "IPF-00001: Halting Problem (Undecidability)." 
Impossibility Patterns Finder Catalog v1.0. Zenodo. [DOI]
```

**Entire Catalog:**
```
Williams, Thomas C. 2025. Impossibility Patterns Finder Catalog v1.0. 
Zenodo. [DOI]
```

## References

- **Concept Note:** Williams (2025). IPF: A reliability layer for AI-assisted research. DOI: 10.5281/zenodo.17388374
- **Schema Specification:** Williams (2025). IPF Schema v1.0. [DOI]
- **SCR Taxonomy:** Williams (2025). Structural Mechanisms of Theoretical Limits. DOI: 10.5281/zenodo.17083195

## License

<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a>

This catalog is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.

You are free to:
- **Share** — copy and redistribute the material
- **Adapt** — remix, transform, and build upon the material

Under the following terms:
- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made.

## Contact

For questions, contributions, or collaborations:
- **Email:** [Your professional email]
- **GitHub:** [Repository URL]
- **Project Page:** https://impossibility-patterns-finder.org

---

**Version History:**
- v1.0 (2025-10-19): Initial seed catalog with 11 entries