# uniq コマンド

テキストファイル内の重複行を検出または削除します。

## 概要

`uniq` コマンドは、連続する重複行を検出し、削除するために使用されます。デフォルトでは、入力テキストから連続する重複行を1行だけ残して削除します。通常は `sort` コマンドと組み合わせて使用され、ファイル内のすべての重複行を処理します。

## オプション

### **-c (--count)**

各行の出現回数を行の先頭に表示します。

```console
$ cat sample.txt
apple
apple
banana
orange
orange
orange
$ uniq -c sample.txt
      2 apple
      1 banana
      3 orange
```

### **-d (--repeated)**

重複する行のみを出力します（各重複グループから1行）。

```console
$ cat sample.txt
apple
apple
banana
orange
orange
orange
$ uniq -d sample.txt
apple
orange
```

### **-u (--unique)**

重複しない行のみを出力します。

```console
$ cat sample.txt
apple
apple
banana
orange
orange
orange
$ uniq -u sample.txt
banana
```

### **-i (--ignore-case)**

大文字と小文字を区別せずに比較します。

```console
$ cat case.txt
Apple
apple
BANANA
banana
$ uniq -i case.txt
Apple
BANANA
```

## 使用例

### sortと組み合わせた使用

`uniq` は連続する重複行のみを処理するため、通常は `sort` と組み合わせて使用します。

```console
$ cat unsorted.txt
banana
apple
orange
apple
banana
$ sort unsorted.txt | uniq
apple
banana
orange
```

### 重複行の数をカウントして降順に並べ替え

```console
$ cat words.txt
dog
cat
fish
dog
cat
dog
$ sort words.txt | uniq -c | sort -nr
      3 dog
      2 cat
      1 fish
```

### 特定のフィールドのみを比較

`-f` オプションを使用して、比較する前に指定した数のフィールドをスキップします。

```console
$ cat data.txt
1 John Smith
2 John Smith
3 Jane Doe
$ uniq -f 1 data.txt
1 John Smith
3 Jane Doe
```

## ヒント:

### 非連続の重複行を処理するには

`uniq` は連続する重複行のみを処理します。ファイル全体の重複を処理するには、まず `sort` でファイルをソートしてから `uniq` を適用してください。

### 特定の列だけで比較する

`-f` オプション（フィールドをスキップ）と `-s` オプション（文字をスキップ）を使用して、行の特定の部分だけを比較できます。

### 出力のカスタマイズ

`-c`（カウント）、`-d`（重複のみ）、`-u`（ユニークのみ）を組み合わせることで、様々な出力形式を得ることができます。

## よくある質問

#### Q1. `uniq` と `sort | uniq` の違いは何ですか？
A. `uniq` は連続する重複行のみを処理しますが、`sort | uniq` はファイル内のすべての重複行を処理します。ファイル全体から重複を削除したい場合は、まず `sort` でソートする必要があります。

#### Q2. 大文字と小文字を区別せずに重複を削除するにはどうすればよいですか？
A. `-i` または `--ignore-case` オプションを使用します。例：`uniq -i filename`

#### Q3. 特定の列や文字数を無視して比較するにはどうすればよいですか？
A. `-f N`（最初のN個のフィールドをスキップ）または `-s N`（最初のN文字をスキップ）オプションを使用します。

#### Q4. 重複行の数を知りたい場合はどうすればよいですか？
A. `-c` または `--count` オプションを使用すると、各行の出現回数が表示されます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html

## Revisions

- 2025/04/30 初版作成