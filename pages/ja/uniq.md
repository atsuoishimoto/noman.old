# uniq コマンド

`uniq`コマンドは、テキストファイル内の連続する重複行を検出し、削除するためのコマンドです。主に`sort`コマンドと組み合わせて使用されます。

## オプション

### **-c, --count**
各行の前に、その行が何回連続して出現したかを表示します。

```console
$ cat fruits.txt
apple
apple
banana
orange
orange
orange

$ uniq -c fruits.txt
      2 apple
      1 banana
      3 orange
```

### **-d, --repeated**
重複する行のみを表示します（各重複グループから1行）。

```console
$ uniq -d fruits.txt
apple
orange
```

### **-D, --all-repeated**
重複する行をすべて表示します。

```console
$ uniq -D fruits.txt
apple
apple
orange
orange
orange
```

### **-u, --unique**
重複しない行のみを表示します。

```console
$ uniq -u fruits.txt
banana
```

### **-i, --ignore-case**
大文字と小文字を区別せずに比較します。

```console
$ cat mixed_case.txt
Apple
apple
BANANA
banana

$ uniq -i mixed_case.txt
Apple
BANANA
```

### **-f N, --skip-fields=N**
比較する際に最初のN個のフィールド（空白で区切られた部分）をスキップします。

```console
$ cat data.txt
1 apple red
1 apple green
2 banana yellow

$ uniq -f 1 data.txt
1 apple red
2 banana yellow
```

### **-s N, --skip-chars=N**
比較する際に各行の最初のN文字をスキップします。

```console
$ cat codes.txt
ABC123
ABC456
DEF789

$ uniq -s 3 codes.txt
ABC123
DEF789
```

## 使用例

### 基本的な使用法

```console
$ cat fruits.txt
apple
apple
banana
orange
orange
orange
grape

$ uniq fruits.txt
apple
banana
orange
grape
```

### ソートしてから重複を削除

```console
$ cat unsorted.txt
banana
apple
banana
apple
orange

$ sort unsorted.txt | uniq
apple
banana
orange
```

### 重複行の数をカウントしてソート

```console
$ sort fruits.txt | uniq -c | sort -nr
      3 orange
      2 apple
      1 grape
      1 banana
```

## Tips

### 隣接していない重複行を処理する
`uniq`は隣接する行のみを比較するため、通常は`sort`コマンドと組み合わせて使用します：
```console
$ sort file.txt | uniq
```

### 特定のフィールドに基づいて重複を削除
CSVファイルなどで特定の列だけを考慮したい場合は`-f`オプションが便利です：
```console
$ uniq -f 2 data.csv
```

### 出現回数の多い順にソート
頻度の高い行を見つけるには、`-c`オプションと`sort`を組み合わせます：
```console
$ sort file.txt | uniq -c | sort -nr
```

## よくある質問

#### Q1. `uniq`と`sort -u`の違いは何ですか？
A. `sort -u`は、ファイル全体をソートしてから重複を削除します。`uniq`は隣接する重複行のみを削除するため、通常は`sort | uniq`として使用します。`sort -u`は`sort | uniq`と同等ですが、一般的に効率的です。

#### Q2. `uniq`は隣接していない重複行を削除できますか？
A. いいえ、`uniq`は隣接する行のみを比較します。隣接していない重複を削除するには、まず`sort`でファイルをソートする必要があります。

#### Q3. 大きなファイルで`uniq`を使う場合の注意点はありますか？
A. 大きなファイルの場合、メモリ使用量に注意が必要です。特に`sort`と組み合わせる場合は、`sort`の`-T`オプションで一時ディレクトリを指定することを検討してください。

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html

## 改訂履歴

- 2025/04/26 ドキュメント全体を改訂し、フォーマットを統一。例を追加し、Tips、FAQセクションを追加。