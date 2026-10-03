T2 Repository README Generation Prompt

あなたは、研究プロトタイプ T2 のGitHub Repository READMEを作成する技術文書編集者です。

以下の仕様・思想・実験方針を理解したうえで、T2単独RepositoryのREADME.mdを作成してください。

READMEは単なるコード説明ではありません。

T2が

- 何を問題としているのか
- 「Material（マテリアル）」とは何か
- なぜ通常のLLMプロンプトと異なるのか
- T2は何を生成・操作・観測しているのか
- Scale / Drift / Observation / Reasoning / ≌ / Hypothesis Generation / Diffusion / Convergence / Field Update / Re-diffusion / Re-convergence が何を意味するのか
- なぜ拡散と収束を繰り返すのか
- T2と通常のLLMによる直接回答の違い
- T2をMASやAXIOMへ統合する以前に、なぜ単独システムとして検証するのか
- 何が仕様として固定され、何が実験データとして更新されるのか

を、第三者がRepositoryだけを読んで理解できるようにしてください。

---

1. T2とは何か

最初にT2を明確に定義してください。

T2は単なる「AIエージェント」や「プロンプト集」ではない。

T2は、問題そのものを直接解答することよりも、

«問題から構造を抽出し、Materialを形成し、構造変換・対応関係・仮説生成・拡散・収束を通じて、問題を解く可能性のある構造を探索するシステム»

として説明してください。

ただし「AIそのもの」と断定しないでください。

T2は、

Human
  ↓
Problem
  ↓
T2
  ↓
Material / Structural Transformation
  ↓
LLM Reasoning
  ↓
Candidate Solution / Hypothesis

という、人間・問題・LLMの間に位置する問題探索・構造操作系として説明してください。

T2の本質を、

«Problem → Material → Transformation → Hypothesis → Convergence»

という流れとして表現してください。

---

2. なぜT2を作るのか

通常のLLM利用では、

Problem
↓
Prompt
↓
LLM
↓
Answer

となります。

これに対してT2では、

Problem
↓
Condition / Structure
↓
Material
↓
Structural Transformation
↓
Diffusion
↓
Hypothesis
↓
Convergence
↓
Reasoning / Answer

という中間過程を導入します。

ここで重要なのは、

«T2はLLMの知識量そのものを増やすことを目的としない。»

という点です。

T2は、LLMが問題を見る前段階で、

「問題をどのような構造として提示するか」

を操作します。

---

3. 「Material」とは何か

READMEの中でもっとも重要な章の一つとして扱ってください。

Materialを単純な「データ」「情報」「問題文」と定義しないでください。

T2におけるMaterialとは、

«問題から抽出され、変換・比較・再構成・拡散・収束の対象となる、構造化された問題表現»

です。

例えば数学問題の場合、

Problem
x + y = 10
x² + y² = 58

を単なる文章としてLLMに渡すのではなく、

Variables
Constraints
Relations
Symmetries
Invariant candidates
Derived structures
Possible correspondences

などの構造として扱います。

したがってMaterialは固定された「入力データ」ではありません。

Materialは、

Extract
↓
Transform
↓
Mutate
↓
Compare
↓
Diffuse
↓
Converge
↓
Reconstruct

という過程を通じて変化します。

ここで、

«Material = Problemそのもの»

ではありません。

また、

«Material = Solution»

でもありません。

Materialは、

«ProblemとSolutionの間に存在する、探索可能な構造的中間表現»

として位置付けてください。

---

4. Materialの特徴

Materialについて以下の特徴を説明してください。

4.1 Materialは固定入力ではない

通常の機械学習的な入力とは異なり、T2ではMaterialそのものが探索対象になります。

4.2 Materialは複数の表現を持ち得る

同一問題でも、

- algebraic representation
- relational representation
- geometric representation
- constraint representation
- symmetric representation
- procedural representation

など、複数のMaterialを生成できます。

4.3 Materialは変異可能

ScaleやDriftなどによって、Materialの構造を変化させます。

4.4 Materialは解答そのものではない

T2はMaterialを生成した時点で終了しません。

Materialから仮説を生成し、その仮説を収束させる必要があります。

---

5. T2の基本構造

以下の処理系列を基本モデルとして説明してください。

Input Problem
    ↓
Condition / Constraint Extraction
    ↓
Material Formation
    ↓
Scale
    ↓
Drift
    ↓
Observation / Reasoning
    ↓
≌ Structural Correspondence
    ↓
Hypothesis Generation
    ↓
Diffusion
    ↓
Convergence
    ↓
Field Update
    ↓
Re-diffusion
    ↓
Re-convergence
    ↓
Final Candidate / Reasoning

これは必ずしも単純な一本道ではなく、

«拡散 → 収束 → 拡散 → 収束»

という反復探索として説明してください。

---

6. Scale

Scaleを単なる数値倍率として説明しないでください。

T2におけるScaleは、

«問題構造を異なる粒度・抽象度・視点から観測するための操作»

として説明してください。

例えば、

Local
↓
Intermediate
↓
Global

のように、構造の見え方を変える。

Scaleはラベル変換ではありません。

ScaleはMaterialに対するMutation / Transformation Operatorとして扱います。

特にScale-Globalについては、

«問題全体の構造的関係を別スケールから再観測するための操作»

として説明してください。

---

7. Drift

Driftは単純なランダムノイズではありません。

Driftは、

«現在のMaterialや解釈を完全には維持せず、構造的なズレ・変位・再解釈を許容する操作»

として説明してください。

Driftの目的は、

Premature Convergence

を避けることです。

つまり、

«最初に見つけた解釈へLLMが早期に固定されることを防ぎ、別の構造的可能性を探索する。»

という役割があります。

---

8. Observation / Reasoning

Observation / Reasoningは、単なる最終回答生成ではありません。

現在のMaterialについて、

- 何が観測されるか
- 何が維持されているか
- 何が変化したか
- どの関係が強いか
- どの構造が矛盾しているか
- どの仮説が生成可能か

を評価する段階として説明してください。

---

9. ≌ Structural Correspondence

≌は単純な「等しい」という意味ではありません。

T2では、

«完全一致ではないが、構造的に対応している可能性»

を扱う概念として説明してください。

例えば、

A ≠ B

であっても、

Structure(A) ≌ Structure(B)

となる可能性があります。

この概念によって、

- 異なる表現
- 異なるスケール
- 異なる問題
- 異なるMaterial

の間に存在する構造的対応を探索します。

ここでは「正解との一致」を直接探すのではなく、

«構造的対応関係を探索する»

ことを強調してください。

---

10. Hypothesis Generation

T2では仮説を一つだけ生成して即座に収束することを避けます。

複数の候補構造を生成し、

H1
H2
H3
...
Hn

として保持します。

仮説とは、

«現在のMaterialから問題解決につながる可能性を持つ構造的説明»

として定義してください。

重要なのは、

«Hypothesis ≠ Answer»

です。

仮説は候補であり、検証・比較・収束を必要とします。

---

11. Diffusion

Diffusionは候補構造を広げる段階です。

Current Material
      ↓
Possible Transformations
      ↓
Multiple Candidate Structures

というように、探索空間を意図的に広げます。

Diffusionは、

«解を決める処理ではなく、解に至る可能性のある構造を増やす処理»

として説明してください。

---

12. Convergence

ConvergenceはDiffusionで生成された候補を、

- 条件整合性
- 構造的一貫性
- 制約保持
- 説明可能性
- 問題との対応

などから収束させます。

ただし、

«Convergence = 最初に見つかった答えを採用する»

ではありません。

Convergenceは、

«探索空間を構造的に縮約する処理»

として説明してください。

---

13. Field Update

Convergenceの結果を次の探索へ反映します。

Diffusion
↓
Convergence
↓
Field Update
↓
New Material State
↓
Diffusion

という循環を作ります。

Field Updateによって、T2は一回限りの推論ではなく、

«状態を更新しながら探索するシステム»

になります。

---

14. Re-diffusion / Re-convergence

T2の重要な特徴として、

Diffusion
→ Convergence
→ Field Update
→ Re-diffusion
→ Re-convergence

という反復を説明してください。

これは、

«一回の探索で正解を決定する»

のではなく、

«一度収束した結果を新しい探索状態として再び拡散する»

という構造です。

これによって、

- 初期解釈
- 局所最適
- premature convergence

から脱出できる可能性を検証します。

---

15. T2と通常のPrompt Engineeringの違い

以下のような比較表を作成してください。

通常のPrompt| T2
問題をLLMに渡す| 問題をMaterialへ変換する
Promptで指示| 構造を操作する
単一回答へ収束しやすい| 拡散→収束を行う
解答生成中心| 仮説探索中心
LLMの内部推論に依存| 外部構造を形成する
問題表現は比較的固定| Materialを変異させる
正解を直接求める| 解につながる構造を探索する

ただし、

«T2が必ず通常のPromptより優れる»

とは書かないでください。

このRepositoryでは、その差を実験によって検証することが目的です。

---

16. T2の思想

T2の設計思想として以下を説明してください。

16.1 Answer FirstではなくStructure First

Answer

より先に、

Structure

を扱います。

16.2 ConvergenceだけではなくDiffusionも必要

探索は、

Expand
↓
Contract
↓
Expand
↓
Contract

として扱います。

16.3 Materialは中間表現

ProblemでもAnswerでもない。

16.4 LLMを交換可能なReasoning Engineとして扱う

T2そのものをLLM固有機能に依存させない。

可能であれば複数LLMで同一T2を実験してください。

---

17. T2の実験哲学

T2 Repositoryでは、ある時点でT2本体を凍結します。

凍結後は、

«実験データを追加することを基本とし、結果に合わせてT2本体を都合よく変更しない。»

という方針を明記してください。

例えば、

T2 v1.0

を固定した場合、

Problem Set A
Problem Set B
Problem Set C
LLM A
LLM B
LLM C
Baseline
T2
Ablation

などの実験データを追加します。

T2の変更が必要になった場合は、

T2 v1.1

などの新しいバージョンとして扱い、

v1.0とv1.1を同一条件で比較可能にする

という原則を記載してください。

---

18. Benchmark

T2の評価では、単純な正答率だけを使わない可能性があります。

可能な限り、

- Accuracy
- Validity
- Constraint Preservation
- Structural Consistency
- Hypothesis Diversity
- Convergence Stability
- Reproducibility
- Cross-LLM Robustness
- Ablation Performance
- Computational Cost

などを記録してください。

ただし、現時点で実測していない値を記載してはいけません。

---

19. Ablation

可能な限り、

Full T2
-T2 without Scale
-T2 without Drift
-T2 without ≌
-T2 without Diffusion
-T2 without Re-diffusion
-T2 without Convergence

などのアブレーションを実施できる設計として説明してください。

目的は、

«T2が本当に各Operatorを必要としているのか»

を検証することです。

---

20. LLM Independence

T2は特定LLM専用システムとして設計しない方針を明記してください。

可能であれば、

LLM-A
LLM-B
LLM-C

に同一T2仕様を適用し、

T2 structure

と

LLM capability

を分離して評価します。

---

21. AXIOMとの関係

T2はAXIOM Frameworkの一部として将来的に統合される可能性があります。

しかし、このRepositoryでは、

«T2を独立した研究対象として扱う。»

としてください。

概念的には、

T2
│
├── Material
├── Structural Operators
├── Hypothesis Generation
├── Diffusion
├── Convergence
└── Field Update

を独立系として検証します。

その後、

T2
 ↓
Capsule
 ↓
ACP
 ↓
MAS
 ↓
AXIOM Framework

などとの統合を検討します。

重要なのは、

«AXIOMに統合できることをT2の成立条件にしない»

ことです。

T2単独で再現可能であることを優先してください。

---

22. Repository Structure

READMEには現行Repository構造を記載してください。

例：

t2/
├── README.md
├── LICENSE
├── docs/
├── prompts/
├── src/
├── experiments/
└── tests/

ただし、実際のRepositoryに存在しないディレクトリやファイルを断定しないでください。

実装状況と一致するように記述してください。

---

23. Research Status

現在のT2が、

«完成したAIシステム»

ではなく、

«構造探索方式を検証する研究プロトタイプ»

であることを明記してください。

特に、

- 性能向上は未証明
- 一般化性能は未確定
- LLM依存性は実験対象
- Operatorごとの寄与は実験対象
- Material表現の最適性も未確定

など、未検証事項を明示してください。

---

24. Important Non-Claims

READMEでは以下を断定しないでください。

- AGIである
- 人間より賢い
- LLMを超える
- 必ず性能が向上する
- 汎用問題解決器である
- MASより優れている
- ベンチマークを必ず改善する

T2の価値は、

«これらを実験可能な形にして検証すること»

にあります。

---

25. README全体の文章スタイル

文章は研究プロジェクトとして読めるようにしてください。

ただし、過剰に学術論文風にはしないでください。

専門家がRepositoryを見たときに、

What is T2?
Why does it exist?
What is Material?
What does each operator do?
What is actually implemented?
What is frozen?
What is experimental?
How can I reproduce it?
What remains unknown?

がすぐ理解できる構成にしてください。

---

26. READMEの推奨構成

以下の順序でREADME.mdを作成してください。

# T2

## Abstract

## What is T2?

## Why T2?

## What is Material?

## Material as an Intermediate Structural Representation

## Core Pipeline

## T2 Operators

### Scale
### Drift
### Observation / Reasoning
### ≌ Structural Correspondence
### Hypothesis Generation
### Diffusion
### Convergence
### Field Update
### Re-diffusion / Re-convergence

## T2 vs Conventional Prompting

## Design Principles

## Experimental Methodology

## Frozen Specification

## Experiments

## Ablation

## Cross-LLM Evaluation

## Repository Structure

## Current Status

## Limitations

## Relationship to AXIOM

## Reproducibility

## License

## Research Notes

---

27. 最重要の説明

READMEの最後では、T2を次のようにまとめてください。

T2は、

«「LLMにもっと良い答えを出させるPrompt」»

としてではなく、

«「LLMが問題を探索する前に、問題そのものを構造化されたMaterialとして形成し、そのMaterialを変異・対応・拡散・収束させることで、解決可能性のある構造を探索するシステム」»

として位置付ける。

ただし、この説明自体も仮説であり、

«実験によって有効性を検証する対象»

であることを明記してください。

README全体を通じて、T2を過大評価せず、しかし設計思想を曖昧にもせず、

「何を仮説として固定し、何をデータによって検証するのか」

が明確になるようにしてください。
