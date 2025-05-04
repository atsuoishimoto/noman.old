# zip コマンド

ファイルを圧縮アーカイブにパッケージ化します。

## 概要

`zip`コマンドは、1つ以上のファイルやディレクトリを含むZIP形式の圧縮アーカイブを作成します。ファイル圧縮、バックアップ、異なるオペレーティングシステム間でのファイル共有によく使用されます。ZIPは広くサポートされている形式で、ファイル属性やディレクトリ構造を維持します。

## オプション

### **-r, --recurse-paths**

サブディレクトリ内のファイルを再帰的に含めます

```console
$ zip -r archive.zip documents/
  adding: documents/ (stored 0%)
  adding: documents/report.txt (deflated 35%)
  adding: documents/images/ (stored 0%)
  adding: documents/images/photo.jpg (deflated 2%)
```

### **-e, --encrypt**

ZIPアーカイブの内容をパスワードで暗号化します

```console
$ zip -e secure.zip confidential.txt
Enter password: 
Verify password: 
  adding: confidential.txt (deflated 42%)
```

### **-u, --update**

ZIPアーカイブ内の既存エントリを更新し、新しいファイルを追加します

```console
$ zip -u archive.zip newfile.txt updated.txt
  adding: newfile.txt (deflated 30%)
  updating: updated.txt (deflated 25%)
```

### **-d, --delete**

ZIPアーカイブからエントリを削除します

```console
$ zip -d archive.zip unwanted.txt
deleting: unwanted.txt
```

### **-j, --junk-paths**

ディレクトリパスなしでファイル名のみを格納します

```console
$ zip -j flat.zip documents/report.txt documents/images/photo.jpg
  adding: report.txt (deflated 35%)
  adding: photo.jpg (deflated 2%)
```

### **-9, --compress-level**

圧縮レベルを設定します（0-9、9が最大圧縮）

```console
$ zip -9 compressed.zip largefile.dat
  adding: largefile.dat (deflated 68%)
```

## 使用例

### 基本的なZIPアーカイブの作成

```console
$ zip backup.zip file1.txt file2.txt
  adding: file1.txt (deflated 32%)
  adding: file2.txt (deflated 28%)
```

### サブディレクトリを含むディレクトリ全体の圧縮

```console
$ zip -r project.zip project/
  adding: project/ (stored 0%)
  adding: project/src/ (stored 0%)
  adding: project/src/main.c (deflated 45%)
  adding: project/docs/ (stored 0%)
  adding: project/docs/readme.md (deflated 38%)
```

### パスワード保護された最大圧縮のZIPの作成

```console
$ zip -e -9 secure-archive.zip important/*.pdf
Enter password: 
Verify password: 
  adding: important/document1.pdf (deflated 15%)
  adding: important/document2.pdf (deflated 12%)
```

## ヒント:

### 展開せずにZIPの内容を表示する

関連コマンド`unzip -l archive.zip`を使用して、ZIPファイルの内容を展開せずに一覧表示できます。

### 特定のファイルを除外する

`-x`オプションでパターンを使用して特定のファイルを除外できます：`zip -r archive.zip directory/ -x "*.tmp" "*.log"`

### 大きなZIPファイルを分割する

非常に大きなアーカイブの場合、`-s`オプションを使用してZIPを小さな部分に分割できます：`zip -s 100m -r large.zip bigdirectory/`

### 圧縮率の調整

すでに圧縮されているファイル（JPEGなど）には`zip -0`（圧縮なし）を使用し、テキストファイルには`zip -9`（最大圧縮）を使用すると効率的です。

## よくある質問

#### Q1. ZIPファイルを展開するにはどうすればよいですか？
A. 関連コマンド`unzip archive.zip`を使用してZIPアーカイブからファイルを展開できます。

#### Q2. 既存のZIPアーカイブにファイルを追加できますか？
A. はい、`zip -u archive.zip 新しいファイル`を使用して既存のアーカイブにファイルを追加または更新できます。

#### Q3. ファイルを圧縮せずにZIPファイルを作成するにはどうすればよいですか？
A. `zip -0 archive.zip ファイル`を使用して、圧縮なしでファイルを格納できます（JPEGなどの既に圧縮されているファイルに便利です）。

#### Q4. ZIPファイルをパスワード保護するにはどうすればよいですか？
A. `zip -e archive.zip ファイル`を使用して暗号化されたZIPファイルを作成します。パスワードの入力を求められます。

#### Q5. ZIPアーカイブを作成するときにファイルのパーミッションを保持するにはどうすればよいですか？
A. Unixライクなシステムでは、`zip -X archive.zip ファイル`を使用してファイルのパーミッションとUID/GID情報を保持できます。

## macOSに関する注意点

macOSでは、組み込みのArchive Utilityが作成するZIPファイルは、特定のUnixファイル属性を保持しない場合があります。より詳細な制御が必要な場合は、コマンドラインの`zip`ユーティリティを使用してください。また、macOSはディレクトリ内に隠しファイル`.DS_Store`を作成することがあり、`-x "*.DS_Store"`で明示的に除外しない限り、ZIPアーカイブに含まれることに注意してください。

## 参考資料

https://linux.die.net/man/1/zip

## 改訂履歴

- 2025/05/04 初回改訂