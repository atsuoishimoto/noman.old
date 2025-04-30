# for コマンド

指定した範囲の値や項目に対して繰り返し処理を実行します。

## 概要

`for` コマンドは、シェルスクリプトで繰り返し処理を行うための基本的な制御構造です。リスト内の各項目、数値範囲、ファイル名パターンに一致するファイルなどに対して、同じコマンドや処理を繰り返し実行することができます。

## オプション

`for` コマンド自体にはオプションはありませんが、さまざまな構文形式があります。

### **基本的な for ループ**

シェル変数にリスト内の各値を順番に代入して処理を繰り返します。

```console
$ for name in Alice Bob Charlie; do
>   echo "Hello, $name!"
> done
Hello, Alice!
Hello, Bob!
Hello, Charlie!
```

### **数値範囲を使用した for ループ**

連続した数値に対して処理を繰り返します。

```console
$ for i in {1..5}; do
>   echo "Number: $i"
> done
Number: 1
Number: 2
Number: 3
Number: 4
Number: 5
```

### **C言語スタイルの for ループ (Bash)**

Bashでは、C言語に似た構文でループを記述できます。

```console
$ for ((i=1; i<=5; i++)); do
>   echo "Count: $i"
> done
Count: 1
Count: 2
Count: 3
Count: 4
Count: 5
```

## 使用例

### ディレクトリ内のすべてのファイルを処理する

```console
$ for file in *.txt; do
>   echo "Processing $file..."
>   wc -l "$file"
> done
Processing document.txt...
      20 document.txt
Processing notes.txt...
      15 notes.txt
Processing readme.txt...
      35 readme.txt
```

### 複数のコマンドを実行する

```console
$ for server in server1 server2 server3; do
>   echo "Checking $server..."
>   ping -c 1 $server
>   echo "-------------------"
> done
Checking server1...
PING server1 (192.168.1.1): 56 data bytes
64 bytes from 192.168.1.1: icmp_seq=0 ttl=64 time=0.733 ms
-------------------
Checking server2...
PING server2 (192.168.1.2): 56 data bytes
64 bytes from 192.168.1.2: icmp_seq=0 ttl=64 time=1.240 ms
-------------------
Checking server3...
PING server3 (192.168.1.3): 56 data bytes
64 bytes from 192.168.1.3: icmp_seq=0 ttl=64 time=0.890 ms
-------------------
```

### 増分値を指定した数値範囲

```console
$ for i in {0..10..2}; do
>   echo "Value: $i"
> done
Value: 0
Value: 2
Value: 4
Value: 6
Value: 8
Value: 10
```

## ヒント:

### 変数名の選択

変数名は意味のある名前を選ぶと、コードの可読性が向上します。例えば、ファイルを処理する場合は `i` よりも `file` を使用するとよいでしょう。

### IFSの活用

IFS（Internal Field Separator）を変更することで、特定の区切り文字でリストを分割できます。

```console
$ IFS=","
$ data="apple,banana,cherry"
$ for fruit in $data; do
>   echo "Fruit: $fruit"
> done
Fruit: apple
Fruit: banana
Fruit: cherry
```

### ワイルドカードの展開に注意

ワイルドカードを使用する場合、一致するファイルがない場合はワイルドカードがそのまま変数に代入されます。これを防ぐには、nullglob オプションを設定するか、条件分岐で対処します。

## よくある質問

#### Q1. `for` ループと `while` ループの違いは何ですか？
A. `for` ループは事前に定義された項目のリストを反復処理するのに適しています。一方、`while` ループは条件が真である限り繰り返し実行され、終了条件が動的に変化する場合に適しています。

#### Q2. `for` ループを途中で終了するにはどうすればよいですか？
A. `break` コマンドを使用すると、ループを即座に終了できます。特定の条件でループの現在の反復をスキップするには、`continue` コマンドを使用します。

#### Q3. 配列の各要素に対して `for` ループを実行するにはどうすればよいですか？
A. Bashでは、以下のように配列を反復処理できます：
```bash
array=("item1" "item2" "item3")
for item in "${array[@]}"; do
  echo "$item"
done
```

#### Q4. ファイル内の各行に対して処理を行うには？
A. `for` よりも `while read` を使用する方が適しています：
```bash
while read -r line; do
  echo "Line: $line"
done < file.txt
```

## 参考文献

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## Revisions

- 2025/04/30 初版作成