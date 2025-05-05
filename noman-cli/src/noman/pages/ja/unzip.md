# unzip コマンド

ZIPアーカイブからファイルを展開します。

## 概要

`unzip`コマンドはZIPアーカイブからファイルを展開するツールです。様々な圧縮方式に対応し、パスワード保護されたアーカイブの処理、アーカイブの内容表示（展開なし）、特定ファイルの選択的展開などが可能です。Unix系システムでZIPファイルを扱う標準的なツールとして広く使われています。

## オプション

### **-l (--list)**

ZIPアーカイブの内容を展開せずに一覧表示します

```console
$ unzip -l archive.zip
Archive:  archive.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
     1234  2025-01-01 12:34   file1.txt
      567  2025-01-02 15:45   file2.txt
---------                     -------
     1801                     2 files
```

### **-t (--test)**

ZIPアーカイブの整合性を展開せずにテストします

```console
$ unzip -t archive.zip
Archive:  archive.zip
    testing: file1.txt               OK
    testing: file2.txt               OK
No errors detected in compressed data of archive.zip.
```

### **-o (--overwrite)**

確認なしに既存のファイルを上書きします

```console
$ unzip -o archive.zip
Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
```

### **-n (--never-overwrite)**

既存のファイルを上書きしません（既に存在するファイルの展開をスキップします）

```console
$ unzip -n archive.zip
Archive:  archive.zip
 extracting: file1.txt
 extracting: file2.txt
```

### **-d (--directory)**

指定したディレクトリにファイルを展開します

```console
$ unzip archive.zip -d extracted_files/
Archive:  archive.zip
   creating: extracted_files/
  inflating: extracted_files/file1.txt
  inflating: extracted_files/file2.txt
```

### **-P (--password)**

暗号化されたアーカイブのパスワードを指定します

```console
$ unzip -P mypassword protected.zip
Archive:  protected.zip
  inflating: secret.txt
```

### **-j (--junk-paths)**

ディレクトリ構造を作成せずにファイルを展開します（パスを無視します）

```console
$ unzip -j archive.zip
Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
```

## 使用例

### アーカイブから特定のファイルを展開する

```console
$ unzip archive.zip file1.txt
Archive:  archive.zip
  inflating: file1.txt
```

### ワイルドカードパターンを使ってファイルを展開する

```console
$ unzip archive.zip "*.txt"
Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
```

### 詳細な出力で展開する

```console
$ unzip -v archive.zip
Archive:  archive.zip
 Length   Method    Size  Cmpr    Date    Time   CRC-32   Name
--------  ------  ------- ---- ---------- ----- --------  ----
    1234  Defl:N      567  54% 2025-01-01 12:34 a1b2c3d4  file1.txt
     567  Defl:N      234  59% 2025-01-02 15:45 e5f6g7h8  file2.txt
--------          -------  ---                            -------
    1801              801  56%                            2 files
```

## ヒント:

### 展開前にアーカイブの内容をプレビューする

展開前に必ず`unzip -l archive.zip`を使用して内容を確認しましょう。これにより、既存のファイルを誤って上書きしてしまう可能性を避けることができます。

### パストラバーサルを安全に処理する

信頼できないソースからのアーカイブには注意が必要です。一部のZIPファイルには「../」パスを含むエントリが含まれており、展開ディレクトリ外のファイルを上書きする可能性があります。`-d`オプションを使用して専用の展開ディレクトリを指定することをお勧めします。

### 一時ディレクトリへの展開

不慣れなアーカイブを扱う場合は、まず`unzip archive.zip -d temp/`を使用して一時ディレクトリに展開し、最終的な場所に移動する前に内容を確認しましょう。

### 大きなアーカイブの処理

大きなアーカイブの場合は、`unzip -q`（静かモード）を使用して出力を減らし展開を高速化するか、以前の展開を再開する場合は`unzip -n`を使用して既存のファイルを上書きしないようにしましょう。

## よくある質問

#### Q1. パスワード保護されたZIPファイルを展開するにはどうすればよいですか？
A. `unzip -P パスワード archive.zip`を使用します。コマンド履歴にパスワードを残したくない場合は、-Pオプションを省略すると、unzipがパスワードの入力を求めます。

#### Q2. ZIPアーカイブから特定のファイルだけを展開するにはどうすればよいですか？
A. `unzip archive.zip ファイル名1 ファイル名2`のように指定したファイルのみを展開できます。`unzip archive.zip "*.txt"`のようにワイルドカードも使用できます。

#### Q3. ディレクトリ構造を作成せずにZIPファイルを展開するにはどうすればよいですか？
A. `unzip -j archive.zip`を使用すると、サブディレクトリを作成せずに現在のディレクトリにすべてのファイルを展開します。

#### Q4. ZIPファイルを展開せずに有効かどうかを確認するにはどうすればよいですか？
A. `unzip -t archive.zip`を使用すると、ファイルを展開せずにアーカイブの整合性をテストできます。

#### Q5. ファイル名のエンコーディングの問題を処理するにはどうすればよいですか？
A. ファイル名が文字化けする場合は、`-O`オプションを使用してエンコーディングを指定してみてください。例えば、中国語のWindowsアーカイブの場合は`unzip -O CP936 archive.zip`のようにします。

## References

https://linux.die.net/man/1/unzip

## Revisions

- 2025/05/04 初回リビジョン