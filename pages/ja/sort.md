# `sort` コマンド

テキストファイルの行を並べ替えるためのUnixコマンドです。デフォルトでは文字列を辞書順（アルファベット順）に並べ替えます。

## オプション

### **`-n`（数値として並べ替え）**
文字列ではなく数値として認識して並べ替えます。

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

### **`-r`（逆順に並べ替え）**
通常の並び順を逆にします（降順）。

```console
$ sort -r fruits.txt
orange
banana
apple
```

### **`-k FIELD`（特定のフィールドで並べ替え）**
区切り文字で分けられたテキストの特定の列を基準に並べ替えます。

```console
$ sort -k2 users.txt
bob 25 engineer
alice 30 designer
carol 40 manager
```

### **`-t DELIMITER`（フィールド区切り文字を指定）**
デフォルトはタブやスペースですが、カンマなど他の区切り文字を指定できます。

```console
$ sort -t, -k2 data.csv
Bob,20,Kyoto
John,25,Tokyo
Mary,30,Osaka
```

### **`-u`（重複行を削除）**
並べ替え結果から重複する行を取り除きます。

```console
$ sort -u duplicates.txt
apple
banana
orange
```

### **`-f`（大文字小文字を区別しない）**
「A」と「a」を同じものとして扱います。

```console
$ sort -f mixed_case.txt
apple
Apple
Banana
banana
```

## 使用例

### 基本的な使い方

```console
$ cat fruits.txt
orange
apple
banana
$ sort fruits.txt
apple
banana
orange
```

### 数値の降順で並べ替え

```console
$ cat scores.txt
Alice 85
Bob 92
Carol 78
$ sort -k2 -nr scores.txt
Bob 92
Alice 85
Carol 78
```

### CSVファイルの3列目で並べ替え

```console
$ cat employees.csv
名前,部署,年齢
田中,営業,32
佐藤,開発,28
鈴木,人事,35
$ sort -t, -k3 -n employees.csv
名前,部署,年齢
佐藤,開発,28
田中,営業,32
鈴木,人事,35
```

## よくある質問

#### Q1. `sort`コマンドは元のファイルを変更しますか？
A. いいえ、`sort`は一時的な並べ替えを行うだけで、元のファイルは変更されません。結果を保存するには、リダイレクト（`>`）を使用します：`sort file.txt > sorted_file.txt`

#### Q2. 複数の条件で並べ替えるにはどうすればよいですか？
A. 複数の `-k` オプションを指定します：`sort -t, -k1,1 -k2,2n data.csv`（1列目を文字列、2列目を数値として並べ替え）

#### Q3. 特定の列の一部だけを使って並べ替えることはできますか？
A. はい、`-k` オプションで開始位置と終了位置を指定できます：`sort -k2.3,2.5` は2列目の3文字目から5文字目を使用します。

## 追加情報

* `sort`はパイプ（`|`）と組み合わせて使うことが多いコマンドです：
  ```bash
  ls -l | sort -k5n  # ファイルサイズ順にディレクトリ内容を表示
  ```

* macOSの`sort`コマンドはGNU版と若干動作が異なる場合があります。特に複雑な並べ替えを行う場合は、オプションの挙動を確認してください。

* メモリ使用量を抑えるために、大きなファイルを扱う場合は `-S` オプションでメモリ使用量を制限できます。

## 参照

https://www.gnu.org/software/coreutils/manual/html_node/sort-invocation.html

## 改訂履歴

- 2025/04/26 macOSに関する注意点を追加。よくある質問を追加。
- 2025/04/01 コマンドの概要を冒頭に追加。