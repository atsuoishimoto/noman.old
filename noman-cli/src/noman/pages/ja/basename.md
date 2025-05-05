# basename コマンド

パス名からファイル名やディレクトリ名を抽出します。

## 概要

`basename` コマンドは、指定されたパスからディレクトリ部分や指定された接尾辞を取り除き、ファイル名や最終的なディレクトリ名だけを残します。シェルスクリプトでフルパスからファイル名を抽出したり、ファイル拡張子を削除したりする際によく使用されます。

## オプション

### **-a, --multiple**

複数の引数を処理し、それぞれを NAME として扱います。

```console
$ basename -a /usr/bin/sort /usr/bin/cut
sort
cut
```

### **-s, --suffix=SUFFIX**

各 NAME から末尾の SUFFIX を削除します。

```console
$ basename -s .txt file.txt
file
```

### **-z, --zero**

各出力行を改行ではなく NUL で終了します。

```console
$ basename -z file.txt | hexdump -C
00000000  66 69 6c 65 2e 74 78 74  00                       |file.txt.|
00000009
```

## 使用例

### 基本的なファイル名抽出

```console
$ basename /usr/local/bin/example.sh
example.sh
```

### ファイル拡張子の削除

```console
$ basename /home/user/documents/report.pdf .pdf
report
```

### シェルスクリプトでの使用

```console
$ filename=$(basename "$path")
$ echo "The filename is: $filename"
The filename is: example.txt
```

### 複数のパスの処理

```console
$ basename -a /var/log/syslog /etc/passwd /usr/bin/bash
syslog
passwd
bash
```

## ヒント:

### dirname と組み合わせる

`basename` を `dirname` と組み合わせてパスをコンポーネントに分割できます：

```console
$ path="/home/user/documents/report.pdf"
$ dir=$(dirname "$path")
$ file=$(basename "$path")
$ echo "Directory: $dir, File: $file"
Directory: /home/user/documents, File: report.pdf
```

### 引数を引用符で囲む

スペースや特殊文字を含むファイル名を扱う場合は、常に引数を引用符で囲みましょう：

```console
$ basename "/path/to/my file.txt"
my file.txt
```

### パラメータ展開の使用

Bashでは、`basename` の代わりにパラメータ展開を使用できることがあります：

```console
$ path="/home/user/documents/report.pdf"
$ echo "${path##*/}"
report.pdf
```

## よくある質問

#### Q1. `basename` と `dirname` の違いは何ですか？
A. `basename` はパスから最後のコンポーネント（ファイル名またはディレクトリ名）を抽出し、`dirname` はパスからディレクトリ部分を抽出します。

#### Q2. 複数の拡張子（.tar.gz など）を削除するにはどうすればよいですか？
A. `basename` は一度に1つの接尾辞しか削除できません。複数の拡張子の場合は、複数回使用するかシェルのパラメータ展開を使用する必要があります。

#### Q3. `basename` は相対パスでも動作しますか？
A. はい、絶対パスと相対パスの両方で動作し、常に最後のコンポーネントを返します。

#### Q4. `basename` はスペースを含むパスを処理できますか？
A. はい、できますが、シェルがスペースを引数の区切り文字として解釈しないように、引数を引用符で囲む必要があります。

## 参照

https://www.gnu.org/software/coreutils/manual/html_node/basename-invocation.html

## 改訂履歴

- 2025/05/04 初回改訂