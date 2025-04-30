# git branch コマンド

ブランチの作成、一覧表示、名前変更、削除を行います。

## 概要

`git branch` は Git リポジトリ内のブランチを管理するためのコマンドです。引数なしで実行すると、現在のリポジトリに存在するローカルブランチの一覧を表示します。ブランチの作成、名前変更、削除などの操作も行えます。ブランチは Git の重要な機能で、異なる作業を並行して進めるために使用されます。

## オプション

### **-a, --all**

ローカルブランチとリモートブランチの両方を表示します。

```console
$ git branch -a
* main
  feature/login
  remotes/origin/main
  remotes/origin/develop
```

### **-v, --verbose**

各ブランチの最新コミットのハッシュとメッセージを表示します。

```console
$ git branch -v
* main        a1b2c3d [ahead 2] 最新の機能を追加
  feature/login e4f5g6h ログイン画面の実装
```

### **-d, --delete**

指定したブランチを削除します。マージ済みのブランチのみ削除できます。

```console
$ git branch -d feature/login
Deleted branch feature/login (was e4f5g6h).
```

### **-D**

指定したブランチを強制的に削除します。マージされていないブランチも削除できます。

```console
$ git branch -D feature/unmerged
Deleted branch feature/unmerged (was 7h8i9j0).
```

### **-m, --move**

ブランチの名前を変更します。

```console
$ git branch -m old-name new-name
```

### **-r, --remotes**

リモートブランチのみを表示します。

```console
$ git branch -r
  origin/main
  origin/develop
  origin/feature/api
```

## 使用例

### ブランチの作成

```console
$ git branch feature/search
$ git branch
* main
  feature/login
  feature/search
```

### 詳細情報付きでブランチ一覧を表示

```console
$ git branch -vv
* main        a1b2c3d [origin/main: ahead 2] 最新の機能を追加
  feature/login e4f5g6h [origin/feature/login] ログイン画面の実装
```

### マージ済みブランチの一覧表示

```console
$ git branch --merged
* main
  feature/completed
```

### マージされていないブランチの一覧表示

```console
$ git branch --no-merged
  feature/in-progress
```

## ヒント:

### 現在のブランチの確認

現在作業中のブランチには、一覧表示時に名前の前に `*` が付きます。`git status` でも確認できます。

### ブランチの切り替え

ブランチを作成しただけでは切り替わりません。`git checkout <ブランチ名>` または `git switch <ブランチ名>` で切り替えます。

### ブランチの作成と切り替えを同時に行う

`git checkout -b <新ブランチ名>` または `git switch -c <新ブランチ名>` で、ブランチの作成と切り替えを一度に行えます。

### リモートブランチの追跡

`git branch --track <ローカルブランチ名> <リモートブランチ名>` で、リモートブランチを追跡するローカルブランチを作成できます。

## よくある質問

#### Q1. ブランチとは何ですか？
A. ブランチとは、コードの独立した開発ラインです。メインのコードベースに影響を与えずに新機能の開発やバグ修正を行うために使用されます。

#### Q2. 現在のブランチを確認するにはどうすればよいですか？
A. `git branch` コマンドを実行すると、現在のブランチには `*` マークが付きます。また、`git status` でも確認できます。

#### Q3. 間違えて削除したブランチを復元できますか？
A. はい、ブランチの最後のコミットハッシュがわかれば `git branch <ブランチ名> <コミットハッシュ>` で復元できます。`git reflog` で最近の操作履歴を確認できます。

#### Q4. リモートブランチを削除するにはどうすればよいですか？
A. `git push origin --delete <ブランチ名>` または `git push origin :<ブランチ名>` でリモートブランチを削除できます。

#### Q5. ブランチ名を変更した後、リモートリポジトリにも反映させるにはどうすればよいですか？
A. ローカルでブランチ名を変更した後、古いブランチを削除して新しいブランチをプッシュします：
```
git push origin --delete <古いブランチ名>
git push -u origin <新しいブランチ名>
```

## 参考

https://git-scm.com/docs/git-branch

## 改訂履歴

- 2025/04/30 初版作成