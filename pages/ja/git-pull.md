# git pull コマンド

リモートリポジトリから変更を取得し、ローカルブランチに統合します。

## 概要

`git pull` は、リモートリポジトリから最新の変更を取得し（`git fetch`）、その変更をローカルブランチに統合（`git merge` または `git rebase`）するコマンドです。これにより、ローカルの作業コピーを最新の状態に保つことができます。

## オプション

### **--rebase**

マージの代わりにリベースを使用して変更を統合します。これにより、履歴がよりクリーンになります。

```console
$ git pull --rebase origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 1), reused 3 (delta 1), pack-reused 0
Unpacking objects: 100% (3/3), 285 bytes | 285.00 KiB/s, done.
From github.com:username/repo
   a1b2c3d..e4f5g6h  main     -> origin/main
Successfully rebased and updated refs/heads/main.
```

### **--ff-only**

Fast-forwardできる場合のみマージを実行します。コンフリクトを避けたい場合に便利です。

```console
$ git pull --ff-only
Updating a1b2c3d..e4f5g6h
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
```

### **-v, --verbose**

詳細な情報を表示します。

```console
$ git pull -v
From github.com:username/repo
 * branch            main     -> FETCH_HEAD
Updating a1b2c3d..e4f5g6h
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
```

## 使用例

### 特定のリモートとブランチから変更を取得

```console
$ git pull origin develop
From github.com:username/repo
 * branch            develop   -> FETCH_HEAD
Updating a1b2c3d..e4f5g6h
Fast-forward
 src/main.js | 10 +++++++---
 1 file changed, 7 insertions(+), 3 deletions(-)
```

### 複数のリモートリポジトリから変更を取得

```console
$ git pull upstream main && git pull origin main
From github.com:upstream/repo
 * branch            main     -> FETCH_HEAD
Already up to date.
From github.com:username/repo
 * branch            main     -> FETCH_HEAD
Updating a1b2c3d..e4f5g6h
Fast-forward
 README.md | 2 ++
 1 file changed, 2 insertions(+)
```

## ヒント:

### プルする前に変更を退避する

未コミットの変更がある場合、`git stash`で一時的に保存してからプルし、その後`git stash pop`で復元するとコンフリクトを避けられます。

```console
$ git stash
Saved working directory and index state WIP on main: a1b2c3d Initial commit
$ git pull
$ git stash pop
```

### リベースを使用してクリーンな履歴を維持する

`git pull --rebase`を使用すると、マージコミットが作成されず、履歴が直線的になります。チームで作業する場合に特に便利です。

### プル前にローカルの状態を確認する

`git status`を実行して、未コミットの変更がないことを確認してからプルすると安全です。

## Frequently Asked Questions

#### Q1. `git pull`と`git fetch`の違いは何ですか？
A. `git fetch`はリモートの変更を取得するだけで、ローカルブランチには統合しません。一方、`git pull`は`fetch`と`merge`（または`rebase`）を一度に行います。

#### Q2. プル時にコンフリクトが発生した場合はどうすればよいですか？
A. コンフリクトを解決するには、コンフリクトファイルを編集し、`git add`でマークしてから`git commit`（マージの場合）または`git rebase --continue`（リベースの場合）を実行します。

#### Q3. 特定のブランチだけをプルするにはどうすればよいですか？
A. `git pull origin branch-name`のように、リモート名とブランチ名を指定します。

#### Q4. プルを取り消すにはどうすればよいですか？
A. マージの場合は`git reset --hard ORIG_HEAD`、リベースの場合は`git reflog`で以前の状態を見つけて`git reset --hard`で戻します。

## macOSでの注意点

macOSでは特別な注意点はありませんが、Keychain Accessを使用してGitの認証情報を保存している場合があります。認証に問題がある場合は、Keychain Accessアプリで認証情報を確認してください。

## References

https://git-scm.com/docs/git-pull

## Revisions

- 2025/04/30 初回作成