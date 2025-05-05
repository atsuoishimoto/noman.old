# git コマンド

分散型バージョン管理システムで、ソフトウェア開発中のソースコードの変更を追跡します。

## 概要

Gitは分散型バージョン管理システムで、複数の開発者が同時にプロジェクトで作業することを可能にします。ファイルの変更を追跡し、修正履歴を維持し、異なるソースからの変更をマージすることでコラボレーションを促進します。Gitは主にローカルリポジトリを通じて操作し、リモートリポジトリと同期する機能を持っています。

## オプション

### **-v, --version**

インストールされているGitのバージョンを表示します

```console
$ git --version
git version 2.39.2
```

### **-h, --help**

GitまたはGitの特定のコマンドのヘルプ情報を表示します

```console
$ git --help
usage: git [-v | --version] [-h | --help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | -P | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           [--super-prefix=<path>] [--config-env=<name>=<envvar>]
           <command> [<args>]
```

### **-C, --work-tree=<path>**

指定されたパスでgitが起動されたかのようにコマンドを実行します

```console
$ git -C /path/to/repository status
On branch main
Your branch is up to date with 'origin/main'.

nothing to commit, working tree clean
```

### **-c, --config-env=<name>=<value>**

単一のコマンドに対して設定変数を設定します

```console
$ git -c user.name="Temporary User" commit -m "One-time commit with different user"
[main 1a2b3c4] One-time commit with different user
 1 file changed, 5 insertions(+)
```

## 使用例

### 新しいリポジトリの初期化

```console
$ git init
Initialized empty Git repository in /path/to/project/.git/
```

### 既存のリポジトリのクローン

```console
$ git clone https://github.com/username/repository.git
Cloning into 'repository'...
remote: Enumerating objects: 1463, done.
remote: Counting objects: 100% (1463/1463), done.
remote: Compressing objects: 100% (750/750), done.
remote: Total 1463 (delta 713), reused 1463 (delta 713), pack-reused 0
Receiving objects: 100% (1463/1463), 2.56 MiB | 5.12 MiB/s, done.
Resolving deltas: 100% (713/713), done.
```

### 基本的なワークフロー例

```console
$ git add file.txt
$ git commit -m "Add new file"
[main 1a2b3c4] Add new file
 1 file changed, 10 insertions(+)
 create mode 100644 file.txt
$ git push origin main
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 8 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 294 bytes | 294.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/username/repository.git
   a1b2c3d..1a2b3c4  main -> main
```

### リポジトリのステータス確認

```console
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")
```

## ヒント:

### 個人情報の設定

コミットする前に名前とメールアドレスを設定しましょう：

```console
$ git config --global user.name "Your Name"
$ git config --global user.email "your.email@example.com"
```

### よく使うコマンドのエイリアス作成

頻繁に使用するコマンドのショートカットを作成して時間を節約できます：

```console
$ git config --global alias.co checkout
$ git config --global alias.br branch
$ git config --global alias.st status
```

### .gitignoreファイルの使用

リポジトリに`.gitignore`ファイルを作成して、ビルド成果物、一時ファイル、機密情報など、Gitが無視すべきファイルを指定しましょう。

### アトミックなコミット

複数の無関係な変更を混ぜた大きなコミットではなく、単一の論理的な変更に対応する小さな焦点を絞ったコミットを行いましょう。

## よくある質問

#### Q1. 最後のコミットを取り消すにはどうすればよいですか？
A. 変更を保持したままコミットを取り消すには`git reset HEAD~1`を、変更を完全に破棄するには`git reset --hard HEAD~1`を使用します。

#### Q2. 新しいブランチを作成するにはどうすればよいですか？
A. `git branch ブランチ名`でブランチを作成し、`git checkout ブランチ名`で切り替えます。または、`git checkout -b ブランチ名`で作成と切り替えを一度に行うこともできます。

#### Q3. あるブランチから別のブランチに変更をマージするにはどうすればよいですか？
A. まず`git checkout ターゲットブランチ`でターゲットブランチに切り替え、次に`git merge ソースブランチ`でマージします。

#### Q4. マージの競合を解決するにはどうすればよいですか？
A. 競合が発生した場合、競合したファイルを編集して差異を解決し、`git add`で解決済みとマークし、最後に`git commit`でマージを完了します。

#### Q5. ローカルリポジトリをリモートの変更で更新するにはどうすればよいですか？
A. `git pull`を使用して変更を取得してマージするか、より制御したい場合は`git fetch`の後に`git merge`を使用します。

## 参考資料

https://git-scm.com/docs/git

## 改訂履歴

2025/05/04 初回改訂