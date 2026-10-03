# T2 Design Specification

**Status:** Design Baseline / Frozen Candidate  
**Origin:** Tpc1.5 → T2  
**Purpose:** Define the current T2 structure independently from experimental results.

---

## 1. Scope

T2 is an **LLM-executable exploration protocol**, not a conventional AI agent or conventional software MAS.

The current baseline is:

```text
Human Problem
    ↓
Material
    ↓
Scale
    ↓
Drift
    ↓
Observation / Reasoning
    ↓
≌C
    ↓
Hypothesis Generation
    ↓
Diffusion
    ↓
Convergence
    ↓
Field Update
    ↓
Re-Diffusion
    ↓
Re-Convergence
    ↓
Final Hypothesis / Residual
```

The design concerns **exploration structure**, not a claim of intrinsic LLM capability improvement.

---

## 2. Design Position

T2 sits between:

```text
Prompt
Protocol
Pseudo-MAS
Code
Specification
```

- **Prompt:** execution interface to an LLM.
- **Protocol:** processing order, constraints, and state transitions.
- **Pseudo-MAS:** role separation and mutual observation inside one execution context.
- **Code:** mechanical processing and verification where appropriate.
- **Specification:** structural and semantic definition.

---

## 3. Core Design Hypothesis

T2 operationalizes the hypothesis that transforming a problem into explicit Material, then repeatedly transforming, comparing, diffusing, and converging that Material, may produce a different exploration space from direct answer generation.

This does **not** establish:

```text
T2 = smarter LLM
T2 = guaranteed performance improvement
```

---

## 4. State Model

A conceptual execution state is:

```text
State_t =
{
    material,
    scale,
    drift,
    observations,
    correspondences,
    hypotheses,
    field,
    residuals
}
```

The important requirement is that the exploration trajectory remain inspectable.

---

## 5. Material Model

Material is the central T2 object.

```text
Problem ≠ Material
Material ≠ Answer
```

Material is a structured intermediate representation that can itself be transformed, compared, diffused, and converged.

### Material classes

| Type | Meaning |
|---|---|
| `M_input` | Directly obtained from the input |
| `M_external` | Introduced from external / existing knowledge |
| `M_derived` | Produced by transformation or computation |
| `M_emergent` | Newly appearing during exploration |
| `M_residual` | Unresolved material remaining after convergence |

Material provenance should be preserved whenever practical.

---

## 6. Scale Operator

Scale transforms Material into another granularity, viewpoint, or structural representation.

```text
Scale(M, direction) → M'
```

Scale is not merely numerical resizing.

Possible transformations include:

```text
Local → Intermediate → Global
```

or:

```text
Geometric → Algebraic → Relational → Constraint
```

### Scale modes

**Human-directed**

```text
Human → Scale Direction → T2
```

**Problem-structural**

```text
Problem Structure → Candidate Scale Directions
```

**Cycle-derived**

```text
Previous Material
+ Previous Field
+ Previous Convergence
→ Next Scale Direction
```

Scale direction itself may become Material.

---

## 7. Drift Operator

Drift changes the current exploration trajectory.

```text
Drift(M, state) → M'
```

Drift is not defined as arbitrary random noise.

Its purpose is to permit:

- alternative interpretations,
- alternative structures,
- alternative hypotheses,
- alternative exploration trajectories.

The intended behavior is:

```text
Current trajectory
        ↓
      Drift
        ↓
Alternative but problem-related trajectory
```

---

## 8. Observation / Reasoning

Observation / Reasoning evaluates the current Material and transformation state.

Potential observations include:

```text
Invariant
Difference
Constraint
Conflict
Relation
Candidate Structure
Residual
Potential Hypothesis
```

This stage is not equivalent to final answer generation.

---

## 9. Structural Correspondence — ≌C

`≌C` is the principal horizontal exploration mechanism.

Scale changes Material along a structural direction:

```text
M0 → M1 → M2
```

while `≌C` searches between Materials:

```text
M0 ≌ M2
```

The correspondence does not require complete identity.

The operational question is:

> Do these structures retain a useful correspondence despite structural differences?

A structural-difference tolerance ("Chaos Margin") may be wider during diffusion and narrower during convergence.

---

## 10. Hypothesis Generation

Hypotheses are candidate structural explanations, not answers.

```text
Observation
+ Drift
+ ≌C
+ Material
    ↓
H1 / H2 / H3 / ...
```

Multiple hypotheses may be retained to avoid premature closure.

---

## 11. Diffusion

Diffusion expands the exploration space.

```text
H
↓
H1 H2 H3 H4
↓
H11 H12 H21 H22 ...
```

It may expand:

- hypotheses,
- structural representations,
- viewpoints,
- correspondences,
- transformations.

---

## 12. Convergence

Convergence contracts the current candidate space.

Evaluation may consider:

- constraints,
- structural consistency,
- correspondence,
- hypothesis validity,
- residuals.

Convergence is not necessarily final answer selection.

Its design role is to produce a more useful state for the next cycle.

---

## 13. Field Update

The result of convergence is returned to the exploration state.

```text
Candidates
   ↓
Convergence
   ↓
Field Update
   ↓
New Field
```

The Field may contain accepted structures, rejected structures, residuals, hypothesis states, observed relations, and possible next directions.

---

## 14. Re-Diffusion / Re-Convergence

The core cycle is:

```text
Diffusion
   ↓
Convergence
   ↓
Field Update
   ↓
Re-Diffusion
   ↓
Re-Convergence
```

In shorthand:

```text
Expand → Contract → Update → Expand → Contract
```

A convergence result is therefore not necessarily the end of exploration.

---

## 15. Residual Material

Unresolved structures should not automatically be deleted.

```text
Unresolved
    ↓
M_residual
    ↓
Next Cycle
```

Residuals may contain unresolved constraints, contradictions, incomplete hypotheses, unexplained differences, or unexplored branches.

---

## 16. Pseudo-MAS Interpretation

T2 may emulate MAS-like roles inside one LLM context:

| MAS-like role | T2 |
|---|---|
| Agent | observation / hypothesis role |
| Coordinator | state integration |
| Memory | Material / previous states |
| Evaluator | ≌C / consistency evaluation |
| Mutation | Scale / Drift |

This does not make T2 an actual distributed software MAS.

It is a protocol-level role structure.

---

## 17. Canonical Mathematical Example

A mathematical problem can be transformed as:

```text
Mathematical Problem
       ↓
Formula / Code
       ↓
M_input
       ↓
Scale
       ↓
M_derived
       ↓
Drift / Observation
       ↓
≌ Structural Correspondence
       ↓
Hypothesis
       ↓
Diffusion / Convergence
```

For a 3D triangle example, the same mathematical object can be represented through:

```text
Geometric Material
      ↓ Scale
Vector / Edge Material
      ↓ Scale
Algebraic Material
      ↓ Scale
Constraint Material
```

and then compared through:

```text
Geometric Material
        ≌
Algebraic Material
        ≌
Constraint Material
```

The original 3D-triangle implementation should be preserved as the canonical executable example when added to the repository. This document does not invent a replacement for the original artifact.

---

## 18. Discrete Interaction Model

T2 can be abstracted as a graph.

Candidate quantities:

```text
S_i  = local state
w_ij = relationship / edge weight
D_i  = local Drift
```

A candidate interaction term is:

```text
Σ_j w_ij (S_j - S_i)
```

Changing edge scale may represent changes in relation strength, information transfer, interaction range, or Material coupling.

This interpretation remains a research hypothesis.

---

## 19. Continuous-Limit Hypothesis

A refined and scaled discrete T2 structure may potentially be compared with continuous quantities such as:

```text
∇S
∇·F
∂S/∂t
```

The research question is:

```text
Discrete interaction
       ↓ refinement
       ↓ scale transformation
       ↓ continuous limit
Candidate field representation
```

This is **not** a claim that T2 currently derives fluid mechanics or is equivalent to a known fluid equation.

---

## 20. Execution Contract

A T2 implementation should conceptually:

1. Accept a Problem.
2. Extract or generate Material.
3. Apply Scale.
4. Permit controlled Drift.
5. Observe / reason over the state.
6. Search structural correspondence using ≌C.
7. Generate hypotheses.
8. Diffuse candidates.
9. Converge candidates.
10. Update the Field.
11. Re-diffuse.
12. Re-converge.
13. Preserve residual Material.
14. Produce a final hypothesis state and trace.

Changes to this contract should be treated as versioned design changes.

---

## 21. Baseline

Ordinary direct LLM problem solving is the baseline:

```text
Problem
 ↓
LLM
 ↓
Answer
```

T2 is:

```text
Problem
 ↓
Material
 ↓
Operators
 ↓
Exploration
 ↓
Hypothesis / Residual
```

Comparative experiments should control model, problem, external information, and budget where possible.

---

## 22. Ablation

The current design supports operator removal or alteration.

Examples:

```text
T2-A : FULL T2
T2-B : Scale removed
T2-C : Scale / ≌ interaction
T2-D : Scale / ≌ ordering and evidence separation
```

Further possible ablations:

```text
without Drift
without ≌C
without Diffusion
without Re-Diffusion
without Convergence
fixed Scale
single hypothesis
no Residual retention
```

Ablation results belong to experimental records, not to the design definition.

---

## 23. Experimental Variables

Potential independent variables:

```text
Scale presence
Scale direction
Drift strength
≌ tolerance
Operator order
Diffusion depth
Convergence depth
Field update rule
Hypothesis branch count
Token budget
Model
External information
```

Potential measurements:

```text
Material Count
Drift Count
Emergent Count
Hypothesis Branch Count
Re-Convergence Count
Premature Closure
Traceability
Validity
Accuracy
Token usage
Step count
Reproducibility
```

---

## 24. Traceability Contract

A useful trace should permit inspection of:

```text
Input
  ↓
Material
  ↓
Operation
  ↓
Derived Material
  ↓
Observation
  ↓
Hypothesis
  ↓
Evaluation
  ↓
Field Update
```

For important claims, the system should ideally identify:

```text
Origin
Operation
Material type
Dependent hypothesis
Retention / rejection / residual status
```

---

## 25. Failure Handling

Possible outcomes are:

```text
Accepted
Rejected
Contradicted
Unresolved
Residual
Requires further exploration
```

A rejected hypothesis may still generate useful information.

```text
H1
 ↓ Counterexample
Rejected
 ↓
Boundary condition discovered
 ↓
M_derived
 ↓
Next cycle
```

---

## 26. Frozen Baseline Policy

When a T2 version is frozen, the following should remain fixed for that version:

```text
Protocol
Prompt
Operator definitions
Order
Material model
Evaluation rules
Constraints
```

New experiments add:

```text
Data
Runs
Analysis
Comparisons
```

A structural modification creates a new version.

---

## 27. Non-Goals

T2 does not currently claim to:

- prove a theory of human cognition,
- replace all AI agents,
- guarantee correct answers,
- force a single conclusion,
- treat Drift as random noise,
- mix external knowledge without provenance,
- constitute AGI,
- improve intrinsic LLM capability,
- be equivalent to a physical field,
- derive fluid mechanics.

---

## 28. Design Invariants

### Invariant 1 — Problem as Material

The problem can become an exploration object.

### Invariant 2 — Material is Transformable

Material is not read-only input.

### Invariant 3 — Scale is Structural

Scale changes representation or interaction scale, not merely visual size.

### Invariant 4 — Drift is Purposeful

Drift creates alternative trajectories without requiring arbitrary divergence.

### Invariant 5 — ≌ is Correspondence

Structural differences are permitted.

### Invariant 6 — Hypotheses May Coexist

The system need not collapse immediately to one hypothesis.

### Invariant 7 — Diffusion and Convergence are Complementary

Exploration uses both expansion and contraction.

### Invariant 8 — Convergence Can Feed Exploration

A convergence result may become input to the next cycle.

### Invariant 9 — Residuals Can Persist

Unresolved material is not automatically discarded.

### Invariant 10 — Provenance Matters

Material origin should remain distinguishable whenever practical.

---

## 29. Versioning

Suggested policy:

```text
T2 v1.0
    Frozen baseline

T2 v1.1
    Structural modification

T2 v2.0
    Architectural modification
```

Every experiment should record the exact T2 version used.

Example:

```text
protocol    = T2 v1.0
model       = <model>
problem_set = <set>
budget      = <budget>
```

---

## 30. Current Status

T2 is a research prototype.

Current design status:

- Material model defined
- Scale / Drift / ≌ roles defined
- Diffusion / Convergence cycle defined
- Pseudo-MAS interpretation documented
- Baseline / ablation structure defined
- Traceability model defined
- Mathematical / discrete-field direction documented
- General performance claims remain unverified

Once the repository baseline is frozen, subsequent changes should be versioned rather than silently replacing the original definition.

---

## 31. Summary

T2 can be reduced to:

```text
Problem
   ↓
Material
   ↓
Scale
   ↓
Drift
   ↓
Observation
   ↓
≌ Correspondence
   ↓
Hypothesis
   ↓
Diffusion
   ↓
Convergence
   ↓
Field Update
   ↓
Re-Diffusion
   ↓
Re-Convergence
   ↓
Hypothesis / Residual
```

The central design idea is:

> **Do not treat the problem as a static input to an LLM. Treat the problem as a transformable exploration medium.**

T2 is therefore a protocol for changing the structure of exploration while keeping the underlying LLM replaceable.

Its effectiveness remains an empirical question.
