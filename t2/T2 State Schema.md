T2 State Schema

Protocol: T2
Baseline: v1.0
Role: Canonical state representation
Status: Research prototype / schema definition

---

1. Purpose

T2 already defines the execution sequence:

INPUT
→ MATERIAL
→ SCALE
→ DRIFT
→ ≌C
→ HYPOTHESIS
→ DIFFUSION
→ CONVERGENCE

This document defines what information should be preserved while moving between those states.

The purpose is to make T2 execution traces inspectable and reproducible without requiring a specific programming language, database, or serialization format.

This is a semantic schema, not yet a mandatory JSON, YAML, or programming-language implementation.

---

2. Design Principle

A T2 execution should be represented as a sequence of inspectable state transitions rather than opaque LLM responses.

State_t
   ↓ Operator
State_t+1

Each transition should preserve enough information to determine:

- what entered the state,
- what operation was performed,
- what changed,
- what remained invariant,
- what was generated,
- what was rejected,
- what remains unresolved,
- and where resulting Material came from.

---

3. Top-Level T2 State

T2State
├── execution
├── input
├── material
├── scale
├── drift
├── correspondences
├── hypotheses
├── diffusion
├── convergence
├── field
├── residuals
├── uncertainty
└── trace

Not every field must contain a value at every execution step.

Absent information must not be silently converted into a positive claim.

---

4. Execution Metadata

execution:
  protocol: T2
  protocol_version: v1.0
  execution_id:
  problem_id:
  prompt_version:
  model:
  model_parameters:
  external_information:
  budget:
  run_index:

Field| Meaning
protocol| Protocol identifier
protocol_version| Frozen T2 version
execution_id| Unique execution identifier
problem_id| Problem identifier
prompt_version| Exact LLM-facing prompt revision
model| Model used
external_information| Whether external information was permitted
budget| Applicable execution budget
run_index| Repetition index when applicable

The schema does not prescribe how identifiers are generated.

---

5. INPUT State

The input state preserves the original problem before exploratory transformation.

input:
  problem_text:
  explicit_constraints:
  requested_output:
  provided_information:
  assumptions:
  external_information:

The distinction between provided information and assumptions is important.

An inferred assumption must not be silently promoted to an input fact.

---

6. Material State

Material is the central T2 object.

material:
  id:
  type:
  content:
  structure:
  relations:
  constraints:
  invariants:
  differences:
  provenance:
  status:

Material Types

Baseline categories:

M_input
M_external
M_derived
M_emergent
M_residual

These categories describe origin or state, not truth value.

For example:

M_derived ≠ guaranteed true
M_external ≠ guaranteed correct
M_emergent ≠ guaranteed useful

---

7. Material Provenance

Derived or important Material should preserve its origin where practical.

provenance:
  source_material:
  source_state:
  operator:
  transformation:
  derivation_note:

Example:

M0
 ↓ Scale
M1
 ↓ Drift
M2

The relationship between M2 and its source states should remain inspectable.

---

8. Scale State

Scale describes a transformation of representation, granularity, or structural viewpoint.

scale:
  direction:
  source_representation:
  target_representation:
  preserved:
  altered:
  newly_visible:
  rationale:

A Scale operation should distinguish:

Preserved structure
Altered structure
Newly visible structure

Scale direction itself may become Material.

---

9. Drift State

Drift describes a controlled change in exploration trajectory.

drift:
  source_state:
  changed:
  preserved:
  rationale:
  exposed_structure:
  drift_character:

Drift must not be represented merely as random change.

The execution should identify why the drift is relevant to the problem.

---

10. Structural Correspondence State

≌C compares Materials that may differ structurally.

correspondence:
  source_material:
  target_material:
  preserved:
  transferable:
  transformed:
  incompatible:
  residual:
  emergent:
  chaos_margin:
  justification:

The central distinction is:

Difference ≠ No Correspondence

A correspondence record must not imply identity unless identity is independently established.

---

11. Chaos Margin

Chaos Margin is an experimental tolerance for structural difference.

chaos_margin:
  value:
  interpretation:
  acceptance_rule:
  stage:

The value may be qualitative or quantitative depending on the experiment.

It must not be presented as an established physical constant or universal mathematical quantity.

---

12. Hypothesis State

A hypothesis is a candidate structural explanation.

hypothesis:
  id:
  statement:
  source_material:
  structural_basis:
  constraints:
  predicted_implication:
  supporting_evidence:
  contradicting_evidence:
  uncertainty:
  status:

Possible statuses:

candidate
supported
weak
rejected
contradicted
unresolved
retained

A hypothesis status is an evaluation state, not a guarantee of truth.

---

13. Diffusion State

Diffusion records expansion of the exploration space.

diffusion:
  source_state:
  generated_material:
  generated_hypotheses:
  alternative_representations:
  counterexamples:
  boundary_conditions:
  branches:

Diffusion should preserve branch identity where practical.

Example:

H0
├── H1
│   ├── H1a
│   └── H1b
├── H2
└── H3

This permits later analysis of premature closure and branch survival.

---

14. Convergence State

Convergence records contraction or organization of the candidate space.

convergence:
  criteria:
  evaluated_items:
  accepted:
  rejected:
  contradicted:
  unresolved:
  retained_residuals:
  rationale:

Convergence criteria should be explicit whenever possible.

Typical criteria include:

- constraint compatibility,
- structural consistency,
- correspondence quality,
- explanatory usefulness,
- stability across Scale,
- residual size,
- traceability.

---

15. Field State

The Field is the state passed into the next exploration cycle.

field:
  active_material:
  active_hypotheses:
  accepted_structures:
  rejected_structures:
  relations:
  constraints:
  residuals:
  next_directions:

Field Update is therefore not simply selecting a best answer.

Convergence
    ↓
Field Update
    ↓
New exploration state

---

16. Residual State

Residuals are unresolved or intentionally retained Material.

residual:
  id:
  source:
  content:
  reason_retained:
  unresolved_constraints:
  possible_next_operation:
  priority:

Residuals may include:

- unresolved constraints,
- contradictions,
- incomplete hypotheses,
- unexplained differences,
- unexplored branches,
- failed correspondences that revealed useful boundaries.

A residual is not necessarily an error.

---

17. Uncertainty State

T2 should distinguish uncertainty from contradiction.

uncertainty:
  item:
  reason:
  confidence:
  evidence:
  unresolved_questions:

Conceptually:

Unknown
≠ False
≠ Contradicted

This distinction is important for avoiding premature convergence.

---

18. Transition Record

Every meaningful operator transition should be representable as:

T2_STEP:
  step_id:
  state_before:
  operator:
  state_after:
  input_material:
  output_material:
  changes:
  invariants:
  hypotheses:
  residuals:
  provenance:
  uncertainty:

The minimum semantic requirement is:

Before
→ Operator
→ After

The additional fields improve auditability.

---

19. Operator Vocabulary

The v1.0 baseline uses:

INPUT
MATERIAL
SCALE
DRIFT
≌C
HYPOTHESIS
DIFFUSION
CONVERGENCE

Field Update, Re-Diffusion, and Re-Convergence are state-cycle mechanisms rather than replacements for the frozen v1.0 canonical sequence.

---

20. State Transition Invariants

Invariant 1 — Provenance

Derived Material should not silently become input Material.

Invariant 2 — State Separation

A hypothesis must remain distinguishable from supporting Material.

Invariant 3 — Residual Preservation

Unresolved Material may remain available for later exploration.

Invariant 4 — Correspondence ≠ Identity

≌C must not silently convert correspondence into equality.

Invariant 5 — Observation ≠ Interpretation

Observed output and explanatory interpretation should remain distinguishable.

Invariant 6 — Rejection ≠ Deletion

Rejected Material may remain useful as evidence, boundary information, or residual context.

Invariant 7 — Uncertainty ≠ Falsehood

Insufficient evidence must not automatically become contradiction.

Invariant 8 — Version Traceability

Every experimental state should be attributable to a specific T2 protocol version.

---

21. Minimal State

A minimal implementation does not need every optional field.

The smallest useful state is:

T2State:
  state
  material
  operator
  changes
  invariants
  hypotheses
  residuals
  provenance

This permits a lightweight prompt-only implementation while preserving the core trace model.

---

22. Extended State

A more complete implementation may add:

execution metadata
multiple Material objects
Material graph
hypothesis graph
correspondence graph
branch history
evaluation metrics
uncertainty
cost
token usage
timing
model metadata
raw LLM output
parsed trace

These are implementation extensions and do not alter the T2 v1.0 execution order.

---

23. State Example

A conceptual execution may look like:

STATE 0
INPUT
  problem = P0

STATE 1
MATERIAL
  M0 = M_input

STATE 2
SCALE
  M0 → M1
  preserved = constraints
  altered = representation

STATE 3
DRIFT
  M1 → M2
  preserved = core relation
  changed = viewpoint

STATE 4
≌C
  M1 ≌ M2
  correspondence = partial
  residual = R1

STATE 5
HYPOTHESIS
  H1
  H2
  H3

STATE 6
DIFFUSION
  H1 → H1a, H1b
  H2 → H2a

STATE 7
CONVERGENCE
  H1a = retained
  H1b = rejected
  H2a = unresolved
  R1 = retained

FIELD UPDATE
  active = H1a
  residual = R1

RE-DIFFUSION
  ...

RE-CONVERGENCE
  ...

This example is schematic and does not constitute an experimental result.

---

24. Serialization Boundary

The semantic schema does not prescribe a serialization format.

Possible future representations include:

JSON
YAML
TOML
Python dataclasses
Rust structs
database records
plain Markdown traces

The semantic meaning should remain stable if the serialization format changes.

---

25. Relationship to T2 Documentation

T2_DESIGN.md
    ↓
Why / conceptual architecture

T2_EXECUTION.md
    ↓
How / execution order

T2_STATE_SCHEMA.md
    ↓
What state must be preserved

prompts/T2_v1.0.md
    ↓
LLM-facing execution interface

T2_EXPERIMENT_PROTOCOL.md
    ↓
How executions are evaluated

No document should silently redefine another document's frozen semantics.

---

26. Research Boundary

This schema does not establish:

- improved intrinsic LLM capability,
- general benchmark superiority,
- validity of every structural correspondence,
- equivalence to a distributed MAS,
- AGI,
- physical field equivalence,
- or a universal mathematical theory.

It establishes only a structured representation for inspecting T2 exploration states.

---

27. Frozen v1.0 Interpretation

For T2 v1.0:

Problem
  ↓
Material
  ↓
Scale
  ↓
Drift
  ↓
≌C
  ↓
Hypothesis
  ↓
Diffusion
  ↓
Convergence

The state schema exists to make those transitions observable.

It does not add a new operator to the protocol.

---

28. Summary

The central requirement is:

«A T2 execution should leave behind an inspectable state trajectory, not only a final answer.»

The canonical semantic chain is:

Input
→ Material
→ Transformation
→ Correspondence
→ Hypothesis
→ Exploration
→ Convergence
→ Residual / Next State

T2_STATE_SCHEMA.md defines the minimum conceptual structure required to preserve that trajectory.
