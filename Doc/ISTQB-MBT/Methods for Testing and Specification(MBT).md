Methods for Testing and Specification(MBT)
==========================================
ETSI ES 202 951 V1.1.1 (2011-07)

URL:https://www.etsi.org/deliver/etsi_es/202900_202999/202951/01.01.01_50/es_202951v010101m.pdf

## 知的財産権
本文書に不可欠または潜在的に不可欠な知的財産権は、ETSIに宣言されている可能性があります。 これらの重要な知的財産権に関する情報がある場合は、ETSI会員および非会員向けに公開されており、ETSI SR 000 314に記載されています。「知的財産権（IPR）。 ETSI規格に関して "、ETSI事務局から入手可能です。 最新のアップデートはETSI Webサーバー（http://ipr.etsi.org）で入手できます。

## 序文
このETSI規格（ES）は、ETSI技術委員会試験および規格用方法（MTS）によって作成されています。

## 前書き
業界でのモデルの使用による自動テスト設計の最近の成功と展開に基づき、TC MTSは特に標準テスト仕様開発の文脈におけるモデルベーステストの研究を調査しました[i.1]。 主にテスト実行の自動化に焦点を当てている他の方法およびアプローチとは対照的に、本文書はテスト設計の自動化のためのモデルベースのテストの使用を考慮している。

モデルベースのテストは、標準のより徹底的で早い検証と、テストケース成果物の効率的な自動生成を容易にします。 システムの外部の動作のテストを実行するテキストまたは表形式の説明、スクリプトまたはプログラム。 モデルベースのテストでは、出力形式に依存しないことと抽象度が高いことから、テストケースの成果物と比較して、標準によって課せられる要件をより直接的に確認できます。 さらに、テスト設計の自動化により、他の組織と同様にETSIがテストスイートをより効率的に作成し、標準化における相互運用性およびコンフォーマンステストに対する需要の高まりに対処することができます。

この文書を作成する動機は次のとおりです。

* 製品ベンダ、モデルベーステストツールのメーカー、テストサービスプロバイダ、テストエンジニア、ソフトウェア開発者、政府機関、調達担当者および研究者などのモデルベースのテスト技術に晒されているすべてのインタレストグループのテスト専用のモデルの仕様に必要な合意された用語と概念を1つの文書にまとめる。 

* 標準化された適合性と相互運用性テストケースの導出のためのモデルの仕様をサポートする。

* 製品認証のためのモデルベーステストの利用を促進する

* そのようなモデルを処理し、そのようなモデルを異なるツール間で交換できる、オープンで競争の激しいモデルベースのテストツール市場の基盤を築くこと。

* 顧客への説明責任を可能にする（法的問題も含む）

その成功と品質を確実にするために、この文書はテスト仕様開発に関わるあらゆる種類の利害関係者、すなわち研究者、ツールメーカー、産業ユーザー、ならびにETSIのテストと相互運用性センターのテスト専門家からのエキスパートのグループによって開発されました。 

それが標準化の文脈でテストの世代に適切であるためにモデル化記法のための要件を指定するので、現在のドキュメントは標準化におけるモデルベースのテストの展開のための基礎を築きます。 そのようなテストは手動テスト仕様[i.2]で定義され使用された十分に確立された概念を固守する必要があります。 加えて、本文書は、標準化されたETSIテスト仕様に含まれるためにモデルによって満たされる必要がある基準、およびモデルが生成されたテストに対して持つ関係を定義します。

# 1 範囲

本文書は、特に通信システムの機能テストの目的に限定されないが、モデルを特定するために必要とされるモデリング表記法のすべての概念を識別し収集する。 そのようなモデルは、例えばTTCN-3テストスイート[i.3]で提唱されているように、ISO / IEC 9646-1 [i.2]の原則に従う抽象テストケースを生成するための基礎を形成します。 モデルベースのテストは手動テスト設計の代替手段を提示しますが、生成されたテストケースを自動的に補完して実行するテストシステム[i.4]、[i.5]の必要性を排除しません。 本文書に記載されている要件に準拠するモデリング表記法を使用するモデルベースのテストツールを使用して、標準化に適した抽象的なテストケースを自動的に生成することができます。

この文書で説明されている概念と要件は、主にTR 102 840 [i.1]で収集された勧告から開発されており、ITU-T勧告Z.500 [i.6]で指定されたモデリング標準仕様の理論的基礎を補完します。 そしてOMG formal / 05-07-07 [i.10]のメタオブジェクト機能を検討した。 それらは特定のモデリング表記やツールとは無関係に指定されます。 具体的なモデリング表記法への概念のマッピングは、この文書では意図的に扱われず、将来の標準のために保存されています。

# 2 参照

＜翻訳省略：原本参照のこと＞

# 3 定義と略語

## 3.1 定義

本文書の目的のために、以下の用語および定義が適用される。

**抽象テストケース**：ISO / IEC 9646-1 [i.2]を参照。

>注：特定のテスト目的を達成するために必要とされる行動の完全かつ独立した仕様。 抽象テストケースは、TTCN-3テストケースのような一連の非公式の指示または形式的な仕様として表すことができます。
>

**抽象テストスイート**：ISO / IEC 9646-1 [i.2]を参照。

> 注：抽象テストケースで構成されるテストスイート。
>

**アクション**：アクション名と一連のデータパラメータで構成される、システムインタフェースを介して起動または監視されるシステムのアトミックアクティビティ

> 注：アクションは入力アクションと出力アクションに分けられます。
>

**（機能的）振る舞い**：仕様の一連の要件によって指定され、一連のアクションシーケンスとして与えられるシステムの機能的振る舞い。各シーケンスは法的シナリオを表し、このセットにないすべてのシーケンスは違法なシナリオを表します。

**決定論的振る舞い**：各入力動作シーケンスに対して、可能な出力動作シーケンスが1つしか存在しないシステムの動作。

**入力行動**：メッセージ、操作、または他の種類の通信手段を表す環境によって刺激される行動

>注：入力アクションはパラメータを持つことがあります。
>

**モデルベースのテスト**：モデルからテストを生成するアプローチの傘

**モデリング表記法**：モデルの仕様に使用される形式言語

**非決定論的挙動**：1つの入力動作シーケンスに対して複数の可能な出力動作シーケンスが存在するシステムの動作

**オフラインテスト生成**：テスト実行時間より先のモデルからのテスト生成

**オンラインテスト生成**：テスト実行中のモデルからの動的テスト生成

**出力アクション**：入力アクションに対する反応として、または自発的にシステムまたはSUTが環境に対して発行したアクション

>注：出力アクションはパラメータを持っているかもしれません
>

**要件**：システムがどのようなものであるべきか、または実行するべきかの文書化された必要性

**（システム）モデル**：システムインターフェースの観点から、システムの意図された外部動作特性、すなわちモデル化されているシステムがその環境とどのように相互作用するかを記述するコンピュータ可読行動モデル。

>注：目的に応じて、システムモデルは、システムインタフェースによって選択された抽象化レベルによって決定されるように、実際のシステム動作の側面のみを取り込むことがあります。
>

**システムインタフェース**：与えられたモデル化とテストの問題に対して選択された抽象化レベルでシステムの入力と出力の動作を定義するモデル要素

**（システム）状態**：SUTが特定の入力アクションを受け入れたり、特定の出力アクションを発行したりするモダリティ

**（システム状態）遷移**：あるシステム状態から次のシステム状態へのSUTの遷移。通常、遷移を引き起こす入力または出力アクションに関連付けられています。

**被試験システム（SUT）**：ISO / IEC 9646-1 [i.2]を参照。

>注：テスト対象の実装が存在する実際のオープンシステム。
>

**テスト生成**：ユーザー定義のテスト選択基準に基づいて、モデルから1つ以上の異なる形式で抽象テストケースを自動的に導出

**テスト目的**：ISO / IEC 9646-1 [i.2]を参照。

>注：テストの明確に定義された目的の散文の説明。
>

**テスト選択**：モデルから導出することができるより大きなまたは無限のテストセットからテスト生成中にテストのサブセットを選択するプロセスまたは結果。

**テスト選択基準**：モデルから生成されたテストケースのセットによって満たされるプロパティ

## 3.2 略語

本文書の目的のために、以下の略語が適用される。

* ASM:Abstract State Machine
* EFSM:Extended Finite State Machine
* MBT:Model-Based Testing
* MSC:Message Sequence Chart
* SUT:System Under Test
* TTCN-3:Testing and Test Control Notation
* UML:Unified Modeling Language

# 4 モデルベースのテスト開発

★ 作成中

# 5 一般的なモデリング表記法の要件

★ 作成中

# 6 システムインタフェースのモデリング

★ 作成中

# 7 システム動作のモデリング

★ 作成中

# 附属書A（参考）表記法スタイルのモデル化の例

★ 作成中

以上。