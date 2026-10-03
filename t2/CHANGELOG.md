# T2 Changelog

All meaningful changes to the T2 protocol, execution specification, prompts, examples, and experimental infrastructure should be recorded here.

## v1.0 — Initial Frozen Baseline

### Protocol

```text
INPUT
→ MATERIAL
→ SCALE
→ DRIFT
→ ≌C
→ HYPOTHESIS
→ DIFFUSION
→ CONVERGENCE
```

### Included Concepts

- Material-centered exploration
- Material provenance
- Scale
- Drift
- Structural Correspondence (≌C)
- Chaos Margin
- Hypothesis branching
- Diffusion
- Convergence
- Residual retention
- Traceability
- Baseline / ablation methodology

### Repository Documentation

- T2 README
- T2 Design
- Repository Build Instructions
- Execution Protocol
- Experiment Protocol
- Glossary
- Results Ledger

## Versioning Policy

### Documentation-only changes
Corrections that do not change protocol semantics may be recorded without changing the protocol version.

### Minor changes
Changes to a defined operator, evaluation rule, or execution detail that preserve the overall architecture should receive a new minor version.

### Major changes
Changes to the architecture or canonical execution model should receive a new major version.

## Experimental Rule

Do not rewrite historical results when the protocol changes.

```text
T2 v1.0
   ↓
Experiment
   ↓
Results

T2 v1.1
   ↓
New Experiment
   ↓
New Results
```

This keeps protocol evolution distinguishable from experimental outcomes.
