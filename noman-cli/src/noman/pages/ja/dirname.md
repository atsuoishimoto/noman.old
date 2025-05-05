# dirname コマンド

パス名からディレクトリ部分を出力します。

## 概要

`dirname` コマンドはパス名から最後のコンポーネント（ファイル名部分）を削除し、ディレクトリパスのみを残します。シェルスクリプトでファイルパスからディレクトリ部分を抽出するために一般的に使用され、ファイルの場所に移動したり、同じディレクトリ内のファイルを処理したりする際に役立ちます。

## オプション

### **-z, --zero**

各パス名の後に改行ではなくゼロバイト（ASCII NUL）を出力します。

```console
$ dirname -z /usr/bin/zip
/usr/bin$
```

注意: 出力は `$` プロンプトで終わるように見えますが、実際には改行の代わりにヌル文字が含まれています。

### **--help**

ヘルプメッセージを表示して終了します。

```console
$ dirname --help
Usage: dirname [OPTION] NAME...
Output each NAME with its last non-slash component and trailing slashes
removed; if NAME contains no /'s, output '.' (meaning the current directory).

  -z, --zero     end each output line with NUL, not newline
      --help     display this help and exit
      --version  output version information and exit

Examples:
  dirname /usr/bin/          -> "/usr"
  dirname dir1/str dir2/str  -> "dir1" followed by "dir2"
  dirname stdio.h            -> "."
```

### **--version**

バージョン情報を出力して終了します。

```console
$ dirname --version
dirname (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by David MacKenzie.
```

## 使用例

### 基本的な使い方

```console
$ dirname /usr/bin/zip
/usr/bin
```

### 複数の引数

```console
$ dirname /usr/bin/zip /etc/passwd /home/user/file.txt
/usr/bin
/etc
/home/user
```

### カレントディレクトリ

```console
$ dirname file.txt
.
```

### シェルスクリプトでの使用

```console
$ script_dir=$(dirname "$0")
$ echo "このスクリプトの場所: $script_dir"
このスクリプトの場所: .
```

## ヒント:

### basename と組み合わせる

`dirname` と `basename` を一緒に使用して、パスをディレクトリとファイル名のコンポーネントに分割できます：

```console
$ path="/home/user/documents/report.pdf"
$ dir=$(dirname "$path")
$ file=$(basename "$path")
$ echo "ディレクトリ: $dir, ファイル: $file"
ディレクトリ: /home/user/documents, ファイル: report.pdf
```

### 変数は常に引用符で囲む

スクリプトで変数と共に `dirname` を使用する場合、スペースを含むパスを正しく処理するために、常に変数を引用符で囲みましょう：

```console
$ path="/home/user/my documents/report.pdf"
$ dirname "$path"  # 正しい方法
/home/user/my documents
```

### コマンド置換での使用

`dirname` の出力をコマンド置換で取得して、ファイルのディレクトリに移動できます：

```console
$ cd "$(dirname "/path/to/file.txt")"
```

## よくある質問

#### Q1. パスなしのファイル名を渡すと `dirname` は何を返しますか？
A. `.`（カレントディレクトリ）を返します。

#### Q2. `dirname` は一度に複数のパスを処理できますか？
A. はい、複数の引数を渡すことができ、それぞれを個別に処理します。

#### Q3. `dirname` は末尾のスラッシュをどのように処理しますか？
A. 処理前に末尾のスラッシュを削除するので、`/usr/bin/` は `/usr` になります。

#### Q4. `dirname` と `basedir` の違いは何ですか？
A. 標準的なUnixコマンドとして `basedir` は存在しません。おそらく `basename` のことを指していると思われます。`basename` はパスからファイル名部分を抽出し、`dirname` はディレクトリ部分を抽出します。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html

## 改訂履歴

- 2025/05/04 初版作成