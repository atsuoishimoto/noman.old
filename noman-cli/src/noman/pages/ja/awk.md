# awk コマンド

テキストファイルのパターンスキャンと処理を行う言語です。

## 概要

`awk` は強力なテキスト処理ツールで、ファイルを1行ずつスキャンし、各行をフィールドに分割して、パターンとアクションに基づいてそれらのフィールドに対して操作を実行します。構造化されたテキストから特定の列を抽出したり、レポートを生成したり、データを変換したりするのに特に便利です。`awk` は各行をレコードとして、各単語をフィールドとして扱うため、CSVファイル、ログ、その他の構造化されたテキストデータの処理に最適です。

## オプション

### **-F fs, --field-separator fs**

フィールド区切り文字を指定します（デフォルトは空白）

```console
$ echo "apple,orange,banana" | awk -F, '{print $2}'
orange
```

### **-f file, --file file**

コマンドラインではなくファイルからAWKプログラムを読み込みます

```console
$ cat script.awk
{print $1}
$ awk -f script.awk data.txt
[data.txtの各行の最初のフィールドが表示される]
```

### **-v var=val, --assign var=val**

プログラム実行前に変数に値を割り当てます

```console
$ awk -v name="John" '{print "Hello, " name "!"}'
Hello, John!
```

### **-W version, --version**

バージョン情報を表示して終了します

```console
$ awk --version
GNU Awk 5.1.0, API: 3.0 (GNU MPFR 4.1.0, GNU MP 6.2.1)
```

## 使用例

### 基本的なフィールド表示

```console
$ echo "John Smith 42" | awk '{print $1, $2}'
John Smith
```

### パターンマッチングによる行のフィルタリング

```console
$ cat /etc/passwd | awk -F: '/root/ {print $1, $6}'
root /root
```

### 合計の計算

```console
$ cat numbers.txt
10
20
30
$ awk '{sum += $1} END {print "Sum:", sum}' numbers.txt
Sum: 60
```

### CSVデータの処理

```console
$ cat data.csv
Name,Age,City
John,25,New York
Mary,30,Boston
$ awk -F, 'NR>1 {print "Name: " $1 ", Age: " $2}' data.csv
Name: John, Age: 25
Name: Mary, Age: 30
```

## ヒント:

### 組み込み変数

`awk` にはいくつかの組み込み変数があります：`NR`（現在のレコード番号）、`NF`（現在のレコードのフィールド数）、`FS`（フィールド区切り文字）、`OFS`（出力フィールド区切り文字）。これらを使用してスクリプトを簡素化できます。

### 複数のコマンド

セミコロンで複数のコマンドを区切ります：`awk '{count++; sum+=$1} END {print "Average:", sum/count}'`

### 正規表現

`awk` はパターンマッチングのための強力な正規表現をサポートしています：`awk '/^[0-9]+$/ {print "Number:", $0}'` は数字のみを含む行にマッチします。

### BEGIN と END ブロック

初期化には `BEGIN` を、最終処理には `END` を使用します：`awk 'BEGIN {print "Start"} {print $1} END {print "Done"}'`

## よくある質問

#### Q1. ファイルから特定の列を表示するにはどうすればよいですか？
A. `awk '{print $n}'` を使用します。ここで n は列番号です。例えば、`awk '{print $1, $3}'` は1列目と3列目を表示します。

#### Q2. フィールド区切り文字を変更するにはどうすればよいですか？
A. `-F` オプションを使用します：`awk -F, '{print $1}'` はカンマをフィールド区切り文字として使用します。

#### Q3. 数値フィールドで計算を実行するにはどうすればよいですか？
A. 算術演算子を使用します：`awk '{sum+=$1} END {print sum}'` は1列目の合計を計算します。

#### Q4. awkでif-else文を使用できますか？
A. はい、`awk` は条件文をサポートしています：`awk '{if ($1 > 10) print "Large"; else print "Small"}'`

#### Q5. 特定の行だけを処理するにはどうすればよいですか？
A. パターンを使用します：`awk 'NR > 1 {print}'` は最初の行をスキップし、`awk '/pattern/ {print}'` はパターンに一致する行のみを処理します。

## 参考資料

https://www.gnu.org/software/gawk/manual/gawk.html

## 改訂履歴

- 2025/05/04 初版作成