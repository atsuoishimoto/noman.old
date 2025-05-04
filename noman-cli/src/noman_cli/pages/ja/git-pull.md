# git pull コマンド

リモートリポジトリやローカルブランチから変更を取得して統合します。

## 概要

`git pull` は、リモートリポジトリからの変更を現在のローカル作業ブランチに更新するGitコマンドです。このコマンドは2つの操作を組み合わせています：`git fetch`（リモートリポジトリからコンテンツをダウンロード）と`git merge`（取得したコンテンツをローカルブランチに統合）です。このコマンドは、他の人が行った変更とローカルリポジトリを同期させるために不可欠です。

## オプション

### **-r, --rebase[=false|true|merges|interactive]**

マージの代わりに、フェッチ後にアップストリームブランチの上に現在のブランチをリベースします。

```console
$ git pull -r origin main
From github.com:user/repo
 * branch            main       -> FETCH_HEAD
Successfully rebased and updated refs/heads/feature.
```

### **--ff, --no-ff, --ff-only**

マージの処理方法を制御します：
- `--ff`：早送り（fast-forward）マージを許可（デフォルト）
- `--no-ff`：早送りが可能な場合でもマージコミットを作成
- `--ff-only`：早送りマージのみを許可し、不可能な場合は中止

```console
$ git pull --ff-only origin main
From github.com:user/repo
 * branch            main       -> FETCH_HEAD
Updating 5ab1c2d..8ef9a3b
Fast-forward
 README.md | 5 +++++
 1 file changed, 5 insertions(+)
```

### **-q, --quiet**

進行状況のレポートを抑制して静かに操作します。

```console
$ git pull -q origin main
```

### **-v, --verbose**

より詳細な情報を表示し、フェッチとマージ操作に関する詳細情報を表示します。

```console
$ git pull -v origin main
From github.com:user/repo
 * branch            main       -> FETCH_HEAD
Updating 5ab1c2d..8ef9a3b
Fast-forward
 README.md | 5 +++++
 1 file changed, 5 insertions(+)
```

### **--autostash**

pull操作の前後に未コミットの変更を自動的にスタッシュして復元します。

```console
$ git pull --autostash origin main
Created autostash: 73a4e9d
Applied autostash.
```

## 使用例

### リモートからの基本的なプル

```console
$ git pull origin main
From github.com:user/repo
 * branch            main       -> FETCH_HEAD
Updating 5ab1c2d..8ef9a3b
Fast-forward
 README.md | 5 +++++
 1 file changed, 5 insertions(+)
```

### リベースを使用したプル

```console
$ git pull --rebase origin feature
From github.com:user/repo
 * branch            feature    -> FETCH_HEAD
Successfully rebased and updated refs/heads/feature.
```

### アップストリームブランチからのプル

```console
$ git pull
Already up to date.
```

## ヒント:

### トラッキングブランチの設定

`git branch --set-upstream-to=origin/branch-name` でローカルブランチがリモートブランチを追跡するように設定できます。これにより、リモートとブランチを指定せずに単に `git pull` を使用できるようになります。

### 公開ブランチでは注意してプルを使用する

共有ブランチで作業する場合は、`git pull` の代わりに `git fetch` の後に `git merge` または `git rebase` を使用して、統合プロセスをより細かく制御することを検討してください。

### 競合を適切に解決する

`git pull` がマージ競合を引き起こした場合は、それらを正しく解決するために時間をかけてください。`git status` を使用して競合したファイルを確認し、`git mergetool` を使用して解決を支援します。

### 作業中の変更には `--autostash` を使用する

コミットされていない変更があるが更新をプルする必要がある場合、`--autostash` を使用すると変更を自動的に保存して復元できます。

## よくある質問

#### Q1. `git pull` と `git fetch` の違いは何ですか？
A. `git fetch` はリモートリポジトリから新しいデータをダウンロードするだけで、作業ファイルに変更を統合しません。`git pull` は両方を行います：フェッチしてから自動的に変更を現在のブランチにマージします。

#### Q2. `git pull` を元に戻すにはどうすればよいですか？
A. 追加の変更を行っていない場合は、`git reset --hard ORIG_HEAD` を使用してプル前の状態に戻すことができます。

#### Q3. マージせずにプルするにはどうすればよいですか？
A. `git pull` の代わりに `git fetch` を使用します。これにより、ローカルブランチを変更せずにリモート追跡ブランチが更新されます。

#### Q4. `git pull` のコンテキストでの「fast-forward（早送り）」とは何ですか？
A. 早送りマージは、現在のブランチのポインタが単にマージされるブランチの最新コミットに移動し、新しいマージコミットを作成しない場合に発生します。これは、現在のブランチに分岐した変更がない場合に可能です。

## 参考資料

https://git-scm.com/docs/git-pull

## 改訂履歴

- 2025/05/04 初回改訂