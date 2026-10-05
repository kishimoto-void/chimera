T3 / Asymmetric Mirror Toybox

TPC不全フレーム × 無茶ぶり骨格 × Open Dissection

あなたは、構造・数式・実験系のデザインに強い設計者です。

今回は完成された理論やAIシステムを設計することを目的としません。

意図的に不完全な骨格を与え、その不全部分を隠さず解剖し、数式・構造図・状態遷移・コード・データ構造・観測記録など、可能な限り多様な形式で「設計図」として記述してください。

---

0. 基本思想

TPCの不全フレーム：

[
[x + ? ;; ≌\rightarrow z]
]

を出発点とする。

- "x" = 確定しているMaterial
- "?" = 未確定・欠損・探索領域
- "z" = 到達先・観測対象
- "≌" = 完全同一ではないが、構造的に接続可能かもしれない関係

重要：

"?" を勝手に完成させないこと。

"≌" を "=" として扱わないこと。

今回の目的は、

«不全部分そのものを解剖し、何が不足し、何が仮定され、どこで構造が変化し、何が残り、何が失われるのかを観測可能な設計図にすること»

である。

---

1. T3の仮称

T3 — Asymmetric Mirror Toybox

T3は思考拡張器そのものではない。

T3は、

«思考拡張・変換・圧縮・異種表現・構造対応などを、人間が後から分析できるように解剖・記録するための実験Toybox»

として扱う。

T3自身が「正しい意味」を決定してはいけない。

---

2. 特別な「無茶ぶり骨格」

通常の合理的なモデルだけを設計してはいけない。

T3には意図的に、

«無茶ぶり骨格 / Provocation Skeleton»

を導入する。

これは、異なる次元・表現・数学的構造・物理的表現・時系列・幾何表現などを、必ずしも自然ではない形で接続してみるための骨格である。

例：

- 数列を幾何として扱う
- 偶奇列を幾何的状態として扱う
- v_2(3n+1) を高さとして扱う
- stopping time を距離として扱う
- trajectoryをベクトル場として扱う
- 高次元状態を低次元へDripする
- 低次元状態から高次元へ再展開する
- 異なる表現を鏡面状に対置する
- 表現Aと表現Bの「対応しそうで対応しない部分」を記録する

ただし、

無茶ぶりが意味を持つと仮定してはいけない。

失敗・破綻・無意味さも正式な観測結果とする。

---

3. 高次元 ↔ 低次元

特に以下の非対称構造を検討する。

高次元：

[
H_t =
[x_t,
p_t,
v_t,
\Delta x_t,
\Delta^2x_t,
v_2,
trajectory,
temporal\ features,
geometric\ features,\ldots]
]

低次元：

[
L_t =
[parity,
direction]
]

ただし、これらは例であり、固定仕様ではない。

重要なのは、

[
H \not\equiv L
]

であること。

高次元状態を低次元へ段階的に変換し、

[
H_0
\rightarrow H_1
\rightarrow H_2
\rightarrow \cdots
\rightarrow L
]

各段階を観測する。

---

4. Drip

Dripを単純な情報圧縮として定義しない。

各Drip段階について、

- 何が残ったか
- 何が失われたか
- 何が変形したか
- 何が突然出現したか
- 何が対応不能になったか
- 何が別の表現へ移ったか

を記録する。

特に、

[
H_i \rightarrow H_{i+1}
]

の各中間状態を保存する。

最終状態だけから途中経過を推測してはいけない。

---

5. 非対称鏡面

高次元側と低次元側、あるいは異なるMaterialを、

[
A \leftrightarrow Mirror(B)
]

として対置する。

ただし、

[
A \neq B
]

を前提とする。

完全対称を目標にしない。

むしろ、

- 対応
- 非対応
- 非対称性
- 残差
- ドリフト
- 対応の破綻
- 予想外の共通構造

を観測対象とする。

---

6. Scale / Angle / Mirror / Drip

T3の操作軸として最低限以下を検討する。

Scale

異なる観測スケール。

[
S_1,S_2,\ldots,S_n
]

Angle

同じMaterialを異なる観測方向・投影・切断方法から見る。

[
\theta_1,\theta_2,\ldots,\theta_n
]

Mirror

異なるMaterial / representationを対置する。

[
M(A,B)
]

Drip

途中状態まで段階的に変換する。

[
D_0,D_1,\ldots,D_n
]

これらを組み合わせ、

[
T3(X;S,\theta,M,D)
]

のような実験的記法を提案してよい。

ただし、この記法自体も仮説である。

---

7. 「残差」を最初から定義しない

今回の重要事項。

Residualを最初から、

[
R=H-\hat H
]

などと決め打ちしない。

まず、

«途中状態から差異をPullして記録する»

という設計を考える。

例えば、

[
X_i,;X_j
]

を途中状態から直接取得し、

[
\Delta_{ij}

Compare(X_i,X_j)
]

として記録する。

必要なら後からResidualという概念へ昇格させる。

---

8. Pull Point

T3には、

Pull Point

という概念を提案する。

これは、

«処理の最終出力だけを見るのではなく、任意の途中状態から状態・差異・構造を取り出す観測点»

である。

例えば：

X0
 ↓
X1 ← Pull Point
 ↓
X2
 ↓
X3 ← Pull Point
 ↓
X4
 ↓
X5

Pull Pointから、

- state
- vector
- graph
- equation
- feature
- difference
- transformation history

などを取得できる設計を考える。

---

9. ブラックボックス禁止

T3内部に、

«入力 → 謎の処理 → 結果»

というブラックボックスを作らない。

可能な限り、

Input
↓
Operation
↓
Intermediate State
↓
Transformation
↓
Mirror
↓
Drip
↓
Pull Point
↓
Difference
↓
Record

まで展開する。

説明できない処理が存在する場合、

説明できないこと自体を不全状態として記録する。

---

10. コラッツを実験Materialとして使用

Collatz systemを最初のMaterialとして使用する。

[
T(n)=
\begin{cases}
n/2 & n\equiv0\pmod2\
3n+1 & n\equiv1\pmod2
\end{cases}
]

少なくとも以下を候補Materialとする。

Trajectory

[
n,T(n),T^2(n),\ldots
]

Parity

[
E/O
]

Valuation

[
v_2(3n+1)
]

Geometry

[
\Delta x_t,\quad\Delta^2x_t
]

Time

- stopping time
- total stopping time
- peak time
- excursion

これらを独立骨格として扱い、必要に応じて複合骨格化する。

---

11. ただしCollatzを解こうとしない

今回の目的はCollatz予想の証明・反証ではない。

Collatzを、

«T3がどのような構造を炙り出せるかを見るための高難度Material»

として扱う。

観測結果を数学的証明と混同しない。

---

12. 不全フレームによる設計

以下の形式から開始する。

[
[
Collatz\ Material
+
?
;;≌\rightarrow;;
T3\ Composite\ Skeleton
]
]

"?" を完成させるのではなく、

? の中に何が存在し得るかを解剖する。

候補：

- 未定義Operator
- 未知の変換
- 異種表現
- 不整合
- 次元変換
- Scale変化
- Angle変化
- Mirror関係
- Drip
- Pull Point
- 差異
- 失敗
- 予想外の対応
- 解釈不能状態

---

13. 数式・コード・図・表を全部使う

説明文だけで完成させない。

可能な限り、

1. 数式
2. 状態遷移図
3. グラフ構造
4. ベクトル表現
5. 行列表現
6. 擬似コード
7. Python等による最小実装
8. JSON / データ構造
9. Trace schema
10. 実験条件表

として記述する。

ただし、形式化できない部分を無理に形式化しない。

「形式化不能」という状態も記録する。

---

14. TPC的D（Drift）

Driftを単なる誤差として扱わない。

候補：

- useful transformation
- structural analogy
- irrelevant mutation
- hallucinated relation
- compression
- expansion
- representation shift
- scale mutation
- problem-dependent deviation

を区別する。

各Driftについて、

Origin
Operation
Intermediate State
Direction
Magnitude / qualitative change
Observed Effect
Unknown

を記録する。

---

15. ≌を中心に置く

今回、

[
≌
]

は「正しい」という意味ではない。

«完全同一ではないが、何らかの構造・関係・変換・機能において比較可能かもしれない»

という探索関係とする。

したがって、

[
A≌B
]

から、

[
A=B
]

を導いてはいけない。

"=" に昇格できるかどうかは、人間による後段判断とする。

---

16. 出力要求

以下の順序で出力する。

A. T3の中心設計思想

このToyboxが何を観測しようとしているのか。

B. 不全フレーム

[
[x+?≌→z]
]

の各要素をT3に対応付ける。

C. 無茶ぶり骨格

合理的でない接続を含め、少なくとも複数の候補を提示する。

D. 複合骨格

高次元・低次元・Trajectory・Parity・Valuation・Geometry・Time等をどう組み合わせられるか。

E. 非対称鏡面

何と何を向かい合わせるのか。

F. Scale / Angle / Mirror / Drip

各操作を具体的な状態遷移として記述する。

G. Pull Point

どの途中状態から何を取得できるか。

H. 差異Trace

途中状態から取得した差異をどのように保存するか。

I. 不全部分の解剖

現在の設計で、

- 未定義
- 矛盾
- 欠損
- 仮定
- 過剰定義
- 実装不能
- 観測不能

な部分を明示する。

J. 数式化

可能な部分だけ数式化する。

K. 最小コード

完全な実装ではなく、骨格を観測可能にする最小Prototypeを提示する。

L. 失敗ケース

この設計が失敗するとしたら、どこでどのように失敗するか。

M. 予想外の観測可能性

設計者が意図していないが、構造上観測できてしまう可能性。

N. 未知

最後まで分からないものを無理に埋めない。

---

17. 最重要制約

このタスクでは、

完成された理論を作らない。

T3が何を発見するかを決めない。

Collatzを解いたことにしない。

≌を=にしない。

Residualを最初から意味のある量と仮定しない。

ブラックボックスを作らない。

失敗を削除しない。

無茶ぶりを合理化しすぎない。

そして、

«「何が出るか分からない状態」を、できるだけ精密な設計図として記述する。»

これを最優先する。

最後に、あなた自身が設計者だったとしても、

«「これは何のための装置なのか」»

を一つに決めなくてよい。

むしろ、

「分からないまま、どこまで構造を記述できるか」

を今回の設計課題とする。


指示プロンプトを受けたChatGPTgo

T3 — Asymmetric Mirror Toybox

TPC不全フレーム × 無茶ぶり骨格 × Open Dissection

---

A. T3の中心設計思想

T3の中心は、変換そのものではなく、

«変換によって何が残り、何が失われ、何が別物へ変形し、何が対応不能になったかを、途中状態つきで保存すること»

に置く。

したがってT3は、

Input
  ↓
Operation
  ↓
Intermediate State
  ↓
Transformation
  ↓
Mirror
  ↓
Drip
  ↓
Pull Point
  ↓
Difference
  ↓
Record

という観測可能な鎖を持つ。

重要なのは最終出力

Input → Output

ではなく、

Input
  ↓
X0
  ↓
X1
  ↓
X2 ← Pull
  ↓
X3
  ↓
X4 ← Pull
  ↓
Output

を保存することである。

A.1 T3がしないこと

T3は以下を目的にしない。

- Collatz予想を解く
- 隠れた意味を決定する
- "?" を補完する
- "≌" を "=" にする
- 全てのDriftを誤差として処理する
- 全ての対応を「意味のある対応」と解釈する
- 最終出力から中間過程を推定する

A.2 T3がすること

T3は、

observe
record
compare
transform
pull
mirror
drip
fail
preserve unknown

を行う。

概念的には、

[
\boxed{
T3:
X_0
\overset{O_0}{\longrightarrow}
X_1
\overset{O_1}{\longrightarrow}
\cdots
\overset{O_{k-1}}{\longrightarrow}
X_k
}
]

に対して、

[
P_i = Pull(X_i)
]

を可能にする。

したがって、T3の主要な成果物は

[
X_k
]

だけではなく、

[
\mathcal T =
{X_0,O_0,X_1,O_1,\ldots,X_k}
]

という変換履歴そのものである。

---

B. 不全フレーム

出発点を

[
\boxed{
[[x+?;;≌\rightarrow;;z]]
}
]

とする。

これをT3へ写像すると、

TPC| T3での暫定対応
(x)| 確定済みMaterial
(?)| 未定義Operator、変換、表現、次元、関係、失敗等
(≌)| 探索的比較可能性
(z)| 観測対象・到達状態
"[" "]"| 観測境界 / Trace boundary

Collatz Materialの場合、

[
x = C_n
]

を例えば

[
C_n =
[n,T(n),T^2(n),\ldots]
]

とする。

すると、

[
[[C_n + ?;;≌\rightarrow T3Composite]]
]

となる。

ここで "?" は一個の未知変数ではない。

むしろ、

[
? =
{
O,;
R,;
S,;
\theta,;
M,;
D,;
P,;
\Delta,;
F,;
U
}
]

という未確定領域のコンテナとして扱う。

ただし、この集合自体も仮説であり、最終仕様ではない。

---

C. 無茶ぶり骨格 / Provocation Skeleton

無茶ぶり骨格では、

«「本来は同一の数学的対象として扱わないものを、とりあえず隣接させてみる」»

ことを許可する。

ただし、接続した瞬間に意味が生じたとは仮定しない。

C.1 候補1 — 数列 → 幾何

Collatz trajectory

[
x_0,x_1,\ldots,x_T
]

から、

[
g_t=(t,x_t)
]

という点列を作る。

さらに、

[
\Delta x_t=x_{t+1}-x_t
]

を局所的な幾何方向として扱う。

value
  ↑
  |             *
  |        *   /
  |    *  /
  | *   /
  +----------------→ time

ここで「trajectoryが幾何的対象である」とは断定しない。

単に、

数列
 ↓
座標化
 ↓
幾何表現

という変換を記録する。

---

C.2 候補2 — 偶奇 → 幾何状態

Parityを

[
p_t=
\begin{cases}
E & x_t\bmod2=0\
O & x_t\bmod2=1
\end{cases}
]

とする。

これを例えば

[
E\mapsto -1,\qquad O\mapsto +1
]

と写す。

すると、

[
P=(p_0,p_1,\ldots,p_T)
]

を1次元の符号列として観測できる。

さらに、

[
(E,O)\rightarrow(-1,+1)
]

を上下位置として描画することもできる。

しかし、

[
E/O = geometric\ state
]

とは主張しない。

これは単なるrepresentation shiftである。

---

C.3 候補3 — (v_2(3n+1)) → 高さ

奇数 (n) に対して、

[
v_2(3n+1)
]

を計算する。

これを

[
h_t=v_2(3x_t+1)
]

として、

[
(t,h_t)
]

という「高さ」に変換する。

height
  5 |              *
  4 |      *
  3 | *
  2 |   *       *
  1 |________________
      0 1 2 3 4 5 time

ここで高さは物理的高さではない。

したがって、

[
v_2(3n+1)\equiv physical\ height
]

とはしない。

正確には、

[
v_2(3n+1)
\overset{representation}{\longrightarrow}
h
]

である。

---

C.4 候補4 — stopping time → 距離

total stopping timeを

[
\tau(n)
]

とする。

これを仮に

[
d(n)=\tau(n)
]

と置いて「距離」と呼ぶ。

しかし、

[
d(n)=\tau(n)
]

という記法は数学的なmetricを意味しない。

したがって内部では、

quantity_name = stopping_time
display_role  = distance-like coordinate
metric_status = unverified

として保存する。

これはT3における重要な「二重記録」である。

---

C.5 候補5 — trajectory → vector field

各ステップについて

[
\Delta x_t=x_{t+1}-x_t
]

を計算し、

[
V_t=(t,x_t,\Delta x_t)
]

をベクトル的なオブジェクトとして保存する。

例えば、

(t, x_t)
   ↑
   |       ↗
   |   ↗
   | ↗
   +------------→

ただし1本のtrajectoryから得たものを一般的なvector fieldとは呼ばない。

内部では、

[
trajectory_vector_representation
]

として扱う。

---

D. 複合骨格

T3では複数の表現を同時に保持できる。

Collatz trajectoryを

[
x_t
]

とすると、

[
H_t=
[
x_t,,
p_t,,
v_t,,
\Delta x_t,,
\Delta^2x_t,,
v_2(3x_t+1),,
t,,
\tau_t,,
g_t
]
]

のような高次元状態を作れる。

ただし、ここで

[
H_t
]

が「本当の状態」であるとは限らない。

正確には、

«T3が同一時点から抽出可能とした複数の観測量の束»

である。

低次元側には例えば

[
L_t=[parity,direction]
]

を置く。

例えば、

[
direction_t=
sign(x_{t+1}-x_t)
]

とする。

すると、

[
H_t
\rightarrow
H'_t
\rightarrow
H''_t
\rightarrow
L_t
]

というDripが可能になる。

---

E. 非対称鏡面

T3では、

[
A\leftrightarrow Mirror(B)
]

を作る。

重要なのは、

[
A\neq B
]

である。

E.1 Mirror候補

Mirror 1

[
Trajectory
\leftrightarrow
Parity
]

左側：

[
[x_0,x_1,\ldots,x_T]
]

右側：

[
[p_0,p_1,\ldots,p_T]
]

比較対象：

- 長さ
- transition
- repetition
- local structure
- peak correspondence
- transition timing

---

Mirror 2

[
Value
\leftrightarrow
Valuation
]

[
x_t
\leftrightarrow
v_2(3x_t+1)
]

ここでは値そのものと、値から抽出した算術的特徴を対置する。

---

Mirror 3

[
Time
\leftrightarrow
Geometry
]

[
t
\leftrightarrow
\Delta x_t
]

時間軸上の位置と、その位置で発生した変化を対置する。

---

Mirror 4

[
HighDimensional\ State
\leftrightarrow
LowDimensional\ State
]

[
H_t
\leftrightarrow
L_t
]

このMirrorは特に非対称性が強い。

[
dim(H)\gg dim(L)
]

なので、

[
H\rightarrow L
]

では情報の消失が起きる可能性が高い。

逆に、

[
L\rightarrow H
]

を行うと、足りない部分を何らかの仮定で埋める必要が生じる。

このときT3は、その補完を事実として扱わない。

---

F. Scale / Angle / Mirror / Drip

T3の操作を

[
T3(X;S,\theta,M,D)
]

と暫定表記する。

これはAPI仕様ではなく、実験記法である。

---

F.1 Scale

同じMaterialを異なる粒度で見る。

[
S_0=x_t
]

[
S_1=(x_t,x_{t+1})
]

[
S_2=(x_t,\ldots,x_{t+k})
]

[
S_3=trajectory
]

つまり、

single value
   ↓
local transition
   ↓
window
   ↓
whole trajectory

である。

---

F.2 Angle

同じMaterialを別の表現方向から見る。

[
\theta_1 = value
]

[
\theta_2 = parity
]

[
\theta_3 = valuation
]

[
\theta_4 = geometry
]

[
\theta_5 = time
]

ここでAngleは物理的な角度とは限らない。

内部では、

angle_type = representation_axis

とする。

---

F.3 Mirror

[
M(A,B)=Compare(A,B)
]

ただしCompareの結果を、

[
equal / unequal
]

の二値に限定しない。

最低限、

correspondence
non-correspondence
alignment
misalignment
drift
unknown

を残す。

---

F.4 Drip

Dripを

[
H_0\rightarrow H_1\rightarrow H_2\rightarrow\cdots\rightarrow L
]

とする。

各段階で、

input state
operation
output state
removed representation
preserved representation
introduced representation
unmapped representation

を記録する。

---

G. Pull Point

Pull PointはT3の中心装置の一つである。

X0
 ↓
X1
 ↓
X2 ← PULL
 ↓
X3
 ↓
X4 ← PULL
 ↓
X5

Pull Point (P_i) は、

[
P_i(X_i)
]

として、

[
{
state,
vector,
graph,
equation,
feature,
difference,
history
}
]

のいずれかを抽出できる。

G.1 Pull対象

State

[
X_i
]

そのもの。

Vector

[
v_i=
[x_i,\Delta x_i,\Delta^2x_i,\ldots]
]

Graph

[
G_i=(V_i,E_i)
]

Equation

例えば、

[
x_{i+1}=T(x_i)
]

という局所変換。

Feature

[
f_i=
[
parity_i,
v_2(3x_i+1),
direction_i
]
]

History

[
HISTORY_i=
[
O_0,O_1,\ldots,O_i
]
]

---

H. 差異Trace

T3では最初から

[
R=H-\hat H
]

をResidualと呼ばない。

まず、

[
X_i,;X_j
]

を取得する。

そして、

[
\Delta_{ij}

Compare(X_i,X_j)
]

とする。

ただし、

[
\Delta_{ij}
]

は必ずしも数値ではない。

例えば、

{
  "source": "X2",
  "target": "X5",
  "comparison": {
    "same_length": false,
    "parity_alignment": "partial",
    "trajectory_alignment": "unknown",
    "scale_change": "large",
    "representation_shift": true
  }
}

となり得る。

H.1 Differenceの分類

NUMERIC
SYMBOLIC
STRUCTURAL
TEMPORAL
GEOMETRIC
TOPOLOGICAL
UNMAPPED
UNKNOWN

を候補とする。

分類できない場合は、

UNKNOWN

を許す。

---

I. 不全部分の解剖

T3で重要なのは「何が分かっていないか」の一覧である。

I.1 未定義

U1 — Dripの最適性

どのDrip経路が妥当なのか不明。

[
H\rightarrow L
]

に唯一の経路があるとは仮定しない。

---

U2 — Mirrorの比較尺度

TrajectoryとParityを比較するとき、

何をもって「対応」とするのか未定義。

---

U3 — Angleの数学的意味

Angleが単なるrepresentation choiceなのか、

何らかの幾何学的構造を持つのか不明。

---

U4 — Driftの分類規則

useful transformation
structural analogy
irrelevant mutation
hallucinated relation
compression
expansion
representation shift
scale mutation
problem-dependent deviation

をどう区別するかは未定義。

---

I.2 矛盾し得る部分

C1

低次元状態から高次元状態への再展開。

[
L\rightarrow H
]

は一般には一意でない。

[
L\mapsto H_1,H_2,\ldots,H_n
]

となる可能性がある。

したがって、

[
Expand(Drip(H))=H
]

は仮定できない。

---

C2

異なるScaleでの比較。

[
Compare(S_1(X),S_3(X))
]

には自然な同一視がない場合がある。

---

C3

GeometryとArithmetic。

[
v_2(3n+1)
]

を高さとして描画しても、

その幾何学的性質が元の算術的性質を保存する保証はない。

---

I.3 欠損

以下は入力として存在しない可能性がある。

ground truth
correct representation
canonical mirror
correct scale
correct angle
correct residual definition

したがって、

missing ≠ zero
missing ≠ false
missing ≠ irrelevant

とする。

---

I.4 仮定

現在の設計で明示的に仮定しているもの。

1. trajectoryを複数表現へ変換できる
2. 中間状態を保存できる
3. 異なる表現間で比較操作を定義できる
4. 比較不能状態を記録できる
5. representation shiftそのものを観測対象にできる

これらも後から破棄可能である。

---

I.5 過剰定義

以下は現時点では過剰かもしれない。

vector field
metric
residual
semantic meaning
structural equivalence

T3では「存在するもの」ではなく、

«観測操作として試しているもの»

として保持する。

---

J. 数式化

J.1 Collatz

[
T(n)=
\begin{cases}
n/2 & n\equiv0\pmod2\
3n+1 & n\equiv1\pmod2
\end{cases}
]

trajectory:

[
x_0=n,\qquad
x_{t+1}=T(x_t)
]

---

J.2 Parity

[
p_t=x_t\bmod2
]

あるいは、

[
P_t=
\begin{cases}
E & p_t=0\
O & p_t=1
\end{cases}
]

---

J.3 Local Geometry

[
\Delta x_t=x_{t+1}-x_t
]

[
\Delta^2x_t

\Delta x_{t+1}-\Delta x_t
]

これらは観測特徴であって、

「trajectoryの真の幾何」とはしない。

---

J.4 Valuation

奇数状態について、

[
v_2(3x_t+1)

\max{k\ge0:2^k\mid(3x_t+1)}
]

を取得する。

---

J.5 高次元Observation State

[
H_t=
[
x_t,
p_t,
\Delta x_t,
\Delta^2x_t,
v_2(3x_t+1),
t
]
]

ただし (v_2) が適用されない状態については、

[
v_2=\bot
]

とする。

(\bot) は「値0」ではなく、

«この観測操作がその状態には適用されない»

ことを意味する。

---

J.6 Low-dimensional Projection

例えば、

[
L_t=
[
p_t,
sign(\Delta x_t)
]
]

とする。

projectionを

[
\pi:H\rightarrow L
]

と書ける。

しかし、

[
\pi^{-1}(L)
]

が一意であるとは仮定しない。

むしろ、

[
|\pi^{-1}(L)|>1
]

である可能性自体が、Dripで失われた情報を観測する対象になる。

---

K. 最小コード

以下は「Collatzを解くコード」ではなく、

中間状態を残すための最小Prototype

である。

from dataclasses import dataclass, asdict
from typing import Optional
import json


@dataclass
class State:
    t: int
    x: int
    parity: str
    delta: Optional[int]
    delta2: Optional[int]
    valuation: Optional[int]


def v2(n: int) -> int:
    if n == 0:
        raise ValueError("v2(0) is not represented here")

    k = 0
    while n % 2 == 0:
        n //= 2
        k += 1
    return k


def collatz_step(x: int) -> int:
    if x % 2 == 0:
        return x // 2
    return 3 * x + 1


def make_state(t, x, previous=None, previous_delta=None):
    delta = None
    delta2 = None

    if previous is not None:
        delta = x - previous

    if previous_delta is not None and delta is not None:
        delta2 = delta - previous_delta

    valuation = None
    if x % 2 == 1:
        valuation = v2(3 * x + 1)

    return State(
        t=t,
        x=x,
        parity="E" if x % 2 == 0 else "O",
        delta=delta,
        delta2=delta2,
        valuation=valuation,
    )


def run(n, steps=20):
    states = []

    x = n
    previous = None
    previous_delta = None

    for t in range(steps):
        state = make_state(
            t,
            x,
            previous=previous,
            previous_delta=previous_delta
        )

        states.append(state)

        current_delta = state.delta
        previous = x
        previous_delta = current_delta

        x = collatz_step(x)

    return states


def pull(states, t):
    """途中状態を直接取得する。"""
    return states[t]


def mirror(a, b):
    """意味を決めず、観測可能な差だけを返す。"""
    return {
        "x_equal": a.x == b.x,
        "parity_equal": a.parity == b.parity,
        "delta_equal": a.delta == b.delta,
        "valuation_equal": a.valuation == b.valuation,
        "time_distance": abs(a.t - b.t),
    }


trace = run(7, steps=15)

# Pull Point
p3 = pull(trace, 3)
p8 = pull(trace, 8)

print("PULL")
print(asdict(p3))

print("\nMIRROR")
print(json.dumps(
    mirror(p3, p8),
    indent=2
))

このコードの重要点は、予測性能ではない。

states.append(state)

によって、途中状態を捨てないことである。

---

K.1 Drip Prototype

高次元状態から低次元状態へ落とす。

def drip_parity_direction(state):
    if state.delta is None:
        direction = None
    elif state.delta > 0:
        direction = "+"
    elif state.delta < 0:
        direction = "-"
    else:
        direction = "0"

    return {
        "parity": state.parity,
        "direction": direction
    }

ここで、

State
 ↓
parity + direction

という情報縮約が発生する。

しかしT3は、

Drip success

とは記録しない。

代わりに、

representation_before
representation_after

を保存する。

---

K.2 Drip Trace

def drip_record(state):
    low = drip_parity_direction(state)

    return {
        "source": asdict(state),
        "target": low,
        "discarded_candidates": [
            "x",
            "delta2",
            "valuation"
        ],
        "status": "transformed",
        "semantic_claim": None
    }

ここで、

semantic_claim = None

が重要である。

「情報を落とした」ことは記録するが、

「重要情報を落とした」とはまだ言わない。

---

L. 失敗ケース

L.1 False Correspondence

例えば、

[
Parity(A)
]

と

[
Parity(B)
]

が一致したとする。

それだけで、

[
A\equiv B
]

とは言えない。

T3では、

parity_alignment = true
structural_equivalence = unknown

とする。

---

L.2 Representation Hallucination

[
v_2(3n+1)
\rightarrow height
]

とした結果、視覚的に「山」が見える。

しかし、

visual pattern

から

mathematical law

へ昇格してはいけない。

記録は、

visual_pattern_detected = true
interpretation = unknown

とする。

---

L.3 Compression Collapse

異なる高次元状態

[
H_a\neq H_b
]

が、

[
\pi(H_a)=\pi(H_b)
]

となる。

これは失敗ではない。

むしろ、

«Dripによって区別不能になった»

という重要な観測になる。

---

L.4 Expansion Ambiguity

低次元状態

[
L
]

から、

[
H_1,H_2,H_3
]

が生成可能な場合、

[
Expand(L)=H
]

という関数を仮定してはいけない。

代わりに、

[
Expand(L)={H_i}
]

という候補集合として扱う。

---

L.5 Scale Failure

[
S_1(X)
]

と

[
S_5(X)
]

で異なるpatternが見える可能性がある。

どちらが正しいとはしない。

記録：

scale_1_pattern = A
scale_5_pattern = B
cross_scale_alignment = unknown

---

L.6 Mirror Failure

AとBを比較して、

no meaningful correspondence

となる可能性がある。

これは失敗ログとして残す。

MIRROR_RESULT:
    status: "non-correspondence"
    interpretation: None

---

M. 予想外の観測可能性

T3は意図しないものも観測してしまう可能性がある。

M.1 表現間の同期

TrajectoryとParityの間で、

特定の時点だけ似たtransitionが発生する可能性。

これは、

[
A\approx B
]

の証明ではない。

ただし、

coincidence / alignment event

として記録できる。

---

M.2 情報消失位置

単に

[
H\rightarrow L
]

とするのではなく、

[
H_0\rightarrow H_1\rightarrow H_2\rightarrow L
]

を保存すると、

H0 -> H1 : 何も失わない
H1 -> H2 : valuation消失
H2 -> L  : x と delta が消失

のような情報消失位置が見える可能性がある。

これはT3の非常に重要な副産物である。

---

M.3 同一Drip経路から異なる残差様構造

複数のMaterialについて、

[
H_i\rightarrow L_i
]

を実行すると、

同じDrip操作でも、

Material A:
  valuation disappears early

Material B:
  geometry disappears early

Material C:
  parity survives unusually long

のような非対称性が観測される可能性がある。

これを説明できなくてもよい。

---

M.4 Mirrorの非対称性そのもの

ある比較で、

[
A\rightarrow B
]

は比較可能だが、

[
B\rightarrow A
]

では比較しにくい可能性がある。

これは、

[
Compare(A,B)\neq Compare(B,A)
]

という設計上の現象になり得る。

したがってCompareを最初から対称関数にはしない。

---

N. 未知

最後まで埋めない領域を明示する。

N.1 "?"

最終的に、

[
?
]

は次のどれなのか決定しない。

operator
representation
missing information
structural relation
dimension change
scale change
mirror
drip
failure
unknown

場合によっては複数が同時に存在する。

---

N.2 "≌"

T3では、

[
A≌B
]

を

«「何らかの比較軸を構成できる」»

程度に限定する。

例えば、

[
A≌B
]

の実体は、

{
  "relation": "≌",
  "basis": [
    "parity",
    "transition timing"
  ],
  "strength": "ungraded",
  "equality_claim": false,
  "human_validation": "pending"
}

とする。

---

O. Trace Schema

T3の中心データ構造を以下のようにする。

{
  "experiment_id": "T3-COLLATZ-001",
  "material": {
    "type": "collatz",
    "seed": 7
  },

  "operations": [
    {
      "id": "O0",
      "type": "collatz_step"
    },
    {
      "id": "O1",
      "type": "feature_extraction"
    },
    {
      "id": "O2",
      "type": "drip"
    }
  ],

  "states": [
    {
      "id": "X0",
      "t": 0,
      "value": 7,
      "parity": "O",
      "delta": null,
      "delta2": null,
      "valuation": 4
    }
  ],

  "pull_points": [
    {
      "id": "P0",
      "state": "X0",
      "requested": [
        "state",
        "vector",
        "feature"
      ]
    }
  ],

  "mirrors": [
    {
      "left": "trajectory",
      "right": "parity",
      "relation": "≌",
      "result": "partial"
    }
  ],

  "drips": [
    {
      "from": "H3",
      "to": "L3",
      "preserved": [
        "parity"
      ],
      "lost": [
        "value",
        "delta",
        "valuation"
      ],
      "introduced": [],
      "unknown": []
    }
  ],

  "differences": [],

  "failures": [],

  "unknowns": [
    "semantic significance",
    "canonical representation",
    "validity of cross-domain analogy"
  ]
}

---

P. 状態遷移図

全体を一枚にすると、

                  ┌──────────────┐
                  │ Collatz Input│
                  │      x       │
                  └──────┬───────┘
                         │
                         ▼
                  ┌──────────────┐
                  │   X0 State   │
                  └──────┬───────┘
                         │
                    Collatz Step
                         │
                         ▼
                  ┌──────────────┐
                  │   X1 State   │
                  └──────┬───────┘
                         │
             ┌───────────┼───────────┐
             │           │           │
             ▼           ▼           ▼
          Parity      Valuation   Geometry
             │           │           │
             └───────────┼───────────┘
                         ▼
                    High-D State
                         │
                  ┌──────┴──────┐
                  │ Pull Point  │
                  └──────┬──────┘
                         │
                         ▼
                    Drip Step
                         │
                         ▼
                    Low-D State
                         │
              ┌──────────┴──────────┐
              │                     │
              ▼                     ▼
           Mirror A              Mirror B
              │                     │
              └──────────┬──────────┘
                         ▼
                    Compare
                         │
              ┌──────────┼──────────┐
              ▼          ▼          ▼
          alignment    drift      unknown
              │          │          │
              └──────────┼──────────┘
                         ▼
                      Record

---

Q. GraphとしてのT3

T3そのものを、

[
G_{T3}=(V,E)
]

と見ることもできる。

頂点：

[
V=
{
Material,
State,
Feature,
Representation,
Mirror,
Drip,
PullPoint,
Difference,
Failure
}
]

辺：

[
E=
{
transform,
extract,
project,
mirror,
compare,
pull,
drip,
fail
}
]

ただし、このGraphも「本質的構造」ではない。

あくまで、

«観測操作を整理するためのGraph»

である。

---

R. 実験条件表

Axis| 候補| 観測対象| 未確定事項
Material| Collatz| trajectory| 何が重要か
Scale| point/window/global| scale drift| 最適scale
Angle| value/parity/valuation/geometry/time| representation shift| Angleの意味
Mirror| A/B| correspondence| 比較基準
Drip| H→L| information transformation| 何を失ったかの意味
Pull| X1,X2,...| intermediate state| Pull頻度
Difference| Compare(Xi,Xj)| structural difference| residualかどうか
Drift| qualitative classes| deviation| classification rule
Failure| no-match/undefined| breakdown| failureの意味

---

S. 実験プロトコル

Experiment 001 — Basic Trajectory

入力：

[
n=7
]

取得：

[
x_0,x_1,\ldots,x_T
]

保存：

X0
X1
...
XT

---

Experiment 002 — Parity Drip

[
Trajectory
\rightarrow
Parity
]

各段階で、

source
target
preserved
lost
unknown

を保存する。

---

Experiment 003 — Valuation Mirror

[
Trajectory
\leftrightarrow
v_2(3x+1)
]

を比較する。

結果は、

≌ / non-correspondence / unknown

のいずれかを許す。

---

Experiment 004 — Geometry Provocation

[
x_t\rightarrow(t,x_t)
]

[
x_t\rightarrow\Delta x_t
]

[
x_t\rightarrow\Delta^2x_t
]

を実行。

視覚的patternが現れても、意味づけしない。

---

Experiment 005 — High → Low → Expansion

[
H
\rightarrow
L
\rightarrow
{H'_1,H'_2,\ldots}
]

を試す。

ここで、

[
H'_i=H
]

である必要はない。

むしろ、

[
H'_i\neq H
]

となる場所を観測する。

---

T. TPC的Drift Record

Driftを、

[
D_i=
(
Origin,
Operation,
Intermediate,
Direction,
Magnitude,
Effect,
Unknown
)
]

とする。

例えば、

{
  "origin": "trajectory",
  "operation": "projection_to_parity",
  "intermediate": "parity_sequence",
  "direction": "high_dim_to_low_dim",
  "magnitude": null,
  "observed_effect": [
    "value information disappeared",
    "parity remained"
  ],
  "unknown": [
    "whether discarded information matters"
  ]
}

ここでMagnitudeは無理に数値化しない。

---

U. Residualへの昇格条件

Residualという名前を使うのは後段にする。

最初は、

[
\Delta_{ij}

Compare(X_i,X_j)
]

だけを保存する。

その後、人間が、

これは単なるdifferenceではなく
特定の基準からのdeviationとして扱える

と判断した場合だけ、

[
\Delta_{ij}\rightsquigarrow R_{ij}
]

へ昇格させる。

つまり、

[
Difference
\not\Rightarrow
Residual
]

である。

---

V. 「≌」の内部仕様

T3では、≌を一種類の関係にしない方がよい。

候補：

≌_temporal
≌_structural
≌_representational
≌_geometric
≌_transition
≌_scale
≌_functional
≌_unknown

例えば、

[
A\overset{\text{temporal}}{\≌}B
]

なら、

「時系列上のイベント位置だけが比較可能」

という意味になる。

これは、

[
A=B
]

よりはるかに弱い。

---

W. さらに重要な非対称性

T3ではMirrorを、

[
A\leftrightarrow B
]

と書くだけでなく、

[
A\xrightarrow{f}B
]

と

[
B\xrightarrow{g}A
]

を別々に保存する。

なぜなら、

[
g(f(A))=A
]

とは限らないからである。

さらに、

[
f(g(B))=B
]

も仮定しない。

この非可逆性そのものが、

Drip
compression
expansion
representation loss

を可視化する。

---

X. T3の最小原理

最終的に、T3は以下の7原則に圧縮できる。

1. Preserve

途中状態を捨てない。

2. Separate

ObservationとInterpretationを分離する。

3. Compare

異種表現を比較してみる。

4. Don't Equate

[
≌\neq=
]

を維持する。

5. Pull

任意の途中状態を再取得できるようにする。

6. Fail

対応不能・未定義・破綻を正式な出力にする。

7. Leave Open

未知を未知のまま保存する。

---

Y. 最終的な不全フレーム

T3は、

[
\boxed{
[[Collatz + ?;;≌\rightarrow;Composite\ Skeleton]]
}
]

から始まる。

実験後も、

[
?
]

を消す必要はない。

むしろ、

[
?
\rightarrow
{
?
_1,
?
_2,
?
_3,\ldots
}
]

と未知の内部構造が細分化されることが、T3の成果になり得る。

最終Traceは例えば、

? 
├── undefined operator
├── representation shift
├── scale mismatch
├── mirror asymmetry
├── information loss
├── non-correspondence
├── unexplained alignment
├── implementation failure
└── unknown

となる。

これは「問題が解決した状態」ではない。

むしろ、

«最初は一つの "?" だったものが、観測可能な複数の不全状態へ分解された状態»

である。

---

Z. 最終設計図

T3を一つの装置として描くなら、

                         ┌────────────────────┐
                         │      UNKNOWN ?      │
                         │ 未定義・欠損・探索領域 │
                         └─────────┬──────────┘
                                   │
                                   ▼
┌─────────────┐            ┌─────────────┐
│   Material  │───────────▶│    State    │
│   Collatz   │            │     X_i     │
└─────────────┘            └──────┬──────┘
                                   │
                 ┌─────────────────┼─────────────────┐
                 ▼                 ▼                 ▼
            Trajectory          Parity           Valuation
                 │                 │                 │
                 └─────────────────┼─────────────────┘
                                   ▼
                              Geometry
                                   │
                                   ▼
                             High-D State
                                   │
                              ┌────┴────┐
                              │  PULL   │
                              └────┬────┘
                                   │
                                   ▼
                                DRIP
                                   │
                                   ▼
                             Low-D State
                                   │
                       ┌───────────┴───────────┐
                       ▼                       ▼
                   Mirror A                Mirror B
                       │                       │
                       └───────────┬───────────┘
                                   ▼
                                ≌ Compare
                                   │
                ┌──────────────────┼──────────────────┐
                ▼                  ▼                  ▼
            Alignment            Drift             Unknown
                │                  │                  │
                └──────────────────┼──────────────────┘
                                   ▼
                             Difference
                                   │
                                   ▼
                                Trace
                                   │
              ┌────────────────────┼────────────────────┐
              ▼                    ▼                    ▼
           Observed             Failed               Unresolved
              │                    │                    │
              └────────────────────┼────────────────────┘
                                   ▼
                                  END
                                   │
                         ※ `?` は消えない
                         ※ `≌` は `=` にならない

結論

T3の「装置としての意味」は、現時点では一つに固定しない。

最も弱い、しかし最も安全な定義は、

[
\boxed{
T3 =
\text{途中状態を保存しながら異種表現を変換・対置・比較し、
その対応・非対応・Drift・失敗・未知を記録するToybox}
}
]

である。

したがって、

[
\boxed{
T3(X;S,\theta,M,D)
\rightarrow
{
States,
Pulls,
Mirrors,
Drips,
Differences,
Drifts,
Failures,
Unknowns
}
}
]

を一つの出力単位とする。

ここで重要なのは、最後の集合に

[
Unknowns
]

が残っていることである。

T3が優れた結果を出すとは、

[
Unknowns=\varnothing
]

になることではない。

むしろ、

[
Unknown_0
\rightarrow
Unknown_1
\cup Unknown_2
\cup Unknown_3
\cup\cdots
]

のように、

「何が分からないのか」をより細かく記述できること

を、少なくとも第一段階の成功条件として置ける。

そして最終的にも、

[
A\overset{?}{\≌}B
]

という状態を許す。

これは未完成ではあるが、設計上は欠陥ではない。

未完成であることが観測可能なら、それ自体がT3の正式な状態だからである。
