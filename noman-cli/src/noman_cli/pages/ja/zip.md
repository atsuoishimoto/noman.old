# zip コマンド

ファイルを圧縮して ZIP アーカイブを作成します。

## 概要

`zip` コマンドは、ファイルやディレクトリを圧縮して ZIP 形式のアーカイブを作成するためのツールです。Windows や macOS など、ほとんどのオペレーティングシステムで互換性のある形式であるため、クロスプラットフォームでのファイル共有に適しています。

## オプション

### **-r (再帰的)**

ディレクトリとその中身を再帰的に圧縮します。

```console
$ zip -r archive.zip directory/
  adding: directory/ (stored 0%)
  adding: directory/file1.txt (stored 0%)
  adding: directory/file2.txt (deflated 35%)
  adding: directory/subdirectory/ (stored 0%)
  adding: directory/subdirectory/file3.txt (deflated 42%)
```

### **-e (暗号化)**

パスワード保護された ZIP ファイルを作成します。

```console
$ zip -e secure.zip confidential.txt
Enter password: 
Verify password: 
  adding: confidential.txt (deflated 45%)
```

### **-u (更新)**

既存の ZIP アーカイブを更新し、新しいファイルを追加したり、変更されたファイルを置き換えたりします。

```console
$ zip -u archive.zip newfile.txt
  adding: newfile.txt (deflated 30%)
```

### **-d (削除)**

ZIP アーカイブから特定のファイルを削除します。

```console
$ zip -d archive.zip unwanted.txt
deleting: unwanted.txt
```

### **-j (ジャンク・パス)**

ディレクトリ構造を保存せずにファイルを圧縮します。

```console
$ zip -j flat.zip directory/subdirectory/file.txt
  adding: file.txt (deflated 33%)
```

## 使用例

### 複数のファイルを圧縮する

```console
$ zip documents.zip report.pdf spreadsheet.xlsx presentation.pptx
  adding: report.pdf (deflated 12%)
  adding: spreadsheet.xlsx (deflated 57%)
  adding: presentation.pptx (deflated 62%)
```

### 圧縮レベルを指定する

```console
$ zip -9 highly_compressed.zip largefile.dat
  adding: largefile.dat (deflated 75%)
```

### 除外パターンを使用する

```console
$ zip -r project.zip src/ -x "*.log" "*.tmp" "*/.git/*"
  adding: src/ (stored 0%)
  adding: src/main.c (deflated 45%)
  adding: src/utils.c (deflated 38%)
```

## ヒント:

### 圧縮レベルの調整

`-0`（無圧縮）から`-9`（最大圧縮）までの数字を使って圧縮レベルを指定できます。大きなファイルを素早く圧縮したい場合は低い値を、サイズを最小化したい場合は高い値を使用します。

### 進捗状況の表示

大きなファイルを圧縮する際は `-v` オプションを使用すると詳細な進捗状況が表示されます。

### 自己解凍アーカイブの作成

`-A` オプションを使用すると、Windows で自己解凍可能な実行ファイルを作成できます（ただし追加のツールが必要です）。

## よくある質問

#### Q1. ZIP と TAR の違いは何ですか？
A. ZIP は圧縮とアーカイブを同時に行いますが、TAR はアーカイブのみを作成し、通常は gzip などの別のツールと組み合わせて圧縮します。ZIP は Windows との互換性が高く、個別のファイルを抽出しやすいという利点があります。

#### Q2. ZIP ファイルのパスワードを忘れた場合はどうすればよいですか？
A. ZIP のパスワード保護は比較的弱いため、パスワード解析ツールで復元できる場合がありますが、強力なパスワードを使用していた場合は復元が困難です。重要なデータには強力なパスワードマネージャーの使用をお勧めします。

#### Q3. 大きなファイルを ZIP で圧縮する際の注意点は？
A. 非常に大きなファイル（数GB以上）を圧縮する場合、ZIP には4GBのファイルサイズ制限があるため、代わりに `zip64` 形式をサポートする実装を使用するか、分割アーカイブの作成を検討してください。

#### Q4. macOS で作成した ZIP ファイルに隠しファイルが含まれてしまうのはなぜですか？
A. macOS では `.DS_Store` や `__MACOSX` などのメタデータファイルが自動的に含まれることがあります。これらを除外するには `-X` オプションを使用します。

## macOS での注意点

macOS の Finder から ZIP ファイルを作成すると、`.DS_Store` や `__MACOSX` ディレクトリなどのメタデータファイルが含まれることがあります。コマンドラインで ZIP を作成する際に `-X` オプションを使用すると、これらの macOS 固有のファイルを除外できます。

```console
$ zip -X -r clean_archive.zip directory/
```

## 参考資料

https://linux.die.net/man/1/zip

## 改訂履歴

- 2025/04/30 初版作成