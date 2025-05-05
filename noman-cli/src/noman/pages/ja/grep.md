# grep コマンド

ファイル内のパターンを検索します。

## 概要

`grep`は、ファイルや標準入力から指定したパターンに一致する行を検索する強力なテキスト検索ユーティリティです。特定のテキストをファイル内で見つけたり、コマンド出力をフィルタリングしたり、大規模なデータセットを検索したりするのによく使用されます。名前は「global regular expression print（グローバル正規表現プリント）」に由来しています。

## オプション

### **-i, --ignore-case**

大文字と小文字を区別せずに検索します。

```console
$ grep -i "hello" file.txt
Hello World
HELLO everyone
hello there
```

### **-v, --invert-match**

一致を反転させ、パターンに一致しない行を表示します。

```console
$ grep -v "error" log.txt
Starting application
Loading configuration
Application running
Shutting down
```

### **-r, --recursive**

ディレクトリを再帰的に検索します。

```console
$ grep -r "TODO" ./src/
./src/main.c:// TODO: Implement error handling
./src/utils.h:/* TODO: Add documentation */
./src/config.c:// TODO: Fix configuration parsing
```

### **-l, --files-with-matches**

一致を含むファイルの名前のみを表示します。

```console
$ grep -l "function" *.js
utils.js
main.js
helpers.js
```

### **-n, --line-number**

一致する行の行番号を表示します。

```console
$ grep -n "import" app.py
3:import os
5:import sys
12:import datetime
```

### **-c, --count**

ファイルごとに一致する行数のみを表示します。

```console
$ grep -c "error" *.log
app.log:15
system.log:3
access.log:0
```

### **-A NUM, --after-context=NUM**

各一致の後にNUM行を表示します。

```console
$ grep -A 2 "function main" main.c
function main() {
  int x = 5;
  printf("Starting program\n");
```

### **-B NUM, --before-context=NUM**

各一致の前にNUM行を表示します。

```console
$ grep -B 1 "Exception" error.log
2023-05-04 15:30:22 Processing request
2023-05-04 15:30:23 Exception: Invalid input
```

### **-E, --extended-regexp**

拡張正規表現を使用します。

```console
$ grep -E "(error|warning)" log.txt
System error: disk full
Warning: connection timeout
```

## 使用例

### 基本的なパターン検索

```console
$ grep "password" config.txt
password=mysecretpassword
# default password is 'admin'
```

### 複数のオプションの組み合わせ

```console
$ grep -in "todo" --color *.py
utils.py:45:# TODO: Refactor this function
helpers.py:23:# todo: Add error handling
main.py:102:# TODO: Implement caching
```

### 正規表現の使用

```console
$ grep "^[0-9]" data.txt
123 Main St
456 Oak Ave
789 Pine Rd
```

### コマンド出力をgrepにパイプする

```console
$ ps aux | grep "firefox"
user     12345  2.5  1.8 3458196 298796 ?      Sl   09:15   0:45 /usr/lib/firefox/firefox
```

## ヒント:

### コンテキストを使用して理解を深める

`-A`、`-B`、または両方の前後のコンテキストを表示する`-C`を組み合わせて、一致の周囲の行を確認することで、一致の文脈をより理解しやすくなります。

### 一致を色付けして視認性を高める

`--color=auto`を使用して一致するテキストを色付けすると、大量の出力の中で見つけやすくなります。多くのシステムではデフォルトでこのオプションを含むようにgrepにエイリアスが設定されています。

### ディレクトリを除外する

再帰的に検索する際に`--exclude-dir=PATTERN`を使用してPATTERNに一致するディレクトリをスキップすると、大規模なコードベースでの検索が大幅に高速化されます。

### 完全一致の単語を検索する

`-w`または`--word-regexp`を使用して完全な単語のみを一致させ、より大きな単語内の部分一致を防ぎます。

### スクリプト用の静かなモード

スクリプトでは`-q`または`--quiet`を使用して出力を抑制し、終了ステータスのみを使用して一致が見つかったかどうかを判断します。

## よくある質問

#### Q1. 複数のファイルでパターンを検索するにはどうすればよいですか？
A. パターンの後にファイルを列挙するだけです：`grep "pattern" file1.txt file2.txt file3.txt`、またはワイルドカードを使用します：`grep "pattern" *.txt`。

#### Q2. スペースを含むパターンを検索するにはどうすればよいですか？
A. パターンを引用符で囲みます：`grep "hello world" file.txt`。

#### Q3. 特殊文字を含むパターンを検索するにはどうすればよいですか？
A. 特殊文字をバックスラッシュでエスケープするか、シングルクォートを使用します：`grep 'pattern\*' file.txt`または`grep "pattern\*" file.txt`。

#### Q4. grepで一度に複数のパターンを検索できますか？
A. はい、`-e`オプションを複数回使用するか、`-E`で拡張正規表現を使用します：`grep -e "pattern1" -e "pattern2" file.txt`または`grep -E "pattern1|pattern2" file.txt`。

#### Q5. grepで行の一致部分のみを表示するにはどうすればよいですか？
A. `-o`または`--only-matching`オプションを使用します：`grep -o "pattern" file.txt`。

## 参考資料

https://www.gnu.org/software/grep/manual/grep.html

## 改訂履歴

- 2025/05/04 初回改訂