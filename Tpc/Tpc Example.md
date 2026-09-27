Tpc Example

"x + D?% ≌ z" — Persistent Drift Exploration

この例では、Tpcの基本的な探索構造を、単純化した問題を使って説明する。

---

1. Basic Frame

Tpcでは、問題を次の不全フレームとして扱う。

x + D?% ≌ z

ここで、

x    = 現在保持している情報
D?%  = 未確定な差分・変換・探索領域
z    = 現在の観測対象
≌    = 探索・変形・近似・収束を含む関係

"D?%" は最初から確定した変数ではない。

探索によって候補が発生し、次の状態へ引き継がれる。

---

2. Example Problem

例として次の問題を与える。

A → Z

ただし、AからZへの変換経路は与えられていない。

通常の問題解決では、

A → ? → Z

の "?" を直接求めようとする。

Tpcでは、この未知領域を "D?%" として保持する。

A + D?% ≌ Z

---

3. Exploration Prompt

あなたはTpc探索ノードです。

以下の不全フレームを探索してください。

A + D?% ≌ Z

D?%を単一の答えとして確定してはいけません。

複数の可能な変換経路を生成してください。

各候補について、

1. 何が変化したか
2. どの中間状態を仮定したか
3. AとZの関係をどのように解釈したか

を記録してください。

さらに、既存の候補とは異なる探索方向があれば、
それを新しい候補として保持してください。

最終的に、

Observation
Candidate
Hypothesis
Verification Status

を分離してください。

---

4. Minimal State Model

Tpcでは探索状態を保持する。

from dataclasses import dataclass, field


@dataclass
class TpcState:
    x: str
    z: str
    history: list = field(default_factory=list)
    step: int = 0

    def snapshot(self):
        return {
            "step": self.step,
            "x": self.x,
            "z": self.z,
            "history": self.history.copy(),
        }

    def observe(self, d_candidate, observed_z):
        self.history.append({
            "step": self.step,
            "x": self.x,
            "D?%": d_candidate,
            "z": observed_z,
        })

        self.x = observed_z
        self.z = observed_z
        self.step += 1

---

5. Iterative Exploration

最初の状態：

x₀ = A
z₀ = Z

A + D?₀% ≌ Z

探索によって例えば、

D?₀ = "direct transformation"

が得られたとする。

次の状態では、その結果を保持する。

x₁ + D?₁% ≌ z₁

さらに別の探索を行う。

x₁ + D?₁% ≌ z₁
          ↓
        drift
          ↓
x₂ + D?₂% ≌ z₂

これを繰り返す。

x₀ + D?₀% ≌ z₀
        ↓
x₁ + D?₁% ≌ z₁
        ↓
x₂ + D?₂% ≌ z₂
        ↓
x₃ + D?₃% ≌ z₃
        ↓
...

---

6. Important Difference

Tpcでは、"D?%" を毎回消去しない。

通常の探索:

x + ? → z
       ↓
      解
       ↓
     終了

ではなく、

Tpc:

x₀ + D?₀% ≌ z₀
       ↓
     保持
       ↓
x₁ + D?₁% ≌ z₁
       ↓
     保持
       ↓
x₂ + D?₂% ≌ z₂
       ↓
     ...

とする。

つまり、探索履歴そのものが次の探索状態の一部になる。

---

7. Drift

異なるLLMや異なる探索条件を通すことで、"D?%" の候補が変化する。

             ┌─ D?₁ ─→ z
             │
x ───────────┼─ D?₂ ─→ z
             │
             ├─ D?₃ ─→ z
             │
             └─ D?₄ ─→ z
                    ↓
                  drift
                    ↓
             新しい候補空間

ここで重要なのは、

drift ≠ discovery

である。

ドリフトによって得られたものは、まず観測データとして保持する。

その後、

Observation
      ↓
Hypothesis
      ↓
Verification
      ↓
Reusable mechanism?

という順番で扱う。

---

8. Human Conductor

Tpcでは、人間が探索を終了させることができる。

LLM側は、

≌

を繰り返しながら候補を探索する。

人間は、

≌ ≌ ≌ ≌
        ↓
        =

として、必要な時点で探索結果を確定する。

したがって、

LLM
  = exploration / transformation

Human
  = selection / verification / closure

という役割分担になる。

---

9. What This Example Demonstrates

この単純な例でTpcが扱おうとしているものは、

- 未知領域を即座に確定しない
- 複数の候補を保持する
- 探索結果を次の状態へ引き継ぐ
- LLM間の差異を探索資源として扱う
- ドリフトを観測する
- 最後の確定判断を人間が行う

という構造である。

この例はTpcの完成形を示すものではない。

あくまで、

x + D?% ≌ z

という考え方を実験可能な状態へ落とすための最小モデルである。
