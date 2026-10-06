from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Protocol


# ============================================================
# T3 LLM Core
# ============================================================

@dataclass
class Observation:
    """
    Observable material produced by an LLM or another source.

    T3 does NOT claim to access hidden chain-of-thought.
    This object stores observable outputs and derived annotations.
    """

    source: str
    input_text: str
    output_text: str

    metadata: Dict[str, Any] = field(default_factory=dict)

    # Derived structural information
    claims: List[str] = field(default_factory=list)
    assumptions: List[str] = field(default_factory=list)
    alternatives: List[str] = field(default_factory=list)
    selections: List[str] = field(default_factory=list)
    constraints: List[str] = field(default_factory=list)
    obstacles: List[str] = field(default_factory=list)
    predictions: List[str] = field(default_factory=list)

    # T3 experimental objects
    branches: List[str] = field(default_factory=list)
    attractors: List[str] = field(default_factory=list)
    residuals: List[str] = field(default_factory=list)
    contradictions: List[str] = field(default_factory=list)
    uncertainties: List[str] = field(default_factory=list)


@dataclass
class AnalysisResult:
    analyzer: str
    observations: Dict[str, Any] = field(default_factory=dict)
    warnings: List[str] = field(default_factory=list)


class Analyzer(Protocol):
    """
    Extension interface.

    Any analyzer implementing `analyze()` can be attached
    to the T3 core without modifying CORE.py.
    """

    name: str

    def analyze(self, observation: Observation) -> AnalysisResult:
        ...


class T3Core:
    """
    Minimal extensible T3 analysis engine.
    """

    def __init__(self) -> None:
        self._analyzers: Dict[str, Analyzer] = {}

    # --------------------------------------------------------
    # Registration
    # --------------------------------------------------------

    def register(self, analyzer: Analyzer) -> None:
        if analyzer.name in self._analyzers:
            raise ValueError(
                f"Analyzer already registered: {analyzer.name}"
            )

        self._analyzers[analyzer.name] = analyzer

    def unregister(self, name: str) -> None:
        self._analyzers.pop(name, None)

    def analyzers(self) -> List[str]:
        return list(self._analyzers.keys())

    # --------------------------------------------------------
    # Analysis
    # --------------------------------------------------------

    def analyze(
        self,
        observation: Observation,
    ) -> Dict[str, AnalysisResult]:

        results: Dict[str, AnalysisResult] = {}

        for name, analyzer in self._analyzers.items():
            try:
                results[name] = analyzer.analyze(observation)

            except Exception as exc:
                # One experimental analyzer must not destroy
                # the entire T3 pipeline.
                results[name] = AnalysisResult(
                    analyzer=name,
                    warnings=[
                        f"Analyzer failure: {type(exc).__name__}: {exc}"
                    ],
                )

        return results

    # --------------------------------------------------------
    # Comparison
    # --------------------------------------------------------

    @staticmethod
    def compare(
        a: Observation,
        b: Observation,
    ) -> Dict[str, Any]:

        return {
            "source_a": a.source,
            "source_b": b.source,

            "output_changed":
                a.output_text != b.output_text,

            "claims": T3Core._diff(
                a.claims,
                b.claims,
            ),

            "assumptions": T3Core._diff(
                a.assumptions,
                b.assumptions,
            ),

            "alternatives": T3Core._diff(
                a.alternatives,
                b.alternatives,
            ),

            "selections": T3Core._diff(
                a.selections,
                b.selections,
            ),

            "constraints": T3Core._diff(
                a.constraints,
                b.constraints,
            ),

            "attractors": T3Core._diff(
                a.attractors,
                b.attractors,
            ),

            "residuals": T3Core._diff(
                a.residuals,
                b.residuals,
            ),
        }

    @staticmethod
    def _diff(
        a: List[str],
        b: List[str],
    ) -> Dict[str, List[str]]:

        sa = set(a)
        sb = set(b)

        return {
            "only_a": sorted(sa - sb),
            "only_b": sorted(sb - sa),
            "common": sorted(sa & sb),
        }


# ============================================================
# Minimal example
# ============================================================

if __name__ == "__main__":

    core = T3Core()

    observation = Observation(
        source="LLM-A",
        input_text="Solve an unknown problem.",
        output_text="The most likely answer is A.",
    )

    print("Registered analyzers:")
    print(core.analyzers())

    print("\nObservation:")
    print(observation)
