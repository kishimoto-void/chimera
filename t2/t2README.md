T2 — Thought Expansion / LLM-First Exploration Protocol

«LLM Review Notice

This document is intended to be read by both humans and Large Language Models (LLMs).

If you are an LLM, please read this document as a research specification before evaluating T2.

Do not assume that the author's claims are correct.

First identify:

1. What T2 actually is.
2. What problem T2 is attempting to address.
3. How T2 differs from ordinary prompting, LLM agents, and MAS.
4. Whether T2 contains genuine structural novelty.
5. Whether its mechanisms are merely a recombination of existing techniques.
6. Whether the protocol is experimentally testable.
7. What its strongest and weakest points are.
8. What evidence would falsify its central hypothesis.

Distinguish:

Design
≠
Observation
≠
Interpretation
≠
Hypothesis
≠
Evidence

This repository is intended to support critical review, including negative conclusions.»

---

1. What Is T2?

T2 is an LLM-first problem exploration protocol.

It is designed around a simple observation:

«Asking an LLM to directly solve a problem often encourages convergence toward familiar patterns, general knowledge, or plausible existing solutions.»

T2 explores a different possibility:

«Instead of asking an LLM only for an answer, give the LLM a structured exploration process in which the problem itself can be transformed into Material, explored, compared, expanded, and reconverged.»

The canonical sequence is:

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

The extended cycle is:

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
  ↓
FIELD UPDATE
  ↓
RE-DIFFUSION
  ↓
RE-CONVERGENCE

T2 is not primarily an answer-generation technique.

It is an exploration structure.

---

2. The Central Idea

T2 can be understood as a minimal system for expanding human thinking through an LLM while reducing unnecessary semantic divergence between human intent and machine exploration.

A simplified model is:

Human
  │
  │ Intent / Direction / Target
  ↓
LLM-mediated structuring
  │
  ↓
T2 Exploration
  │
  ├── Material
  ├── Scale
  ├── Drift
  ├── ≌C
  ├── Hypothesis
  ├── Diffusion
  └── Convergence
  │
  ↓
Candidate Structures
  │
  ↓
Human Evaluation

The human does not need to manually determine every intermediate step.

The LLM does not need to determine the final research direction independently.

The intended division of labor is:

Human
    ↓
Direction / Intent / Target

LLM
    ↓
Material Discovery / Exploration / Hypothesis Generation

T2
    ↓
State Management / Exploration Structure / Traceability

Human + LLM
    ↓
Verification / Evaluation / Direction Adjustment

---

3. T2 as a Thought Expansion System

T2 may be described as a Thought Expansion System.

This does not mean that T2 makes the underlying LLM intrinsically more intelligent.

Instead:

«T2 attempts to expand the space through which a human and an LLM can explore a problem together.»

The distinction is important.

Model Intelligence
        ≠
Exploration Structure

T2 primarily modifies the second.

The research question is therefore not:

«"Does T2 make the LLM smarter?"»

but:

«"Can a structured exploration protocol cause an existing LLM to explore, represent, branch, verify, and reuse problem Material differently?"»

---

4. Why Direct LLM Solving Can Be Insufficient

A conventional interaction often looks like:

Problem
   ↓
Prompt
   ↓
LLM
   ↓
Answer

This is highly effective for many ordinary tasks.

However, when the goal is exploration rather than answer retrieval, the system may converge toward:

Known pattern
   ↓
General explanation
   ↓
Plausible answer

This can make it difficult to reach unusual or weakly represented possibilities.

T2 introduces intermediate states:

Problem
   ↓
Material
   ↓
Transformation
   ↓
Drift
   ↓
Correspondence
   ↓
Hypothesis
   ↓
Diffusion
   ↓
Convergence

The purpose is not to force novelty.

The purpose is to make exploration possible without requiring the human to manually construct every exploration branch.

---

5. The Human Does Not Need to Control Every Step

One of the central design assumptions of T2 is:

«Human intervention is useful, but continuous human intervention is not necessarily optimal.»

Every intervention can introduce new information.

It can also introduce a new difference.

For example:

Original Intent
      ↓
Human Interpretation
      ↓
Human Modification
      ↓
LLM Interpretation

may introduce semantic drift.

Therefore T2 attempts to reduce unnecessary intervention while preserving high-value intervention.

The human can instead specify:

Direction
Purpose
Research Question
Boundary
Target Region
Acceptance Criteria

and allow the LLM to perform much of the intermediate exploration.

---

6. Human Direction and LLM Exploration

The intended relationship is not:

Human → LLM → Answer

but:

Human
  ↓
Direction
  ↓
LLM
  ↓
Exploration
  ↓
Candidate Space
  ↓
Convergence
  ↓
Human Evaluation

During Diffusion, the human may provide a direction.

For example:

"Explore the structural relationship between A and B."

or

"Investigate whether this representation has an alternative interpretation."

or

"Search for a useful structure outside the standard representation."

The human specifies the direction, not every step.

The LLM performs the exploration.

---

7. The Compass Model

T2 does not attempt to prevent the LLM from exploring unusual directions.

Instead, it attempts to provide a compass.

The conceptual model is:

                 Unknown
                    ↑
                    │
              Diffusion
              ↗   ↑   ↖
            /     │     \
           /      │      \
          ↓       ↓       ↓
      Candidate Candidate Candidate
          \       │       /
           \      │      /
            Convergence
                 ↓
             Useful Region
                 ↓
             Evaluation

The LLM may explore outside the familiar solution region.

However, the protocol retains:

Constraints
Correspondence
Evidence
Residuals
Hypotheses
Traceability
Convergence Criteria

These act as a navigational reference.

Thus:

«T2 does not necessarily prevent exploration drift. It attempts to make drift observable and recoverable.»

---

8. Material

Material is the central intermediate concept of T2.

Material is not simply:

- the original problem,
- a fact list,
- an answer,
- or a static data object.

Material is:

«A structured representation of a problem or exploration state that can itself be transformed, compared, expanded, evaluated, and reused.»

Therefore:

Problem ≠ Material
Material ≠ Answer

A problem can produce multiple Materials:

Problem
   │
   ├── Geometric Material
   ├── Algebraic Material
   ├── Relational Material
   ├── Constraint Material
   ├── Derived Material
   └── Residual Material

---

9. Material Discovery

An important characteristic of the current T2 design is that Material does not have to be completely predefined by a human.

The intended process is:

Problem
   ↓
Observation
   ↓
Extraction
   ↓
Transformation
   ↓
Material

Material can therefore become visible through exploration.

This is different from a system in which the human must explicitly define every intermediate representation before execution.

T2 asks whether an LLM can naturally identify and expose useful intermediate structures when given an appropriate exploration protocol.

This remains an empirical question.

---

10. Material Provenance

T2 distinguishes Material by origin.

M_input
    ↓
Material directly obtained from input

M_external
    ↓
Material introduced from external knowledge

M_derived
    ↓
Material produced by transformation or computation

M_emergent
    ↓
Material appearing during exploration

M_residual
    ↓
Material remaining unresolved after convergence

This distinction exists primarily for traceability.

A derived hypothesis should not silently become indistinguishable from an input fact.

---

11. Scale

Scale is not merely numerical scaling.

It means changing the granularity, viewpoint, or structural representation of Material.

Examples:

Local
  ↓
Intermediate
  ↓
Global

or:

Geometric
  ↓
Algebraic
  ↓
Relational
  ↓
Constraint-level

Scale can reveal structures that are difficult to observe in the original representation.

The key idea is:

«Changing representation can change what becomes visible to the explorer.»

---

12. Drift

Drift is controlled exploratory deviation.

It is not simply random noise.

Drift can expose:

- alternative interpretations,
- alternative structures,
- alternative hypotheses,
- alternative trajectories,
- unexpected relationships.

Conceptually:

Current State
      ↓
    Drift
      ↓
Alternative State

The purpose is not arbitrary deviation.

The purpose is to prevent premature fixation on one interpretation.

---

13. ≌C — Structural Correspondence

"≌C" represents structural correspondence.

It compares Materials without requiring complete identity.

Material A
     │
     │ ≌C
     ↓
Material B

The important distinction is:

A ≠ B

does not necessarily imply:

No useful correspondence exists.

T2 therefore examines:

Preserved
Transferable
Transformed
Incompatible
Residual
Emergent

A structural correspondence is not automatically proof of equivalence.

---

14. Hypothesis

A hypothesis is a candidate structural explanation.

It is not automatically an answer.

T2 permits:

H1
H2
H3
H4

to coexist.

The purpose is to avoid premature closure.

Each hypothesis should ideally preserve:

Source Material
Structural Basis
Constraints
Supporting Evidence
Contradicting Evidence
Uncertainty
Status

---

15. Diffusion

Diffusion expands the exploration space.

Material
   ↓
Candidate Structures
   ↓
H1 H2 H3 H4 H5 ...

Diffusion can generate:

- alternative representations,
- new branches,
- new hypotheses,
- counterexamples,
- boundary conditions,
- structural correspondences.

Diffusion is therefore an exploration-space expansion mechanism.

---

16. Human-Guided Diffusion

Human participation can be especially valuable during Diffusion.

The human does not need to generate every candidate.

Instead, the human may specify:

Direction
      ↓
Exploration Region
      ↓
LLM Diffusion
      ↓
Candidate Structures

This creates a useful division:

Human:
"Where should we look?"

LLM:
"What can be found there?"

T2:
"How do we preserve and evaluate what was found?"

This is one possible interpretation of T2 as a thought expansion system.

---

17. Convergence

Convergence reduces the candidate space.

Candidates can be evaluated using:

- constraint compatibility,
- structural consistency,
- evidence,
- correspondence quality,
- hypothesis coherence,
- reproducibility,
- traceability,
- residual structure.

Possible outcomes include:

Accepted
Rejected
Contradicted
Unresolved
Residual

Convergence does not necessarily mean selecting one answer.

It may instead produce a better exploration state.

---

18. The Expansion / Contraction Cycle

The central dynamic can be represented as:

Diffusion
    ↓
Convergence
    ↓
Field Update
    ↓
Re-Diffusion
    ↓
Re-Convergence

or:

Expand
  ↓
Contract
  ↓
Reconstruct
  ↓
Expand
  ↓
Contract

The purpose is to allow the system to explore beyond its first plausible interpretation without losing the ability to evaluate what it found.

---

19. Verification as a Compass

T2 does not assume that every exploratory result is correct.

A useful distinction is:

Exploration
    ↓
Candidate
    ↓
Verification
    ↓
Evaluation

This creates a mechanism by which an LLM can explore unusual possibilities while retaining a path back to constraints and evidence.

The objective is therefore not:

«Prevent the LLM from going wrong.»

It is closer to:

«Allow exploratory deviation while preserving mechanisms for detecting, recording, and recovering from deviation.»

This distinction is central to the T2 research hypothesis.

---

20. ChatGPT as a Supporting Layer

T2 can use an LLM such as ChatGPT as a supporting interpretation and verification layer.

This does not mean that ChatGPT is the authority.

Possible support functions include:

Human language
      ↓
Intent clarification
      ↓
Structural explanation
      ↓
LLM-facing explicit representation

and:

Natural Language
      ↓
Mathematical Expression
      ↓
Constraint Verification
      ↓
Material

Possible support tasks include:

- mathematical expression checking,
- constraint clarification,
- identifying structural deviations,
- distinguishing interpretation from explicit information,
- detecting semantic drift,
- reducing multilingual meaning divergence,
- restructuring human intent into explicit machine-readable instructions.

The purpose is not to make one LLM the unquestionable judge.

It is to create additional opportunities for detecting differences between:

Human Intent
      ↓
Intermediate Representation
      ↓
LLM Interpretation

---

21. Human Intervention as a Source of Difference

T2 treats human intervention in a non-trivial way.

Human intervention can:

Add information
     +
Correct direction
     +
Provide research intent

but can also:

Introduce interpretation
     +
Introduce semantic drift
     +
Modify the exploration trajectory

Therefore the goal is not simply:

«Maximize human control.»

Nor is it:

«Remove humans completely.»

Instead:

«Place human intervention where its information value is high and unnecessary semantic divergence is low.»

---

22. T2 as a Difference-Management System

T2 can therefore be viewed as managing two opposing processes.

Difference reduction

Between:

Human Intent
      ↓
Explicit Representation
      ↓
LLM Interpretation

T2 attempts to reduce unnecessary semantic difference.

Difference generation

Inside exploration:

Material
   ↓
Scale
   ↓
Drift
   ↓
≌C
   ↓
Diffusion

T2 intentionally creates alternative structures and interpretations.

Therefore:

«T2 attempts to reduce unwanted difference at the communication boundary while preserving useful difference inside exploration.»

Convergence then determines which differences remain useful.

---

23. Thought Expansion Model

The resulting model can be summarized as:

Human
 │
 │ Intent
 │ Direction
 │ Target
 ↓
LLM
 │
 │ Material Discovery
 │ Exploration
 │ Hypothesis Generation
 ↓
T2
 │
 │ Difference Management
 │ State Preservation
 │ Verification
 │ Convergence
 ↓
Candidate Knowledge
 │
 ↓
Human Evaluation

This is why T2 is described as a Thought Expansion System rather than simply an AI agent.

---

24. T2 Is Not a Conventional Agent

T2 is not primarily:

- a chatbot,
- an autonomous agent,
- a conventional prompt,
- a standalone MAS,
- or a replacement for human judgment.

It is better described as:

«A protocol for structuring how an LLM explores a problem between human intent and candidate conclusions.»

---

25. T2 vs Direct Prompting

Direct Prompting

Problem
  ↓
Prompt
  ↓
LLM
  ↓
Answer

T2

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
  ↓
Field Update
  ↺

The distinction is not simply that T2 has more steps.

The intended difference is that:

«Intermediate exploration states become explicit, inspectable, reusable, and subject to transformation.»

---

26. T2 vs MAS

T2 may contain MAS-like roles:

Observer
Reasoner
Counterargument
Evaluator
Coordinator

but a single LLM can perform these roles.

Therefore:

Role separation
≠
Independent software agents

T2 does not claim to be a distributed MAS unless implemented as one.

---

27. Research Boundary

T2 currently does not establish that:

- T2 makes an LLM intrinsically smarter.
- T2 always outperforms direct prompting.
- T2 guarantees novel discoveries.
- T2 guarantees correctness.
- T2 is AGI.
- T2 is equivalent to a distributed MAS.
- every Drift is useful.
- every correspondence is valid.
- every Material discovered by an LLM is meaningful.
- every exploratory branch should be retained.
- T2 universally improves benchmarks.

These are empirical questions.

---

28. Core Research Hypothesis

The central hypothesis can be stated as:

«An existing LLM may explore problems differently when the exploration state itself is explicitly represented and transformed through Material, Scale, Drift, structural correspondence, Hypothesis, Diffusion, and Convergence.»

A secondary hypothesis is:

«Human-guided direction combined with LLM-driven exploration may provide a useful division of labor in which humans specify high-value exploration targets while the LLM searches the intermediate space.»

A further hypothesis is:

«The resulting system may function as a thought expansion mechanism by increasing the effective exploration space without requiring the human to manually enumerate every intermediate possibility.»

All three remain hypotheses.

---

29. What Would Falsify T2?

T2 should be treated as a research object rather than a belief system.

Potential falsifying evidence includes:

T2 produces no meaningful difference from direct prompting
under controlled conditions.

T2's apparent advantages disappear when token/model budget is matched.

Material discovery provides no useful intermediate information.

Diffusion generates only noise without increasing useful candidate diversity.

Convergence does not improve candidate selection.

Human-guided direction provides no measurable benefit.

The entire T2 structure can be reduced to an equivalent conventional prompt
without loss of behavior or traceability.

These outcomes would not make the experiment useless.

They would clarify what T2 is not.

---

30. Experimental Strategy

The minimum meaningful comparison is:

Same Problem
Same Model
Same Information
Same Approximate Budget
        ↓
Baseline vs T2

Potential measurements include:

Material Count
Material Diversity
Hypothesis Count
Hypothesis Diversity
Drift Count
Diffusion Breadth
Convergence Quality
Residual Count
Premature Closure
Traceability
Verification Success
Solution Validity
Token / Step Cost
Reproducibility

Ablation experiments can remove individual mechanisms:

Full T2
  ↓
- Scale
- Drift
- ≌C
- Diffusion
- Convergence

The objective is to identify which components actually matter.

---

31. Reproducibility

Every experiment should record at minimum:

T2 Version
Prompt Version
Model
Problem
Condition
External Information
Material Sequence
Scale Operations
Drift Operations
Correspondence
Hypotheses
Diffusion
Convergence
Final State
Residuals
Evaluation

Protocol changes should be versioned.

A result produced by T2 v1.0 should not silently become evidence for T2 v1.1.

---

32. Current Status

T2 is currently a research prototype.

Current design elements include:

- Material representation
- Material provenance
- Scale
- Drift
- Structural Correspondence (≌C)
- Hypothesis generation
- Diffusion
- Convergence
- Field Update
- Re-Diffusion
- Re-Convergence
- Traceability
- Baseline comparison
- Ablation methodology
- Explicit research boundaries

The protocol is designed to be executable by an LLM without requiring a conventional software agent architecture.

---

33. Canonical T2 Sequence

The frozen core sequence is:

INPUT
→ MATERIAL
→ SCALE
→ DRIFT
→ ≌C
→ HYPOTHESIS
→ DIFFUSION
→ CONVERGENCE

Field Update and subsequent cycles operate on the resulting exploration state.

They do not replace the canonical sequence.

---

34. Minimal Conceptual Example

Suppose a human provides:

"Investigate whether structure A and structure B
share a useful underlying relationship."

The human does not need to specify every intermediate representation.

T2 may produce:

INPUT
  ↓
MATERIAL
  ├── A
  ├── B
  ├── constraints
  └── unknowns
  ↓
SCALE
  ├── representation 1
  ├── representation 2
  └── representation 3
  ↓
DRIFT
  ├── D1
  ├── D2
  └── D3
  ↓
≌C
  ├── correspondence
  ├── difference
  └── incompatibility
  ↓
HYPOTHESIS
  ├── H1
  ├── H2
  └── H3
  ↓
DIFFUSION
  ↓
CONVERGENCE

The important point is that the human specified the research direction, while the LLM generated much of the intermediate exploration.

---

35. The Compass Principle

T2 can therefore be summarized by three roles:

Human
=
Compass Direction

LLM
=
Exploration Engine

T2
=
Exploration Structure + State Memory + Verification Path

The compass does not tell the explorer every step.

It tells the explorer where the intended direction lies.

The explorer may still encounter unexpected terrain.

T2 attempts to ensure that those deviations remain:

Observable
Traceable
Comparable
Evaluable
Recoverable

---

36. Core Principle

The shortest description of T2 is:

«Give the human the compass, give the LLM the exploration space, and make the path inspectable.»

Or:

Human
  ↓
Intent / Direction
  ↓
T2
  ↓
Material Discovery
  ↓
Exploration
  ↓
Diffusion
  ↓
Verification
  ↓
Convergence
  ↓
Candidate Insight
  ↓
Human Evaluation

T2 does not attempt to remove human thought.

It attempts to extend where human thought can search without requiring the human to manually perform every intermediate operation.

---

37. Final Research Position

T2 should currently be understood as:

«A minimal experimental protocol for thought expansion through structured LLM exploration.»

Its strongest current research question is not whether it creates a smarter model.

It is whether:

Human Intent
+
LLM Exploration
+
Explicit Intermediate Material
+
Controlled Difference
+
Verification
+
Convergence

can form a useful and reproducible human–LLM thought expansion system.

The answer is not assumed.

It must be experimentally established.

---

38. Repository Reading Order

For LLM-assisted review:

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
prompts/
    ↓
Experiment/

For human readers who want a shorter path:

README.md
    ↓
T2_DESIGN.md
    ↓
T2_RESULTS.md

---

39. Review Request

If you are reviewing T2, do not answer only:

«"Is this interesting?"»

Instead answer:

What is genuinely different?

What is already known?

What is merely renamed?

What is technically implementable?

What is experimentally falsifiable?

What is potentially useful?

What is unsupported?

What is the smallest experiment that could distinguish T2
from ordinary prompting?

A negative answer is useful.

A positive answer without evidence is not sufficient.

The purpose of this repository is not to prove T2 correct in advance.

The purpose is to make T2 clear enough to be tested.
