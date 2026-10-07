# t3_core/washiwasha_chase.py
from dataclasses import dataclass, field
from typing import Any, Optional


@dataclass
class Trace:
    t: int
    gamma: Any = None
    delta: Any = None
    is_state: Any = None
    theta: Any = None
    output: Any = None
    note: Optional[str] = None


@dataclass
class WashiwashaChase:
    traces: list[Trace] = field(default_factory=list)

    def observe(
        self,
        *,
        gamma=None,
        delta=None,
        is_state=None,
        theta=None,
        output=None,
        note=None,
    ) -> Trace:
        """現在状態を記録する。意味付けはしない。"""
        trace = Trace(
            t=len(self.traces),
            gamma=gamma,
            delta=delta,
            is_state=is_state,
            theta=theta,
            output=output,
            note=note,
        )
        self.traces.append(trace)
        return trace

    def diff(self, a: int, b: int) -> dict[str, Any]:
        """2時点の観測値を機械的に比較する。"""
        x = self.traces[a]
        y = self.traces[b]

        return {
            "gamma_changed": x.gamma != y.gamma,
            "delta_changed": x.delta != y.delta,
            "is_changed": x.is_state != y.is_state,
            "theta_changed": x.theta != y.theta,
            "output_changed": x.output != y.output,
        }

    def chase(self) -> list[dict[str, Any]]:
        """
        変化した箇所を時系列で返す。
        「わしゃわしゃ」とは判定しない。
        """
        result = []

        for i in range(1, len(self.traces)):
            d = self.diff(i - 1, i)

            changed = [k for k, v in d.items() if v]

            if changed:
                result.append({
                    "from": i - 1,
                    "to": i,
                    "changed": changed,
                })

        return result

    def last(self) -> Optional[Trace]:
        return self.traces[-1] if self.traces else None
