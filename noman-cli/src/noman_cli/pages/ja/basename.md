# basename コマンド

ファイルパスからディレクトリ部分を削除し、ファイル名のみを取得します。

## 概要

`basename` コマンドは、ファイルパスからディレクトリ部分を取り除き、ファイル名だけを表示します。オプションを使用すると、ファイル名から拡張子を削除することもできます。シェルスクリプトでファイル名の処理を行う際によく使用されます。

## オプション

### **-a, --multiple**

複数のパスを一度に処理します。

```console
$ basename -a /usr/bin/zip /usr/bin/gzip
zip
gzip
```

### **-s, --suffix=接尾辞**

指定した接尾辞（拡張子など）をファイル名から削除します。

```console
$ basename -s .txt /home/user/document.txt
document
```

### **-z, --zero**

出力の区切り文字として改行ではなくNULL文字を使用します。

```console
$ basename -z file1.txt file2.txt | hexdump -C
00000000  66 69 6c 65 31 00 66 69  6c 65 32 00              |file1.file2.|
0000000c
```

## 使用例

### 基本的な使用方法

```console
$ basename /usr/local/bin/python3
python3
```

### 拡張子の削除

```console
$ basename /var/log/syslog.1.gz .gz
syslog.1
```

### シェルスクリプトでの使用例

```console
$ filename=$(basename "$filepath")
$ echo "ファイル名は $filename です"
ファイル名は document.txt です
```

## ヒント:

### パスとファイル名の分離

`dirname` コマンドと組み合わせると、パスとファイル名を完全に分離できます。

```console
$ filepath="/home/user/documents/report.pdf"
$ dirname "$filepath"  # パス部分を取得
/home/user/documents
$ basename "$filepath"  # ファイル名部分を取得
report.pdf
```

### 複数の拡張子の処理

複数の拡張子（例：.tar.gz）を持つファイルを処理する場合は、`basename` を複数回使用するか、パターンマッチングを使用します。

```console
$ filename="archive.tar.gz"
$ basename "$filename" .gz | basename -s .tar
archive
```

### 変数展開での代替方法

Bashでは、変数展開を使って同様の処理を行うこともできます。

```console
$ filepath="/home/user/documents/report.pdf"
$ echo "${filepath##*/}"  # basename と同等
report.pdf
```

## よくある質問

#### Q1. `basename` と `dirname` の違いは何ですか？
A. `basename` はパスからファイル名部分を抽出し、`dirname` はディレクトリ部分を抽出します。

#### Q2. 拡張子なしのファイル名を取得するにはどうすればよいですか？
A. `basename filename.ext .ext` のように、第2引数に拡張子を指定します。

#### Q3. シェルスクリプトで `basename` を使わずに同じ結果を得る方法はありますか？
A. Bashでは `${filepath##*/}` のような変数展開パターンを使用できます。

#### Q4. macOSと Linux で `basename` の動作に違いはありますか？
A. 基本的な機能は同じですが、一部のオプション（特に GNU 拡張）は macOS では利用できない場合があります。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/basename-invocation.html

## 改訂履歴

- 2025/04/30 初版作成