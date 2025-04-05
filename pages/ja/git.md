# Git コマンド概要

Git は分散型バージョン管理システムで、ファイルの変更履歴を追跡し、複数の開発者が協力して作業するためのツールです。コードの変更を記録、共有、管理することができます。

## 主なコマンド

- **git init**: 新しいGitリポジトリを作成します
  - 例: `git init`

- **git clone**: リモートリポジトリのコピーを作成します
  - 例: `git clone https://github.com/username/repository.git`

- **git add**: 変更をステージングエリアに追加します
  - 例: `git add ファイル名` または `git add .`（すべての変更をステージング）

- **git commit**: ステージングされた変更を記録します
  - 例: `git commit -m "コミットメッセージ"`

- **git status**: 作業ディレクトリの状態を確認します
  - 例: `git status`

- **git pull**: リモートリポジトリから変更を取得して統合します
  - 例: `git pull origin main`

- **git push**: ローカルの変更をリモートリポジトリに送信します
  - 例: `git push origin main`

- **git branch**: ブランチの作成、一覧表示、削除を行います
  - 例: `git branch` (一覧表示)、`git branch ブランチ名` (作成)

- **git checkout**: ブランチを切り替えます
  - 例: `git checkout ブランチ名` または `git checkout -b 新ブランチ名` (作成して切り替え)

- **git merge**: あるブランチの変更を現在のブランチに統合します
  - 例: `git merge ブランチ名`

## 使用例

### 基本的なワークフロー

```bash
# 新しいリポジトリを初期化
git init

# ファイルを追加してコミット
git add index.html
git commit -m "初期コミット"

# リモートリポジトリを追加
git remote add origin https://github.com/username/repository.git

# 変更をプッシュ
git push -u origin main
```

### ブランチの作成と操作

```bash
# 新しいブランチを作成して切り替え
git checkout -b feature-branch

# いくつかの変更を行った後
git add .
git commit -m "新機能を追加"

# メインブランチに戻る
git checkout main

# 変更をマージ
git merge feature-branch
```

### リモートリポジトリとの連携

```bash
# リモートリポジトリをクローン
git clone https://github.com/username/repository.git

# 変更を取得
git pull

# 変更を行った後、プッシュ
git add .
git commit -m "バグ修正"
git push
```

## 追加のヒント

- **git log**: コミット履歴を表示します。`git log --oneline` で簡潔に表示できます。

- **git diff**: 変更内容を表示します。`git diff ファイル名` で特定ファイルの変更を確認できます。

- **.gitignore** ファイルを作成して、バージョン管理に含めたくないファイル（ログファイルや一時ファイルなど）を指定できます。

- コミットメッセージは具体的かつ明確に書くことで、後から変更内容を理解しやすくなります。

- 大きな変更を行う前には、新しいブランチを作成することをお勧めします。これにより、メインコードに影響を与えずに作業できます。

- コンフリクト（競合）が発生した場合は、該当ファイルを編集して解決し、`git add` してから `git commit` を実行します。