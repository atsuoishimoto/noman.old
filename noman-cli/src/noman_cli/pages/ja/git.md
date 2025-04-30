# git command

バージョン管理システムで、ファイルの変更履歴を追跡し、複数の開発者との共同作業を可能にします。

## 概要

Git はファイルの変更履歴を追跡するための分散型バージョン管理システムです。ローカルでの作業とリモートリポジトリとの同期が可能で、複数の開発者が同じプロジェクトで並行して作業できます。ブランチ機能により、メインコードに影響を与えずに新機能開発やバグ修正が行えます。

## オプション

### **git init**

新しいGitリポジトリを初期化します

```console
$ git init
Initialized empty Git repository in /path/to/project/.git/
```

### **git clone**

既存のリポジトリをローカルにコピーします

```console
$ git clone https://github.com/username/repository.git
Cloning into 'repository'...
remote: Enumerating objects: 125, done.
remote: Counting objects: 100% (125/125), done.
remote: Compressing objects: 100% (80/80), done.
remote: Total 125 (delta 40), reused 120 (delta 35), pack-reused 0
Receiving objects: 100% (125/125), 2.01 MiB | 3.50 MiB/s, done.
Resolving deltas: 100% (40/40), done.
```

### **git status**

作業ディレクトリの状態を表示します

```console
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        new-file.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

### **git add**

変更をステージングエリアに追加します

```console
$ git add README.md
$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        modified:   README.md

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        new-file.txt
```

### **git commit**

ステージングされた変更をリポジトリに記録します

```console
$ git commit -m "Update README.md with new information"
[main 5d7e9f4] Update README.md with new information
 1 file changed, 10 insertions(+), 2 deletions(-)
```

### **git push**

ローカルの変更をリモートリポジトリに送信します

```console
$ git push origin main
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 340 bytes | 340.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/username/repository.git
   a1b2c3d..5d7e9f4  main -> main
```

### **git pull**

リモートリポジトリの変更をローカルに取り込みます

```console
$ git pull origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (1/1), done.
remote: Total 3 (delta 2), reused 3 (delta 2), pack-reused 0
Unpacking objects: 100% (3/3), 285 bytes | 95.00 KiB/s, done.
From https://github.com/username/repository
 * branch            main       -> FETCH_HEAD
   a1b2c3d..e4f5g6h  main       -> origin/main
Updating a1b2c3d..e4f5g6h
Fast-forward
 README.md | 5 +++++
 1 file changed, 5 insertions(+)
```

## 使用例

### ブランチの作成と切り替え

```console
$ git branch feature-branch
$ git checkout feature-branch
Switched to branch 'feature-branch'

# または一行で
$ git checkout -b new-feature-branch
Switched to a new branch 'new-feature-branch'
```

### 変更履歴の確認

```console
$ git log
commit 5d7e9f4a7e9f4a7e9f4a7e9f4a7e9f4a7e9f4a7e
Author: Your Name <your.email@example.com>
Date:   Wed Apr 30 10:00:00 2025 +0900

    Update README.md with new information

commit a1b2c3d4a1b2c3d4a1b2c3d4a1b2c3d4a1b2c3d4
Author: Your Name <your.email@example.com>
Date:   Tue Apr 29 15:30:00 2025 +0900

    Initial commit
```

### マージの実行

```console
$ git checkout main
Switched to branch 'main'
$ git merge feature-branch
Updating a1b2c3d..5d7e9f4
Fast-forward
 feature.txt | 20 ++++++++++++++++++++
 1 file changed, 20 insertions(+)
 create mode 100644 feature.txt
```

## ヒント:

### コミットメッセージの書き方

良いコミットメッセージは、変更内容を明確に伝えるものです。最初の行は50文字以内の要約とし、必要に応じて空行の後に詳細な説明を追加しましょう。

### .gitignoreファイルの活用

`.gitignore`ファイルを作成して、バージョン管理に含めたくないファイル（ログファイル、ビルド成果物、個人設定ファイルなど）を指定できます。これにより、リポジトリを整理された状態に保てます。

### ブランチ戦略の採用

「Git Flow」や「GitHub Flow」などのブランチ戦略を採用すると、チーム開発がスムーズになります。プロジェクトの規模や要件に合わせて適切な戦略を選びましょう。

### エイリアスの設定

頻繁に使用するコマンドには、エイリアスを設定すると便利です。例えば：
```
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
```

## よくある質問

#### Q1. Gitとは何ですか？
A. Gitは分散型バージョン管理システムで、ソースコードの変更履歴を追跡し、複数の開発者が効率的に協力して作業できるようにするツールです。

#### Q2. リモートリポジトリとローカルリポジトリの違いは何ですか？
A. ローカルリポジトリはあなたのコンピュータ上にあり、リモートリポジトリはサーバー上（GitHubなど）にあります。ローカルで作業した後、変更をリモートにプッシュして共有します。

#### Q3. コミットをやり直すにはどうすればよいですか？
A. 直前のコミットを修正するには `git commit --amend` を使用します。すでにプッシュしたコミットを変更する場合は注意が必要です。

#### Q4. 間違えてコミットした変更を元に戻すにはどうすればよいですか？
A. `git revert <commit-hash>` を使用すると、特定のコミットの変更を打ち消す新しいコミットが作成されます。履歴を書き換えずに変更を元に戻せます。

#### Q5. ブランチとは何ですか？
A. ブランチは独立した作業ラインで、メインコードに影響を与えずに新機能開発やバグ修正を行えます。作業が完了したら、メインブランチにマージできます。

## macOSでの注意点

macOSでは、Gitはデフォルトでインストールされていない場合があります。Xcodeコマンドラインツールをインストールするか、Homebrewを使用してインストールできます：

```console
$ xcode-select --install
# または
$ brew install git
```

また、macOSでは`.DS_Store`ファイルが自動生成されるため、グローバルな`.gitignore`ファイルに追加しておくと良いでしょう：

```console
$ echo ".DS_Store" >> ~/.gitignore_global
$ git config --global core.excludesfile ~/.gitignore_global
```

## 参考資料

https://git-scm.com/doc

## 改訂履歴

- 2025/04/30 初版作成