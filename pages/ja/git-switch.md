# git switch コマンド

ブランチを切り替えたり、作業ツリーのファイルを復元したりします。

## 概要

`git switch` コマンドは、Gitリポジトリ内でブランチを切り替えるために使用されます。Git 2.23で導入され、`git checkout`の特定の用途に対するよりユーザーフレンドリーな代替手段となっています。`git checkout`は複数の目的を果たしますが、`git switch`は特にブランチ操作のために設計されており、より明確でエラーが発生しにくくなっています。

## オプション

### **-c, --create \<branch>**

新しいブランチを作成して切り替えます。

```console
$ git switch -c feature-login
Switched to a new branch 'feature-login'
# 新しいブランチ 'feature-login' に切り替えた
```

### **-d, --detach**

デタッチドHEAD状態でコミットに切り替えます。

```console
$ git switch --detach HEAD~3
Note: switching to 'HEAD~3'.

You are in 'detached HEAD' state...
HEAD is now at a1b2c3d Previous commit message
# 'HEAD~3' に切り替えている
# 'デタッチドHEAD'状態になっている
# HEADは現在 a1b2c3d（前のコミットメッセージ）にある
```

### **-t, --track**

新しいブランチを作成する際に、「upstream」設定をセットアップします。

```console
$ git switch -c feature-auth --track origin/feature-auth
Branch 'feature-auth' set up to track remote branch 'feature-auth' from 'origin'.
Switched to a new branch 'feature-auth'
# ブランチ 'feature-auth' は 'origin' からのリモートブランチ 'feature-auth' を追跡するように設定された
# 新しいブランチ 'feature-auth' に切り替えた
```

### **--discard-changes**

切り替える前にローカルの変更を破棄します。

```console
$ git switch --discard-changes main
Switched to branch 'main'
# ブランチ 'main' に切り替えた（ローカルの変更は破棄された）
```

### **-m, --merge**

ローカルの変更を新しいブランチにマージします。

```console
$ git switch -m feature-branch
Switched to branch 'feature-branch'
# ブランチ 'feature-branch' に切り替えた（ローカルの変更はマージされた）
```

### **-**

前のブランチに切り替えます。

```console
$ git switch -
Switched to branch 'main'
# 前のブランチ 'main' に切り替えた
```

## 使用例

### 基本的なブランチ切り替え

```console
$ git switch main
Switched to branch 'main'
# ブランチ 'main' に切り替えた
```

### 新しいブランチの作成と切り替え

```console
$ git switch -c new-feature
Switched to a new branch 'new-feature'
# 新しいブランチ 'new-feature' に切り替えた
```

### リモートブランチへの切り替え

```console
$ git switch feature-branch
Branch 'feature-branch' set up to track remote branch 'feature-branch' from 'origin'.
Switched to a new branch 'feature-branch'
# ブランチ 'feature-branch' は 'origin' からのリモートブランチ 'feature-branch' を追跡するように設定された
# 新しいブランチ 'feature-branch' に切り替えた
```

## ヒント:

### `git switch -` を使用してブランチ間をトグルする

Unixの `cd -` と同様に、`git switch -` を使用すると、現在のブランチと前のブランチの間を素早く切り替えることができます。開発中に頻繁にコンテキストを切り替える必要がある場合に便利です。

### ブランチ操作には `git checkout` よりも `git switch` を優先する

`git switch` は、ブランチを扱う際に `git checkout` よりも明示的で安全です。`checkout` の二重目的（ブランチの切り替えとファイルの復元）による混乱を避けることができます。

### `--discard-changes` は注意して使用する

`--discard-changes` オプションはすべてのローカル変更を破棄します。このオプションを使用する前に、それらの変更が不要であることを確認してください。破棄された変更は復元できません。

### 自動的に追跡ブランチを作成する

ローカルに存在しないリモートブランチに切り替える場合、Gitは自動的に追跡ブランチを作成します。これにより、`-c` と `--track` オプションを明示的に使用する必要がなくなります。

## よくある質問

#### Q1. `git switch` と `git checkout` の違いは何ですか？
A. `git switch` はブランチ操作のみに焦点を当てていますが、`git checkout` はブランチの切り替えやファイルの復元など複数の目的を持っています。`git switch` は、より明確で焦点を絞ったコマンドを提供するために導入されました。

#### Q2. 特定のコミットから新しいブランチを作成するにはどうすればよいですか？
A. `git switch -c <新しいブランチ名> <コミットハッシュ>` を使用して、特定のコミットから始まる新しいブランチを作成して切り替えることができます。

#### Q3. コミットされていない変更がある状態でブランチを切り替えることはできますか？
A. はい、変更がターゲットブランチと競合しない場合は可能です。競合がある場合、Gitは切り替えを防止します。`--discard-changes` を使用して変更を破棄するか、`--merge` を使用して変更をターゲットブランチにマージすることができます。

#### Q4. リモートブランチに切り替えるにはどうすればよいですか？
A. 単に `git switch ブランチ名` を使用します。ブランチがリモートに存在し、ローカルには存在しない場合、Gitは自動的に追跡ブランチを作成します。

#### Q5. 特定のタグに切り替えるにはどうすればよいですか？
A. `git switch --detach タグ名` を使用して、タグが指すコミットにデタッチドHEAD状態で切り替えることができます。

## 参考文献

https://git-scm.com/docs/git-switch

## 改訂履歴

- 2025/05/04 初回改訂