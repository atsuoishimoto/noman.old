# git merge コマンド

複数の開発履歴を統合します。

## 概要

`git merge`は複数のコミット履歴を一つの統一された履歴に結合します。主に、あるブランチの変更を別のブランチに統合するために使用され、一般的には開発が完了した後にフィーチャーブランチをメインブランチにマージするときに使われます。このコマンドは指定されたブランチの変更を現在のブランチに取り込みます。

## オプション

### **-m, --message=\<message\>**

マージコミットに使用するコミットメッセージを設定します。

```console
$ git merge feature-branch -m "ログイン機能の新しいフィーチャーブランチをマージ"
```

### **--no-ff**

マージがfast-forwardで解決できる場合でも、マージコミットを作成します。

```console
$ git merge --no-ff feature-branch
Merge made by the 'recursive' strategy.
 login.js | 75 ++++++++++++++++++++++++++++++++++++++++
 1 file changed, 75 insertions(+)
 create mode 100644 login.js
```

### **--ff-only**

現在のHEADが既に最新であるか、マージがfast-forwardとして解決できる場合を除いて、マージを拒否し、非ゼロのステータスで終了します。

```console
$ git merge --ff-only upstream/main
Updating 1234abc..5678def
Fast-forward
 README.md | 10 +++++-----
 1 file changed, 5 insertions(+), 5 deletions(-)
```

### **--abort**

現在の競合解決プロセスを中止し、マージ前の状態に戻そうとします。

```console
$ git merge feature-branch
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.

$ git merge --abort
```

### **--squash**

マージが行われたかのように作業ツリーとインデックス状態を生成しますが、実際にはコミットを作成せず、HEADも移動しません。

```console
$ git merge --squash feature-branch
Updating 1234abc..5678def
Fast-forward
Squash commit -- not updating HEAD
 login.js | 75 ++++++++++++++++++++++++++++++++++++++++
 1 file changed, 75 insertions(+)
 create mode 100644 login.js
```

### **-s, --strategy=\<strategy\>**

指定されたマージ戦略を使用します。一般的な値はrecursive、resolve、octopus、ours、subtreeなどです。

```console
$ git merge -s recursive feature-branch
```

## 使用例

### 基本的なブランチのマージ

```console
$ git checkout main
Switched to branch 'main'

$ git merge feature-branch
Updating 1234abc..5678def
Fast-forward
 login.js | 75 ++++++++++++++++++++++++++++++++++++++++
 1 file changed, 75 insertions(+)
 create mode 100644 login.js
```

### 複数のブランチをマージする

```console
$ git checkout main
Switched to branch 'main'

$ git merge feature1 feature2 feature3
Merge made by the 'octopus' strategy.
 feature1.js | 20 ++++++++++++++++++++
 feature2.js | 15 +++++++++++++++
 feature3.js | 30 ++++++++++++++++++++++++++++++
 3 files changed, 65 insertions(+)
```

### マージ競合の解決

```console
$ git merge feature-branch
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
Automatic merge failed; fix conflicts and then commit the result.

# index.htmlの競合を手動で解決した後
$ git add index.html
$ git commit
[main 1234abc] Merge branch 'feature-branch'
```

## ヒント:

### フィーチャーブランチには`--no-ff`を使用する

フィーチャーブランチをマージする際は、`--no-ff`を使用してブランチの履歴を保持し、コミット履歴にフィーチャーブランチがマージされたことを明確にすることを検討してください。

### マージ結果のプレビュー

実際のマージを実行する前に、以下のコマンドを使用してマージされる変更をプレビューできます：
```console
$ git diff ...branch-name
```

### Fast-Forwardマージを理解する

Fast-forwardマージは、ターゲットブランチのコミットが現在のブランチの直接の子孫である場合に発生します。Gitはマージコミットを作成せずにポインタを前方に移動するだけです。マージコミットを強制したい場合は`--no-ff`を使用してください。

### 履歴をクリーンにするためのSquashマージ

フィーチャーブランチからの全ての変更を対象ブランチの単一のコミットにまとめたい場合は`--squash`を使用します。これによりコミット履歴がより整理され、読みやすくなります。

## よくある質問

#### Q1. マージとリベースの違いは何ですか？
A. マージは両方のブランチからの変更を組み合わせた新しいコミットを作成し、ブランチの履歴を保持します。リベースはブランチのコミットをターゲットブランチの上に再生し、線形の履歴を作成しますが、コミット履歴を書き換えます。

#### Q2. マージを元に戻すにはどうすればよいですか？
A. マージをプッシュしていない場合は、`git reset --hard HEAD~1`を使用して最後のコミットを元に戻せます。既にプッシュしている場合は、`git revert -m 1 <マージコミットのハッシュ>`を使用してマージを元に戻す新しいコミットを作成することを検討してください。

#### Q3. Gitマージでの「fast-forward」とは何ですか？
A. Fast-forwardマージは、フィーチャーブランチが作成されてから基本ブランチに新しいコミットがない場合に発生します。Gitはマージコミットを作成せずに、基本ブランチのポインタをフィーチャーブランチのポインタまで前進させるだけです。

#### Q4. マージ競合を解決するにはどうすればよいですか？
A. Gitが競合を報告した場合、競合したファイルを編集して差異を解決し、`git add`を使用して解決済みとマークし、最後に`git commit`を実行してマージを完了します。

## 参考資料

https://git-scm.com/docs/git-merge

## 改訂履歴

- 2025/05/04 初版作成