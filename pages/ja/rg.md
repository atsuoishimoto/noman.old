# rg コマンド

正規表現を使用してファイル内のパターンを検索し、ディレクトリの再帰的な走査をサポートします。

## 概要

`rg`（ripgrep）は、現在のディレクトリを再帰的に検索して正規表現パターンを見つける行指向の検索ツールです。デフォルトで.gitignoreルールを尊重し、grep、ag、ackなどの他の検索ツールよりも高速に動作するように設計されています。Ripgrepは明示的に指示されない限り、隠しファイル、バイナリファイル、.gitignoreにリストされているファイルを自動的にスキップします。

## オプション

### **-i, --ignore-case**

検索で大文字と小文字を区別しなくなります。

```
$ rg -i "function"
src/main.js:10:function calculateTotal(items) {
src/utils.js:5:Function to handle API responses
```

### **-v, --invert-match**

指定したパターンに一致しない行を表示します。

```
$ rg -v "TODO" todo.txt
These items are completed
Remember to check email
```

### **-w, --word-regexp**

単語の境界で囲まれた一致のみを表示します。

```
$ rg -w "log"
logger.js:15:  log("User logged in");
logger.js:20:  log("Error occurred");
```

### **-c, --count**

ファイルごとの一致する行数のみを表示します。

```
$ rg -c "error" *.log
app.log:15
system.log:3
```

### **-l, --files-with-matches**

少なくとも1つの一致があるパスのみを表示します。

```
$ rg -l "TODO"
src/main.js
docs/roadmap.md
```

### **-n, --line-number**

行番号を表示します（デフォルトで有効）。

```
$ rg -n "function"
src/main.js:10:function calculateTotal(items) {
src/utils.js:15:function formatDate(date) {
```

### **--no-ignore**

無視ファイル（.gitignore、.ignoreなど）を尊重しません。

```
$ rg --no-ignore "password"
node_modules/config.js:5:  password: "dummy_password",
.git/config:10:  password = hunter2
```

### **-A, --after-context NUM**

各一致の後にNUM行を表示します。

```
$ rg -A 2 "class User"
src/models.js:10:class User {
src/models.js:11:  constructor(name, email) {
src/models.js:12:    this.name = name;
```

### **-B, --before-context NUM**

各一致の前にNUM行を表示します。

```
$ rg -B 1 "throw new Error"
src/api.js:24:  if (!response.ok) {
src/api.js:25:    throw new Error('API request failed');
```

### **-C, --context NUM**

各一致の前後にNUM行を表示します。

```
$ rg -C 1 "TODO"
src/main.js:19:function processData(data) {
src/main.js:20:  // TODO: Implement validation
src/main.js:21:  return transform(data);
```

## 使用例

### 特定のファイルタイプで検索

```
$ rg -t js "useState"
src/components/Form.js:3:import { useState } from 'react';
src/components/Counter.js:5:  const [count, setCount] = useState(0);
```

### ripgrepとsedを使用した検索と置換

```
$ rg -l "oldFunction" | xargs sed -i 's/oldFunction/newFunction/g'
```

### グロブパターンでの検索

```
$ rg "error" --glob "*.{js,ts}"
src/utils.js:25:  console.error("Connection failed");
src/api.ts:42:  throw new Error("Invalid response");
```

### 検索からディレクトリを除外

```
$ rg "TODO" --glob "!node_modules"
src/main.js:20:  // TODO: Implement validation
docs/roadmap.md:15:TODO: Add authentication
```

## ヒント:

### より高速な検索には固定文字列を使用

正規表現パターンではなく文字通りのテキストを検索する場合は、パフォーマンス向上のために `-F` または `--fixed-strings` を使用します：

```
$ rg -F "React.useState" src/
```

### 他のツールと組み合わせる

ripgrepの結果を他のコマンドにパイプして追加処理を行います：

```
$ rg -n "TODO" | sort -k1,1 | less
```

### 隠しファイルを検索

デフォルトでは、ripgrepは隠しファイルとディレクトリを無視します。それらを含めるには `-. または --hidden` を使用します：

```
$ rg --hidden "password" ~/
```

### スマートケースを使用

`-S` または `--smart-case` オプションを使用すると、パターンがすべて小文字の場合は大文字と小文字を区別しない検索になり、それ以外の場合は大文字と小文字を区別する検索になります：

```
$ rg -S "function" # 大文字小文字を区別しない
$ rg -S "Function" # 大文字小文字を区別する
```

## よくある質問

#### Q1. ripgrepはgrepとどう違いますか？
A. ripgrepは一般的にgrepよりも高速で、デフォルトで.gitignoreファイルを尊重し、バイナリファイルを自動的にスキップし、より優れたUnicodeサポートを持っています。

#### Q2. 特殊な正規表現文字を含むパターンを検索するにはどうすればよいですか？
A. `-F` または `--fixed-strings` を使用して文字通りのテキストを検索するか、特殊文字をバックスラッシュでエスケープします。

#### Q3. パターンを含まないファイルを検索するにはどうすればよいですか？
A. `-L` または `--files-without-match` を使用して、パターンを含まないファイルを見つけます。

#### Q4. ripgrepでシンボリックリンクをたどるにはどうすればよいですか？
A. `-L` または `--follow` を使用して、検索時にシンボリックリンクをたどります。

#### Q5. --no-ignoreオプションは何をしますか？
A. `--no-ignore` オプションは、.gitignore、.ignore、または同様のファイルによって通常無視されるファイルやディレクトリも検索するようripgrepに指示します。これは、node_modulesや他の通常無視される場所で検索する必要がある場合に便利です。

## 参考文献

https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md

## 改訂履歴

- 2025/05/05 --no-ignoreオプションの説明を追加し、FAQを拡充しました。