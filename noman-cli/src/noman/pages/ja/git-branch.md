# git-branch コマンド

Gitリポジトリ内のブランチを一覧表示、作成、または削除します。

## 概要

`git branch`コマンドはGitリポジトリ内のブランチを管理するために使用されます。既存のブランチの一覧表示、新しいブランチの作成、ブランチの名前変更、ブランチの削除などが可能です。ブランチはコミットを指す軽量な移動可能なポインタであり、並行開発ワークフローには不可欠な機能です。

## オプション

### **-a, --all**

リモート追跡ブランチとローカルブランチの両方を一覧表示します。

```console
$ git branch -a
* main
  feature-login
  remotes/origin/main
  remotes/origin/feature-login
```

### **-r, --remotes**

リモート追跡ブランチを一覧表示または削除します。

```console
$ git branch -r
  origin/main
  origin/feature-login
  origin/dev
```

### **-v, --verbose**

各ブランチのSHA-1とコミットの件名行を表示します。

```console
$ git branch -v
* main        a72f324 Update README.md
  feature-login 8d3e5c1 Implement login functionality
```

### **-d, --delete**

ブランチを削除します。ブランチは上流ブランチに完全にマージされている必要があります。

```console
$ git branch -d feature-login
Deleted branch feature-login (was 8d3e5c1).
```

### **-D**

完全にマージされていなくてもブランチを強制的に削除します。

```console
$ git branch -D unmerged-branch
Deleted branch unmerged-branch (was 7c3a9f2).
```

### **-m, --move**

ブランチとそのreflogを移動/名前変更します。

```console
$ git branch -m 古いブランチ名 新しいブランチ名
```

### **--list**

ブランチを一覧表示します。オプションでパターンを指定できます（例：`git branch --list 'feature-*'`）。

```console
$ git branch --list 'feature-*'
  feature-login
  feature-signup
  feature-dashboard
```

## 使用例

### 新しいブランチの作成

```console
$ git branch new-feature
$ git branch
* main
  new-feature
```

### 新しいブランチの作成と切り替え

```console
$ git branch new-feature
$ git checkout new-feature
Switched to branch 'new-feature'

# より簡潔に git checkout -b を使用する方法
$ git checkout -b new-feature
Switched to a new branch 'new-feature'
```

### コミット情報を含むすべてのブランチの表示

```console
$ git branch -av
* main                  a72f324 [ahead 2] Update README.md
  feature-login         8d3e5c1 Implement login functionality
  remotes/origin/main   3e4f2a1 Initial commit
  remotes/origin/dev    9c2d1b3 Fix bug in API
```

## ヒント:

### ブランチの説明を使用する

`git branch --edit-description`を使用してブランチに説明を追加できます。これは長期間存在するブランチの目的を文書化するのに役立ちます。

### リモート追跡ブランチのクリーンアップ

`git fetch --prune`を使用して削除されたリモートブランチをクリーンアップします。これにより、リモートに存在しなくなったリモート追跡ブランチが削除されます。

### マージされたブランチの識別

`git branch --merged`を使用して、現在のブランチにマージされたブランチを一覧表示します。これにより、安全に削除できるブランチを特定するのに役立ちます。

### ブランチの命名規則

`feature/login`、`bugfix/header`、`hotfix/security-issue`などのような一貫した命名規則に従いましょう。これにより、目的別にブランチを整理するのに役立ちます。

## よくある質問

#### Q1. 新しいブランチを作成するにはどうすればよいですか？
A. `git branch <ブランチ名>`を使用して新しいブランチを作成します。これはブランチを作成するだけで、そのブランチに切り替えるわけではないことに注意してください。

#### Q2. ブランチを削除するにはどうすればよいですか？
A. 完全にマージされたブランチを削除するには`git branch -d <ブランチ名>`を使用し、マージ状態に関係なくブランチを強制的に削除するには`git branch -D <ブランチ名>`を使用します。

#### Q3. ブランチの名前を変更するにはどうすればよいですか？
A. `git branch -m <古い名前> <新しい名前>`を使用してブランチの名前を変更します。名前を変更したいブランチ上にいる場合は、単に`git branch -m <新しい名前>`を使用できます。

#### Q4. 現在のブランチにマージされているブランチを確認するにはどうすればよいですか？
A. `git branch --merged`を使用して、現在のブランチにマージされているブランチを確認できます。

#### Q5. リモートブランチを一覧表示するにはどうすればよいですか？
A. `git branch -r`を使用してリモート追跡ブランチを一覧表示します。

## 参考資料

https://git-scm.com/docs/git-branch

## 改訂履歴

- 2025/05/04 初版作成