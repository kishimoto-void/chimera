# T2 Experiment Protocol

## Status

**Protocol:** T2  
**Baseline:** v1.0  
**Purpose:** Reproducible experimental evaluation

## 1. Experimental Principle

A T2 experiment should distinguish:

```text
Protocol
Condition
Input
Model
Execution
Observation
Measurement
Interpretation
```

The T2 specification should not be modified during an experiment merely to improve a result.

## 2. Required Metadata

| Field | Description |
|---|---|
| Experiment ID | Unique identifier |
| T2 Version | Exact protocol version |
| Problem ID | Exact problem identifier |
| Model | LLM/model used |
| Prompt Version | Exact prompt revision |
| External Information | Whether external information was permitted |
| Sampling Settings | Relevant generation parameters |
| Token Budget | Maximum budget where applicable |
| Number of Runs | Number of repetitions |
| Baseline | Direct prompting condition |
| T2 Condition | Active T2 configuration |
| Ablation | Removed/modified operators |
| Evaluation Method | How outputs are evaluated |

## 3. Baseline

```text
Problem
  ↓
LLM
  ↓
Answer
```

The baseline is not assumed to be inferior.

## 4. T2 Condition

```text
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
```

Record the exact prompt version.

## 5. Ablation

Possible ablations:

```text
without Scale
without Drift
without ≌C
without Diffusion
without Convergence
fixed Scale
single hypothesis
no residual retention
altered operator order
```

## 6. Candidate Metrics

### Exploration

```text
Material Count
Drift Count
Emergent Count
Hypothesis Branch Count
Diffusion Depth
Convergence Depth
Re-convergence Count
Residual Count
```

### Output

```text
Validity
Accuracy
Constraint Satisfaction
Structural Coherence
Traceability
Reproducibility
Premature Closure
```

### Cost

```text
Token Usage
Step Count
Execution Time
Number of Model Calls
```

## 7. Experimental Record

```text
## Experiment E001

Problem:
Model:
T2 Version:
Prompt Version:
Runs:
Budget:

Baseline:
...

T2:
...

Ablation:
...

Metrics:
...

Observed Differences:
...

Interpretation:
...

Limitations:
...
```

## 8. Observation vs Interpretation

**Observation:** What the experiment directly produced.

**Interpretation:** A proposed explanation for the observation.

Interpretation must not be written as if it were directly measured.

## 9. Reproducibility

Where practical, preserve:

```text
problem input
prompt
model identifier
settings
raw output
parsed trace
metrics
analysis
```

## 10. Statistical Caution

Small experiments should be described as exploratory. Do not infer general performance from one problem, one run, one model, one prompt, one benchmark, or one successful demonstration.

## 11. Negative Results

Record failures, contradictions, no measurable differences, worse outcomes, unexpected behavior, operator instability, and traceability failures.

## 12. Protocol Freeze

```text
T2 v1.0
   ↓
FREEZE
   ↓
Experiment
   ↓
Results
```

A specification change creates a new version.

## 13. Evidence Boundary

Results support claims about tested conditions. They do not automatically establish general superiority, intrinsic model capability improvement, cross-domain generalization, AGI, or physical equivalence.
