# T2 Glossary

## T2
**Problem-Mediated Exploration Protocol.** An LLM-first protocol in which the problem is transformed into structured Material and explored through explicit operators.

## Material
A structured intermediate representation extracted or generated from a problem that can itself be transformed, compared, diffused, and converged.

```text
Problem ≠ Material
Material ≠ Answer
```

## M_input
Material obtained directly from the input problem.

## M_external
Material introduced from external knowledge or an external source.

## M_derived
Material produced by transformation, computation, or reasoning from existing Material.

## M_emergent
Material that appears during exploration and was not explicitly present in the initial Material inventory.

## M_residual
Unresolved Material retained after a convergence step or other filtering operation.

## Scale
A structural transformation that changes granularity, viewpoint, representation, or interaction scale.

## Drift
A controlled modification of the current exploration trajectory intended to expose alternative structures or hypotheses. Drift is not defined as arbitrary noise.

## ≌C
**Structural Correspondence.** The T2 comparison mechanism for identifying potentially useful correspondence between structurally different Materials. It does not require identity.

## Structural Correspondence
A relationship between two Materials in which some structure, relation, constraint, or transformation can be meaningfully mapped despite differences.

## Chaos Margin
An experimental tolerance for structural difference during correspondence search. It is a research control concept, not an established physical law.

## Hypothesis
A candidate structural explanation generated from Material and its transformations. It is not automatically an answer or fact.

## Diffusion
Expansion of the current exploration space through additional candidate structures, representations, correspondences, or hypotheses.

## Convergence
Contraction or organization of a candidate space using explicit evaluation criteria. It does not necessarily mean final answer selection.

## Field Update
Returning convergence results to the next exploration state.

## Residual
Material that remains unresolved, unexplained, contradictory, or otherwise useful for further exploration.

## Emergent
A structure or Material that appears during exploration rather than being explicitly supplied at input.

## Traceability
The ability to inspect where Material or a hypothesis came from and which operations transformed it.

## Premature Closure
Collapsing the exploration space before relevant alternatives, transformations, or residuals have been adequately considered.

## Operator
A defined transformation or processing step such as Scale, Drift, ≌C, Diffusion, or Convergence.

## State
The inspectable representation of the current T2 exploration condition.

## Pseudo-MAS
A protocol-level separation of roles resembling multi-agent behavior within one LLM context. It is not automatically a distributed software MAS.

## Baseline
The comparison condition in which the problem is given directly to the LLM without the T2 exploration protocol.

## Ablation
An experimental condition in which a T2 operator or mechanism is removed or altered to examine its contribution.

## Protocol Version
A frozen version of the T2 execution contract. Results must identify the protocol version under which they were produced.
