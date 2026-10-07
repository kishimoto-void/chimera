# t3_core/problem_chase.py

from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class ProblemState:
    t: int
    problem: Any
    gamma: Any = None
    delta: Any = None
    note: Optional[str] = None


@dataclass
class ProblemChase:
    history: list[ProblemState] = field(default_factory=list)

    def observe(
        self,
        problem: Any,
        *,
        gamma=None,
        delta=None,
        note=None,
    ) -> ProblemState:
        state = ProblemState(
            t=len(self.history),
            problem=problem,
            gamma=gamma,
            delta=delta,
            note=note,
        )
        self.history.append(state)
        return state

    def chase(self) -> list[dict[str, Any]]:
        """問題がどのように変化したかを時系列で返す。"""
        result = []

        for i in range(1, len(self.history)):
            prev = self.history[i - 1]
            curr = self.history[i]

            result.append({
                "from": prev.t,
                "to": curr.t,
                "problem_changed": prev.problem != curr.problem,
                "gamma_changed": prev.gamma != curr.gamma,
                "delta_changed": prev.delta != curr.delta,
                "problem_before": prev.problem,
                "problem_after": curr.problem,
                "note": curr.note,
            })

        return result

    def trace(self) -> list[ProblemState]:
        return list(self.history)

    def last(self) -> Optional[ProblemState]:
        return self.history[-1] if self.history else None
