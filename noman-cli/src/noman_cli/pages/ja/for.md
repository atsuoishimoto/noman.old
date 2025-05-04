# for コマンド

リスト内の各項目に対してコマンドまたはコマンドセットを実行します。

## 概要

`for` コマンドはシェルのループ構文で、値のリストを反復処理し、各値に対して指定されたコマンドを一度ずつ実行します。シェルスクリプトでのバッチ処理、自動化、繰り返しタスクによく使用されます。ループ変数はリスト内の各値を順番に取り、単一のコマンド構造で複数の項目に対して操作を実行できるようにします。

## オプション

`for` コマンドはシェル組み込みコマンドであり、スタンドアロンプログラムのような従来のコマンドラインオプションはありません。代わりに、異なる構文のバリエーションがあります：

### **基本構文**

単語のリストを反復処理する標準的な形式です。

```console
$ for i in one two three; do echo "番号: $i"; done
番号: one
番号: two
番号: three
```

### **C言語スタイル構文**

bashやその他のシェルで利用可能な、数値反復のためのC言語風の構文です。

```console
$ for ((i=1; i<=3; i++)); do echo "カウント: $i"; done
カウント: 1
カウント: 2
カウント: 3
```

## 使用例

### ファイルに対する反復処理

```console
$ for file in *.txt; do echo "処理中: $file"; cat "$file"; done
処理中: notes.txt
これはnotes.txtの内容です
処理中: readme.txt
これはreadme.txtの内容です
```

### コマンド出力に対する反復処理

```console
$ for user in $(cut -d: -f1 /etc/passwd | head -3); do echo "ユーザー: $user"; done
ユーザー: root
ユーザー: daemon
ユーザー: bin
```

### 数値範囲に対する反復処理

```console
$ for i in {1..5}; do echo "数字 $i"; done
数字 1
数字 2
数字 3
数字 4
数字 5
```

### ステップ値を使用した反復処理

```console
$ for i in {0..10..2}; do echo "偶数: $i"; done
偶数: 0
偶数: 2
偶数: 4
偶数: 6
偶数: 8
偶数: 10
```

## ヒント:

### 適切な引用符の使用

ループ内の変数は常に引用符で囲み、スペースを含むファイル名や値を正しく処理できるようにしましょう：

```console
$ for file in *.txt; do echo "処理中: '$file'"; done
```

### break と continue

`break` を使用してループを早期に終了し、`continue` を使用して次の反復にスキップできます：

```console
$ for i in {1..10}; do
>   if [ $i -eq 5 ]; then continue; fi
>   if [ $i -eq 8 ]; then break; fi
>   echo $i
> done
1
2
3
4
6
7
```

### ネストしたループ

より複雑な反復処理のために `for` ループをネストできます：

```console
$ for i in {1..3}; do
>   for j in a b c; do
>     echo "$i-$j"
>   done
> done
1-a
1-b
1-c
2-a
2-b
2-c
3-a
3-b
3-c
```

## よくある質問

#### Q1. 数値の範囲を反復処理するにはどうすればよいですか？
A. 波括弧展開を使用します：`for i in {1..10}; do echo $i; done` または C言語スタイル構文：`for ((i=1; i<=10; i++)); do echo $i; done`。

#### Q2. ファイルの各行を処理するにはどうすればよいですか？
A. `for` を使用することもできますが、`while` ループと `read` を使用する方が良いでしょう：`while read line; do echo "$line"; done < file.txt`。

#### Q3. 配列要素を反復処理するにはどうすればよいですか？
A. `for element in "${array[@]}"; do echo "$element"; done` を使用します。

#### Q4. コマンド出力を反復処理するために `for` を使用できますか？
A. はい、コマンド置換を使用します：`for item in $(command); do echo "$item"; done`。

#### Q5. 数値範囲でステップ値を指定するにはどうすればよいですか？
A. 拡張波括弧展開を使用します：`for i in {開始..終了..ステップ}; do echo $i; done`。

## 参考文献

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## 改訂履歴

- 2025/05/04 初版作成