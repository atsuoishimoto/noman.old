# tar

`tar` コマンドは、複数のファイルやディレクトリをアーカイブ（単一のファイル）にまとめたり、圧縮・展開したりするためのユーティリティです。名前は "tape archive" に由来しています。

## オプション

### **-c (--create)**

新しいアーカイブを作成します。

```bash
$ tar -cf archive.tar file1 file2 directory1
```

### **-x (--extract)**

アーカイブからファイルを展開します。

```bash
$ tar -xf archive.tar
```

### **-f (--file)**

アーカイブファイル名を指定します。ほとんどの場合必須です。

```bash
$ tar -cf archive.tar files/
```

### **-v (--verbose)**

処理中のファイル名を表示します。進捗状況を確認したい場合に便利です。

```bash
$ tar -cvf archive.tar files/
files/
files/document1.txt
files/document2.txt
files/images/
files/images/photo.jpg
```

### **-z (--gzip)**

gzip圧縮を使用します。`.tar.gz`または`.tgz`拡張子のファイルを作成・展開します。

```bash
$ tar -czf archive.tar.gz files/
```

### **-j (--bzip2)**

bzip2圧縮を使用します。`.tar.bz2`拡張子のファイルを作成・展開します。

```bash
$ tar -cjf archive.tar.bz2 files/
```

### **-t (--list)**

アーカイブの内容を表示します。

```bash
$ tar -tf archive.tar
files/
files/document1.txt
files/document2.txt
files/images/
files/images/photo.jpg
```

### **-C (--directory)**

指定したディレクトリに移動してから操作を行います。

```bash
$ tar -xf archive.tar -C /path/to/extract/
```

## 使用例

### 基本的なアーカイブ作成

```bash
$ tar -cf backup.tar ~/Documents
```
複数のファイルとディレクトリを backup.tar というアーカイブにまとめている。

### 圧縮アーカイブの作成（gzip）

```bash
$ tar -czf backup.tar.gz ~/Documents ~/Pictures
```
Documentsディレクトリと Picturesディレクトリをgzip圧縮したアーカイブにまとめている。

### アーカイブの内容確認

```bash
$ tar -tvf backup.tar
-rw-r--r-- user/group 12345 2023-04-10 10:30 Documents/report.docx
drwxr-xr-x user/group     0 2023-04-09 15:45 Documents/project/
-rw-r--r-- user/group  5678 2023-04-08 09:15 Documents/project/notes.txt
```
アーカイブ内のファイル一覧と詳細情報を表示している。

### アーカイブの展開

```bash
$ tar -xf backup.tar
```
カレントディレクトリにアーカイブの内容を展開する。

### 特定のファイルのみ展開

```bash
$ tar -xf backup.tar Documents/report.docx
```
アーカイブから特定のファイルのみを展開している。

## よくある質問

### Q1. tarファイルと.tar.gzファイルの違いは何ですか？
A. tarファイル（.tar）は単純にファイルをまとめただけのアーカイブで、圧縮はされていません。.tar.gzファイルはtarアーカイブをgzipで圧縮したもので、サイズが小さくなります。

### Q2. 既存のアーカイブにファイルを追加するにはどうすればいいですか？
A. `-r`（または`--append`）オプションを使用します：`tar -rf archive.tar newfile`

### Q3. アーカイブを展開せずに中身を確認するには？
A. `-t`（または`--list`）オプションを使用します：`tar -tf archive.tar`

### Q4. 特定のファイルやディレクトリを除外してアーカイブするには？
A. `--exclude`オプションを使用します：`tar -cf archive.tar directory/ --exclude='*.log'`

## 追加情報

- オプションの前のハイフン（`-`）は省略可能です（例：`tar cf archive.tar files/`）。
- macOSでは基本的な機能は同じですが、一部のGNU tarの拡張オプションが使えない場合があります。
- 大きなディレクトリをアーカイブする場合は、`-v`オプションを使うと処理状況が確認できて便利です。
- 圧縮率を高めたい場合は、gzip（`-z`）よりもbzip2（`-j`）の方が効果的ですが、処理時間は長くなります。
- 最近のバージョンでは、`.tar.xz`形式の圧縮に対応する`-J`オプションも利用可能です。

## 参考情報

https://www.gnu.org/software/tar/manual/