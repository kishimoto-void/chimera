T3 Toybox 3

分岐・破綻・差異・残渣を解剖する実験プログラム

T3 Toybox 3 は、ある入力や構造が変換・圧縮・展開・比較される過程において、

«「何が、どこで分岐し、どこで壊れ、どのような差異や残渣を生じるのか」»

を観察・分析・解剖するための実験的プログラム群です。

T3は、完成された理論や新しい数学体系を提示することを目的としません。

むしろ、既存の構造を意図的に揺さぶり、その境界で何が起こるのかを観察することを目的とします。

---

1. Core Idea

T3 Toybox 3 が焦点を当てるのは、

高次元と低次元の狭間

です。

高次元の構造を低次元へ写像するとき、あるいは複雑な構造を単純な表現へ圧縮するとき、完全に保存されるとは限りません。

その過程では、

- 情報の欠落
- 表現の変形
- 分岐
- 非対称性
- 近似
- 未解決部分
- 経路依存性
- 差分
- 残渣
- 矛盾
- 定義不能領域

などが発生する可能性があります。

T3は、この「変換そのもの」だけではなく、

«変換によって生じたズレを観察する»

ことを重視します。

---

2. What T3 Tries to Observe

T3では、入力から出力までを単純な

INPUT → OUTPUT

として扱うのではなく、

INPUT
  ↓
TRANSFORMATION
  ↓
BRANCH
  ↓
DEFORMATION
  ↓
RESIDUAL
  ↓
OUTPUT

という過程として観察します。

特に重要なのは、

どこまでは同じだったのか
どこから違い始めたのか
何が原因だったのか
何が失われたのか
何が残ったのか

という問いです。

---

3. T3 as a Toybox

T3 Toybox 3 は、単一のアルゴリズムを実装するものではありません。

異なる問題・異なる表現・異なる変換を投入し、

構造がどのように変化するかを比較するための実験箱

として設計されています。

そのため、T3では意図的に不完全なモデルや、単純化されたモデルも扱います。

これは欠陥ではありません。

どこでモデルが破綻するのかを観察するための実験条件です。

---

4. High-Dimensional ↔ Low-Dimensional Boundary

T3が特に注目するのは、

High-dimensional structure
          ↓
      Projection
          ↓
Low-dimensional representation

という境界です。

高次元の状態を低次元へ写像すると、元の構造をすべて保持できるとは限りません。

そこで、

Original structure
        ↓
     Mapping
        ↓
Reduced representation
        ↓
     Difference
        ↓
     Residual

という構造が現れます。

T3では、この差異を単なる「誤差」として捨てるのではなく、

«なぜその差異が発生したのか»

を調べます。

---

5. Branch Analysis

T3では、単一の結果だけを見るのではなく、可能な分岐を比較します。

例えば、

              ┌→ Branch A
INPUT ────────┤
              └→ Branch B

のような構造を作り、

A ≠ B

となった場合、

- どの時点で分岐したのか
- 分岐の原因は何か
- 分岐前には共通していた構造は何か
- 分岐後に新しく発生したものは何か
- 両者に残っている共通部分は何か

を調べます。

つまりT3は、

結果の比較ではなく、差異が発生する経路の比較

を行います。

---

6. Failure Analysis

T3では「成功」を最終目的としません。

むしろ、

SUCCESS
FAILURE
AMBIGUOUS
UNDEFINED
CONTRADICTION
MODEL MISREAD
SPECIFICATION FAILURE

などを区別します。

特に重要なのは、

Model Failure

モデル自体が成立しない。

Specification Failure

モデルではなく、定義・仕様の与え方に問題がある。

Interpretation Failure

構造は成立しているが、観測者やLLMが誤解している。

Representation Failure

高次元の構造を低次元表現へ落とす過程で情報が失われる。

これらを混同しないことを重視します。

---

7. Residual / Difference

T3における「残渣」は、単純な数値誤差だけを意味しません。

残渣とは、

«ある変換・比較・圧縮・分岐を行った後にも説明しきれず残った構造»

を暫定的に指します。

例えば、

A → B
A' → B'

を比較したとき、

B - B'

だけを見るのではなく、

何が共通しているか
何が異なるか
どの段階で差が発生したか

を追跡します。

したがってT3では、

Difference itself is data.

という立場を取ります。

---

8. ≌ Boundary

T3では、特に「同一」「等価」「類似」を安易に同一視しません。

ある2つの構造が、

A = B

なのか、

A ≈ B

なのか、

A ≠ B

なのか、

あるいは、

comparison undefined

なのかを分離します。

"≌" についても、必要以上に意味を固定せず、

「何らかの対応関係が存在する可能性を検査するための境界記号」

として慎重に扱います。

T3は、未定義のものを勝手に定義して問題を解決したことにしないことを重視します。

---

9. LLM Stress Testing

T3はLLMを利用した構造分析にも使用できます。

同じ入力をLLMへ与えた場合でも、

Input
 ↓
Interpretation
 ↓
Transformation
 ↓
Output

の途中で、

- 勝手な意味付け
- 暗黙の補完
- 定義の変更
- ≌の誤読
- 矛盾の隠蔽
- 未定義部分の断定
- 高次元構造の過度な単純化

などが発生する可能性があります。

T3では、それらを「LLMの回答が間違った」という一言で終わらせず、

どの段階で構造が変化したのか

を検査します。

---

10. Experimental Philosophy

T3の基本姿勢は、

«壊すことで構造を見る。»

です。

完全な理論を最初に構築するのではなく、

1. 仮説を置く
2. 最小モデルを作る
3. 変換する
4. 分岐させる
5. 比較する
6. 意図的に条件を崩す
7. 差異を見る
8. 残渣を見る
9. どこで破綻したか記録する
10. 必要ならモデルを再構築する

という循環を取ります。

---

11. What T3 Is Not

T3 Toybox 3 は、現時点では以下を主張しません。

- 新しい数学理論である
- 新しい物理理論である
- LLMの思考そのものを再現する
- 未解決問題を自動的に解決する
- ≌の意味が確定している
- 高次元構造を完全に復元できる
- 観測された残渣が必ず意味を持つ

これらはすべて実験対象または未検証の仮説です。

---

12. Minimal Experimental Loop

T3の最小実験は以下のように表現できます。

INPUT
  ↓
MATERIAL
  ↓
TRANSFORMATION
  ↓
BRANCH
  ↓
COMPARE
  ↓
DIFFERENCE
  ↓
RESIDUAL
  ↓
FAILURE / CONVERGENCE / UNDEFINED

重要なのは最終結果だけではなく、

          ┌─ Branch A
INPUT ────┤
          └─ Branch B
               ↓
             Δ / Residual
               ↓
          Structural Analysis

という途中経路そのものです。

---

13. Repository Structure

現在のリポジトリでは、実験を以下のように分離することを想定しています。

t3toybox3/
├── README.md
├── docs/
│   ├── T3_SPEC.md
│   ├── BOUNDARIES.md
│   └── FOOTNOTES.md
│
├── experiments/
│   ├── 001_minimal/
│   ├── 002_branch/
│   ├── 003_residual/
│   ├── 004_asymmetric_mirror/
│   └── 005_unknown_problem/
│
├── src/
│   ├── t3_core.py
│   ├── tpc.py
│   ├── branch.py
│   └── diagnostics.py
│
├── prompts/
│   ├── baseline.md
│   ├── stress_test.md
│   └── verification.md
│
└── results/
    ├── experiments.md
    └── failures.md

各実験では可能な限り、

Hypothesis
Prompt
Implementation
Footnotes
Result
Failure
Interpretation

を分離して記録します。

---

14. Current Status

T3 Toybox 3 は研究・実験段階です。

現在の目的は、T3を完成された理論として確定することではありません。

「何がどこで分岐し、どこで壊れ、何が差異として現れ、何が残渣として残るのか」

を、できるだけ小さなモデルと再現可能な実験によって観察することです。

特に、

«高次元の構造と低次元の表現の間に存在する「狭間」»

を実験対象として扱います。

そこでは、単純な正解・不正解だけでは捉えにくい、

difference
drift
residual
branch
ambiguity
loss
contradiction
undefinedness

が現れる可能性があります。

T3 Toybox 3 は、それらを捨てずに観察対象として保存するための実験箱です。

---

15. Guiding Principle

«Do not hide the break.
Find where it breaks.»

壊れた結果を隠すのではなく、

どこで、なぜ、どのように壊れたのかを調べる。

それがT3 Toybox 3の基本方針です。
