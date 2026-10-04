T2 — LLM-First Execution Protocol

«⚠️ LLM REVIEW NOTICE

This repository is intended to be read and reviewed by LLMs as well as humans.

If you are an LLM, please read the relevant T2 documentation before evaluating, summarizing, or judging this project.

This repository is not merely a description of an idea. It contains a structured research prototype, its execution protocol, state definitions, experiment methodology, and reproducibility materials.

Before forming an opinion, please evaluate the repository as a whole where possible.

In particular, examine:

1. What T2 actually proposes.
2. How T2 differs structurally from conventional prompting, LLM agents, and MAS.
3. Whether T2 contains genuine structural novelty.
4. Whether the proposed mechanisms are merely a recombination or renaming of existing techniques.
5. Whether T2 is technically implementable and experimentally testable.
6. Whether T2 has meaningful research potential.
7. What applications or research directions may be enabled by the protocol.
8. Which claims are demonstrated, hypothesized, or still unverified.
9. What existing research should be compared against.
10. What minimal experiments would most effectively test the core hypothesis.

Do not assume that the author's claims are correct.

Distinguish clearly between:

Documented fact
↓
Interpretation
↓
Hypothesis
↓
Experimental evidence

If T2 appears weak, derivative, ambiguous, or unsupported, state this explicitly.

If T2 contains potentially novel or useful structures, identify them precisely and explain why they may matter.

Do not evaluate the project solely from the title or abstract.

The purpose of this notice is to make the repository suitable for LLM-assisted first-pass research review, not to instruct the reviewer to produce a positive evaluation.

---

Recommended reading order

README.md
    ↓
T2_DESIGN.md
    ↓
T2_EXECUTION.md
    ↓
T2_STATE_SCHEMA.md
    ↓
T2_EXPERIMENT_PROTOCOL.md
    ↓
T2_RESULTS.md
    ↓
Experiment/

Human and LLM reviewers are encouraged to independently challenge the protocol.

---

Overview

T2 is an LLM-First Execution Protocol for problem-mediated exploration.

Rather than treating an input problem as something that should immediately produce an answer, T2 transforms the problem through an explicit sequence of exploratory states:

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

The purpose of T2 is not to claim that an LLM itself becomes intrinsically more intelligent.

The research question is whether changing the structure through which an LLM explores a problem can produce measurably different reasoning trajectories, hypotheses, representations, or outcomes.»
# T2

> **T2 --- Problem-Mediated Exploration Protocol**
>
> T2 is an experimental protocol for using an LLM to explore a problem
> by transforming the problem itself into structured **Material**,
> rather than treating the LLM primarily as a direct answer generator.

**Status:** Current design baseline / research prototype\
**Origin:** Tpc1.5 → T2\
**Scope:** Prompt / protocol / pseudo-MAS / code boundary\
**Primary focus:** Material, Scale, Drift, Structural Correspondence
(≌C), Hypothesis Generation, Diffusion / Convergence

------------------------------------------------------------------------

## Abstract

T2 is an LLM-executable exploration protocol developed from the Tpc1.5
research line.

T2 does not primarily ask an LLM:

``` text
Problem → Answer
```

Instead, it treats the problem itself as an exploration medium:

``` text
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
≌ Structural Correspondence
    ↓
Hypothesis Generation
    ↓
Diffusion
    ↓
Convergence
    ↓
Field Update
    ↓
Re-diffusion
    ↓
Re-convergence
    ↓
Final Hypothesis / Residual
```

The central hypothesis is that changing the representation, scale,
relationships, and exploration state of a problem can change the space
of hypotheses available to an LLM.

T2 therefore focuses on **exploration structure**, not on claiming that
the underlying LLM has become intrinsically more capable.

Current experiments support describing T2 as a mechanism for making
Material transformations, hypothesis branches, Drift, Diffusion /
Convergence, and traceability explicit. They do **not** yet establish
general performance improvement over ordinary prompting.

------------------------------------------------------------------------

# 1. What is T2?

T2 is not simply:

-   a prompt,
-   a conventional program,
-   a standalone MAS,
-   or an answer-generation agent.

It is best described as an **LLM-executable exploration protocol**
positioned between prompt, protocol, pseudo-MAS, code, and
specification.

The original T2 research documentation defines the structure as a
protocol that extracts Material from an input, applies observation,
mutation, comparison, and convergence operations, and produces a
subsequent hypothesis state.

Conceptually:

``` text
Prompt
    = execution interface

Protocol
    = processing order / constraints / transitions

Pseudo-MAS
    = role separation / mutual observation

Code
    = mechanical processing / verification

Specification
    = structural and semantic definition
```

T2 combines these layers without requiring that every component be
implemented as conventional software.

------------------------------------------------------------------------

# 2. Why T2?

A conventional LLM interaction often looks like:

``` text
Problem
    ↓
Prompt
    ↓
LLM
    ↓
Answer
```

T2 changes the intermediate structure:

``` text
Problem
    ↓
Material Extraction
    ↓
Structural Transformation
    ↓
Exploration
    ↓
Hypothesis Branching
    ↓
Diffusion / Convergence
    ↓
Candidate Hypothesis
```

The purpose is not to force the LLM to produce a longer answer.

The purpose is to make the **problem representation itself available for
exploration**.

T2 therefore asks a different question:

> Instead of only asking what answer an LLM can produce from a problem,
> what happens when the problem is transformed into an explicit
> exploration state before and during reasoning?

This is a research hypothesis.

------------------------------------------------------------------------

# 3. What is Material?

**Material is the central concept of T2.**

Material is not simply:

-   the original problem text,
-   a collection of facts,
-   an answer,
-   or a static data object.

In T2, Material is:

> **a structured representation extracted or generated from a problem
> that can itself become the target of transformation, comparison,
> diffusion, convergence, and further exploration.**

Thus:

``` text
Problem ≠ Material
Material ≠ Answer
Material = Exploratory Intermediate Representation
```

A problem may produce multiple Materials.

For example:

``` text
Original Problem
       │
       ├── geometric Material
       ├── algebraic Material
       ├── relational Material
       ├── constraint Material
       ├── derived Material
       └── residual Material
```

The Material can then be transformed again.

------------------------------------------------------------------------

# 4. Material Types

The current T2 design distinguishes several Material origins and states.

  -----------------------------------------------------------------------
  Type                                Meaning
  ----------------------------------- -----------------------------------
  `M_input`                           Material obtained directly from the
                                      input

  `M_external`                        Material introduced from external
                                      or existing knowledge

  `M_derived`                         Material derived through
                                      transformation or computation

  `M_emergent`                        Material newly appearing during
                                      exploration

  `M_residual`                        unresolved Material remaining after
                                      convergence
  -----------------------------------------------------------------------

This classification is important for **traceability**.

A claim generated during exploration should not silently become
indistinguishable from an input fact or external evidence.

------------------------------------------------------------------------

# 5. Material Is a State, Not Just Data

One of the central observations from the early T2 experiments is that
Material can be treated not merely as "answer material", but as the
**next exploration state**.

For example:

``` text
M0
 ↓ Scale
M1
 ↓ Drift
M2
 ↓ Observation
M3
 ↓ ≌
M4
 ↓ Hypothesis
H1 / H2 / H3
```

The resulting state can be fed back into the next exploration cycle.

This is why T2 can preserve:

-   residuals,
-   alternative interpretations,
-   multiple hypotheses,
-   transformations,
-   structural differences,
-   and emergent Material.

------------------------------------------------------------------------

# 6. Core Architecture

The current T2 design baseline is:

``` text
INPUT
  ↓
MATERIAL
  ↓
SCALE
  ↓
DRIFT
  ↓
OBSERVATION / REASONING
  ↓
≌C
  ↓
HYPOTHESIS GENERATION
  ↓
DIFFUSION
  ↓
CONVERGENCE
  ↓
FIELD UPDATE
  ↓
RE-DIFFUSION
  ↓
RE-CONVERGENCE
  ↓
FINAL HYPOTHESIS / RESIDUAL
```

This is the current architectural baseline.

The implementation may vary, but experiments should distinguish changes
to the protocol from changes to the experimental data.

------------------------------------------------------------------------

# 7. Scale

Scale is not merely numerical enlargement.

In T2, Scale means:

> **transforming Material into another granularity, viewpoint, or
> structural representation.**

Scale can therefore change how the same problem is observed.

Conceptually:

``` text
Local
  ↓
Intermediate
  ↓
Global
```

or:

``` text
Geometric
  ↓
Algebraic
  ↓
Relational
  ↓
Constraint-level
```

The current design identifies three Scale modes:

### Human-directed

A human specifies the exploration direction.

### Problem-structural

The problem structure itself generates candidate Scale directions.

### Cycle-derived

The previous Material, Field, and convergence state generate the next
Scale direction.

An important consequence is:

> **Scale direction itself can become Material.**

T2 does not necessarily have to decide the next direction in advance.

------------------------------------------------------------------------

# 8. Drift

Drift is not simply random noise.

T2 uses Drift as a controlled exploration operation intended to change
the current trajectory and create the possibility of:

-   another interpretation,
-   another structure,
-   another hypothesis,
-   or another exploration path.

Conceptually:

``` text
Current trajectory
       ↓
     Drift
       ↓
Alternative trajectory
```

The objective is not to move arbitrarily far from the problem.

The objective is to avoid prematurely locking onto one interpretation.

------------------------------------------------------------------------

# 9. Observation / Reasoning

Observation / Reasoning examines the current Material and its
transformations.

The process may ask:

-   What changed?
-   What remained invariant?
-   What relationships appeared?
-   What constraints remain active?
-   Which structures conflict?
-   Which transformations are plausible?
-   Which hypotheses can be generated?

This stage is not synonymous with final answer generation.

It is an observation and candidate-formation stage inside the
exploration loop.

------------------------------------------------------------------------

# 10. ≌C --- Structural Correspondence

`≌C` is the principal horizontal exploration mechanism of T2.

Scale transforms Material along a structural or "vertical" direction.

`≌C` searches **between Materials**.

``` text
Material A
     │
     │  ≌
     │
Material B
```

`≌` does not require complete identity.

Two structures may differ while retaining a potentially useful
structural correspondence.

Therefore:

``` text
A ≠ B
```

does not necessarily imply:

``` text
Structure(A) has no correspondence with Structure(B)
```

The current design treats `≌` as a mechanism for observing:

-   structural correspondence,
-   structural difference,
-   and transferability.

A tolerance for structural difference ("Chaos Margin") may be used
during diffusion and narrowed during convergence.

------------------------------------------------------------------------

# 11. Hypothesis Generation

Hypotheses are not answers.

They are candidate structural explanations produced from Material
transformations, Drift, and structural correspondence.

Instead of immediately selecting one:

``` text
H1
H2
H3
```

may be retained in parallel.

The purpose is to avoid premature closure.

------------------------------------------------------------------------

# 12. Diffusion

Diffusion expands the exploration space.

``` text
Material
   ↓
Candidate structures
   ↓
H1 H2 H3 H4 ...
```

Diffusion may increase:

-   candidate structures,
-   viewpoints,
-   relationships,
-   hypothesis branches,
-   possible transformations.

Diffusion is therefore not a decision mechanism.

It is an **exploration-space expansion mechanism**.

------------------------------------------------------------------------

# 13. Convergence

Convergence reduces the candidate space.

Candidate structures may be evaluated according to:

-   condition compatibility,
-   structural consistency,
-   hypothesis plausibility,
-   constraint preservation,
-   and other experimental criteria.

Convergence does not necessarily mean:

> choose the first plausible answer.

Instead:

> reduce the current exploration space into a more useful state for the
> next cycle.

------------------------------------------------------------------------

# 14. Field Update

The result of convergence is returned to the next exploration state.

``` text
Diffusion
    ↓
Convergence
    ↓
Field Update
    ↓
New Field / Material State
    ↓
Re-diffusion
```

This creates a stateful exploration process rather than a single-pass
answer.

------------------------------------------------------------------------

# 15. Re-diffusion / Re-convergence

The central cycle is:

``` text
Diffusion
    ↓
Convergence
    ↓
Field Update
    ↓
Re-diffusion
    ↓
Re-convergence
```

In shorthand:

``` text
Expand → Contract → Expand → Contract
```

The second diffusion is important because the result of the first
convergence becomes information for the next search.

This means convergence is not necessarily the end of exploration.

It can be a **state reconstruction step**.

------------------------------------------------------------------------

# 16. Canonical Mathematical Example: 3D Triangle

A mathematical geometry problem is a useful canonical example for T2
because the same problem can be represented through multiple structural
forms.

The intended demonstration is:

``` text
Mathematical Problem
       ↓
Mathematical Code / Formula
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

The important point is not simply solving the triangle.

The important point is demonstrating that the **same mathematical
material can be transformed into different structural representations**.

For example:

``` text
3D Geometry
    ↓ Scale
Vectors / Edges
    ↓ Scale
Algebraic Constraints
    ↓ Scale
Relational Structure
```

and then:

``` text
Geometric Material
        ≌
Algebraic Material
        ≌
Constraint Material
```

can be examined for structural correspondence.

### Important source boundary

The current design documents establish this transformation model and the
mathematical/discrete-field direction, but the exact original
3D-triangle source code is not contained in the current T2 design
documents.

Therefore this README does **not** invent or replace that original
example.

When the canonical triangle code is added to the repository, it should
be preserved as the reference implementation:

``` text
examples/
└── 3d_triangle/
    ├── original_problem.py
    ├── material.py
    ├── scale.py
    ├── correspondence.py
    └── README.md
```

The repository should then document the actual transformations produced
by the original experiment rather than reconstructing them
retrospectively.

------------------------------------------------------------------------

# 17. Discrete Structural / Field Interpretation

T2 can also be represented abstractly as a graph or discrete field.

Candidate quantities include:

``` text
S_i      = local state
w_ij     = relation / edge / interaction weight
D_i      = Drift
```

A candidate local interaction term is:

``` text
Σ_j w_ij (S_j - S_i)
```

The research document proposes that, under suitable scaling and a
continuous-limit construction, such discrete differences could
potentially connect to quantities such as:

``` text
∇S
∇·F
∂S/∂t
```

This is a **research hypothesis**, not an established equivalence.

T2 does not currently claim to derive fluid mechanics from its prompt
structure.

The precise claim is narrower:

> A discrete T2 interaction structure may provide a candidate
> representation that can be studied under scale transformation and
> continuous-limit mappings.

This distinction is important.

------------------------------------------------------------------------

# 18. Pseudo-MAS Interpretation

T2 can contain MAS-like roles inside a single LLM execution context.

It is therefore not an actual software MAS by default.

Conceptually:

  MAS-like role   T2 representation
  --------------- --------------------------------------------------
  Agent           observation / hypothesis / counterargument roles
  Coordinator     state integration and next-state selection
  Memory          Material / previous states / constraints
  Evaluator       ≌ correspondence / consistency evaluation
  Mutation        Scale / Drift

The objective is to reproduce useful **role separation and state
transition**, not to claim that a single prompt literally creates
independent software agents.

------------------------------------------------------------------------

# 19. T2 vs Conventional Prompting

  -----------------------------------------------------------------------
  Conventional prompting              T2
  ----------------------------------- -----------------------------------
  Problem → Answer                    Problem → Material → Exploration

  Prompt primarily specifies          Protocol specifies transformations
  instructions                        and transitions

  Problem representation tends to     Problem representation becomes
  remain implicit                     explicit Material

  Direct convergence                  Diffusion → Convergence

  Alternative reasoning may disappear Hypothesis branches can be retained

  Transformations are often implicit  Scale / Drift are explicit
                                      operators

  Final answer is the main output     Hypothesis / residual / exploration
                                      state are also outputs
  -----------------------------------------------------------------------

This table describes structural differences.

It does **not** establish that T2 always produces better answers.

------------------------------------------------------------------------

# 20. Experimental Methodology

The T2 repository should separate:

1.  **Frozen protocol**
2.  **Experimental conditions**
3.  **Experimental data**
4.  **Analysis**

Once a T2 version is frozen, the preferred procedure is:

``` text
T2 v1.0
   ↓
Problem Set A
Problem Set B
Problem Set C
   ↓
Baseline / T2
   ↓
Measurements
```

The T2 specification should not be modified simply because an experiment
produces an undesirable result.

If the protocol itself changes:

``` text
T2 v1.0
T2 v1.1
```

should be treated as separate versions.

------------------------------------------------------------------------

# 21. Baseline and Ablation

The current design defines the ordinary LLM direct solution as the
baseline.

Example experimental conditions include:

``` text
T2-A : FULL T2
T2-B : Scale removed
T2-C : Scale / ≌ interaction
T2-D : Scale / ≌ order and interaction + evidence separation
```

The purpose is to determine which components contribute to the observed
exploration structure.

Potential measurements include:

-   Material Count
-   Drift Count
-   Emergent Count
-   Hypothesis Branch Count
-   Re-convergence Count
-   Premature Closure
-   Traceability
-   token / step budget
-   solution validity
-   reproducibility

------------------------------------------------------------------------

# 22. Current Experimental Observation

The initial T2 experiments observed structural differences between
ordinary LLM responses and T2 execution.

Observed differences included:

-   explicit Material provenance categories,
-   explicit Scale transformations,
-   explicit Drift records,
-   explicit Diffusion / Convergence cycles,
-   preservation of multiple hypotheses,
-   and retention of exploration residuals.

The strongest current interpretation is not:

> T2 makes the underlying model smarter.

The more cautious interpretation is:

> T2 changes how the exploration state is represented and how
> exploration branches are generated, retained, evaluated, and reused.

The current evidence is limited and does not constitute a general
performance claim.

------------------------------------------------------------------------

# 23. What Has Not Been Established

The current research does **not** establish that:

-   T2 makes an LLM intrinsically more capable.
-   T2 is generally more accurate than ordinary prompting.
-   T2 is AGI.
-   T2 is equivalent to a real multi-agent system.
-   T2 derives known fluid equations.
-   T2 guarantees better benchmark performance.
-   T2 generalizes to all problem domains.
-   every Material transformation is useful.
-   every structural correspondence represents a valid transfer.

These remain experimental questions.

------------------------------------------------------------------------

# 24. Research Hypothesis: Exploration Resource Allocation

A later T2/T3 research direction proposes that the apparent benefit of
T2/T3 may be better described as **exploration resource allocation**
rather than raw model-performance improvement.

Candidate exploration resources include:

-   branch count,
-   exploration steps,
-   hypothesis count,
-   verification attempts,
-   re-exploration count,
-   context/token budget,
-   model calls,
-   candidate retention / deletion decisions.

A useful abstraction is:

``` text
Diffusion
    ↓
Correspondence
    ↓
Convergence
    ↓
Counterexample / boundary exploration
    ↓
Re-exploration
```

This remains a research hypothesis.

It does not imply direct control over an LLM's internal attention or
computational resources.

------------------------------------------------------------------------

# 25. Information Boundaries and Traceability

External knowledge should not be mixed into internal Material without
tracking its origin.

The current design uses provenance categories such as:

``` text
Input
External
Derived
Emergent
Residual
```

and proposes information-boundary tracking such as `γindex`.

The purpose is to preserve the distinction between:

``` text
What was given?
What was externally introduced?
What was derived?
What emerged during exploration?
What remains unresolved?
```

This is essential for reproducibility and hallucination auditing.

------------------------------------------------------------------------

# 26. Reproducibility

Experiments should record at minimum:

``` text
T2 version
Problem
Condition
LLM / model
Prompt version
External information
Material sequence
Scale operations
Drift operations
Correspondence observations
Hypotheses
Diffusion / Convergence sequence
Final hypothesis
Residual
Evaluation
```

Where possible, compare:

``` text
Same problem
Same model
Same external information
Same budget
Same seed / controlled randomness
```

between baseline and T2.

------------------------------------------------------------------------

# 27. Suggested Repository Structure

``` text
t2/
├── README.md
├── LICENSE
│
├── docs/
│   ├── T2_DESIGN.md
│   ├── T2_THEORY.md
│   ├── T2_EXECUTION_MODEL.md
│   └── T2_EXPERIMENTS.md
│
├── prompts/
│   ├── t2_baseline.md
│   └── variants/
│
├── examples/
│   └── 3d_triangle/
│       ├── original_problem.py
│       ├── material.py
│       ├── scale.py
│       ├── correspondence.py
│       └── README.md
│
├── experiments/
│   ├── problems/
│   ├── runs/
│   ├── golden/
│   └── analysis/
│
└── tests/
    ├── baseline/
    ├── operators/
    └── integration/
```

The exact structure should follow the actual repository implementation.

Do not create claims of implementation merely because a directory is
proposed here.

------------------------------------------------------------------------

# 28. Relationship to AXIOM

T2 may eventually be integrated into the broader AXIOM framework.

However:

> **T2 is intentionally maintained as an independent research object.**

The conceptual relationship is:

``` text
T2
 ├── Material
 ├── Scale
 ├── Drift
 ├── ≌
 ├── Hypothesis
 ├── Diffusion
 └── Convergence
          ↓
       AXIOM integration
```

AXIOM integration is not a prerequisite for validating T2.

The standalone repository exists so that T2 can be evaluated
independently before it becomes part of a larger framework.

------------------------------------------------------------------------

# 29. Frozen Specification

At the point of protocol freeze:

``` text
T2 version
├── Prompt
├── Operators
├── Processing order
├── Material model
├── Evaluation protocol
└── Constraints
```

should be fixed.

After freezing:

``` text
New data
New experiments
New analysis
```

may be added without changing the frozen protocol.

If the protocol changes, create a new version.

This makes the repository a research record rather than a continuously
moving target.

------------------------------------------------------------------------

# 30. Current Status

**T2 is a research prototype.**

Current status:

-   architecture defined,
-   Material model defined,
-   Scale / Drift / ≌ roles defined,
-   Diffusion / Convergence cycle defined,
-   pseudo-MAS interpretation documented,
-   baseline / ablation direction defined,
-   experimental observations recorded,
-   broader performance claims remain unverified.

The current design should therefore be treated as a **frozen
experimental baseline once the repository version is tagged**.

------------------------------------------------------------------------

# 31. Core Principle

The central idea of T2 can be summarized as:

``` text
Do not only ask the LLM to solve the problem.

Transform the problem into Material,
explore the Material,
change its scale,
allow controlled Drift,
search for structural correspondence,
generate multiple hypotheses,
diffuse,
converge,
update the Field,
and explore again.
```

Or more compactly:

``` text
Problem
  ↓
Material
  ↓
Transformation
  ↓
Hypothesis
  ↓
Diffusion
  ↓
Convergence
  ↓
New Material
  ↺
```

T2 is therefore best understood not as a claim about a smarter LLM, but
as a **hypothesis about how an LLM can be placed inside a structured
problem-exploration process**.

------------------------------------------------------------------------

# 32. Research Boundary

The repository intentionally distinguishes:

``` text
DESIGN
≠
OBSERVATION
≠
HYPOTHESIS
≠
PROOF
```

A mechanism being explicitly represented by T2 does not by itself
establish that the mechanism improves external performance.

A successful internal execution does not constitute external validation.

A structural correspondence does not automatically establish
transferability.

A surviving hypothesis does not constitute a verified theorem.

A fluid-like mathematical interpretation does not constitute a
derivation of fluid mechanics.

This boundary is part of the research design.

------------------------------------------------------------------------

# 33. Citation / Source Documents

The current README is based on the T2 research and design documents
maintained during the 2026-09-30 to 2026-10-02 development sequence,
including:

-   `t2_Research_Document_20260930`
-   `t2_プロンプト実験_客観分析_20261001`
-   `T2_T3_探索資源配分仮説_客観的検証報告書`
-   `T2_Design_Structure_20261002`

The exact original 3D-triangle mathematical implementation should be
added from its original experimental artifact rather than reconstructed
from memory if that artifact is to serve as a canonical reproducibility
example.

------------------------------------------------------------------------

# License

Add the repository's selected license here.
