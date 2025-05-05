# tr コマンド

標準入力から文字を変換または削除し、標準出力に書き込みます。

## 概要

`tr` コマンドは文字単位で操作するテキスト変換ユーティリティです。標準入力から読み取り、文字の置換、削除、または圧縮操作を実行し、結果を標準出力に書き込みます。大文字小文字の変換、文字の削除、基本的なテキスト変換などのタスクでシェルスクリプトでよく使用されます。

## オプション

### **-d, --delete**

SET1 に含まれる文字を削除します（変換はしません）。

```console
$ echo "Hello, World!" | tr -d 'aeiou'
Hll, Wrld!
```

### **-s, --squeeze-repeats**

SET1 内の繰り返し文字のシーケンスを、その文字の単一の出現に置き換えます。

```console
$ echo "Hello    World!" | tr -s ' '
Hello World!
```

### **-c, --complement**

SET1 の補集合（SET1 に含まれない全ての文字）を使用します。

```console
$ echo "Hello, World!" | tr -cd 'a-zA-Z'
HelloWorld
```

### **-t, --truncate-set1**

SET1 を SET2 の長さに切り詰めます。

```console
$ echo "Hello" | tr -t 'aeiou' '12345'
H2ll4
```

## 使用例

### 小文字から大文字への変換

```console
$ echo "hello world" | tr 'a-z' 'A-Z'
HELLO WORLD
```

### テキストからすべての数字を削除

```console
$ echo "Phone: 123-456-7890" | tr -d '0-9'
Phone: --
```

### スペースを改行に変換

```console
$ echo "one two three" | tr ' ' '\n'
one
two
three
```

### 印刷不可能な文字をすべて削除

```console
$ cat file.txt | tr -cd '[:print:]\n'
[印刷可能な文字と改行のみが出力される]
```

## ヒント:

### 文字クラス

`[:alnum:]`、`[:alpha:]`、`[:digit:]`、`[:lower:]`、`[:upper:]`、`[:space:]` などの定義済み文字クラスを使用すると、より読みやすく移植性の高いコマンドになります。

```console
$ echo "Hello123" | tr '[:lower:]' '[:upper:]'
HELLO123
```

### オプションの組み合わせ

より複雑な変換のためにオプションを組み合わせることができます。例えば、`-cd` は集合の補集合を取り、文字を削除します。

```console
$ echo "abc123!@#" | tr -cd '[:digit:]'
123
```

### 特殊文字のエスケープ

改行やタブなどの特殊文字を使用する場合は、バックスラッシュで適切にエスケープします。

```console
$ echo "one,two,three" | tr ',' '\n'
one
two
three
```

## よくある質問

#### Q1. 複数のスペースを1つのスペースに置き換えるにはどうすればよいですか？
A. `tr -s ' '` を使用して、複数のスペースを1つに圧縮します。

#### Q2. trは単語やフレーズを置き換えることができますか？
A. いいえ、`tr` は単語やパターンではなく、個々の文字のみを操作します。単語/パターンの置換には、`sed` や `awk` を使用してください。

#### Q3. 英数字以外のすべての文字を削除するにはどうすればよいですか？
A. `tr -cd '[:alnum:]'` を使用して、英数字のみを残します。

#### Q4. なぜtrはファイルを直接処理できないのですか？
A. `tr` は標準入力からのみ読み取ります。ファイルを処理するには、`cat file.txt | tr ...` のようにパイプするか、`tr ... < file.txt` のようにリダイレクションを使用する必要があります。

## macOSでの注意点

macOSの`tr`コマンドはGNU版と若干の違いがあります。特に文字クラスの扱いが異なる場合があるため、ポータブルなスクリプトを書く際は注意が必要です。また、macOSでは一部のBSD由来の動作が見られることがあります。

## 参考文献

https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html

## 改訂履歴

- 2025/05/04 初版作成