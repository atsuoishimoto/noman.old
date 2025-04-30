# git merge コマンド

複数のコミット履歴を統合します。

## 概要

`git merge` は、異なるブランチの変更内容を現在のブランチに統合するためのコマンドです。複数の開発ラインを一つにまとめる際に使用され、Git の基本的な機能の一つです。マージには「fast-forward」と「non-fast-forward（3-way）」の2種類があります。

## オプション

### **--ff**（デフォルト）

可能であれば「fast-forward」マージを行います。これは履歴が直線的な場合に使用され、マージコミットは作成されません。

```console
$ git checkout main
$ git merge feature
Updating 5ab1c2d..8ef9a01
Fast-forward
 file.txt | 2 ++
 1 file changed, 2 insertions(+)
```

### **--no-ff**

常に新しいマージコミットを作成します。ブランチの履歴を明示的に残したい場合に便利です。

```console
$ git checkout main
$ git merge --no-ff feature
Merge made by the 'recursive' strategy.
 file.txt | 2 ++
 1 file changed, 2 insertions(+)
```

### **--squash**

マージ対象ブランチの全変更を現在のブランチに統合しますが、コミット履歴はマージせず、変更のみをステージングエリアに追加します。

```console
$ git checkout main
$ git merge --squash feature
Squash commit -- not updating HEAD
Automatic merge went well; stopped before committing as requested
$ git commit -m "機能Aの実装"
[main ab12c3d] 機能Aの実装
 1 file changed, 10 insertions(+)
```

### **--abort**

コンフリクト発生時にマージを中止し、マージ前の状態に戻します。

```console
$ git merge feature
Auto-merging file.txt
CONFLICT (content): Merge conflict in file.txt
Automatic merge failed; fix conflicts and then commit the result.
$ git merge --abort
```

## 使用例

### 基本的なマージ

```console
$ git checkout main
Switched to branch 'main'
$ git merge feature
Merge made by the 'recursive' strategy.
 feature.txt | 5 +++++
 1 file changed, 5 insertions(+)
```

### コンフリクトの解決

```console
$ git merge feature
Auto-merging README.md
CONFLICT (content): Merge conflict in README.md
Automatic merge failed; fix conflicts and then commit the result.

$ vim README.md  # コンフリクトを編集して解決

$ git add README.md
$ git commit
[main 3e4f5a6] Merge branch 'feature'
```

### 特定のコミットをマージ

```console
$ git cherry-pick abc1234
[main 5e6f7a8] 特定の機能を追加
 1 file changed, 3 insertions(+)
```

## ヒント:

### マージ前の確認

マージを実行する前に `git diff <ブランチ名>` を使用して、どのような変更が取り込まれるか確認しましょう。

### ブランチの整理

マージ完了後、不要になったブランチは `git branch -d <ブランチ名>` で削除できます。

### マージ戦略の選択

大きな機能開発では `--no-ff` オプションを使うと、どの変更がどの機能に関連しているか履歴から把握しやすくなります。小さな修正では `--ff`（デフォルト）が適しています。

### リベースとの使い分け

公開ブランチでは `merge` を、ローカルの作業ブランチでは `rebase` を使うというワークフローが一般的です。

## よくある質問

#### Q1. マージとリベースの違いは何ですか？
A. マージは2つのブランチの履歴を結合するのに対し、リベースはあるブランチのコミットを別のブランチの先端に移動させます。マージは履歴をそのまま保持しますが、リベースは履歴を書き換えます。

#### Q2. マージコンフリクトが発生したらどうすればいいですか？
A. コンフリクトが発生したファイルを開き、コンフリクトマーカー（`<<<<<<<`, `=======`, `>>>>>>>`)を編集して解決します。その後、`git add` でファイルをステージングし、`git commit` でマージを完了させます。

#### Q3. マージを取り消すにはどうすればいいですか？
A. マージ直後であれば `git reset --hard ORIG_HEAD` で取り消せます。すでに他の操作を行っている場合は `git reflog` で以前の状態を確認し、`git reset --hard <コミットハッシュ>` で戻ります。

#### Q4. fast-forwardマージとnon-fast-forwardマージの違いは何ですか？
A. fast-forwardは履歴が直線的な場合に使用され、単にHEADポインタを進めるだけです。non-fast-forwardは分岐した履歴を持つ場合に使用され、新しいマージコミットを作成します。

## 参考資料

https://git-scm.com/docs/git-merge

## Revisions

- 2025/04/30 初版作成