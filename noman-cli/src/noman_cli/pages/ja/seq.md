# seq コマンド

指定された範囲の数値を順番に出力します。

## 概要

`seq` コマンドは、指定された開始値から終了値までの連続した数値を生成します。デフォルトでは1から始まり、1ずつ増加して指定された数値まで出力します。ステップ値（増分）を変更することも可能です。シェルスクリプトでループ処理を行う際や、連番ファイルを作成する場合などに便利です。

## オプション

### **-s, --separator=STRING**

数値の間に挿入する区切り文字を指定します（デフォルトは改行）。

```console
$ seq -s " " 5
1 2 3 4 5
```

### **-f, --format=FORMAT**

出力形式を printf スタイルで指定します。

```console
$ seq -f "Number %g" 3
Number 1
Number 2
Number 3
```

### **-w, --equal-width**

ゼロパディングを行い、すべての数値を同じ幅で出力します。

```console
$ seq -w 8 10
08
09
10
```

## 使用例

### 基本的な使用方法

```console
$ seq 5
1
2
3
4
5
```

### 開始値と終了値を指定

```console
$ seq 3 7
3
4
5
6
7
```

### 開始値、ステップ値、終了値を指定

```console
$ seq 1 2 10
1
3
5
7
9
```

### シェルのforループで使用

```console
$ for i in $(seq 1 3); do echo "Processing item $i"; done
Processing item 1
Processing item 2
Processing item 3
```

## ヒント:

### 逆順に数値を生成

負のステップ値を使用して、大きい数から小さい数へ逆順に生成できます。

```console
$ seq 5 -1 1
5
4
3
2
1
```

### ゼロパディング

桁数を揃えたい場合は `-w` オプションを使用します。これはファイル名の連番などで役立ちます。

```console
$ seq -w 1 10 > files.txt
$ cat files.txt
01
02
...
10
```

### 小数点の使用

`seq` は小数点を含む数値も扱えます。

```console
$ seq 0.5 0.5 2.5
0.5
1.0
1.5
2.0
2.5
```

## よくある質問

#### Q1. `seq` コマンドの代替方法はありますか？
A. Bashでは `{start..end..step}` という記法も使えます。例: `echo {1..5}` または `echo {1..10..2}`

#### Q2. 大量の数値を生成する場合のパフォーマンスは？
A. 非常に大きな範囲の数値を生成する場合、メモリ使用量に注意が必要です。パイプを使って処理することをお勧めします。

#### Q3. macOSでの `seq` コマンドの違いはありますか？
A. macOSのデフォルトの `seq` はGNU版と若干異なる場合があります。Homebrewで `coreutils` をインストールすると、GNU版の `gseq` が使用できます。

#### Q4. 出力をファイルに保存するには？
A. リダイレクトを使用します: `seq 1 100 > numbers.txt`

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/seq-invocation.html

## 改訂履歴

- 2025/04/30 初版作成