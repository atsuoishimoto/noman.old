# rg コマンド

ファイル内の文字列を高速に検索するためのツール。

## 概要

`rg`（ripgrep）は、ファイル内のテキストパターンを検索するための高速なコマンドラインツールです。Gitリポジトリやプロジェクトディレクトリ内で特定のコードやテキストを素早く見つけることができます。デフォルトでは、バイナリファイルや隠しファイル、.gitignoreに記載されたファイルは無視されます。

## オプション

### **-i, --ignore-case**

大文字と小文字を区別せずに検索します。

```console
$ rg -i "error" 
src/main.rs:15:    if let Err(error) = process() {
src/utils.rs:42:    println!("ERROR: {}", message);
```

### **-v, --invert-match**

パターンに一致しない行を表示します。

```console
$ rg -v "success" log.txt
2025-04-28 10:15:23 ERROR: Connection failed
2025-04-28 10:16:45 WARNING: Retry attempt 1
2025-04-28 10:17:12 INFO: Processing started
```

### **-A, --after-context**

マッチした行の後に指定した行数を表示します。

```console
$ rg -A 2 "error" log.txt
2025-04-28 10:15:23 ERROR: Connection failed
2025-04-28 10:15:24 INFO: Attempting reconnect
2025-04-28 10:15:25 INFO: Reconnected successfully
```

### **-B, --before-context**

マッチした行の前に指定した行数を表示します。

```console
$ rg -B 2 "error" log.txt
2025-04-28 10:15:21 INFO: Connecting to server
2025-04-28 10:15:22 INFO: Handshake initiated
2025-04-28 10:15:23 ERROR: Connection failed
```

### **-C, --context**

マッチした行の前後に指定した行数を表示します。

```console
$ rg -C 1 "error" log.txt
2025-04-28 10:15:22 INFO: Handshake initiated
2025-04-28 10:15:23 ERROR: Connection failed
2025-04-28 10:15:24 INFO: Attempting reconnect
```

### **--no-ignore**

.gitignoreなどで指定された無視ファイルも検索対象に含めます。

```console
$ rg --no-ignore "TODO"
node_modules/some-package/README.md:10:TODO: Update documentation
.git/COMMIT_EDITMSG:3:TODO: Fix this before merging
src/main.rs:42:// TODO: Refactor this function
```

### **-t, --type**

特定のファイルタイプのみを検索します。

```console
$ rg -t rust "impl"
src/lib.rs:15:impl Database {
src/models.rs:24:impl User {
```

### **-g, --glob**

指定したグロブパターンに一致するファイルのみを検索します。

```console
$ rg -g "*.json" "api_key"
config.json:5:  "api_key": "abcd1234"
settings.json:12:  "api_key": "xyz789"
```

## 使用例

### 複数のディレクトリを検索

```console
$ rg "function" src/ lib/ tests/
src/main.js:15:function processData(input) {
lib/utils.js:42:function formatOutput(data) {
tests/main.test.js:7:function testProcessing() {
```

### 正規表現を使用した検索

```console
$ rg "\d{4}-\d{2}-\d{2}" logs/
logs/app.log:2025-04-28 10:15:23 ERROR: Connection failed
logs/app.log:2025-04-29 09:30:45 INFO: Application started
logs/system.log:2025-04-30 14:22:18 WARNING: Disk space low
```

### 再帰的に検索して結果をファイルに保存

```console
$ rg -r "TODO|FIXME" --json > todos.json
# 「TODO」または「FIXME」を含む行をJSON形式で出力し、ファイルに保存する
```

## ヒント:

### 検索速度の最適化

大規模なプロジェクトでは、`-t` オプションを使って特定のファイルタイプに絞り込むことで検索速度が大幅に向上します。例えば `rg -t js "function"` とすると JavaScript ファイルのみを検索します。

### 複雑な検索パターン

正規表現をサポートしているため、複雑な検索パターンを使用できます。例えば `rg "\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b" -i` でメールアドレスを検索できます。

### 検索結果のフィルタリング

`rg` の結果を `grep` や他のコマンドと組み合わせることで、さらに結果をフィルタリングできます。例えば `rg "error" | grep "critical"` とすると、"error" を含む行のうち "critical" も含む行だけを表示します。

### 隠しファイルの検索

デフォルトでは隠しファイルやディレクトリは検索されませんが、`-u` または `--unrestricted` オプションを使用すると検索対象に含めることができます。

## よくある質問

#### Q1. `rg` と `grep` の違いは何ですか？
A. `rg` は `grep` よりも高速で、デフォルトで再帰的に検索し、.gitignore ファイルを尊重します。また、ファイルタイプの指定やカラー出力などの機能が標準で組み込まれています。

#### Q2. 大文字と小文字を区別せずに検索するにはどうすればいいですか？
A. `-i` または `--ignore-case` オプションを使用します。例: `rg -i "error"`

#### Q3. バイナリファイルも検索対象に含めるにはどうすればいいですか？
A. `-a` または `--text` オプションを使用します。ただし、バイナリファイルの検索は時間がかかる場合があります。

#### Q4. .gitignore で無視されているファイルも検索するにはどうすればいいですか？
A. `--no-ignore` オプションを使用します。例: `rg --no-ignore "password"`

#### Q5. macOS で `rg` をインストールするにはどうすればいいですか？
A. Homebrew を使用して `brew install ripgrep` でインストールできます。

## 参考

https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md

## 改訂

- 2025/04/30 --no-ignoreオプションの説明を追加。
- 2025/04/30 初版作成。