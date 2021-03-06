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

* 製品ベンダ、モデルベーステストツールのメーカー、テストサービスプロバイダ、テストエンジニア、ソフトウェア開発者、政府機関、調達担当者および研究者などのモデルベースのテスト技術に晒されているすべての関係するグループのテスト専用のモデルの仕様に必要な合意された用語と概念を1つの文書にまとめる。 

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

モデルベースのテスト開発では、エンジニアはテストされるシステムの一連の要件から開始します。通常は自然言語で書かれた仕様で与えられます。 技術者は、この文書に記載されている要件を満たすモデリング表記法を使用してモデルを作成します。 このモデルはこれらの要件をコード化し、機能的な振る舞いの側面とこれらがテストされるインタフェースを記述します。

次に、モデルは、テスト選択基準、すなわち対象範囲またはカバーされるべきものを指定するテスト目的、およびこれらの目標がどのようにカバーされるべきかを指定するテスト目的を追加または選択することによってテスト生成の目的で作成される。 すべての自明でないモデルから、無限または膨大な量のテストを導き出すことができるので、テストの選択が必要です。 モデルベースのテストツールは、これらの基準に適合する抽象テストスイートを自動的に生成します。 この結果として生じる抽象テストスイートは、SUTに対するテスト実行を可能にするために適応させる必要があるかもしれません[i.4]、[i.5]。

>注：テスト選択基準の仕様は本文書の範囲外である。
>

モデルベースのテストでは、手動テスト実行のための非公式の指示、テーブルやメッセージシーケンスチャートのようなグラフィカルフォーマット[i.11]、JavaやC＃のようなスクリプトやプログラミング言語を含む1つ以上のフォーマットで抽象テストをオフラインで生成できます。 またはＴＴＣＮ − ３ ［ｉ．３］。 第２のステップにおいて、オフラインテストは、テスト適応と共に実行可能テストにコンパイルされ、テスト中のシステムに対して実行される。 抽象テストもオンラインで生成することができ、すなわち個々のテストステップはテスト中のシステムに対するテスト適応を介して直ちに実行され、テストステップの実行から得られる観察結果は直接テスト生成エンジンにフィードバックされる。 テスト実行中に、テストシステムは最終的に、生成された各テストの結果に基づいて合格、不合格、または決定的でないテスト判定を発行します。

図1モデルベースのテスト開発★

モデルベースのテスト開発は、関連する成果物に対して複数のレベルでフィードバックを提供します。 まず、機能要件を取り込むモデルを作成するプロセスは、潜在的にテストが実行される前、またはシステムの任意の部分が実装される前に、システム仕様の整合性に関するフィードバックを提供します。 次に、生成されたテストケースの検査とモデル分析からのフィードバック（デッドロックや安全条件の確認など）により、システム仕様またはモデルの問題が明らかになります。 第3に、テストが最終的に実行されると、SUT、システム仕様、またはモデルの問題が発見される可能性があります。

本文書の残りの部分では、記述されたモデルベースのテスト開発を可能にするモデリング表記法の要件は概念レベルでとらえられている。 これらの要件に適合する一般的に使用されているモデリング表記法スタイルの有益な議論については、付録Aを参照してください。

# 5 一般的なモデリング表記法の要件

モデルは、プログラミング言語とよく似たエンジニアリングプロセスで使用される明確に定義された言語の成果物です。 それらは、複雑なシステムでは大きくなり、システム上のさまざまな観点に対処し、チームで作成され、繰り返し進化し、さまざまな方法で再利用され、ドキュメントを必要とし、ライフサイクル管理を必要とします。 さらに、モデルはしばしばそれらが記述する行動的側面のいくつかについてのアルゴリズム記述を必要とします。 そのため、モデリング表記は、ソフトウェア工学のプログラミング言語に共通の概念をサポートするものとします。 これらの概念はこの節で説明されています。

## 5.1 モジュール化

全体モデルは、システムの多数の複雑な側面を記述することができ、それは最もよく理解され独立して維持されることができる。 したがって、モデリング表記は、モジュール化のための手段を提供し、システム仕様の側面を分離して再結合することで、それらを独立して開発、理解、発展、そしてシステム全体に統合できるようにすることで、問題分離のソフトウェアエンジニアリングの原則をサポートします。 モジュール化は、1つまたは複数のシステムの異なる構成またはバージョンにおける個々のコンポーネントのモデル再利用もサポートする必要があります。

より具体的には、モデリング表記は以下をサポートする必要があります。

* a）1つの文書または一連の文書のように、独立した成果物内でモデル全体の側面を分離する方法を提供します。
* b）他のモデル成果物からの孤立した成果物の依存関係を特定する方法を提供する。
* c）モデル成果物を階層的に階層化する方法を提供する。
* d）孤立したモデルアーティファクトの構成について明確に定義された意味論を持つ。

モジュール化は多くの方法で達成することができ、その詳細は本文書の範囲外である。 一般に、モジュール化は、コンポーネント、モジュール、名前空間、および明確に定義されたインターフェースを持つクラスなどの概念を使用することによって、プログラミング言語と非常によく似た方法で実現できます。 ただし、モジュール化は、モデル構成、モデル変換など、モデル固有の概念によっても実現できます。

## 5.2 アルゴリズム

ほとんどすべての自明でないモデリング問題は、入力データから出力を計算し、次のシステム状態を計算し、条件をチェックし、データ値に対する制約を定義するなどのアルゴリズムの仕様を必要とします。 例えば、SUTの状態の変化を記述するためには言語サポートが必要です。

したがって、モデリング表記法は、以下に説明するように、アルゴリズム設計およびデータ操作のための基本的な手段を提供します。

* a）表記法は明確な操作上の意味論に基づいていなければならない。
* b）表記法は、ISO / IEC 11404 [1]で定義されているように、少なくとも基本データ型のboolean、integer、および文字列、ならびにユーザ定義のデータ型の記録および配列をサポートする。
* c）表記法は、浮動小数点数、列挙型、連想配列など、より高度なデータ型をサポートする必要があります。
* d）表記法は、任意精度の整数やサイズが固定されていない配列など、無制限のデータをサポートする必要があります。
* e）表記法は、変数、代入、条件文などの基本制御構文をサポートしなければならない。
* f）表記法はループのような高度な制御構造をサポートするべきです。
* g）表記法は、手続き上の抽象化、すなわち特定のアルゴリズムの実現を抽象化する手続き、方法、または機能の定義を可能にすることをサポートするべきである。

これらの機能を提供することは多くの方法で達成することができるが、これらの機能が特定のモデリング表記法のために最初から定義されるのではなく確立された表記法に基づくことが有益であると考えられる。

## 5.3 ドキュメンテーション

モデルはシステムの正確な形式化された記述を提供しますが、レビューアや他の第三者にとって理解しやすくするために、自然言語のドキュメントを伴う必要があります。 したがって、モデリング表記法は、多くのプログラミング言語と同様に、モデル要素の正式な定義をコメントやより正式な文書で補強する手段をサポートするものとします。

すなわち：

* a）モデリング表記法は、非公式コメントを関連するモデル要素定義に添付する方法をサポートしなければならない。
* b）モデリング表記法は、正式な文書を関連するモデル要素の定義に添付する方法をサポートするべきである。

上の（a）と（b）の違いは形式化の程度であることに注意してください。非公式なコメントは元のモデルアーティファクトに現れるかもしれませんが、その形式は任意で、ツールチェーンで処理することはできません。  - 定義されたフォーマットで、ツールチェーンによって処理することができます。 たとえば、一貫性を検証したり、モデルレポート生成プログラムの入力として使用したりできます。

# 6 システムインタフェースのモデリング

テストを容易にするために、モデルベースのテストのためのモデリング表記は、システムと通信するために利用可能なインタフェースを正確に定義する方法を提供しなければならない。 **システムインタフェースはシステムを制御し観察することを可能にする入力および出力動作を定義する。** モデルから生成されたテストスイートは、入力アクションを使用してシステムの機能を刺激し、システムの応答を表す出力アクションを観察して、それらがモデル化された動作に準拠しているかどうかを検証します。 図2はその関係を示しています。

図2システムインタフェースの役割★

モデリングで指定されているシステムインタフェースはほんの一部であり、実際のシステムインタフェースを抽象化したものです。 抽象化は、他のものを隠しながらシステムの特定の側面をテストすることに集中することから生じる、または例えばメッセージまたはオペレーションの低レベルデータ表現を除外し、システムによって提供されるすべての利用可能なインタフェースのサブセットのみをモデル化することのような詳細を単純化することから生じる。 またはメッセージまたは操作パラメータのサブセットのみをモデリングする。 モデルと生成されたテストスイートにとって、実際のシステムはブラックボックスです。 モデルとテストは選ばれたシステムインタフェース抽象化の観点から定義されます。

## 6.1 アクション

アクションは、アクション名、一連のパラメータ、および方向性（入力または出力）からなる、システムインタフェースを介してトリガまたは観察されるシステムのアトミックアクティビティです。 アクションは、メッセージ、イベント、操作の呼び出しまたは操作からの戻り、その他の種類の通信手段など、非同期通信と同期通信の両方を表すために使用されます。

モデリング表記法は、以下に説明するように動作をサポートするものとします。

a）モデル化表記法は、名前、アクションが入力アクションか出力アクションか、そしてパラメータタイプと一緒にアクションの宣言をサポートしなければならない。
b）パラメータ型は、少なくとも5.2 b）項で定義されている基本型を含み、5.2 c項で定義されている高度な型を含むべきである。

## 6.2 オペレーション

操作は一連の操作で、1つの操作は操作（例： "call"操作）またはcall-back操作（例： "get call"操作）を開始する入力を表し、他の操作はさまざまな方法での出力を表します。 操作の終了（例：「戻る」または「例外」アクション）またはコールバック操作。 同期通信が支配的なドメインでは、この概念が直接サポートされていれば有益です。 そのようなドメインでは、モデリング表記法は基本的な構成アクションを宣言するための速記として宣言操作をサポートする必要があります。

## 6.3 ポート

ポートは、全体としてシステム全体の特定の論理インタフェースを構成する一連のアクション（または操作）を表します。 たとえば、ポートは、システムによって提供されるいくつかのアクセスポイントまたはサービスのうちの1つを表します。 ポートでのクラスター化行動はモデルの構造的な明快さを助ける。 ポートは、例えば、要求に応じて異なるクライアントに同様のサービスを提供するために、複数のインスタンスに存在してもよい。

* a）モデリング表記法は、アクションや操作をグループ化する方法として、ポートまたは同様の概念（アクセスポイント、通信チャネルのエンドポイント、インタフェース、契約など）をサポートする必要があります。
* b）モデリング表記法は、複数のポートのインスタンス（または同様の概念）をサポートする必要があります。 複数のインスタンスの代わりに、モデリング表記法は、入出力アクションまたはポートのオペレーションの専用パラメータを使用して、アクションまたはオペレーションが動作しているポートのインスタンスを区別することができる。

## 6.4 構成

多くの場合、より複雑なシステムは、何らかの形式の通信チャネルを使用して互いに同時に対話するエンティティの構成によって妥協されています。 場合によっては、システムコンポーネントのトポロジが動的に変化していることもあれば、システムの存続期間中静的に定義されていることもあります。

a）モデリング表記法は、静的コンポーネント構成の具体化と同様に、それらの間の同時アクティビティと通信チャネルを持つ個々のモデルコンポーネントの仕様をサポートするべきである。 理想的には、モデルコンポーネントインタフェースの仕様は、モデルコンポーネントインタフェースの仕様と同じ概念に従います。
ＳＵＴとモデルから導出されたテストスイートとの間のシステムインタフェース - すなわち、それは１つまたは複数のポートにクラスタ化された入力および出力動作または動作に関して与えられる。

# 7 システム動作のモデリング

システムの機能的な振る舞いの仕様は、モデルベースのテストにおけるコアモデリング活動です。 **機能的な振る舞いは、例えば、ルール指向またはプロセス指向のテキスト表記法、またはステートマシン、状態図、シーケンスチャート、フローチャートなどの図式表記法**を使用して、さまざまな方法でモデル化できます。 本文書は特定の表記スタイルを規定しているのではなく、むしろ概念レベルでの行動モデリングのための要件を捉えている。

## 7.1 システム状態

SUTの抽象状態のモデリングは、特定のアクションが許可されているかどうかを特定するため、行動モデリングの中心的側面です。 そのような状態のモデル化には、次の表記法が適用されます。

a）モデル化表記法は、以下のうちの少なくとも1つを許可することによってシステム状態をモデル化することを許可しなければならない。
 * これらの変数に割り当てられた現在の値がシステムの状態を構成する一連の状態変数の定義。
 * システムの状態を論理的に定義する一連の制約の定義。
 * 現在のプログラムカウンタとプログラムスタックがシステムの状態を構成するプログラムの定義。
 *  UMLステートマシン図[i.8]、[i.9]などのステートマシンを表す図の定義。図中のすべての状態は、システムの状態または状態の一部を構成します。
 *  UMLアクティビティ図[i.8]、[i.9]のようなフローチャートを表す図の定義。2つのアクションまたはアクティビティノード間のすべてのエッジがシステムの状態を構成します。
 * メッセージシーケンス図[i.11]、UML相互作用図[i.8]、[i.9]のようなシーケンス図を表す図の定義。システムに関連するインスタンスは、システムの状態を表します。
 * 上記の2つ以上のアプローチの組み合わせ。 特に、状態変数を使用して状態を記述する最初の方法と他の方法の組み合わせ。 組み合わせでは、システムの状態は組み合わされたアプローチの状態の積で表されます。

b）現実的なシステムを扱うために、モデル化表記法は、無制限の数のシステム状態をモデル化することを可能にするべきです。 これは通常、モデル設計時に境界が定められていない領域にわたって状態変数を範囲指定できるようにすることで実現されます。

>注：テスト選択時の範囲の境界は、この要件によって除外されません。
>

c）モデリング表記法は、次のうち少なくとも1つを許可することによって、非公式の要件参照をシステム状態に関連付けることを許可する必要があります。
 * ルールシステム[i.7]の状態変数について述語を定義し、それを特別な識別子と関連づける。述語が真のとき、識別子に関連する非公式の要件が満たされるようにする。
 * 非公式の要件参照をモデルの状態に関連付けることを可能にするプログラム内の特別な命令のサポート。
 * 一連の制約に特別な識別子で注釈を付ける。
 *  UML状態図[i.8]、[i.9]などのステートマシン内のステートに特別な識別子を付けて注釈付けする。
 *  UMLアクティビティ図[i.8]、[i.9]などのフローチャート内のエッジに特別な識別子で注釈を付ける。

d）モデル化表記法は、初期状態の識別を可能にし、最終システム状態の識別を可能にしなければならない。

## 7.2 システム状態遷移

与えられた機能がシステム仕様に従って実装されていることを評価するために、SUTは一連の状態遷移を通して動かされる必要があります。 システム状態遷移は、入力アクションを提供することによってトリガーされ、1つ以上の出力アクションの観察を必要とする場合があります。 状態遷移は、システム仕様に記載されている非公式の要件とも密接に関連していることがよくあります。 最後に、他のシステムとの通信を処理するときには、時間が中心的な役割を果たすことがよくあります。 状態遷移のモデリングには、次の表記法が適用されます。

a）モデリング表記法は、次のうち少なくとも1つを許可することによって、2つのシステム状態間の遷移を定義できるようにしなければならない。
 * 動作状態遷移規則[i.7]の定義。有効化条件（状態変数に対する述語）と状態変数のアルゴリズム更新からなる。
 * ソース状態を識別する事前条件とターゲット状態を識別する事後条件からなる宣言的状態遷移規則[i.7]の定義。両方の条件は状態に対する述語である。変数
 * ポートからメッセージを受信または送信する、あるいはプログラム内の状態変数に新しい値を割り当てる。
 *  UML状態図[i.8]、[i.9]のように、ステートマシンで2つの状態間に矢印を描く。
 *  UMLアクティビティ図[i.8]、[i.9]などのフローチャートでアクションまたはアクティビティノードを描画する。
 *  UML相互作用図[i.8]、[i.9]、またはメッセージシーケンス図[i.11]のように、シーケンス図で2つのライフライン間に矢印を引く。
 * 上記のアプローチを2つ以上組み合わせる。

b）モデリング表記法は、次のうちの少なくとも1つを許可することによって、1つの入力と1つ以上の出力アクション、または（サポートされている場合は）パラメーターを含む操作を遷移に関連付けることを許可します。
 * アクションまたは操作名とパラメータを状態遷移規則[i.7]と関連付け、パラメータを規則の有効化条件、事前条件または事後条件と関連付ける。
 * プログラム内のポートとの間でパラメータを使用して特定のアクションまたは操作を送受信する。
 *  UML相互作用図[i.8]、[i.9]、またはメッセージシーケンス図[i.11]のようなシーケンス図の矢印を、アクションまたは操作の名前とパラメータに関連付ける。
 *  UMLアクティビティ図[i.8]、[i.9]のようなフローチャート内のアクションまたはアクティビティノードを、アクションまたは操作の名前とパラメータに関連付ける。
 * 上記の1つ以上のアプローチを組み合わせる。

c）モデリング表記法は、次のうち少なくとも1つを許可することによって、非公式の要件参照を状態遷移に関連付けることを許可する必要があります。
 * 参照がルールから作成された各状態遷移に追加されるように、要件参照をルール[i.7]に関連付ける。
 * 参照を状態遷移に関連付けることを可能にするプログラム内の特別な命令をサポートする。
 *  UML相互作用図[i.8]、[i.9]、メッセージシーケンス図[i.11]などのシーケンス図の矢印に特別な識別子を付けて注釈を付ける。
 *  UMLアクティビティ図[i.8]、[i.9]などのフローチャート内のアクションまたはアクティビティノードに特別な識別子で注釈を付ける。

d）モデリング表記法は、時間の概念をサポートし、次のうち少なくとも1つを許可することでタイミング制約を状態遷移に関連付けることができるようにする必要があります。
 * 規則の発動のための遷移の許容遅延の定義[i.7]。
 * タイマーの概念をサポートする。
 *  UML状態図[i.8]、[i.9]などの状態図、またはUMLインタラクション図[i.8]、[i.9]などのシーケンスチャート内のライフラインに矢印を注釈する 許容遅延のあるシーケンスチャート[i.11]

## 7.3 非決定論

非決定論は、与えられた状態において、SUTが1つのシーケンスの入力アクションまたは状態遷移に対して1つ以上の可能なシーケンスの出力アクションを生成することができる状況です。 非決定論の概念は、通信システムをモデル化するときに特に重要です。これらのシステムは、テストに利用可能なインタフェースを介して予測または制御することができない環境の影響を受ける可能性があるためです。 モデル決定者がシステムの特定の行動的側面をモデル化しないことを選択した場合、モデルの抽象化からも非決定性が生じる可能性があります。

モデリング表記法は、以下のうちの少なくとも1つを可能にすることによって、与えられた状態から複数のシステム状態遷移のうちの1つをとる可能性をモデル化する能力を可能にするべきです。

* 同一の送信元状態に適用可能な複数の状態遷移規則[i.7]の定義。
* 状態遷移を選択するようにユーザーに問い合わせることによってテスト実行時に解決できる非決定的選択ステートメントをサポートします。
* ポートから送受信できるモデルで、複数の制御スレッドをサポートします。
* UML状態図[i.8]、[i.9]のような状態図内に、同じシステム状態からの同じトリガと異なる出力アクションを持つ複数の矢印の描画。

---

# 附属書A（参考）表記法スタイルのモデル化の例

この附属書は現在の文書で指定された要件を満たすモデリング表記法のいくつかの最も一般的なスタイルの簡単な概要を含みます。

---

## A.1ルールベースの表記

ルールベースの表記法は、状態遷移ルールがシステムの動作を記述するテキストモデリング表記法です。 それらは拡張有限状態機械（EFSM）[i.12]または抽象状態機械（ASM）[i.7]とも呼ばれます。

ルールベースの表記法では、システムの状態は一連の状態変数によって記述されます。 そして、一連の状態遷移規則が運用スタイルで提供されます。 これらの移行ルールは、次のもので構成されています。

* アクション名とそのパラメータ。ルールの起動時に、ルールによって作成された遷移にラベルを付ける方法を記述します。
* 有効化条件。状態変数とアクションパラメータを述語とし、どの状態でどのアクション値を使用してルールを起動するかを記述します。
* 状態更新。ルールが起動された場合に、状態変数がルールによってどのように変更されるかを記述します。
* 非公式の要件やタイミングの制約への参照など、その他の情報。

ルールベースの表記法は通常、1つの区別された初期状態を持ちます。これは状態変数への割り当てによって与えられます。

ルールベースの表記法における非決定性は、与えられた状態で異なる出力アクションを持つルールを有効にすることで簡単に表現できます。

状態変数およびアクションパラメータモデリングで使用されているようなデータドメインに対する基礎となるアルゴリズムサポートが十分にサポートされている場合、ルールベースのモデリング表記法は本文書の要件を満たす。

拡張有限状態機械は、状態と遷移の数が制限されているルールベースの表記法の変形です。 これらの範囲を提供することが方法論的にテスト選択のためのスライスの一部である限り、これは本文書と矛盾しない。

---

## A.2 状態図の表記

状態図は、システムモデリングのさまざまなバリエーションに存在する図表表記です。 それらは、例えばUML [i.8]、[i.9]の一部です。 状態チャートは、ルールベースの表記の側面とグラフィック構造を組み合わせたものです。

一般に、状態図は状態のノードと状態遷移の有向矢印を含む図です。 状態図は、状態変数のセットに関連付けることができます。 状態図の矢印には、通常、次の情報が含まれています。

* アクション名とそのパラメータ。矢印によって作成された遷移に、実行時にラベルを付ける方法を説明します。
* 有効化条件。これは状態変数とアクションパラメータの述語であり、どの状態で矢印をとることができるかを記述します。
* 状態更新。矢印が発生した場合に状態変数がどのように変更されるかを記述します。
* 非公式の要件やタイミングの制約への参照など、その他の情報。

これらの基本的な要素に加えて、状態図は状態の階層的なグループ化や状態の並列合成もサポートしています。 本文書の範囲を超える状態図には、さらに多くの構成要素があります。

状態チャートベースのモデリング表記法は、状態変数およびアクションパラメータモデリングで使用されているようなデータドメインに対する基礎的なアルゴリズムサポートが十分にサポートされているという条件で、本文書の要件を満たす。

## A.3 プロセス指向の表記

プロセス指向モデリングでは、コンポーネントのシステムは、各コンポーネントのアクティビティを独立した順次プロセス（またはスレッド）として記述することによって指定されます。 このプロセスは通常、命令型モデリングを使用して、またはプログラミング言語に基づいて記述されます。 各プロセスは、独立したデータ状態を持ち、一連の状態変数で構成されています。 その寿命の間、プロセスはその環境からの入力を積極的に監視し、通常はポートまたは通信チャネルの概念を使用することによって出力を生成します。

タイミング制約はプログラムによる遅延とタイムアウトによって記述されます。

基礎となるアルゴリズムのサポートが十分であれば、プロセス指向モデリング表記法は本文書の要件を満たします。

以上。