# gzip コマンド

ファイルを圧縮・展開するためのコマンドラインユーティリティです。

## 概要

gzipはファイルを圧縮または展開するためのコマンドです。圧縮されたファイルは元のファイル名に「.gz」拡張子が追加されます。デフォルトでは、圧縮後に元のファイルは削除されます。gzipは主にテキストファイルの圧縮に効果的で、多くのUNIXシステムで標準的に利用されています。

## オプション

### **-d (--decompress)**

圧縮ファイルを展開します。

```console
$ gzip -d file.gz
# file.gzが展開されてfileが作成される
```

### **-k (--keep)**

圧縮・展開時に元のファイルを保持します。

```console
$ gzip -k file.txt
# file.txtが保持されたままfile.txt.gzが作成される
```

### **-c (--stdout)**

圧縮・展開結果を標準出力に出力します。元のファイルは変更されません。

```console
$ gzip -c file.txt > file.txt.gz
# 標準出力に圧縮結果を出力し、リダイレクトでファイルに保存
```

### **-r (--recursive)**

ディレクトリを再帰的に処理します。

```console
$ gzip -r directory/
# directory内のすべてのファイルを圧縮
```

### **-[1-9] (圧縮レベル)**

圧縮レベルを1（最速、圧縮率低）から9（最も遅い、圧縮率高）まで指定します。デフォルトは6です。

```console
$ gzip -9 file.txt
# 最高圧縮率でfile.txtを圧縮
```

## 使用例

### 基本的な圧縮

```console
$ gzip large_file.txt
$ ls
large_file.txt.gz
```

### 複数ファイルの圧縮

```console
$ gzip file1.txt file2.txt file3.txt
$ ls
file1.txt.gz file2.txt.gz file3.txt.gz
```

### 圧縮ファイルの展開

```console
$ gzip -d archive.gz
$ ls
archive
```

### 標準入出力を使った圧縮

```console
$ cat file.txt | gzip > file.txt.gz
# file.txtの内容を圧縮してfile.txt.gzに保存
```

## ヒント:

### パイプラインでの利用

gzipは標準入出力と連携できるため、パイプラインでの処理に適しています。

```console
$ tar cf - directory | gzip > directory.tar.gz
# ディレクトリをtarでアーカイブし、gzipで圧縮
```

### 圧縮率と速度のバランス

大きなファイルを扱う場合、`-1`（高速・低圧縮）から`-9`（低速・高圧縮）までのオプションを状況に応じて選択しましょう。

### ファイルの中身を確認

圧縮ファイルを展開せずに中身を確認するには、`zcat`、`zless`、`zgrep`などの関連コマンドが便利です。

```console
$ zcat file.gz
# 圧縮ファイルの内容を表示
```

## よくある質問

#### Q1. gzipで圧縮したファイルを展開するには？
A. `gzip -d ファイル名.gz` または `gunzip ファイル名.gz` を使用します。

#### Q2. 元のファイルを残したまま圧縮するには？
A. `gzip -k ファイル名` を使用します。

#### Q3. 複数のファイルを一つのgzipファイルにまとめるには？
A. gzip単体ではできません。通常は`tar`と組み合わせて使用します：`tar czf アーカイブ名.tar.gz ファイル名...`

#### Q4. 圧縮ファイルの内容を確認するには？
A. `zcat`、`zless`、`zgrep`などのコマンドを使用します。

## 参考資料

https://www.gnu.org/software/gzip/manual/gzip.html

## Revisions

- 2025/04/30 First revision