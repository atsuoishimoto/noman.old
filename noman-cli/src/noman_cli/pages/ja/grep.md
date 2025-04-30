# grep コマンド

テキストファイルやストリーム内のパターンを検索します。

## 概要

`grep`は、ファイルやテキストストリーム内で正規表現パターンに一致する行を検索するコマンドです。テキスト検索、ログ解析、特定のパターンを含む行の抽出など、多くの場面で活用できます。基本的な使い方は `grep [オプション] パターン [ファイル...]` です。

## オプション

### **-i (--ignore-case)**

大文字と小文字を区別せずに検索します。

```console
$ grep -i "hello" sample.txt
Hello World
hello everyone
HELLO THERE
```

### **-v (--invert-match)**

パターンに一致しない行を表示します。

```console
$ grep -v "error" log.txt
Starting application
Loading configuration
Application running
Shutdown complete
```

### **-r, -R (--recursive)**

ディレクトリ内のすべてのファイルを再帰的に検索します。

```console
$ grep -r "function" src/
src/main.js:function initialize() {
src/utils.js:export function formatDate(date) {
src/components/App.js:function App() {
```

### **-n (--line-number)**

一致した行の行番号も表示します。

```console
$ grep -n "import" app.js
3:import React from 'react';
4:import { useState } from 'react';
7:import './styles.css';
```

### **-c (--count)**

一致した行数のみを表示します。

```console
$ grep -c "error" server.log
42
```

### **-A, -B, -C (--after-context, --before-context, --context)**

一致した行の前後の行も表示します。

```console
$ grep -A 2 "Exception" error.log
java.lang.NullPointerException
    at com.example.Main.process(Main.java:42)
    at com.example.Main.main(Main.java:12)
```

## 使用例

### 複数のファイルから検索

```console
$ grep "config" *.conf
app.conf:config.debug=true
server.conf:config.port=8080
db.conf:config.username=admin
```

### 正規表現を使用した検索

```console
$ grep "^[0-9]" data.txt
123 Main St
456 Oak Ave
789 Pine Rd
```

### パイプラインでの使用

```console
$ ps aux | grep "firefox"
user     12345  2.0  1.5 3521408 124800 ?      Sl   09:23   0:45 /usr/lib/firefox/firefox
```

### 複数のパターンを検索

```console
$ grep -E "error|warning|critical" application.log
[2025-04-30 10:15:22] ERROR: Database connection failed
[2025-04-30 10:16:45] WARNING: Low disk space
[2025-04-30 11:30:12] CRITICAL: System shutdown initiated
```

## ヒント:

### 色付き出力を使用する

`--color=auto` オプションを使うと、マッチした部分が色付きで表示されるため、視認性が向上します。多くのLinuxディストリビューションでは、`grep` にこのオプションがエイリアスとして設定されています。

### 正確なワード検索

単語の一部ではなく完全な単語だけを検索したい場合は、`-w` (--word-regexp) オプションを使用します。

```console
$ grep -w "log" file.txt
# "log" という単語のみマッチし、"logical" や "catalog" などはマッチしない
```

### 検索パターンをファイルから読み込む

多数のパターンで検索する場合は、パターンをファイルに保存して `-f` オプションで指定できます。

```console
$ grep -f patterns.txt logfile.txt
# patterns.txt に記載されたすべてのパターンで検索する
```

## よくある質問

#### Q1. `grep` と `egrep` の違いは何ですか？
A. `egrep` は `grep -E` と同等で、拡張正規表現を使用できます。現代のシステムでは `grep -E` の使用が推奨されています。

#### Q2. 大きなファイルを効率的に検索するには？
A. 大きなファイルでは `grep --mmap` オプションを使用すると、メモリマッピングによって検索が高速化される場合があります。

#### Q3. バイナリファイルを検索から除外するには？
A. `-I` オプションを使用すると、バイナリファイルをテキストファイルとして扱わないようになります。

#### Q4. 検索結果をファイルに保存するには？
A. リダイレクト演算子 `>` を使用します。例: `grep "error" log.txt > errors.txt`

## macOSでの注意点

macOSの `grep` は GNU grep と若干異なる場合があります。特に、`--include` や `--exclude` などの一部のオプションが利用できないか、異なる動作をする可能性があります。macOSで GNU grep と同等の機能が必要な場合は、Homebrewを使って `ggrep` をインストールすることをお勧めします。

```console
$ brew install grep
$ ggrep [オプション] パターン [ファイル...]
```

## 参考資料

https://www.gnu.org/software/grep/manual/grep.html

## 改訂履歴

- 2025/04/30 初版作成