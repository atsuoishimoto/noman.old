# dirname コマンド

パス名からディレクトリ部分を抽出します。

## 概要

`dirname` コマンドは、ファイルパスからディレクトリ部分のみを取り出すためのユーティリティです。ファイルパスの最後のスラッシュ（/）より前の部分を出力します。スクリプト内でファイルのディレクトリパスを取得する際によく使用されます。

## オプション

### **-z, --zero**

出力の区切り文字として改行ではなくNULL文字を使用します。

```console
$ dirname -z /usr/bin/file1 /usr/bin/file2
/usr/bin/usr/bin
```

これは実際には2つのパスが連続して出力されています（NULLバイトで区切られているため表示されません）。

## 使用例

### 基本的な使用方法

```console
$ dirname /usr/bin/bash
/usr/bin
```

### 複数のパスを処理する

```console
$ dirname /usr/bin/bash /etc/passwd /home/user/file.txt
/usr/bin
/etc
/home/user
```

### 相対パスでの使用

```console
$ dirname dir1/dir2/file.txt
dir1/dir2
```

### カレントディレクトリのファイル

```console
$ dirname file.txt
.
```

### スクリプト内での使用例

```console
$ script_dir=$(dirname "$0")
$ echo "このスクリプトは $script_dir ディレクトリにあります"
このスクリプトは . ディレクトリにあります
```

## ヒント:

### スクリプトの場所を特定する

シェルスクリプト内で `dirname "$0"` を使用すると、スクリプト自体が存在するディレクトリを取得できます。これはスクリプトと同じディレクトリにある設定ファイルやリソースにアクセスする際に便利です。

### 絶対パスへの変換

`dirname` と `cd` を組み合わせることで、相対パスを絶対パスに変換できます：

```console
$ cd $(dirname "/relative/path/file") && pwd
```

### パス操作の組み合わせ

`dirname` と `basename` を組み合わせると、パスを効果的に操作できます：

```console
$ path="/usr/local/bin/script.sh"
$ dir=$(dirname "$path")
$ file=$(basename "$path")
$ echo "ディレクトリ: $dir, ファイル: $file"
ディレクトリ: /usr/local/bin, ファイル: script.sh
```

## よくある質問

#### Q1. `dirname` と `basename` の違いは何ですか？
A. `dirname` はパスからディレクトリ部分を抽出し、`basename` はファイル名部分を抽出します。例えば、`/path/to/file.txt` に対して、`dirname` は `/path/to` を返し、`basename` は `file.txt` を返します。

#### Q2. `dirname` はファイルの存在を確認しますか？
A. いいえ、`dirname` は単に文字列操作を行うだけで、実際のファイルシステムにアクセスしません。存在しないパスでも処理できます。

#### Q3. スラッシュだけのパスを処理するとどうなりますか？
A. ルートディレクトリ（`/`）を処理すると、`dirname` は `/` を返します。

#### Q4. 末尾にスラッシュがあるパスはどう処理されますか？
A. 末尾のスラッシュは無視されます。例えば、`/usr/bin/` と `/usr/bin` は同じ結果（`/usr`）になります。

## 参照

https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html

## 改訂履歴

- 2025/04/30 初版作成