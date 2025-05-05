# expr コマンド

式を評価し、結果を出力します。

## 概要

`expr` は式を評価して結果を出力するコマンドラインユーティリティです。算術演算、文字列操作、論理比較を実行できます。このコマンドは主にシェルスクリプト内で、シェル組み込みコマンドだけでは難しい計算や文字列操作を行うために使用されます。

## オプション

### **--help**

ヘルプメッセージを表示して終了します。

```console
$ expr --help
Usage: expr EXPRESSION
  or:  expr OPTION
Print the value of EXPRESSION to standard output.
...
```

### **--version**

バージョン情報を出力して終了します。

```console
$ expr --version
expr (GNU coreutils) 9.0
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
```

## 使用例

### 基本的な算術演算

```console
$ expr 5 + 3
8
$ expr 10 - 4
6
$ expr 3 \* 4
12
$ expr 20 / 5
4
$ expr 20 % 3
2
```

### 文字列操作

```console
$ expr length "Hello World"
11
$ expr substr "Hello World" 7 5
World
$ expr index "Hello World" "W"
7
```

### 論理比較

```console
$ expr 5 \> 3
1
$ expr 5 \< 3
0
$ expr 5 = 5
1
$ expr 5 != 5
0
```

### シェルスクリプトでの使用

```console
$ a=5
$ b=3
$ c=$(expr $a + $b)
$ echo $c
8
```

## ヒント:

### 特殊文字のエスケープ

乗算（*）、除算（/）など、シェルで特別な意味を持つ文字はバックスラッシュ（\）でエスケープする必要があります。

```console
$ expr 5 \* 3
15
```

### スペースの要件

`expr` は演算子とオペランドの間にスペースが必要です。スペースがないと、コマンドは正しく動作しません。

```console
$ expr 5+3    # 間違い
5+3
$ expr 5 + 3  # 正しい
8
```

### 戻り値

`expr` は式が0以外かつ空でない値に評価される場合は0を、式が0または空の場合は1を、式が無効な場合は2を返します。

### 変数のインクリメントに使用

`expr` の一般的な使用法はシェルスクリプトでカウンターをインクリメントすることです：

```console
$ i=1
$ i=$(expr $i + 1)
$ echo $i
2
```

## よくある質問

#### Q1. `expr` とシェルの算術演算の違いは何ですか？
A. 現代のシェルは `$(( ))` で算術演算をサポートしていますが、`expr` は異なるシェル間でより移植性が高く、追加の文字列操作関数を提供します。

#### Q2. なぜ `expr` での乗算が失敗するのですか？
A. アスタリスクをバックスラッシュでエスケープする必要があります：`expr 5 \* 3`。そうしないと、シェルはワイルドカードとして解釈します。

#### Q3. 文字列操作に `expr` をどのように使用できますか？
A. `expr` は文字列操作のために `length`、`substr`、`index` などの関数を提供しています。例えば：`expr length "string"` や `expr substr "string" 1 3` などです。

#### Q4. 現代のシェルスクリプティングでも `expr` は関連性がありますか？
A. 新しいシェルには組み込みの算術機能がありますが、`expr` は文字列操作関数や、異なるシェル環境間で移植性が必要なスクリプトに引き続き有用です。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/expr-invocation.html

## 改訂履歴

- 2025/05/04 初版作成