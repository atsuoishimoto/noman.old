# git reset コマンド

コミットポインタを特定のコミットに移動させ、作業ツリーやインデックスを選択的にリセットします。

## 概要

`git reset` は、現在のブランチの HEAD ポインタを移動させるコマンドです。オプションによって、インデックス（ステージングエリア）や作業ディレクトリの状態も変更できます。主に、コミットの取り消しやステージングした変更の取り消しに使用されます。

## オプション

### **--soft**

HEAD ポインタのみを移動し、インデックスと作業ディレクトリはそのままにします。

```console
$ git reset --soft HEAD~1
# 直前のコミットを取り消し、変更はステージングされたままになる
```

### **--mixed（デフォルト）**

HEAD ポインタとインデックスを移動しますが、作業ディレクトリはそのままにします。

```console
$ git reset HEAD~1
# 直前のコミットを取り消し、変更は作業ディレクトリに残るがステージングは解除される
```

### **--hard**

HEAD ポインタ、インデックス、作業ディレクトリをすべて指定したコミットの状態にリセットします。

```console
$ git reset --hard HEAD~1
# 直前のコミットを完全に取り消し、変更も削除される
```

### **<commit>**

リセット先のコミットを指定します。コミットハッシュ、ブランチ名、タグ名、または相対参照（HEAD~n など）を使用できます。

```console
$ git reset --mixed 5a8e4ca
# 指定したコミットに HEAD とインデックスをリセット
```

### **<paths>...**

特定のファイルやディレクトリのみをインデックスからリセットします（HEAD は移動しません）。

```console
$ git reset -- file.txt
# file.txt のステージングを解除する
```

## 使用例

### コミットの取り消し（変更を保持）

```console
$ git reset --soft HEAD~3
# 直近3つのコミットを取り消し、変更はステージングされたままになる
```

### ステージングの解除

```console
$ git reset HEAD file.txt
# file.txt のステージングを解除する（作業ディレクトリの変更は保持される）
```

### 特定のコミットまで完全にリセット

```console
$ git log --oneline
a1b2c3d ファイル追加
e4f5g6h バグ修正
i7j8k9l 初期コミット

$ git reset --hard e4f5g6h
HEAD is now at e4f5g6h バグ修正
# e4f5g6h のコミットまで戻り、それ以降の変更はすべて削除される
```

### マージの取り消し

```console
$ git reset --hard ORIG_HEAD
# 直前のマージを取り消す
```

## ヒント:

### リセット前にブランチを作成する

重要な変更をリセットする前に、現在の状態を新しいブランチに保存しておくと安全です。

```console
$ git branch backup-branch
$ git reset --hard HEAD~3
# 万が一リセットを後悔しても、backup-branch に戻れる
```

### --hard は注意して使用する

`--hard` オプションは作業ディレクトリの変更も削除するため、コミットされていない変更が失われます。使用前に `git status` で状態を確認しましょう。

### reflog で失われたコミットを復元

`--hard` リセット後でも、`git reflog` コマンドを使用すれば、通常は失われたコミットを見つけて復元できます。

```console
$ git reflog
5a8e4ca HEAD@{0}: reset: moving to HEAD~1
2c3d4e5 HEAD@{1}: commit: 失われたコミット

$ git reset --hard 2c3d4e5
# 失われたコミットを復元
```

## よくある質問

#### Q1. `git reset` と `git revert` の違いは何ですか？
A. `git reset` はコミット履歴を書き換えますが、`git revert` は元に戻す操作自体を新しいコミットとして追加します。共有リポジトリでは `git revert` の使用が推奨されます。

#### Q2. ステージングしたファイルを一部だけ解除するには？
A. `git reset <file>` または `git reset -- <file>` を使用して、特定のファイルのみステージングを解除できます。

#### Q3. リセット後に失われたコミットを復元できますか？
A. はい、`git reflog` を使用して過去の HEAD の位置を確認し、`git reset --hard <commit-hash>` で復元できます。

#### Q4. リモートブランチをリセットするには？
A. ローカルブランチをリセットした後、`git push --force` でリモートブランチを更新できますが、共有リポジトリでは注意が必要です。

## 参考

https://git-scm.com/docs/git-reset

## Revisions

- 2025/04/30 初版作成