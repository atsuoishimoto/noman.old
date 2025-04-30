# tar コマンド

ファイルやディレクトリをアーカイブ（まとめて一つのファイルに）したり、圧縮・展開したりします。

## 概要

`tar`（tape archive）コマンドは、複数のファイルやディレクトリを一つのアーカイブファイルにまとめたり、そのアーカイブを展開したりするためのコマンドです。また、gzip、bzip2、xzなどの圧縮形式と組み合わせて使用することもできます。Unixシステムでのファイル配布やバックアップに広く使われています。

## オプション

### **-c (--create)**

新しいアーカイブを作成します。

```console
$ tar -cf archive.tar file1 file2 directory1
# file1、file2、directory1をarchive.tarというアーカイブにまとめる
```

### **-x (--extract)**

アーカイブからファイルを展開します。

```console
$ tar -xf archive.tar
# archive.tarからすべてのファイルを現在のディレクトリに展開する
```

### **-f (--file)**

アーカイブファイル名を指定します。ほとんどの場合、このオプションは必須です。

```console
$ tar -cf backup.tar documents/
# documentsディレクトリをbackup.tarというファイル名でアーカイブする
```

### **-v (--verbose)**

処理中のファイル名を表示します。

```console
$ tar -cvf archive.tar file1 file2
file1
file2
# 処理中のファイル名が表示される
```

### **-z (--gzip)**

gzip形式で圧縮/展開します。拡張子は通常 `.tar.gz` または `.tgz` を使用します。

```console
$ tar -czf archive.tar.gz directory/
# directoryをgzip圧縮してアーカイブする
```

### **-j (--bzip2)**

bzip2形式で圧縮/展開します。拡張子は通常 `.tar.bz2` または `.tbz2` を使用します。

```console
$ tar -cjf archive.tar.bz2 directory/
# directoryをbzip2圧縮してアーカイブする
```

### **-J (--xz)**

xz形式で圧縮/展開します。拡張子は通常 `.tar.xz` を使用します。

```console
$ tar -cJf archive.tar.xz directory/
# directoryをxz圧縮してアーカイブする
```

### **-t (--list)**

アーカイブの内容を一覧表示します。

```console
$ tar -tf archive.tar
file1
file2
directory/
directory/file3
# アーカイブ内のファイル一覧を表示する
```

## 使用例

### 複数のファイルをgzip圧縮してアーカイブする

```console
$ tar -czvf backup.tar.gz documents/ images/ important.txt
documents/
documents/report.pdf
documents/notes.txt
images/
images/photo1.jpg
images/photo2.jpg
important.txt
```

### 特定のディレクトリにアーカイブを展開する

```console
$ tar -xf archive.tar -C /path/to/destination/
# archive.tarを指定したディレクトリに展開する
```

### アーカイブから特定のファイルだけを展開する

```console
$ tar -xf archive.tar file1 directory/file2
# archive.tarからfile1とdirectory/file2だけを展開する
```

### 圧縮アーカイブの内容を確認する

```console
$ tar -tvf archive.tar.gz
-rw-r--r-- user/group 12345 2025-04-01 10:00 file1
drwxr-xr-x user/group     0 2025-04-01 10:01 directory/
-rw-r--r-- user/group  5678 2025-04-01 10:02 directory/file2
# アーカイブ内のファイル一覧と詳細情報を表示する
```

## ヒント:

### オプションの組み合わせ

tarコマンドでは、オプションをまとめて記述できます。例えば、`tar -czvf` は「新しいアーカイブを作成し、gzip圧縮し、処理中のファイル名を表示し、指定したファイル名を使用する」という意味です。

### 圧縮形式の選択

- gzip (-z): 圧縮速度と圧縮率のバランスが良く、最も一般的に使用されます。
- bzip2 (-j): gzipより圧縮率が高いですが、処理時間も長くなります。
- xz (-J): 最も高い圧縮率を提供しますが、圧縮・展開に時間がかかります。

### ファイルパスに注意

展開時、デフォルトでは相対パスが保持されます。絶対パスでアーカイブを作成すると、展開時に元のディレクトリ構造が再現されるため注意が必要です。

### 進捗状況の確認

大きなアーカイブを作成・展開する場合は、`-v`オプションを使用して進捗状況を確認することをお勧めします。

## よくある質問

#### Q1. tarファイルと.tar.gzファイルの違いは何ですか？
A. tarファイル（.tar）は単なるアーカイブで圧縮されていません。.tar.gzファイルはtarアーカイブをgzipで圧縮したものです。圧縮することでファイルサイズが小さくなります。

#### Q2. アーカイブ作成時にファイルを除外するにはどうすればいいですか？
A. `--exclude=パターン`オプションを使用します。例：`tar -czf archive.tar.gz directory/ --exclude="*.log"`

#### Q3. アーカイブを展開せずに中身を確認するには？
A. `tar -tf アーカイブ名`を使用します。詳細情報も見たい場合は`tar -tvf アーカイブ名`を使用します。

#### Q4. 既存のアーカイブにファイルを追加するには？
A. `-r`（または`--append`）オプションを使用します。例：`tar -rf archive.tar newfile.txt`（ただし、圧縮されたアーカイブには直接追加できません）

## macOSでの注意点

macOSに搭載されているtarコマンドはBSD版であり、GNU版と若干の違いがあります。特に、一部のオプションの動作や長いオプション名（--create など）のサポートが異なる場合があります。また、macOSでは`-z`、`-j`、`-J`オプションを使わなくても、ファイル拡張子から自動的に圧縮形式を判断することがあります。

## 参考資料

https://www.gnu.org/software/tar/manual/

## 改訂履歴

- 2025/04/30 初版作成