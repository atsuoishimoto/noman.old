# cmp コマンド

2つのファイルをバイト単位で比較します。

## 概要

`cmp`コマンドは、任意のタイプの2つのファイルを比較し、最初に見つかった相違点の位置を報告します。テキストファイルのすべての違いを表示する`diff`とは異なり、`cmp`は単にファイルが異なる最初のバイトまたは行を識別するだけなので、バイナリファイルの迅速な比較に役立ちます。

## オプション

### **-b, --print-bytes**

異なるバイトを8進数の値として表示します

```console
$ cmp -b file1.txt file2.txt
file1.txt file2.txt differ: byte 5, line 1 is 141 a 142 b
```

### **-i, --ignore-initial=SKIP**

入力の最初のSKIPバイトをスキップします

```console
$ cmp -i 10 file1.txt file2.txt
file1.txt file2.txt differ: byte 11, line 2
```

### **-l, --verbose**

すべての相違点についてバイト番号と異なるバイト値を出力します

```console
$ cmp -l file1.txt file2.txt
5 141 142
10 156 157
15 163 164
```

### **-n, --bytes=LIMIT**

最大LIMITバイトまで比較します

```console
$ cmp -n 20 file1.txt file2.txt
file1.txt file2.txt differ: byte 5, line 1
```

### **-s, --quiet, --silent**

通常の出力をすべて抑制します（終了ステータスのみを返します）

```console
$ cmp -s file1.txt file2.txt
$ echo $?
1
```

## 使用例

### 基本的な比較

```console
$ cmp file1.txt file2.txt
file1.txt file2.txt differ: byte 5, line 1
```

### バイナリファイルの比較

```console
$ cmp image1.jpg image2.jpg
image1.jpg image2.jpg differ: byte 1024, line 8
```

### スクリプトでの終了ステータスを使用したサイレントモード

```console
$ cmp -s file1.txt file2.txt && echo "ファイルは同一です" || echo "ファイルは異なります"
ファイルは異なります
```

## ヒント:

### 終了ステータスの理解

`cmp`コマンドは、ファイルが同一の場合は終了ステータス0、ファイルが異なる場合は1、エラーが発生した場合は2を返します。これはファイルの同一性をチェックする必要があるシェルスクリプトに最適です。

### ファイルの一部分の比較

`-i`と`-n`を一緒に使用して、ファイルの特定のセクションを比較できます。これは、特定の領域だけを気にする大きなファイルを比較する場合に便利です。

### バイナリとテキストの比較

`diff`はテキストファイルに適していますが、`cmp`はテキストファイルとバイナリファイルの両方に適しています。すべての違いを確認する必要がある場合は、詳細なバイナリ比較に`cmp -l`を使用してください。

## よくある質問

#### Q1. `cmp`と`diff`の違いは何ですか？
A. `cmp`はファイルが異なる最初のバイトのみを報告しますが、`diff`はすべての違いを表示し、テキストファイル用に最適化されています。`cmp`はバイナリファイルにも同様に適しています。

#### Q2. スクリプトで2つのファイルが同一かどうかを確認するにはどうすればよいですか？
A. `cmp -s file1 file2`を使用し、`$?`で終了ステータスを確認します。ステータスが0の場合、ファイルは同一です。

#### Q3. `cmp`はディレクトリを比較できますか？
A. いいえ、`cmp`はファイルのみを比較します。ディレクトリの比較には、代わりに`diff -r`を使用してください。

#### Q4. バイナリファイル間のすべての違いを確認するにはどうすればよいですか？
A. `cmp -l file1 file2`を使用して、ファイルが異なるすべてのバイト位置と値を確認できます。

## 参考資料

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html

## 改訂履歴

- 2025/05/04 初版作成