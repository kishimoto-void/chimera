# T2 Execution Protocol

## Status

**Protocol:** T2  
**Baseline:** v1.0  
**Role:** LLM-First Execution Protocol  
**Status:** Research prototype / executable specification

This document defines **how an LLM executes T2**.

- `T2_DESIGN.md` explains why T2 is structured this way.
- `T2_EXECUTION.md` defines the execution sequence and state transitions.
- `prompts/T2_v1.0.md` is the LLM-facing execution prompt.

## 1. Core Execution Sequence

```text
INPUT
  ↓
MATERIAL
  ↓
SCALE
  ↓
DRIFT
  ↓
≌C
  ↓
HYPOTHESIS
  ↓
DIFFUSION
  ↓
CONVERGENCE
```

## 2. Execution Principles

1. Treat the problem as transformable Material.
2. Preserve provenance of generated Material where practical.
3. Make Scale explicit.
4. Treat Drift as controlled exploration rather than arbitrary noise.
5. Search for structural correspondence using ≌C.
6. Permit multiple hypotheses to coexist.
7. Expand the candidate space before contracting it.
8. Preserve useful residuals rather than silently discarding them.
9. Separate observation from unsupported certainty.
10. Do not prematurely collapse exploration into a single answer.

## 3. STATE 0 — INPUT

Receive the original problem without prematurely solving it.

Record:

```text
Problem ID
Problem text
Known constraints
Explicit requested output
Available external information
Execution budget
```

Distinguish explicitly given information, inferred information, external information, and assumptions.

## 4. STATE 1 — MATERIAL

Transform the input into structured exploratory Material.

A Material may contain entities, variables, relations, constraints, structures, invariants, differences, unknowns, and residuals.

Recommended provenance labels:

| Type | Meaning |
|---|---|
| `M_input` | Directly extracted from input |
| `M_external` | Introduced from external knowledge |
| `M_derived` | Produced by transformation or computation |
| `M_emergent` | Newly appearing during exploration |
| `M_residual` | Unresolved material retained for later exploration |

The LLM should not silently convert an inference into an input fact.

## 5. STATE 2 — SCALE

Scale changes the representation, granularity, or structural viewpoint of Material.

Examples:

```text
local → intermediate → global
geometric → algebraic → relational
object → relation → constraint
component → system
```

The LLM should state the current representation, selected Scale direction, transformation, preserved structure, altered structure, and newly visible structure.

## 6. STATE 3 — DRIFT

Drift deliberately perturbs the current exploration trajectory.

It should identify what is changed, what is preserved, why the perturbation is useful, and what alternative structure it exposes.

Drift is not defined as unrestricted randomness.

## 7. STATE 4 — ≌C STRUCTURAL COMPARISON

≌C compares Materials across structural transformations.

The purpose is not to establish identity.

The operational question is:

> Which structural relationships remain correspondable despite differences?

Possible categories:

```text
preserved
transferable
transformed
incompatible
residual
emergent
```

A comparison should record source, target, correspondence, difference, transferability, residual, and Chaos Margin where applicable.

## 8. CHAOS MARGIN PRINCIPLE

Chaos Margin represents an experimental tolerance for non-identical but potentially corresponding structures.

```text
wide margin
    ↓
more candidate correspondence
    ↓
exploration

narrow margin
    ↓
stricter structural filtering
    ↓
convergence
```

Chaos Margin is an experimental control concept, not an established mathematical constant or physical law.

## 9. STATE 5 — HYPOTHESIS

Generate candidate structural explanations from:

```text
Material
+ Scale
+ Drift
+ ≌C
```

Multiple hypotheses may coexist. Each should state its source Material, structural basis, relevant constraints, predicted implication, and unresolved uncertainty.

A hypothesis is not automatically an answer.

## 10. STATE 6 — DIFFUSION

Diffusion expands the current candidate space.

It may introduce alternative representations, correspondences, hypothesis branches, new Material, counterexamples, and boundary conditions.

The objective is exploration, not immediate selection.

## 11. STATE 7 — CONVERGENCE

Convergence contracts the candidate space using explicit criteria such as constraint compatibility, structural consistency, correspondence quality, hypothesis coherence, explanatory usefulness, residual size, stability across Scale, and traceability.

Distinguish:

```text
accepted
rejected
contradicted
unresolved
residual
```

Convergence does not necessarily mean selecting a single final answer.

## 12. STATE TRANSITION RECORD

Recommended trace:

```text
T2_STEP:
  state:
  operator:
  input_material:
  output_material:
  changes:
  invariants:
  hypotheses:
  residuals:
  provenance:
```

## 13. Premature Collapse

Avoid collapsing the exploration space before relevant alternatives, transformations, or residuals have been considered.

## 14. Final State

The final T2 state should distinguish:

```text
Final Hypothesis
Supporting Material
Rejected / Contradicted Material
Residual Material
Uncertainty
Trace
```

## 15. Research Boundary

T2 execution does not imply intrinsic LLM capability improvement, universal validity of structural correspondences, guaranteed improvement, distributed MAS equivalence, AGI, or established physical status for Chaos Margin.

## 16. Frozen v1.0 Contract

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

Changes to this order should be versioned rather than silently modifying v1.0.
