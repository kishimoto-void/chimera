# t3_core/residual_swarm.py
#
# T3 Residual "WASHIWASHI" Analyzer
#
# Purpose:
#   多数の残差を観測し、
#   - 分布
#   - 方向性
#   - 持続性
#   - 偏り
#   - 実効ベクトル候補
# を抽出する。
#
# IMPORTANT:
#   このモジュールは「ベクトルが存在する」と仮定しない。
#   vector は residual field から計算された候補である。
#
#   RESIDUAL → FIELD → VECTOR CANDIDATE
#
# T3 experimental module.


from __future__ import annotations

from dataclasses import dataclass, field
from math import sqrt
from statistics import mean, pstdev
from typing import Iterable, Optional


# ============================================================
# Residual
# ============================================================

@dataclass(frozen=True)
class Residual:
    """
    1つの残差。

    value:
        残差の値。

    direction:
        方向。
        1  = 正方向
        -1 = 負方向
        0  = 中立

    weight:
        その残差を集約するときの重み。

    source:
        任意の観測元。
        例: "collatz", "llm", "simulation"
    """

    value: float
    direction: int
    weight: float = 1.0
    source: Optional[str] = None

    def __post_init__(self):
        if self.direction not in (-1, 0, 1):
            raise ValueError("direction must be -1, 0, or 1")

        if self.weight < 0:
            raise ValueError("weight must be >= 0")


# ============================================================
# Residual Field
# ============================================================

@dataclass
class ResidualField:
    """
    現在観測されている「わしゃわしゃした残差群」。
    """

    residuals: list[Residual] = field(default_factory=list)

    def add(self, residual: Residual) -> None:
        self.residuals.append(residual)

    def extend(self, residuals: Iterable[Residual]) -> None:
        self.residuals.extend(residuals)

    def clear(self) -> None:
        self.residuals.clear()

    @property
    def size(self) -> int:
        return len(self.residuals)


# ============================================================
# Analysis Result
# ============================================================

@dataclass
class WashiwashiResult:
    """
    残差場の解析結果。

    vector_candidate:
        残差から抽出された実効方向候補。

    vector_strength:
        方向の偏りの強さ。

    coherence:
        残差方向のまとまり具合。

    persistence:
        同方向残差の連続性。

    dispersion:
        残差の散らばり。

    NOTE:
        これらは「意味」ではなく観測量。
    """

    count: int

    total_residual: float
    mean_residual: float
    residual_std: float

    positive_mass: float
    negative_mass: float

    vector_candidate: float
    vector_strength: float

    coherence: float
    persistence: float
    dispersion: float

    dominant_direction: int

    notes: list[str] = field(default_factory=list)


# ============================================================
# Analyzer
# ============================================================

class WashiwashiAnalyzer:
    """
    T3 Core に接続するための最小残渣解析器。

    役割:

        Residuals
            ↓
        Residual Field
            ↓
        Statistics
            ↓
        Directionality
            ↓
        Vector Candidate

    まだ「ベクトル」とは断定しない。
    """

    name = "washi_washi"

    def analyze(
        self,
        field: ResidualField,
    ) -> WashiwashiResult:

        if not field.residuals:
            return WashiwashiResult(
                count=0,
                total_residual=0.0,
                mean_residual=0.0,
                residual_std=0.0,
                positive_mass=0.0,
                negative_mass=0.0,
                vector_candidate=0.0,
                vector_strength=0.0,
                coherence=0.0,
                persistence=0.0,
                dispersion=0.0,
                dominant_direction=0,
                notes=["EMPTY_FIELD"],
            )

        values = [r.value for r in field.residuals]

        total = sum(values)
        avg = mean(values)

        std = pstdev(values) if len(values) > 1 else 0.0

        # ----------------------------------------------------
        # Directional mass
        # ----------------------------------------------------

        positive = sum(
            abs(r.value) * r.weight
            for r in field.residuals
            if r.direction > 0
        )

        negative = sum(
            abs(r.value) * r.weight
            for r in field.residuals
            if r.direction < 0
        )

        total_mass = positive + negative

        if total_mass > 0:
            vector_candidate = (
                (positive - negative)
                / total_mass
            )
        else:
            vector_candidate = 0.0

        vector_strength = abs(vector_candidate)

        # ----------------------------------------------------
        # Coherence
        # ----------------------------------------------------

        nonzero = [
            r for r in field.residuals
            if r.direction != 0
        ]

        if nonzero:

            dominant = (
                1
                if positive > negative
                else -1
                if negative > positive
                else 0
            )

            aligned_mass = sum(
                abs(r.value) * r.weight
                for r in nonzero
                if r.direction == dominant
            )

            coherence = (
                aligned_mass / total_mass
                if total_mass > 0
                else 0.0
            )

        else:
            dominant = 0
            coherence = 0.0

        # ----------------------------------------------------
        # Persistence
        #
        # 同方向が連続している割合。
        # 時系列データを与えた場合のみ意味を持つ。
        # ----------------------------------------------------

        persistence = self._persistence(
            field.residuals
        )

        # ----------------------------------------------------
        # Dispersion
        # ----------------------------------------------------

        if abs(avg) > 1e-12:
            dispersion = std / abs(avg)
        else:
            dispersion = std

        notes = []

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

        return WashiwashiResult(
            count=len(values),

            total_residual=total,
            mean_residual=avg,
            residual_std=std,

            positive_mass=positive,
            negative_mass=negative,

            vector_candidate=vector_candidate,
            vector_strength=vector_strength,

            coherence=coherence,
            persistence=persistence,
            dispersion=dispersion,

            dominant_direction=dominant,

            notes=notes,
        )

    # --------------------------------------------------------
    # Persistence
    # --------------------------------------------------------

    @staticmethod
    def _persistence(
        residuals: list[Residual],
    ) -> float:

        directions = [
            r.direction
            for r in residuals
            if r.direction != 0
        ]

        if len(directions) < 2:
            return 0.0

        same = 0

        for a, b in zip(
            directions,
            directions[1:],
        ):
            if a == b:
                same += 1

        return same / (len(directions) - 1)


# ============================================================
# Utility
# ============================================================

def residual_from_delta(
    before: float,
    after: float,
    source: Optional[str] = None,
) -> Residual:
    """
    状態差分から Residual を作る。

        residual = after - before
    """

    delta = after - before

    direction = (
        1 if delta > 0
        else -1 if delta < 0
        else 0
    )

    return Residual(
        value=delta,
        direction=direction,
        source=source,
    )


# ============================================================
# Minimal Example
# ============================================================

if __name__ == "__main__":

    field = ResidualField()

    # わしゃわしゃした残差
    samples = [
        3.0,
        -1.0,
        2.0,
        4.0,
        -2.0,
        3.0,
        1.0,
        -0.5,
        2.0,
    ]

    for x in samples:

        direction = (
            1 if x > 0
            else -1 if x < 0
            else 0
        )

        field.add(
            Residual(
                value=x,
                direction=direction,
                source="demo",
            )
        )

    analyzer = WashiwashiAnalyzer()

    result = analyzer.analyze(field)

    print("=== T3 WASHIWASHI ===")
    print("count:", result.count)
    print("mean:", result.mean_residual)
    print("std:", result.residual_std)
    print("positive_mass:", result.positive_mass)
    print("negative_mass:", result.negative_mass)
    print("vector_candidate:", result.vector_candidate)
    print("vector_strength:", result.vector_strength)
    print("coherence:", result.coherence)
    print("persistence:", result.persistence)
    print("dispersion:", result.dispersion)
    print("dominant_direction:", result.dominant_direction)
    print("notes:", result.notes)
