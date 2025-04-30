# unzip コマンド

ZIP アーカイブファイルを展開するコマンド。

## 概要

`unzip` コマンドは、ZIP 形式で圧縮されたファイルを解凍するために使用されます。ファイル名を指定するだけで、現在のディレクトリにアーカイブの内容を展開できます。また、特定のファイルのみを抽出したり、展開先ディレクトリを指定したりすることも可能です。

## オプション

### **-l (リスト表示)**

ZIP ファイル内のファイル一覧を表示します（実際に展開はしません）。

```console
$ unzip -l archive.zip
Archive:  archive.zip
  Length      Date    Time    Name
---------  ---------- -----   ----
      100  2025-04-20 10:30   file1.txt
      200  2025-04-20 10:31   file2.txt
      300  2025-04-20 10:32   folder/file3.txt
---------                     -------
      600                     3 files
```

### **-d (ディレクトリ指定)**

ZIP ファイルを展開する先のディレクトリを指定します。

```console
$ unzip archive.zip -d extracted_files
Archive:  archive.zip
  inflating: extracted_files/file1.txt
  inflating: extracted_files/file2.txt
  inflating: extracted_files/folder/file3.txt
```

### **-o (上書き)**

既存のファイルを確認なしで上書きします。

```console
$ unzip -o archive.zip
Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
  inflating: folder/file3.txt
```

### **-q (静かモード)**

解凍中の詳細な出力を表示せず、静かに実行します。

```console
$ unzip -q archive.zip
```

## 使用例

### 基本的な解凍

```console
$ unzip archive.zip
Archive:  archive.zip
  inflating: file1.txt
  inflating: file2.txt
  creating: folder/
  inflating: folder/file3.txt
```

### 特定のファイルのみを解凍

```console
$ unzip archive.zip file1.txt
Archive:  archive.zip
  inflating: file1.txt
```

### パスワード付きZIPファイルの解凍

```console
$ unzip -P mypassword secure.zip
Archive:  secure.zip
  inflating: confidential.txt
```

### 解凍前にファイル内容を確認

```console
$ unzip -l archive.zip
Archive:  archive.zip
  Length     Date   Time    Name
 --------    ----   ----    ----
      100  04-20-25 10:30   file1.txt
      200  04-20-25 10:31   file2.txt
      300  04-20-25 10:32   folder/file3.txt
 --------                   -------
      600                   3 files
```

## ヒント:

### 日本語ファイル名の文字化け対策

macOSでは、日本語ファイル名が含まれるZIPファイルを解凍すると文字化けすることがあります。その場合は `unar` コマンド（`brew install unar` でインストール）を使用すると良いでしょう。

### 解凍前の内容確認

大きなZIPファイルを解凍する前に `-l` オプションで内容を確認しましょう。これにより、不要なファイルの解凍を避けることができます。

### 既存ファイルの保護

重要なファイルを誤って上書きしないように、新しいディレクトリに解凍する `-d` オプションを活用しましょう。

## よくある質問

#### Q1. ZIPファイルが破損しているかどうかを確認するには？
A. `unzip -t archive.zip` コマンドを使用すると、ZIPファイルの整合性をテストできます。

#### Q2. 解凍せずにZIPファイルの内容を見るには？
A. `unzip -l archive.zip` を使用すると、ファイルを実際に解凍せずに内容を確認できます。

#### Q3. 特定のファイルやディレクトリだけを解凍するには？
A. `unzip archive.zip filename` のようにZIPファイル名の後に抽出したいファイル名を指定します。ワイルドカード（`*.txt`など）も使用できます。

#### Q4. 解凍時にファイル名の文字化けを防ぐには？
A. macOSでは、`The Unarchiver`や`unar`コマンドラインツールを使用すると文字化けを防げることが多いです。

## macOSでの注意点

macOSの標準の`unzip`コマンドは、日本語などの非ASCII文字を含むファイル名を正しく処理できないことがあります。このような場合は、Homebrewを使って`unar`をインストールし、代わりに使用することをお勧めします：

```console
$ brew install unar
$ unar archive.zip
```

## 参考

https://linux.die.net/man/1/unzip

## 改訂履歴

- 2025/04/30 初版作成