# zipコマンド

zipコマンドは、ファイルを圧縮して.zipアーカイブを作成するためのUnixコマンドです。複数のファイルやディレクトリを一つのアーカイブにまとめて、サイズを小さくすることができます。

## オプション

### **-r**（再帰的圧縮）
ディレクトリを再帰的に圧縮します。ディレクトリ内のすべてのファイルとサブディレクトリを含めます。

```console
$ zip -r archive.zip Documents/
  adding: Documents/ (stored 0%)
  adding: Documents/report.pdf (deflated 15%)
  adding: Documents/images/ (stored 0%)
  adding: Documents/images/photo.jpg (stored 0%)
```

### **-e**（暗号化）
パスワード保護されたアーカイブを作成します。

```console
$ zip -e secure.zip confidential.pdf
Enter password: 
Verify password: 
  adding: confidential.pdf (deflated 12%)
```

### **-u**（更新）
アーカイブを更新します。新しいファイルを追加したり、変更されたファイルを更新したりします。

```console
$ zip -u archive.zip newfile.txt updatedfile.txt
  adding: newfile.txt (stored 0%)
  updating: updatedfile.txt (deflated 32%)
```

### **-d**（削除）
アーカイブから指定したファイルを削除します。

```console
$ zip -d archive.zip oldfile.txt
deleting: oldfile.txt
```

### **-j**（junkパス）
ディレクトリ構造を保存せず、ファイル名のみを使用します。

```console
$ zip -j flat.zip Documents/file1.txt Projects/file2.txt
  adding: file1.txt (deflated 10%)
  adding: file2.txt (deflated 15%)
```

### **-q**（静かモード）
処理中のメッセージを表示しません。

```console
$ zip -q archive.zip file1 file2
```

## 使用例

### 基本的な使用方法

```console
$ zip archive.zip file1.txt file2.txt file3.txt
  adding: file1.txt (stored 0%)
  adding: file2.txt (stored 0%)
  adding: file3.txt (deflated 45%)
```

### 複数のディレクトリを一つのアーカイブに圧縮

```console
$ zip -r backup.zip Documents/ Pictures/ important.txt
  adding: Documents/ (stored 0%)
  adding: Documents/report.doc (deflated 67%)
  adding: Pictures/ (stored 0%)
  adding: Pictures/vacation.jpg (stored 0%)
  adding: important.txt (deflated 42%)
```

### 圧縮レベルの指定

```console
$ zip -9 highly-compressed.zip largefile.dat
  adding: largefile.dat (deflated 75%)
```

## よくある質問

#### Q1. zipとgzipの違いは何ですか？
A. zipは複数ファイルを一つのアーカイブにまとめて圧縮できますが、gzipは単一ファイルのみを圧縮します。zipはWindowsとの互換性が高いという利点があります。

#### Q2. zipアーカイブのパスワードはどれくらい安全ですか？
A. zipの標準暗号化は比較的弱いです。重要なデータには、gpgなどのより強力な暗号化ツールの使用を検討してください。

#### Q3. 既存のzipアーカイブにファイルを追加するにはどうすればよいですか？
A. `-u`オプションを使用して、`zip -u archive.zip newfile.txt`のように実行します。

#### Q4. 大きなディレクトリを圧縮する際のベストプラクティスは？
A. `-r`オプションを使用し、必要に応じて`-9`（最高圧縮率）や`-q`（静かモード）を組み合わせます。例：`zip -r9q archive.zip large_directory/`

## 追加メモ

* Windowsとの互換性が高く、クロスプラットフォームでファイル共有する際に便利です。
* 大量のファイルを圧縮する場合は、`-9`オプションで最高圧縮率を指定できますが、処理時間が長くなります。
* macOSでは日本語ファイル名を含むアーカイブを作成する場合、文字化けを防ぐために適切な文字エンコーディングを指定することが重要な場合があります。
* macOSでは標準でzipコマンドが利用可能ですが、より多くの機能が必要な場合はHomebrewなどでInfo-ZIPバージョンをインストールすることができます。

## 参考

https://linux.die.net/man/1/zip