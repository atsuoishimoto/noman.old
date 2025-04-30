# awk コマンド

テキストファイルを処理し、パターンマッチングに基づいて特定のアクションを実行するテキスト処理ツール。

## 概要

`awk` はテキストファイルを行単位で処理するプログラミング言語兼コマンドラインツールです。入力テキストをレコード（通常は行）とフィールド（通常は空白で区切られた列）に分割し、パターンマッチングに基づいて様々な処理を行うことができます。データの抽出、変換、レポート生成などに非常に便利です。

## オプション

### **-F** (フィールド区切り文字の指定)

入力テキストのフィールド区切り文字を指定します。デフォルトは空白（スペースまたはタブ）です。

```console
$ echo "apple,orange,banana" | awk -F, '{print $2}'
orange
```

### **-v** (変数の設定)

awk プログラム内で使用する変数に値を設定します。

```console
$ awk -v name="John" 'BEGIN {print "Hello, " name "!"}'
Hello, John!
```

### **-f** (プログラムファイルの指定)

awk プログラムをファイルから読み込みます。

```console
$ cat program.awk
{print $1, $3}
$ awk -f program.awk data.txt
# data.txtの1列目と3列目が表示される
```

## 使用例

### 特定の列を抽出する

```console
$ cat data.txt
John 25 Engineer
Mary 30 Doctor
Bob 22 Student
$ awk '{print $1, $3}' data.txt
John Engineer
Mary Doctor
Bob Student
```

### 条件に一致する行を抽出する

```console
$ awk '$2 > 25' data.txt
Mary 30 Doctor
```

### 列の合計を計算する

```console
$ cat numbers.txt
10 20
30 40
50 60
$ awk '{sum += $1} END {print "合計: " sum}' numbers.txt
合計: 90
```

### CSVファイルの処理

```console
$ cat data.csv
名前,年齢,職業
John,25,Engineer
Mary,30,Doctor
$ awk -F, 'NR>1 {print "名前: " $1 ", 職業: " $3}' data.csv
名前: John, 職業: Engineer
名前: Mary, 職業: Doctor
```

## ヒント:

### 組み込み変数を活用する

`NR`（現在の行番号）や`NF`（現在の行のフィールド数）などの組み込み変数を使うと便利です。

```console
$ awk '{print NR ":", $0}' data.txt
1: John 25 Engineer
2: Mary 30 Doctor
3: Bob 22 Student
```

### BEGIN/END ブロックを使う

`BEGIN`ブロックは処理開始前に、`END`ブロックは処理終了後に実行されます。

```console
$ awk 'BEGIN {print "処理開始"} {count++} END {print "合計行数: " count}' data.txt
処理開始
合計行数: 3
```

### 正規表現を活用する

パターンマッチングには正規表現が使えます。

```console
$ awk '/Engineer/' data.txt
John 25 Engineer
```

## よくある質問

#### Q1. awkとgrepの違いは何ですか？
A. `grep`は単純なパターンマッチングに特化していますが、`awk`はより高度なテキスト処理（列の抽出、計算、条件処理など）ができます。

#### Q2. awkで複数の区切り文字を指定するには？
A. `-F`オプションに正規表現を使用します。例：`awk -F'[,|]'`はカンマまたはパイプを区切り文字として扱います。

#### Q3. awkスクリプトを保存して再利用するには？
A. スクリプトをファイルに保存し、`-f`オプションで指定します：`awk -f script.awk data.txt`

#### Q4. awkで特定の列の合計を計算するには？
A. `{sum += $2} END {print sum}`のように、変数に加算して最後に表示します。

## macOSでの注意点

macOSのデフォルトの`awk`はBSD版で、GNU版と若干の違いがあります。より高度な機能が必要な場合は、Homebrewで`gawk`（GNU awk）をインストールすることをお勧めします：`brew install gawk`

## 参考文献

https://www.gnu.org/software/gawk/manual/gawk.html

## 改訂履歴

- 2025/04/30 初版作成