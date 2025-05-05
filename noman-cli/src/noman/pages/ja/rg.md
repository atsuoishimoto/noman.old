# rg コマンド

正規表現を使用してファイル内のパターンを検索し、ディレクトリを再帰的に探索します。

## 概要

`rg`（ripgrep）は、現在のディレクトリを再帰的に検索して正規表現パターンを見つける行指向の検索ツールです。grep、ag、ackなどの他の検索ツールよりも高速に動作するように設計されており、同様の機能を合理的なデフォルト設定で提供します。デフォルトでは、ripgrepは.gitignoreルールを尊重し、隠しファイル/ディレクトリやバイナリファイルを自動的にスキップします。

## オプション

### **-i, --ignore-case**

検索で大文字と小文字を区別しないようにします。

```console
$ rg -i error
./log.txt:10:ERROR: Connection failed
./log.txt:15:error: timeout occurred
./app.js:42:console.log('error handling');
```

### **-v, --invert-match**

指定したパターンに一致しない行を表示します。

```console
$ rg -v error test.log
./test.log:1:Starting application
./test.log:2:Loading configuration
./test.log:5:Application running
```

### **-w, --word-regexp**

単語境界で囲まれた一致のみを表示します。

```console
$ rg -w log
./app.js:42:console.log('error handling');
./utils.js:15:function log(message) {
```

### **-c, --count**

各ファイルの一致する行数のみを表示します。

```console
$ rg -c error logs/
logs/app.log:15
logs/system.log:3
logs/debug.log:0
```

### **-l, --files-with-matches**

少なくとも1つの一致を含むパスのみを表示します。

```console
$ rg -l error
logs/app.log
logs/system.log
src/error_handler.js
```

### **--no-ignore**

無視ファイル（.gitignore、.ignoreなど）を尊重しません。

```console
$ rg --no-ignore password
.git/config:3:password=secret123
node_modules/test-lib/passwords.json:5:"default_password": "admin"
```

### **-A, --after-context NUM**

各一致の後にNUM行を表示します。

```console
$ rg -A 2 error app.log
app.log:15:error: connection failed
app.log:16:  at line 42 in network.js
app.log:17:  attempted reconnect
```

### **-B, --before-context NUM**

各一致の前にNUM行を表示します。

```console
$ rg -B 2 error app.log
app.log:13:attempting connection
app.log:14:using default timeout
app.log:15:error: connection failed
```

## 使用例

### 特定のファイルタイプで検索

```console
$ rg -t js console.log
src/main.js:10:  console.log('Application started');
src/utils.js:25:  console.log('Loading data...');
```

### 複数のパターンで検索

```console
$ rg 'error|warning|critical' logs/app.log
logs/app.log:15:error: connection failed
logs/app.log:23:warning: slow response time
logs/app.log:45:critical: database unavailable
```

### ファイル名パターンで検索

```console
$ rg TODO -g '*.js'
src/app.js:42:// TODO: Implement error handling
src/utils.js:78:// TODO: Optimize this function
```

## ヒント:

### スマートケースで柔軟なマッチングを使用

`-S`または`--smart-case`を使用すると、パターンがすべて小文字の場合は大文字と小文字を区別しない検索を行い、パターンに大文字が含まれる場合は大文字と小文字を区別する検索を行います。

### 他のコマンドと組み合わせる

`rg`の出力を他のコマンドにパイプして、さらに処理することができます：
```console
$ rg -n 'TODO|FIXME' --no-heading | sort -k1,1
```

### 圧縮ファイル内を検索

`--search-zip`を使用して、.gzや.zipなどの圧縮ファイル内を検索できます：
```console
$ rg --search-zip "error" logs/
```

### 特定のディレクトリを除外

`--glob=!{dir}`を使用して、特定のディレクトリを除外できます：
```console
$ rg "function" --glob=!{node_modules,dist}
```

## よくある質問

#### Q1. ripgrepはgrepとどう違いますか？
A. ripgrepは一般的にgrepよりも高速で、自動的に再帰的に検索し、デフォルトで.gitignoreルールを尊重し、多くのファイルタイプやエンコーディングに対する組み込みサポートを持っています。

#### Q2. スペースを含むパターンを検索するにはどうすればよいですか？
A. パターンを引用符で囲みます：`rg "スペースを含む検索パターン"`

#### Q3. ripgrepで隠しファイルやディレクトリを検索するにはどうすればよいですか？
A. `--hidden`フラグを使用します：`rg --hidden パターン`

#### Q4. 正規表現パターンではなくリテラル文字列を検索するにはどうすればよいですか？
A. `-F`または`--fixed-strings`オプションを使用します：`rg -F "特殊文字を含む(文字列)"`

#### Q5. --no-ignoreオプションは何をしますか？
A. `--no-ignore`オプションは、ripgrepにすべての無視ファイル（.gitignore、.ignoreなど）を無視するよう指示し、通常は無視パターンに基づいて除外されるファイルも含めてすべてのファイルを検索します。

## 参考資料

https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md

## 改訂履歴

- 2025/05/04 --no-ignoreオプションの説明を追加し、FAQを拡張しました。