# cut コマンド

各ファイルの行から選択した部分を抽出し、標準出力に出力します。

## 概要

`cut` コマンドは、入力ファイルや標準入力の各行から特定のセクションを抽出するために使用されます。文字位置、バイト位置、または区切り文字で区切られたフィールドで切り取ることができます。これは、CSVやTSVなどの構造化されたテキストファイルの処理や、コマンド出力から特定の列を抽出する場合に特に便利です。

## オプション

### **-b, --bytes=LIST**

各行から特定のバイトを抽出します

```console
$ echo "Hello" | cut -b 1-3
Hel
```

### **-c, --characters=LIST**

各行から特定の文字を抽出します

```console
$ echo "Hello World" | cut -c 1-5
Hello
```

### **-d, --delimiter=DELIM**

デフォルトのタブの代わりにDELIMをフィールド区切り文字として使用します

```console
$ echo "name,age,city" | cut -d, -f2
age
```

### **-f, --fields=LIST**

各行で指定されたフィールドのみを選択します

```console
$ echo "name:age:city" | cut -d: -f1,3
name:city
```

### **-s, --only-delimited**

区切り文字を含まない行を出力しません

```console
$ printf "field1,field2,field3\nno delimiter line\nother,fields,here\n" | cut -d, -f1 -s
field1
other
```

### **--complement**

選択されたバイト、文字、またはフィールドのセットを補完します

```console
$ echo "field1,field2,field3" | cut -d, -f1 --complement
field2,field3
```

### **--output-delimiter=STRING**

入力区切り文字の代わりにSTRINGを出力区切り文字として使用します

```console
$ echo "field1,field2,field3" | cut -d, -f1,3 --output-delimiter=" | "
field1 | field3
```

## 使用例

### CSVファイルから特定の列を抽出する

```console
$ cat data.csv
name,age,city,country
John,25,New York,USA
Alice,30,London,UK
$ cut -d, -f1,3 data.csv
name,city
John,New York
Alice,London
```

### 固定幅データから文字を抽出する

```console
$ cat fixed.txt
ABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
$ cut -c 5-10 fixed.txt
EFGHIJ
efghij
```

### コマンド出力を処理する

```console
$ ps | cut -c 1-5,27-
  PID COMMAND
    1 /sbin/init
  123 bash
  456 ps
```

## ヒント:

### LISTでの範囲指定

文字やフィールドの位置を指定する際には、以下の形式が使えます：
- N: N番目の位置
- N-: N番目の位置から最後まで
- N-M: N番目からM番目の位置まで
- -M: 最初からM番目の位置まで

### 他のコマンドとの組み合わせ

`cut`は`grep`、`sort`、`uniq`などの他のコマンドとパイプラインで組み合わせて、テキストデータを処理・フィルタリングするのに適しています。

### 区切り文字がない場合の処理

デフォルトでは、`cut`は区切り文字を含まない行全体を出力します。必要に応じて`-s`を使用してこれらの行を抑制できます。

### マルチバイト文字の処理

マルチバイト文字（UTF-8など）で`-c`を使用する場合は注意が必要です。このような場合は、適切なバイト範囲で`-b`を使用することを検討してください。

## よくある質問

#### Q1. `-c`と`-b`の違いは何ですか？
A. `-c`は文字位置で選択し、`-b`はバイト位置で選択します。マルチバイト文字（UTF-8エンコーディングなど）では動作が異なります。

#### Q2. 複数のフィールドを抽出するにはどうすればよいですか？
A. `-f`オプションでカンマ区切りの値を使用します。例：`cut -f1,3,5`

#### Q3. 出力区切り文字を変更できますか？
A. はい、`--output-delimiter=STRING`を使用して異なる出力区切り文字を指定できます。

#### Q4. 特定のフィールド以外のすべてを抽出するにはどうすればよいですか？
A. `--complement`オプションを`-f`と一緒に使用して、指定されたフィールド以外のすべてのフィールドを選択します。

#### Q5. なぜcutは可変幅フィールドでうまく動作しないのですか？
A. `cut`は固定幅フィールドまたは区切り文字で区切られたフィールド用に設計されています。可変幅の処理には、代わりに`awk`の使用を検討してください。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/cut-invocation.html

## 改訂履歴

- 2025/05/04 初回改訂