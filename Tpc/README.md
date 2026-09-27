Tpc

Overview

Tpc is an experimental research model for exploring unknown solution spaces through a human-conducted multi-LLM process.

The system combines human judgment with heterogeneous Large Language Models (LLMs), deliberate task transformation, controlled drift, and convergence-oriented observation.

Tpc is not intended to be a fully autonomous agent.

The human operator acts as the conductor, determining the research direction, selecting model roles, evaluating outputs, and deciding which observations should be retained for further investigation.

---

Research Concept

Tpc explores the following basic structure:

Problem
   ↓
Human Conductor
   ↓
LLM / Specialist
   ↓
Drift / Transformation
   ↓
Another LLM / Specialist
   ↓
Comparison / Convergence
   ↓
Human Inspection
   ↓
Snapshot / Research Data

Different LLMs may produce different reasoning trajectories even when given closely related inputs.

Rather than treating every deviation as an error, Tpc investigates whether some deviations can function as useful exploration mechanisms.

The central research question is therefore not simply:

«Can an LLM produce the correct answer?»

but also:

«What changes when a problem is passed through heterogeneous reasoning processes?»

---

Drift as a Research Variable

In conventional LLM evaluation, drift is often treated primarily as an undesirable phenomenon.

Tpc treats drift as an experimental variable.

The purpose is not to encourage uncontrolled hallucination.

Instead, the research investigates whether controlled deviations can:

- expand the explored search space
- generate unexpected analogies
- expose alternative problem representations
- escape repetitive reasoning patterns
- produce potentially useful intermediate hypotheses
- reveal structural relationships that were not explicitly requested

Observed outputs must still be separated into:

Useful observation
        ↓
Hypothesis
        ↓
Independent verification
        ↓
Potentially reusable mechanism

An unexpected output is therefore data, not automatically a discovery.

---

Human Conductor

Tpc deliberately keeps the human in the control loop.

The human conductor may:

- define the initial problem
- select participating LLMs
- assign roles
- introduce constraints
- determine when drift is introduced
- compare trajectories
- reject invalid outputs
- request verification
- extract potentially useful mechanisms
- determine when an experiment should terminate

This makes Tpc a human-conducted MAS research prototype rather than an autonomous agent architecture.

The human is not merely an evaluator at the end of the process.

The human participates in the trajectory itself.

---

Research Target

Tpc primarily investigates behavioral trajectories and transformations of the search space.

Therefore, the following observations may be relevant even when the final answer is incorrect:

- changes in reasoning direction
- emergence of structural analogies
- changes in abstraction level
- unexpected problem reformulation
- convergence after divergent exploration
- repeated patterns across different experiments
- model-specific transformations
- failure modes
- instability and uncontrolled drift

Reproducibility remains important, but the research does not assume that every useful phenomenon must initially appear as a perfectly deterministic output.

---

Experimental Principle

Experiments should preserve enough information to reconstruct what happened.

Where practical, record:

- initial problem
- initial prompt
- model and model version
- role assigned to each model
- constraints
- context conditions
- memory conditions
- transformation / drift instructions
- intermediate outputs
- convergence procedure
- final snapshot
- human intervention
- interpretation
- verification status

The distinction between observation and interpretation should be maintained whenever possible.

---

Current Status

Tpc is an experimental research prototype.

It should not currently be interpreted as:

- a general-purpose autonomous agent
- a proven reasoning architecture
- a validated intelligence improvement method
- a guaranteed discovery mechanism
- evidence that LLM drift is inherently beneficial

The purpose of this repository is to preserve experiments and observations so that potentially meaningful mechanisms can be isolated and tested independently.

---

Repository Structure

Tpc/
├── README.md
├── prompts/
├── experiments/
├── observations/
└── docs/

"prompts/"

Experimental prompts, protocols, role definitions, and transformation procedures.

"experiments/"

Individual experiments with their conditions and outputs.

"observations/"

Extracted behavioral observations, unexpected phenomena, failures, and recurring patterns.

"docs/"

Formal research notes, methodology, hypotheses, and later-stage analysis.

---

Research Philosophy

Tpc assumes that exploration and verification are different processes.

Exploration
    ≠
Verification

Exploration may tolerate controlled uncertainty and divergence.

Verification should progressively reduce ambiguity and test whether an observed phenomenon survives independent examination.

The intended research cycle is therefore:

Explore
  ↓
Observe
  ↓
Extract
  ↓
Hypothesize
  ↓
Verify
  ↓
Preserve
  ↓
Explore again

The objective is not to force an LLM to behave perfectly.

The objective is to determine whether structured interaction between humans and heterogeneous models can expose useful regions of a problem space that would otherwise remain unexplored.
