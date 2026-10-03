# T2 リポジトリ構築・実装指示書

## 目的

現在のT2を「LLM-First Execution Protocol」として整理し、GitHubリポジトリにそのまま配置できる状態にする。

今回の作業では、T2の仕様そのものを勝手に変更しない。

特に現行の実行系列は以下を基準とする。

```text
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
```

---

# 1. 最初にやること

以下のファイルを作る。

```text
README.md

docs/
├── T2_DESIGN.md
├── T2_EXECUTION.md
├── T2_EXPERIMENT_PROTOCOL.md
├── T2_GLOSSARY.md
└── T2_RESULTS.md

prompts/
└── T2_v1.0.md

examples/
└── 3d_triangle/
    ├── README.md
    ├── original_problem.py
    ├── material.py
    ├── scale.py
    └── run.py

experiments/
├── problems/
├── runs/
└── analysis/

tests/

CHANGELOG.md
LICENSE
```

---

# 2. T2_EXECUTION.md

## ここに入れるもの

今回提示した

**T2 LLM-First Execution Protocol
Chaos Margin / ≌C 拡張版**

を基本的にそのまま正式な実行仕様として配置する。

必ず以下を含める。

```text
Execution Rule

STATE 0 — INPUT
STATE 1 — MATERIAL
STATE 2 — SCALE
STATE 3 — DRIFT
STATE 4 — ≌C STRUCTURAL COMPARISON
STATE 5 — HYPOTHESIS
STATE 6 — DIFFUSION
STATE 7 — CONVERGENCE

CHAOS MARGIN PRINCIPLE
RESEARCH NOTE
CORE PRINCIPLE
```

重要：

この文書では説明を勝手に高度化しない。

T2が何をするかではなく、

**LLMがT2をどう実行するか**

を定義する文書にする。

---

# 3. prompts/T2_v1.0.md

これは実際にLLMへ投入するプロンプト。

原則：

```text
T2_EXECUTION.md
    ↓
実行規則を抽出
    ↓
T2_v1.0.md
    ↓
LLMへ投入
```

仕様書と実行プロンプトを混ぜない。

プロンプトでは、

- 現在のState
- 現在のMaterial
- 実行するOperator
- State Output
- 次Stateへの受け渡し
- premature collapse禁止

を明示する。

---

# 4. examples/3d_triangle/

ここが今回重要。

3D三角形数式を、

**T2が実際にどう処理するかを見るためのcanonical example**

として配置する。

ただし注意。

## 元の数式・コードが手元に存在しない場合

勝手に新しい3D三角形問題を「元コード」として捏造しない。

まず既存ファイル・過去成果物から元の数式/コードを探す。

見つかった場合：

```text
original_problem.py
```

に原型を保存する。

見つからない場合：

```text
original_problem.py
```

は仮ファイルとして扱い、

```text
TODO:
Original 3D triangle formulation
```

などと明記する。

---

# 5. 3D triangle exampleの役割

このExampleでは、

```text
Original Mathematical Problem
        ↓
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
```

を追跡できるようにする。

例えばMaterialでは、

```text
variables
relations
constraints
structure
differences
```

を明示する。

Scaleでは、

```text
元表現
↓
別の観測粒度・表現
```

を作る。

Driftでは、

```text
何が保存されたか
何が変化したか
何が消えたか
何が新しく現れたか
```

を記録する。

≌Cでは、

```text
preserved
transferable
transformed
residual
emergent
chaos_margin
```

を記録する。

Hypothesisでは複数候補を残す。

Diffusionでは候補を展開する。

Convergenceでは、

```text
structural coherence
explanatory usefulness
transferable structure
stability across Scale
residual size
emergent value
```

を基準に整理する。

---

# 6. README.md

READMEは研究論文ではなく、

**「このリポジトリは何なのか」**

を最初に理解するための入口にする。

最初に必ず、

```text
T2 is an LLM-First Execution Protocol.
```

という位置づけを置く。

次に、

```text
INPUT
→ MATERIAL
→ SCALE
→ DRIFT
→ ≌C
→ HYPOTHESIS
→ DIFFUSION
→ CONVERGENCE
```

を表示する。

その後、

- Materialとは何か
- Scaleとは何か
- Driftとは何か
- ≌Cとは何か
- Chaos Marginとは何か
- Hypothesisとは何か
- Diffusionとは何か
- Convergenceとは何か

を短く説明する。

READMEでは細かい数学的主張を増やさない。

詳細はdocsへ誘導する。

---

# 7. T2_DESIGN.md

ここは「なぜこの構造になっているか」を整理する文書。

扱うもの：

- T2の設計目的
- Material中心設計
- Scale
- Drift
- ≌C
- Chaos Margin
- Hypothesis
- Diffusion
- Convergence
- Residual
- 再探索
- pseudo-MAS的解釈
- 非目標

ただし、

**実行順序そのものの正式仕様はT2_EXECUTION.mdを優先する。**

---

# 8. T2_EXPERIMENT_PROTOCOL.md

T2を固定した後の実験方法。

最低限、以下を固定する。

```text
T2 Version
Problem ID
LLM
Prompt Version
External Information
Sampling Settings
Token Budget
Number of Runs
Baseline
T2 Condition
Ablation Condition
Evaluation Metrics
```

評価指標候補：

```text
Material Count
Drift Count
Emergent Count
Hypothesis Branch Count
Re-convergence Count
Premature Closure
Traceability
Validity
Accuracy
Token Usage
Step Count
Reproducibility
```

---

# 9. T2_RESULTS.md

ここには仕様を書かない。

実験結果だけを追加する。

形式例：

```text
## Experiment E001

Problem:
Model:
T2 Version:
Prompt:
Runs:

Baseline:
...

T2:
...

Observations:
...

Metrics:
...

Limitations:
...
```

重要：

結果から、

```text
T2は必ず性能が上がる
T2はLLMを賢くする
T2はMASより優れている
```

などの一般化をしない。

観測されたデータと解釈を分離する。

---

# 10. T2_GLOSSARY.md

用語を固定する。

最低限：

```text
Material
M_input
M_external
M_derived
M_emergent
M_residual
Scale
Drift
≌C
Structural Correspondence
Chaos Margin
Hypothesis
Diffusion
Convergence
Residual
Emergent
Traceability
Premature Closure
```

同じ用語を別の意味で使わない。

---

# 11. CHANGELOG.md

バージョン変更を記録。

現在の基準を、

```text
T2 v1.0
```

として扱う場合、

```text
## v1.0

- Initial frozen LLM-First Execution Protocol
- INPUT → MATERIAL → SCALE → DRIFT → ≌C → HYPOTHESIS → DIFFUSION → CONVERGENCE
- Chaos Margin introduced as structural tolerance
```

程度から開始する。

仕様変更をした場合は、

```text
v1.1
v1.2
...
```

とする。

---

# 12. 重要なバージョニングルール

T2の仕様を実験途中で頻繁に変更しない。

原則：

```text
T2 v1.0
↓
FREEZE
↓
実験
↓
結果追加
```

仕様を変更する必要が出た場合：

```text
T2 v1.1
```

などの新バージョンにする。

実験結果は、

**どのT2バージョンで得られたか**

を必ず記録する。

---

# 13. AXIOMとの関係

現段階ではT2を独立プロジェクトとして扱う。

```text
T2
│
├── standalone validation
│
└── future possibility
        ↓
      AXIOM
```

AXIOMに組み込むことを前提としてT2の仕様を変更しない。

まずT2単体で検証する。

---

# 14. やってはいけないこと

以下は禁止。

### 1

元の3D三角形コードがないのに創作して、

```text
original_problem.py
```

として扱う。

### 2

T2の各Stateを勝手に別の概念へ置き換える。

### 3

Chaos Marginを既に数学的に確立された理論として扱う。

### 4

T2をAGI、意識、認知理論などの証明として扱う。

### 5

T2が通常のLLMより必ず高性能だと主張する。

### 6

T2を実際の分散MASと同一視する。

### 7

実験結果と設計思想を混ぜる。

### 8

実験途中で仕様をこっそり変更する。

---

# 15. 今やる作業順

迷ったら、この順番。

```text
① T2_EXECUTION.md
        ↓
② prompts/T2_v1.0.md
        ↓
③ 3D triangle original code探索
        ↓
④ examples/3d_triangle/
        ↓
⑤ T2_EXPERIMENT_PROTOCOL.md
        ↓
⑥ T2_GLOSSARY.md
        ↓
⑦ T2_RESULTS.md
        ↓
⑧ README.md最終調整
        ↓
⑨ CHANGELOG.md
        ↓
⑩ GitHubへ配置
```

---

# 16. 今回の最優先

現時点で全部完成させようとしない。

まず、

```text
T2_EXECUTION.md
+
T2_v1.0.md
```

を完成させる。

その後、

```text
3D triangle example
```

を接続する。

この3つが揃えば、

**「T2とは何か」**
ではなく、

**「T2をLLMにどう実行させるか」**

まで再現可能になる。

---

# 17. 最終的なリポジトリの考え方

最終的には、

```text
README
  ↓
DESIGN
  ↓
EXECUTION
  ↓
PROMPT
  ↓
EXAMPLE
  ↓
EXPERIMENT
  ↓
RESULTS
```

という階層にする。

役割は混ぜない。

```text
README     = 入口
DESIGN     = 設計
EXECUTION  = 実行仕様
PROMPT     = LLM投入物
EXAMPLE    = 実例
EXPERIMENT = 実験
RESULTS    = 観測結果
GLOSSARY   = 用語
CHANGELOG  = 変更履歴
```

これでT2を「アイデア」から「再現可能なプロトコル」に移す。
