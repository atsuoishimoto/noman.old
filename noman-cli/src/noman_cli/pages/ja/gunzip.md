# gunzip コマンド

gzipで圧縮されたファイルを展開します。

## 概要

`gunzip`は、`gzip`プログラムで以前に圧縮されたファイルを展開するユーティリティです。デフォルトでは、元のファイルを復元し、圧縮されたバージョンを削除します。`.gz`、`.z`、`.taz`、`.tgz`、`.tz`などの拡張子を持つファイルに対応しています。

## オプション

### **-c, --stdout, --to-stdout**

出力を標準出力に書き込み、元のファイルを変更せずに保持します。

```console
$ gunzip -c archive.gz > extracted_file
```

### **-f, --force**

ファイルに複数のリンクがある場合や、対応するファイルがすでに存在する場合でも強制的に展開します。

```console
$ gunzip -f already_exists.gz
```

### **-k, --keep**

展開中に入力ファイルを保持（削除しない）します。

```console
$ gunzip -k archive.gz
$ ls
archive  archive.gz
```

### **-l, --list**

展開せずに圧縮ファイルの内容を一覧表示します。

```console
$ gunzip -l archive.gz
         compressed        uncompressed  ratio uncompressed_name
                547                 1213  54.9% archive
```

### **-q, --quiet**

すべての警告を抑制します。

```console
$ gunzip -q archive.gz
```

### **-r, --recursive**

ディレクトリ内のファイルを再帰的に展開します。

```console
$ gunzip -r directory_with_gz_files/
```

### **-t, --test**

展開せずに圧縮ファイルの整合性をテストします。

```console
$ gunzip -t archive.gz
```

### **-v, --verbose**

展開された各ファイルの名前と圧縮率を表示します。

```console
$ gunzip -v archive.gz
archive.gz:	 54.9% -- replaced with archive
```

## 使用例

### 基本的な展開

```console
$ gunzip archive.gz
$ ls
archive
```

### 複数ファイルの展開

```console
$ gunzip file1.gz file2.gz file3.gz
$ ls
file1 file2 file3
```

### 元のファイルを保持しながら展開

```console
$ gunzip -k important_backup.gz
$ ls
important_backup important_backup.gz
```

### アーカイブの整合性テスト

```console
$ gunzip -tv archive.gz
archive.gz: OK
```

## ヒント:

### tarファイルとの使用

`.tar.gz`や`.tgz`ファイルの場合、`gunzip`の後に`tar`を使用できます：

```console
$ gunzip archive.tar.gz
$ tar xf archive.tar
```

あるいは、より効率的に`tar`の`z`オプションを直接使用します：

```console
$ tar xzf archive.tar.gz
```

### 他のコマンドに直接パイプする

`-c`を使用して、中間ファイルを作成せずに展開して別のコマンドにパイプできます：

```console
$ gunzip -c logs.gz | grep "error"
```

### 複数の圧縮形式の処理

圧縮形式が不明な場合は、複数の形式に対応する`zcat`の使用を検討してください：

```console
$ zcat file.gz > uncompressed_file
```

## よくある質問

#### Q1. `gunzip`と`gzip -d`の違いは何ですか？
A. 機能的には同等です。`gunzip`は基本的に`gzip -d`へのシンボリックリンクです。

#### Q2. 元の圧縮ファイルを削除せずにファイルを展開するにはどうすればよいですか？
A. `-k`または`--keep`オプションを使用します：`gunzip -k file.gz`

#### Q3. `gunzip`は複数の圧縮形式を処理できますか？
A. いいえ、`gunzip`は特にgzip圧縮ファイル用です。他の形式には、`bunzip2`（bzip2用）や`unxz`（xz用）などのツールを使用してください。

#### Q4. 展開せずにgzipファイルの内容を確認するにはどうすればよいですか？
A. `gunzip -l file.gz`を使用して、圧縮ファイルに関する情報を一覧表示します。

#### Q5. ファイルを別の名前に展開するにはどうすればよいですか？
A. `-c`オプションを使用して出力をリダイレクトします：`gunzip -c file.gz > newname`

## 参考文献

https://www.gnu.org/software/gzip/manual/gzip.html

## 改訂履歴

- 2025/05/04 初版作成