# gzip コマンド

ファイルをLempel-Ziv符号化（LZ77）を使用して圧縮または展開します。

## 概要

`gzip`はLempel-Ziv圧縮を使用してファイルサイズを縮小します。デフォルトでは、元のファイルを`.gz`拡張子を持つ圧縮バージョンに置き換え、元のファイルの所有権、権限、タイムスタンプを保持します。単一ファイルの圧縮やパイプライン操作の一部としてデータストリームを圧縮するために一般的に使用されます。

## オプション

### **-d, --decompress, --uncompress**

ファイルを圧縮する代わりに展開します。

```console
$ gzip -d file.gz
```

### **-c, --stdout, --to-stdout**

出力を標準出力に書き込み、元のファイルを変更せずに保持します。

```console
$ gzip -c file.txt > file.txt.gz
```

### **-f, --force**

ファイルに複数のリンクがある場合や、対応するファイルが既に存在する場合でも、強制的に圧縮または展開します。

```console
$ gzip -f already_compressed.gz
```

### **-k, --keep**

圧縮または展開中に入力ファイルを保持します（削除しません）。

```console
$ gzip -k important_file.txt
```

### **-l, --list**

圧縮されたファイルごとに圧縮サイズ、非圧縮サイズ、圧縮率、ファイル名を一覧表示します。

```console
$ gzip -l *.gz
         compressed        uncompressed  ratio uncompressed_name
                 220                 631  65.1% file1.txt
                 143                 341  58.1% file2.txt
```

### **-r, --recursive**

ディレクトリ内のファイルを再帰的に圧縮します。

```console
$ gzip -r directory/
```

### **-v, --verbose**

圧縮または展開された各ファイルの名前と削減率を表示します。

```console
$ gzip -v file.txt
file.txt:       63.4% -- replaced with file.txt.gz
```

### **-[1-9], --fast, --best**

指定された数字を使用して圧縮速度を調整します。-1（または--fast）は最速の圧縮方法（圧縮率は低い）を示し、-9（または--best）は最も遅い（最高の圧縮率）を示します。デフォルトの圧縮レベルは-6です。

```console
$ gzip -9 large_file.txt
```

## 使用例

### 基本的な圧縮

```console
$ gzip document.txt
$ ls
document.txt.gz
```

### 複数ファイルの圧縮

```console
$ gzip file1.txt file2.txt file3.txt
$ ls
file1.txt.gz file2.txt.gz file3.txt.gz
```

### 元ファイルを保持しながらの圧縮

```console
$ gzip -k important_data.txt
$ ls
important_data.txt important_data.txt.gz
```

### 展開せずに圧縮ファイルの内容を表示

```console
$ gzip -c file.txt > file.txt.gz
$ zcat file.txt.gz
[file.txtの内容が表示される]
```

### 標準入力の圧縮

```console
$ cat file.txt | gzip > file.txt.gz
```

## ヒント:

### tarとの組み合わせでディレクトリを圧縮

`gzip`は単一ファイルを圧縮しますが、ディレクトリ全体を圧縮するには`tar`と組み合わせて使用します：

```console
$ tar -czf archive.tar.gz directory/
```

### 圧縮率の確認

`-l`オプションを使用して、ファイルがどの程度圧縮されているかを確認してから、保持するかどうかを決定できます：

```console
$ gzip -l *.gz
```

### スクリプトでのgzipパイプの使用

スクリプトやデータ処理での一時的な圧縮には、パイプを使用します：

```console
$ cat large_file | gzip | ssh remote_server "gunzip > large_file"
```

### 最適な圧縮レベル

ほとんどのファイルでは、デフォルトの圧縮レベル（-6）が速度と圧縮率のバランスが良いです。ファイルサイズが重要で処理時間が問題にならない場合にのみ-9を使用してください。

## よくある質問

#### Q1. .gzファイルを展開するにはどうすればよいですか？
A. `gzip -d filename.gz`または同等のコマンド`gunzip filename.gz`を使用します。

#### Q2. gzipはディレクトリを圧縮できますか？
A. いいえ、`gzip`は個々のファイルのみを圧縮します。ディレクトリを圧縮するには、まず`tar`を使用してアーカイブを作成し、その後`gzip`で圧縮するか（または`tar`の`-z`オプションを使用する）必要があります。

#### Q3. 展開せずに.gzファイルの内容を表示するにはどうすればよいですか？
A. 圧縮ファイルの表示用に特別に設計された`zcat`、`zless`、または`zmore`コマンドを使用します。

#### Q4. gzipは圧縮後に元のファイルを削除しますか？
A. はい、デフォルトでは`gzip`は元のファイルを圧縮バージョンに置き換えます。元のファイルを保持するには`-k`オプションを使用してください。

#### Q5. 圧縮レベルを比較するにはどうすればよいですか？
A. 異なる数字で`gzip -[1-9] -c file > file.gz`を使用し、`ls -l`で結果のファイルサイズを確認します。

## References

https://www.gnu.org/software/gzip/manual/gzip.html

## Revisions

- 2025/05/04 First revision