# git switch コマンド

ブランチを切り替えるコマンドです。

## 概要

`git switch` は Git リポジトリ内でブランチを切り替えるために使用されます。このコマンドは Git 2.23 で導入され、以前は `git checkout` が担っていたブランチ切り替え機能を専用のコマンドとして分離したものです。ブランチの作成と切り替えを同時に行うこともできます。

## オプション

### **-c, --create**

新しいブランチを作成して切り替えます。

```console
$ git switch -c feature-login
ブランチ 'feature-login' を作成しました
feature-login ブランチに切り替えました
```

### **-d, --detach**

特定のコミットに HEAD をデタッチ（分離）した状態で切り替えます。

```console
$ git switch --detach HEAD~3
HEAD が 'a1b2c3d' にデタッチされました
```

### **-t, --track**

リモートブランチを追跡する新しいブランチを作成して切り替えます。

```console
$ git switch -t origin/feature
origin/feature を追跡するブランチ 'feature' を作成しました
feature ブランチに切り替えました
```

### **-**

直前に作業していたブランチに切り替えます。

```console
$ git switch -
main ブランチに切り替えました
```

## 使用例

### 既存のブランチに切り替える

```console
$ git switch main
main ブランチに切り替えました
```

### 新しいブランチを作成して切り替える

```console
$ git switch -c hotfix-123
ブランチ 'hotfix-123' を作成しました
hotfix-123 ブランチに切り替えました
```

### リモートブランチを追跡する新しいブランチを作成

```console
$ git switch -c feature-auth origin/feature-auth
origin/feature-auth を追跡するブランチ 'feature-auth' を作成しました
feature-auth ブランチに切り替えました
```

## ヒント:

### 未コミットの変更がある場合の切り替え

未コミットの変更がある状態でブランチを切り替える場合、Git は変更を保持したまま切り替えようとします。ただし、競合がある場合は切り替えが失敗します。`git stash` を使用して変更を一時保存してからブランチを切り替えると安全です。

### 作業中のブランチ名を確認する

現在のブランチを確認するには `git branch` コマンドを使用します。現在のブランチには `*` が付きます。

### 存在しないブランチへの切り替え

存在しないブランチに切り替えようとすると、エラーが発生します。`-c` オプションを使用して新しいブランチを作成するか、正確なブランチ名を指定してください。

## よくある質問

#### Q1. `git switch` と `git checkout` の違いは何ですか？
A. `git switch` はブランチの切り替えに特化したコマンドで、`git checkout` はブランチの切り替えだけでなくファイルの復元など複数の機能を持っています。Git 2.23 以降では、ブランチ操作には `git switch` を使用することが推奨されています。

#### Q2. 作業中の変更を失わずにブランチを切り替えるにはどうすればよいですか？
A. 変更に競合がなければ、そのまま `git switch` で切り替えられます。競合の可能性がある場合は、`git stash` で変更を保存してから切り替え、その後 `git stash pop` で変更を復元するのが安全です。

#### Q3. リモートブランチに切り替えるにはどうすればよいですか？
A. `git switch -c branch-name origin/branch-name` または `git switch -t origin/branch-name` を使用します。これにより、リモートブランチを追跡するローカルブランチが作成されます。

#### Q4. 直前に作業していたブランチに戻るショートカットはありますか？
A. `git switch -` を使用すると、直前に作業していたブランチに素早く切り替えることができます。

## 参考

https://git-scm.com/docs/git-switch

## 改訂履歴

- 2025/04/30 初版作成