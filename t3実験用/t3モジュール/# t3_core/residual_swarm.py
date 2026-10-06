"""
T3 Residual Swarm / WashiWashi Analyzer
========================================

Experimental module for observing residual fields without assuming that
"residual", "vector", "force field", or "self-correction" exists inside
the analyzed system.

Core rule:
    observation -> mapping -> residual field -> measurement -> candidate labels

The module distinguishes:
- observed numeric residuals
- experimenter-defined mappings
- field-level statistics
- temporal residual dynamics
- state/residual co-evolution
- self-correction candidates

Important:
    SELF_CORRECTION_CANDIDATE is an observational classification.
    It is NOT evidence that an LLM or other system internally implements
    a residual variable r or a literal equation r(x) = x.

Compatible with simple v1-style usage:
    field = ResidualField()
    field.add(Residual(value=3.0, direction=1))
    result = WashiWashiAnalyzer().analyze(field)
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from math import isfinite
from statistics import mean, pstdev
from typing import Any, Iterable, Optional, Sequence


EPS = 1e-12


# ============================================================
# Classification enums
# ============================================================

class ResidualFate(str, Enum):
    ACTIVE = "ACTIVE"
    PERSISTED = "PERSISTED"
    DECAYED = "DECAYED"
    AMPLIFIED = "AMPLIFIED"
    STAGNATED = "STAGNATED"
    CANCELLED = "CANCELLED"
    DISCARDED = "DISCARDED"
    REVERSED = "REVERSED"
    TRANSFORMED = "TRANSFORMED"
    UNKNOWN = "UNKNOWN"


class CorrectionStatus(str, Enum):
    NOT_TESTED = "NOT_TESTED"
    NO_EVIDENCE = "NO_EVIDENCE"
    STATE_PRESERVATION_CANDIDATE = "STATE_PRESERVATION_CANDIDATE"
    SELF_CORRECTION_CANDIDATE = "SELF_CORRECTION_CANDIDATE"
    RESIDUAL_PERSISTENCE_CANDIDATE = "RESIDUAL_PERSISTENCE_CANDIDATE"
    DIVERGENCE_CANDIDATE = "DIVERGENCE_CANDIDATE"


# ============================================================
# Core data structures
# ============================================================

@dataclass(frozen=True)
class Residual:
    """
    One experimenter-defined residual observation.

    value:
        Signed residual magnitude.

    direction:
        Optional explicit direction (-1, 0, +1).
        If omitted, it is inferred from value.

    weight:
        Aggregation weight. Must be non-negative.

    source:
        Observation source, e.g. "collatz", "llm-output", "simulation".

    step:
        Optional temporal index.

    mapping:
        Description/name of the mapping that produced this residual.
        Example: "delta = after - before".

    metadata:
        Free experimental metadata. It is not interpreted automatically.
    """

    value: float
    direction: Optional[int] = None
    weight: float = 1.0
    source: Optional[str] = None
    step: Optional[int] = None
    mapping: Optional[str] = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not isfinite(float(self.value)):
            raise ValueError("value must be finite")
        if not isfinite(float(self.weight)) or self.weight < 0:
            raise ValueError("weight must be finite and >= 0")

        inferred = sign(self.value)
        direction = inferred if self.direction is None else self.direction

        if direction not in (-1, 0, 1):
            raise ValueError("direction must be -1, 0, +1, or None")

        object.__setattr__(self, "direction", direction)


@dataclass
class ResidualField:
    """
    A residual collection.

    mapping_name / mapping_description are deliberately explicit because
    analyzer results are functions of the chosen residualization mapping.
    """

    residuals: list[Residual] = field(default_factory=list)
    mapping_name: Optional[str] = None
    mapping_description: Optional[str] = None
    source_description: Optional[str] = None
    metadata: dict[str, Any] = field(default_factory=dict)

    def add(self, residual: Residual) -> None:
        self.residuals.append(residual)

    def extend(self, residuals: Iterable[Residual]) -> None:
        self.residuals.extend(residuals)

    def clear(self) -> None:
        self.residuals.clear()

    @property
    def size(self) -> int:
        return len(self.residuals)

    def values(self) -> list[float]:
        return [r.value for r in self.residuals]

    def directions(self, include_zero: bool = True) -> list[int]:
        ds = [int(r.direction or 0) for r in self.residuals]
        return ds if include_zero else [d for d in ds if d != 0]


@dataclass(frozen=True)
class StateResidualFrame:
    """
    One time slice for state/residual co-evolution.

    state:
        Externally observable scalar state or scalar score.

    residual:
        Externally defined residual value at the same step.

    purpose_signal:
        Optional scalar representing an experimenter-defined purpose signal.
        The analyzer does not infer purpose from text or hidden model state.
    """

    step: int
    state: float
    residual: float
    purpose_signal: Optional[float] = None
    metadata: dict[str, Any] = field(default_factory=dict)


# ============================================================
# Static field analysis
# ============================================================

@dataclass
class WashiWashiResult:
    count: int

    total_residual: float
    mean_residual: float
    residual_std: float

    positive_mass: float
    negative_mass: float
    neutral_count: int

    vector_candidate: float
    vector_strength: float
    dominant_direction: int

    coherence: float
    persistence: float
    dispersion: float

    reversal_rate: float
    oscillation_score: float

    mapping_name: Optional[str] = None
    notes: list[str] = field(default_factory=list)


class WashiWashiAnalyzer:
    """
    Static residual-field analyzer.

    It reports properties of the supplied ResidualField.
    It does not infer problem semantics or hidden internal reasoning.
    """

    name = "washi_washi"

    def analyze(self, residual_field: ResidualField) -> WashiWashiResult:
        rs = residual_field.residuals

        if not rs:
            return WashiWashiResult(
                count=0,
                total_residual=0.0,
                mean_residual=0.0,
                residual_std=0.0,
                positive_mass=0.0,
                negative_mass=0.0,
                neutral_count=0,
                vector_candidate=0.0,
                vector_strength=0.0,
                dominant_direction=0,
                coherence=0.0,
                persistence=0.0,
                dispersion=0.0,
                reversal_rate=0.0,
                oscillation_score=0.0,
                mapping_name=residual_field.mapping_name,
                notes=["EMPTY_FIELD"],
            )

        values = [float(r.value) for r in rs]
        total = sum(values)
        avg = mean(values)
        std = pstdev(values) if len(values) > 1 else 0.0

        positive = sum(
            abs(r.value) * r.weight for r in rs if (r.direction or 0) > 0
        )
        negative = sum(
            abs(r.value) * r.weight for r in rs if (r.direction or 0) < 0
        )
        neutral_count = sum(1 for r in rs if (r.direction or 0) == 0)

        directional_mass = positive + negative

        if directional_mass > EPS:
            vector_candidate = (positive - negative) / directional_mass
        else:
            vector_candidate = 0.0

        vector_strength = abs(vector_candidate)

        if positive > negative:
            dominant = 1
        elif negative > positive:
            dominant = -1
        else:
            dominant = 0

        if directional_mass > EPS and dominant != 0:
            aligned_mass = sum(
                abs(r.value) * r.weight
                for r in rs
                if (r.direction or 0) == dominant
            )
            coherence = aligned_mass / directional_mass
        else:
            coherence = 0.0

        directions = [int(r.direction or 0) for r in rs if (r.direction or 0) != 0]
        persistence = consecutive_same_rate(directions)
        reversal_rate = consecutive_reversal_rate(directions)

        # Oscillation is deliberately a simple observable candidate:
        # frequent sign reversal with at least 3 directional observations.
        oscillation_score = reversal_rate if len(directions) >= 3 else 0.0

        # Keep v1-compatible dispersion semantics.
        dispersion = std / abs(avg) if abs(avg) > EPS else std

        notes: list[str] = []

        if vector_strength < 0.1:
            notes.append("NO_CLEAR_DIRECTION")
        elif vector_strength < 0.3:
            notes.append("WEAK_DIRECTIONAL_BIAS")
        elif vector_strength < 0.7:
            notes.append("MODERATE_DIRECTIONAL_BIAS")
        else:
            notes.append("STRONG_DIRECTIONAL_BIAS")

        if persistence > 0.7:
            notes.append("HIGH_PERSISTENCE")
        if dispersion > 2.0:
            notes.append("HIGH_DISPERSION")
        if reversal_rate > 0.7 and len(directions) >= 3:
            notes.append("OSCILLATION_CANDIDATE")

        return WashiWashiResult(
            count=len(values),
            total_residual=total,
            mean_residual=avg,
            residual_std=std,
            positive_mass=positive,
            negative_mass=negative,
            neutral_count=neutral_count,
            vector_candidate=vector_candidate,
            vector_strength=vector_strength,
            dominant_direction=dominant,
            coherence=coherence,
            persistence=persistence,
            dispersion=dispersion,
            reversal_rate=reversal_rate,
            oscillation_score=oscillation_score,
            mapping_name=residual_field.mapping_name,
            notes=notes,
        )


# ============================================================
# Residual temporal dynamics
# ============================================================

@dataclass(frozen=True)
class ResidualTransition:
    index: int
    previous: float
    current: float
    delta: float
    magnitude_ratio: Optional[float]
    fate: ResidualFate


@dataclass
class ResidualDynamicsResult:
    count: int
    transitions: list[ResidualTransition]

    decay_count: int
    persistence_count: int
    amplification_count: int
    stagnation_count: int
    cancellation_count: int
    reversal_count: int

    decay_rate: float
    persistence_rate: float
    amplification_rate: float
    reversal_rate: float

    net_magnitude_change: float
    notes: list[str] = field(default_factory=list)


class ResidualDynamicsAnalyzer:
    """
    Tracks how a scalar residual sequence changes over time.

    Classification is observational:
    - DECAYED: |r_t| becomes smaller
    - AMPLIFIED: |r_t| becomes larger
    - STAGNATED/PERSISTED: approximately unchanged
    - CANCELLED: reaches approximately zero
    - REVERSED: sign changes

    A sign reversal takes precedence over magnitude classification because
    it is structurally distinct.
    """

    name = "residual_dynamics"

    def __init__(
        self,
        *,
        abs_tolerance: float = 1e-9,
        relative_tolerance: float = 0.05,
    ) -> None:
        self.abs_tolerance = abs_tolerance
        self.relative_tolerance = relative_tolerance

    def analyze(
        self,
        data: ResidualField | Sequence[float],
    ) -> ResidualDynamicsResult:
        values = (
            [float(r.value) for r in data.residuals]
            if isinstance(data, ResidualField)
            else [float(v) for v in data]
        )

        transitions: list[ResidualTransition] = []

        for i, (previous, current) in enumerate(zip(values, values[1:]), start=1):
            fate, ratio = self._classify(previous, current)
            transitions.append(
                ResidualTransition(
                    index=i,
                    previous=previous,
                    current=current,
                    delta=current - previous,
                    magnitude_ratio=ratio,
                    fate=fate,
                )
            )

        total = len(transitions)

        def count(fate: ResidualFate) -> int:
            return sum(t.fate == fate for t in transitions)

        decay_count = count(ResidualFate.DECAYED)
        persistence_count = count(ResidualFate.PERSISTED)
        amplification_count = count(ResidualFate.AMPLIFIED)
        stagnation_count = count(ResidualFate.STAGNATED)
        cancellation_count = count(ResidualFate.CANCELLED)
        reversal_count = count(ResidualFate.REVERSED)

        rate = lambda n: n / total if total else 0.0

        notes: list[str] = []
        if rate(decay_count) > 0.6:
            notes.append("DECAY_DOMINANT")
        if rate(amplification_count) > 0.6:
            notes.append("AMPLIFICATION_DOMINANT")
        if rate(reversal_count) > 0.6:
            notes.append("REVERSAL_DOMINANT")
        if rate(persistence_count + stagnation_count) > 0.6:
            notes.append("RESIDUAL_RETENTION_CANDIDATE")

        net_change = (
            abs(values[-1]) - abs(values[0])
            if len(values) >= 2
            else 0.0
        )

        return ResidualDynamicsResult(
            count=len(values),
            transitions=transitions,
            decay_count=decay_count,
            persistence_count=persistence_count,
            amplification_count=amplification_count,
            stagnation_count=stagnation_count,
            cancellation_count=cancellation_count,
            reversal_count=reversal_count,
            decay_rate=rate(decay_count),
            persistence_rate=rate(persistence_count + stagnation_count),
            amplification_rate=rate(amplification_count),
            reversal_rate=rate(reversal_count),
            net_magnitude_change=net_change,
            notes=notes,
        )

    def _classify(
        self,
        previous: float,
        current: float,
    ) -> tuple[ResidualFate, Optional[float]]:

        ap = abs(previous)
        ac = abs(current)

        if ac <= self.abs_tolerance:
            return ResidualFate.CANCELLED, 0.0

        if ap <= self.abs_tolerance:
            return ResidualFate.AMPLIFIED, None

        ratio = ac / ap

        if sign(previous) != sign(current):
            return ResidualFate.REVERSED, ratio

        tolerance = max(
            self.abs_tolerance,
            self.relative_tolerance * ap,
        )

        magnitude_delta = ac - ap

        if abs(magnitude_delta) <= tolerance:
            # Exact-ish identity is marked as persisted; small numerical
            # movement around the same magnitude is stagnation.
            if abs(current - previous) <= self.abs_tolerance:
                return ResidualFate.PERSISTED, ratio
            return ResidualFate.STAGNATED, ratio

        if ac < ap:
            return ResidualFate.DECAYED, ratio

        return ResidualFate.AMPLIFIED, ratio


# ============================================================
# State / residual co-evolution and self-correction candidates
# ============================================================

@dataclass
class SelfCorrectionResult:
    status: CorrectionStatus

    frame_count: int
    state_change_start_to_end: float
    residual_change_start_to_end: float

    state_step_changes: list[float]
    residual_step_changes: list[float]

    state_convergence_score: float
    residual_reduction_score: float
    residual_persistence_score: float

    purpose_signal_present: bool
    purpose_signal_change: Optional[float]

    evidence: list[str] = field(default_factory=list)
    cautions: list[str] = field(default_factory=list)


class SelfCorrectionAnalyzer:
    """
    Tests an externally observable candidate for self-correction.

    This does NOT implement or assert literal r(x) = x internally.

    Operational candidate:
      1. state updates become small / converge,
      2. residual magnitude decreases,
      3. optionally, a purpose signal may be tracked independently.

    A different case is state preservation with residual persistence:
      x_(t+1) ~= x_t while |r| remains non-zero.
    That is classified separately and is NOT called self-correction.
    """

    name = "self_correction"

    def __init__(
        self,
        *,
        state_tolerance: float = 1e-6,
        residual_tolerance: float = 1e-6,
        convergence_window: int = 3,
    ) -> None:
        self.state_tolerance = state_tolerance
        self.residual_tolerance = residual_tolerance
        self.convergence_window = max(1, convergence_window)

    def analyze(
        self,
        frames: Sequence[StateResidualFrame],
    ) -> SelfCorrectionResult:

        if len(frames) < 2:
            return SelfCorrectionResult(
                status=CorrectionStatus.NOT_TESTED,
                frame_count=len(frames),
                state_change_start_to_end=0.0,
                residual_change_start_to_end=0.0,
                state_step_changes=[],
                residual_step_changes=[],
                state_convergence_score=0.0,
                residual_reduction_score=0.0,
                residual_persistence_score=0.0,
                purpose_signal_present=any(
                    f.purpose_signal is not None for f in frames
                ),
                purpose_signal_change=None,
                evidence=[],
                cautions=["AT_LEAST_TWO_FRAMES_REQUIRED"],
            )

        states = [float(f.state) for f in frames]
        residuals = [float(f.residual) for f in frames]

        state_changes = [
            b - a for a, b in zip(states, states[1:])
        ]
        residual_changes = [
            b - a for a, b in zip(residuals, residuals[1:])
        ]

        tail = state_changes[-self.convergence_window:]
        convergence_hits = sum(
            abs(dx) <= self.state_tolerance for dx in tail
        )
        state_convergence_score = (
            convergence_hits / len(tail) if tail else 0.0
        )

        residual_pairs = list(zip(residuals, residuals[1:]))
        reduction_hits = sum(
            abs(b) < abs(a) - self.residual_tolerance
            for a, b in residual_pairs
        )
        residual_reduction_score = (
            reduction_hits / len(residual_pairs)
            if residual_pairs else 0.0
        )

        nonzero_persistent_hits = sum(
            abs(b) > self.residual_tolerance
            and abs(abs(b) - abs(a)) <= self.residual_tolerance
            for a, b in residual_pairs
        )
        residual_persistence_score = (
            nonzero_persistent_hits / len(residual_pairs)
            if residual_pairs else 0.0
        )

        purpose_values = [
            float(f.purpose_signal)
            for f in frames
            if f.purpose_signal is not None
        ]
        purpose_present = bool(purpose_values)
        purpose_change = (
            purpose_values[-1] - purpose_values[0]
            if len(purpose_values) >= 2
            else None
        )

        evidence: list[str] = []
        cautions: list[str] = [
            "CLASSIFICATION_IS_EXTERNAL_AND_OPERATIONAL",
            "DOES_NOT_ESTABLISH_AN_INTERNAL_RESIDUAL_VARIABLE",
        ]

        state_preserved = (
            state_convergence_score >= 0.8
            and abs(states[-1] - states[-2]) <= self.state_tolerance
        )
        residual_reduced = (
            abs(residuals[-1]) <
            abs(residuals[0]) - self.residual_tolerance
        )
        residual_nonzero = abs(residuals[-1]) > self.residual_tolerance
        residual_persisted = residual_persistence_score >= 0.5

        if state_preserved:
            evidence.append("STATE_CONVERGENCE_OBSERVED")

        if residual_reduced:
            evidence.append("RESIDUAL_MAGNITUDE_REDUCED")

        if residual_nonzero:
            evidence.append("NONZERO_RESIDUAL_REMAINS")

        if residual_persisted:
            evidence.append("RESIDUAL_PERSISTENCE_OBSERVED")

        # Conservative ordering.
        if state_preserved and residual_reduced:
            status = CorrectionStatus.SELF_CORRECTION_CANDIDATE

        elif state_preserved and residual_nonzero and residual_persisted:
            status = CorrectionStatus.RESIDUAL_PERSISTENCE_CANDIDATE

        elif state_preserved:
            status = CorrectionStatus.STATE_PRESERVATION_CANDIDATE

        elif abs(residuals[-1]) > abs(residuals[0]) + self.residual_tolerance:
            status = CorrectionStatus.DIVERGENCE_CANDIDATE
            evidence.append("RESIDUAL_MAGNITUDE_INCREASED")

        else:
            status = CorrectionStatus.NO_EVIDENCE

        if purpose_present:
            cautions.append(
                "PURPOSE_SIGNAL_IS_EXPERIMENTER_DEFINED_AND_NOT_INFERRED"
            )

        return SelfCorrectionResult(
            status=status,
            frame_count=len(frames),
            state_change_start_to_end=states[-1] - states[0],
            residual_change_start_to_end=residuals[-1] - residuals[0],
            state_step_changes=state_changes,
            residual_step_changes=residual_changes,
            state_convergence_score=state_convergence_score,
            residual_reduction_score=residual_reduction_score,
            residual_persistence_score=residual_persistence_score,
            purpose_signal_present=purpose_present,
            purpose_signal_change=purpose_change,
            evidence=evidence,
            cautions=cautions,
        )


# ============================================================
# Composite report
# ============================================================

@dataclass
class T3ResidualReport:
    field: WashiWashiResult
    dynamics: ResidualDynamicsResult
    self_correction: Optional[SelfCorrectionResult]
    boundary_notes: list[str]


class T3ResidualAnalyzer:
    """
    Convenience facade combining the three analyzers.

    Static field:
        What does the supplied residual field look like?

    Dynamics:
        How does residual magnitude/sign evolve?

    Self-correction:
        Does an externally supplied state/residual trajectory meet a
        conservative self-correction candidate definition?
    """

    name = "t3_residual_complete"

    def __init__(
        self,
        field_analyzer: Optional[WashiWashiAnalyzer] = None,
        dynamics_analyzer: Optional[ResidualDynamicsAnalyzer] = None,
        correction_analyzer: Optional[SelfCorrectionAnalyzer] = None,
    ) -> None:
        self.field_analyzer = field_analyzer or WashiWashiAnalyzer()
        self.dynamics_analyzer = (
            dynamics_analyzer or ResidualDynamicsAnalyzer()
        )
        self.correction_analyzer = (
            correction_analyzer or SelfCorrectionAnalyzer()
        )

    def analyze(
        self,
        residual_field: ResidualField,
        frames: Optional[Sequence[StateResidualFrame]] = None,
    ) -> T3ResidualReport:

        field_result = self.field_analyzer.analyze(residual_field)
        dynamics_result = self.dynamics_analyzer.analyze(residual_field)

        correction_result = (
            self.correction_analyzer.analyze(frames)
            if frames is not None
            else None
        )

        boundary_notes = [
            "RESULTS_DESCRIBE_THE_SUPPLIED_MAPPING_NOT_HIDDEN_SEMANTICS",
            "VECTOR_CANDIDATE_IS_A_SUMMARY_NOT_A_PROVEN_FORCE",
            "RESIDUAL_DYNAMICS_DO_NOT_ESTABLISH_CAUSALITY",
        ]

        if residual_field.mapping_name is None:
            boundary_notes.append("MAPPING_NAME_NOT_SPECIFIED")

        return T3ResidualReport(
            field=field_result,
            dynamics=dynamics_result,
            self_correction=correction_result,
            boundary_notes=boundary_notes,
        )


# ============================================================
# Mapping helpers
# ============================================================

def sign(value: float, tolerance: float = EPS) -> int:
    if value > tolerance:
        return 1
    if value < -tolerance:
        return -1
    return 0


def residual_from_delta(
    before: float,
    after: float,
    *,
    source: Optional[str] = None,
    step: Optional[int] = None,
    weight: float = 1.0,
    metadata: Optional[dict[str, Any]] = None,
) -> Residual:
    """
    Explicit mapping:
        r = after - before
    """
    delta = float(after) - float(before)

    return Residual(
        value=delta,
        direction=sign(delta),
        weight=weight,
        source=source,
        step=step,
        mapping="delta = after - before",
        metadata=metadata or {},
    )


def field_from_sequence(
    values: Sequence[float],
    *,
    source: Optional[str] = None,
    mapping_name: str = "adjacent_delta",
) -> ResidualField:
    """
    Converts a scalar sequence x_0...x_n into adjacent differences:
        r_t = x_(t+1) - x_t

    This is a chosen experimental mapping, not an intrinsic residual.
    """

    residuals = [
        residual_from_delta(
            before,
            after,
            source=source,
            step=i,
        )
        for i, (before, after) in enumerate(zip(values, values[1:]))
    ]

    return ResidualField(
        residuals=residuals,
        mapping_name=mapping_name,
        mapping_description="r_t = x_(t+1) - x_t",
        source_description=source,
    )


def frames_from_sequences(
    states: Sequence[float],
    residuals: Sequence[float],
    *,
    purpose_signals: Optional[Sequence[Optional[float]]] = None,
) -> list[StateResidualFrame]:
    if len(states) != len(residuals):
        raise ValueError("states and residuals must have the same length")

    if purpose_signals is not None and len(purpose_signals) != len(states):
        raise ValueError(
            "purpose_signals must have the same length as states"
        )

    if purpose_signals is None:
        purpose_signals = [None] * len(states)

    return [
        StateResidualFrame(
            step=i,
            state=float(state),
            residual=float(residual),
            purpose_signal=(
                None if purpose is None else float(purpose)
            ),
        )
        for i, (state, residual, purpose) in enumerate(
            zip(states, residuals, purpose_signals)
        )
    ]


# ============================================================
# Sequence helpers
# ============================================================

def consecutive_same_rate(directions: Sequence[int]) -> float:
    if len(directions) < 2:
        return 0.0

    same = sum(
        a == b for a, b in zip(directions, directions[1:])
    )
    return same / (len(directions) - 1)


def consecutive_reversal_rate(directions: Sequence[int]) -> float:
    nonzero = [d for d in directions if d != 0]

    if len(nonzero) < 2:
        return 0.0

    reversals = sum(
        a != b for a, b in zip(nonzero, nonzero[1:])
    )
    return reversals / (len(nonzero) - 1)


# ============================================================
# Minimal smoke test / examples
# ============================================================

def _demo() -> None:
    print("=== T3 Residual Complete Demo ===")

    # P4-like Collatz residual example.
    collatz_delta = [55, -41, 83, -62, -31, 63, -47, 95, -71, 143]

    field = ResidualField(
        residuals=[
            Residual(
                value=v,
                source="collatz-27-demo",
                step=i,
                mapping="delta = n_(t+1) - n_t",
            )
            for i, v in enumerate(collatz_delta)
        ],
        mapping_name="collatz_adjacent_delta",
        mapping_description="r_t = n_(t+1) - n_t",
        source_description="Collatz n=27, first 10 transitions",
    )

    report = T3ResidualAnalyzer().analyze(field)

    print("\n[FIELD]")
    print(report.field)

    print("\n[DYNAMICS]")
    for transition in report.dynamics.transitions:
        print(transition)

    # Synthetic self-correction candidate.
    #
    # State changes become tiny while residual magnitude shrinks.
    # This is deliberately synthetic: it demonstrates the classifier,
    # not a claim about an LLM.
    frames = frames_from_sequences(
        states=[0.0, 0.6, 0.9, 0.99, 1.0, 1.0, 1.0],
        residuals=[1.0, 0.6, 0.3, 0.1, 0.02, 0.005, 0.001],
    )

    correction = SelfCorrectionAnalyzer(
        state_tolerance=0.02,
        residual_tolerance=1e-6,
        convergence_window=3,
    ).analyze(frames)

    print("\n[SELF-CORRECTION CANDIDATE TEST]")
    print(correction)


if __name__ == "__main__":
    _demo()
