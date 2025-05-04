# sort コマンド

テキストファイルの行をアルファベット順または数値順に並べ替えます。

## 概要

`sort` コマンドは、テキストファイルや標準入力からの行をアルファベット順、数値順、またはカスタム定義された順序で並べ替えます。複数のソート済みファイルを結合したり、重複行を削除したり、その他の様々な並べ替え操作を実行できます。このユーティリティは、データ処理パイプラインやテキストベースの情報を整理するために一般的に使用されます。

## オプション

### **-n, --numeric-sort**

アルファベット順ではなく数値順に並べ替えます。フィールドの先頭にある数字を認識します。

```console
$ cat numbers.txt
10
2
1
$ sort -n numbers.txt
1
2
10
```

### **-r, --reverse**

比較結果を反転させ、降順に並べ替えます。

```console
$ sort -r fruits.txt
watermelon
orange
banana
apple
```

### **-k, --key=POS1[,POS2]**

入力の特定のフィールド（列）に基づいて並べ替えます。

```console
$ cat employees.txt
John 35 Developer
Alice 28 Designer
Bob 42 Manager
$ sort -k2 -n employees.txt
Alice 28 Designer
John 35 Developer
Bob 42 Manager
```

### **-t, --field-separator=SEP**

フィールド区切り文字を指定します（デフォルトは空白）。

```console
$ cat data.csv
name,age,role
John,35,Developer
Alice,28,Designer
Bob,42,Manager
$ sort -t, -k2 -n data.csv
name,age,role
Alice,28,Designer
John,35,Developer
Bob,42,Manager
```

### **-u, --unique**

等しい行の最初のもののみを出力します（重複を削除）。

```console
$ cat duplicates.txt
apple
banana
apple
orange
banana
$ sort -u duplicates.txt
apple
banana
orange
```

### **-f, --ignore-case**

アルファベット順に並べ替える際に大文字と小文字を区別しません。

```console
$ cat mixed-case.txt
Apple
banana
Carrot
apple
$ sort -f mixed-case.txt
Apple
apple
banana
Carrot
```

### **-h, --human-numeric-sort**

人間が読みやすい数値（例：2K、1M）を比較します。

```console
$ cat sizes.txt
1K
5M
10G
2K
$ sort -h sizes.txt
1K
2K
5M
10G
```

## 使用例

### ファイルを並べ替えて出力を保存する

```console
$ sort names.txt > sorted_names.txt
```

### 複数のソート済みファイルを結合する

```console
$ sort -m sorted1.txt sorted2.txt > merged.txt
```

### 複数のフィールドで並べ替える

```console
$ cat data.txt
John Smith 35 Developer
Alice Johnson 28 Designer
Bob Williams 42 Manager
$ sort -k4,4 -k1,1 data.txt
Alice Johnson 28 Designer
John Smith 35 Developer
Bob Williams 42 Manager
```

### 列内の一意の値を見つける

```console
$ cat logs.txt | cut -d' ' -f3 | sort -u
ERROR
INFO
WARNING
```

## ヒント:

### 安定ソート

`sort -s` を使用すると安定ソートが行われ、等しいソートキーを持つ行の元の順序が保持されます。これは、複数の基準で順番にソートする場合に便利である。

### メモリ使用量

非常に大きなファイルの場合、`sort -S` でメモリバッファサイズを指定するか、`sort -T` でより多くの空き容量がある一時ディレクトリを指定します。例：`sort -S 1G -T /tmp bigfile.txt`

### すでにソートされているかチェック

`sort -c` を使用すると、出力を生成せずにファイルがすでにソートされているかどうかをチェックできます。終了ステータスは、ファイルがソートされている場合（0）またはそうでない場合（1）を示します。

### ランダムソート

`sort -R` を使用すると行の順序をランダム化できます。これはデータからランダムサンプルを選択する際に便利です。

## よくある質問

#### Q1. ファイルを数値順にソートするにはどうすればよいですか？
A. `sort -n ファイル名` を使用して、アルファベット順ではなく数値順にソートします。

#### Q2. 特定の列でソートするにはどうすればよいですか？
A. `sort -k 列番号 ファイル名` を使用します。例えば、`sort -k 2 ファイル名` は2列目でソートします。

#### Q3. ソート中に重複行を削除するにはどうすればよいですか？
A. `sort -u ファイル名` を使用して、一意の行のみを出力します。

#### Q4. 逆順にソートするにはどうすればよいですか？
A. `sort -r ファイル名` を使用して、降順にソートします。

#### Q5. CSVファイルを特定の列でソートするにはどうすればよいですか？
A. `sort -t, -k 列番号 ファイル名.csv` を使用します。ここで `-t,` はカンマをフィールド区切り文字として指定します。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html

## 改訂履歴

- 2025/05/04 初版作成