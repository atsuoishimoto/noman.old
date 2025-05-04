# uniq コマンド

隣接する重複行を入力からフィルタリングまたは報告します。

## 概要

`uniq`コマンドはテキスト入力を処理し、連続して現れる重複行をフィルタリングまたは識別します。このコマンドは隣接する行のみを比較するため、正しく機能するにはソートされた入力が必要です。一般的に`sort`コマンドと組み合わせて使用され、重複を排除したり、ファイル内の各行が何回出現するかをカウントしたりするのに役立ちます。

## オプション

### **-c, --count**

各行の前に出現回数を表示します

```console
$ cat names.txt
Alice
Bob
Bob
Charlie
Charlie
Charlie
$ sort names.txt | uniq -c
      1 Alice
      2 Bob
      3 Charlie
```

### **-d, --repeated**

重複する行のみを表示します（各グループにつき1行）

```console
$ cat names.txt
Alice
Bob
Bob
Charlie
Charlie
Charlie
$ sort names.txt | uniq -d
Bob
Charlie
```

### **-u, --unique**

一意の行のみを表示します（入力で重複していない行）

```console
$ cat names.txt
Alice
Bob
Bob
Charlie
Charlie
Charlie
$ sort names.txt | uniq -u
Alice
```

### **-i, --ignore-case**

行を比較する際に大文字と小文字の違いを無視します

```console
$ cat mixed-case.txt
apple
Apple
banana
BANANA
$ sort mixed-case.txt | uniq -i
apple
banana
```

### **-f N, --skip-fields=N**

最初のN個のフィールドの比較をスキップします

```console
$ cat data.txt
1 John Smith
1 Jane Doe
2 John Smith
$ uniq -f 1 data.txt
1 John Smith
1 Jane Doe
2 John Smith
```

### **-s N, --skip-chars=N**

最初のN文字の比較をスキップします

```console
$ cat codes.txt
ABC123
ABC456
DEF123
$ uniq -s 3 codes.txt
ABC123
DEF123
```

## 使用例

### ファイル内のユニークな単語をカウントする

```console
$ cat words.txt
hello
world
hello
computer
world
$ sort words.txt | uniq -c
      1 computer
      2 hello
      2 world
```

### 一意のエントリのみを見つける

```console
$ cat log.txt
ERROR: Connection failed
INFO: Starting application
ERROR: Connection failed
INFO: Application ready
$ sort log.txt | uniq -u
INFO: Application ready
INFO: Starting application
```

### パイプラインで他のコマンドと組み合わせる

```console
$ cat access.log | grep "404" | cut -d' ' -f1 | sort | uniq -c
     15 192.168.1.5
      3 192.168.1.7
     22 192.168.1.10
```

## ヒント:

### 常に先にソートする

`uniq`コマンドは隣接する重複行のみを検出するため、すべての重複を検出するには常に`uniq`の前に`sort`を使用してください：

```console
$ sort file.txt | uniq
```

### すべての行の出現回数をカウントする

ファイル内の各ユニークな行が何回出現するかを確認するには：

```console
$ sort file.txt | uniq -c | sort -nr
```
これにより頻度順（最も頻繁なものが最初）にソートされる。

### 一意でない行を見つける

2回以上出現する行のみを見つけるには：

```console
$ sort file.txt | uniq -d
```

## よくある質問

#### Q1. なぜ`uniq`がファイル内のすべての重複を削除しないのですか？
A. `uniq`は隣接する重複行のみを削除します。最初に`sort file.txt | uniq`でファイルをソートする必要があります。

#### Q2. ファイル内のユニークな行数をカウントするにはどうすればよいですか？
A. `sort file.txt | uniq | wc -l`を使用してユニークな行数をカウントします。

#### Q3. 比較時に行の特定の部分を無視することは可能ですか？
A. はい、`-f N`でN個のフィールドをスキップするか、`-s N`で各行の先頭からN文字をスキップできます。

#### Q4. ファイル内で最も一般的な行を見つけるにはどうすればよいですか？
A. `sort file.txt | uniq -c | sort -nr`を使用して、頻度順（最も頻繁なものが最初）に行をリストします。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/uniq-invocation.html

## 改訂履歴

- 2025/05/04 初版作成