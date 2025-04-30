# gunzip コマンド

圧縮ファイルを展開するコマンドです。

## 概要

`gunzip`は、gzipで圧縮されたファイルを元の状態に戻すコマンドです。デフォルトでは、元のファイルを展開した後に圧縮ファイルを削除します。主に`.gz`拡張子を持つファイルの展開に使用されます。

## オプション

### **-c, --stdout, --to-stdout**

展開したデータを標準出力に出力し、元の圧縮ファイルを保持します。

```console
$ gunzip -c archive.gz > extracted_file
# 圧縮ファイルを保持したまま内容を展開して別ファイルに保存
```

### **-f, --force**

強制的に展開を行います。既に同名のファイルが存在する場合でも上書きします。

```console
$ gunzip -f already_exists.gz
# 同名ファイルが存在しても強制的に展開
```

### **-k, --keep**

展開後も元の圧縮ファイルを保持します。

```console
$ gunzip -k archive.gz
# archive.gzを展開し、展開後もarchive.gzを残す
```

### **-l, --list**

圧縮ファイル内の情報を表示します。ファイルを展開せずに内容の情報を確認できます。

```console
$ gunzip -l archive.gz
         compressed        uncompressed  ratio uncompressed_name
                547                1536  64.4% archive
```

### **-r, --recursive**

ディレクトリを再帰的に処理し、すべてのサブディレクトリ内の圧縮ファイルも展開します。

```console
$ gunzip -r directory/
# directory内のすべての.gzファイルを再帰的に展開
```

## 使用例

### 基本的な使い方

```console
$ gunzip archive.gz
# archive.gzを展開してarchiveファイルを作成し、archive.gzは削除される
```

### 複数ファイルの展開

```console
$ gunzip file1.gz file2.gz file3.gz
# 複数のファイルを一度に展開
```

### 圧縮ファイルを保持したまま展開

```console
$ gunzip -k large_file.gz
# large_file.gzを展開し、large_fileを作成。large_file.gzも保持される
```

### 標準出力への展開

```console
$ gunzip -c config.gz | grep "setting"
# config.gzを展開して標準出力に送り、grepでフィルタリング
```

## ヒント:

### 拡張子の自動処理

`gunzip`は自動的に`.gz`拡張子を削除します。例えば、`file.txt.gz`は展開すると`file.txt`になります。

### 複数の圧縮形式への対応

多くのシステムでは、`gunzip`は`gzip -d`と同等です。また、`zcat`は`gunzip -c`と同等の機能を持ちます。

### パイプラインでの使用

`gunzip -c`を使うと、圧縮ファイルを展開してその内容を他のコマンドに渡すことができます。これはログファイルの分析などに便利です。

### 大きなファイルの処理

非常に大きなファイルを展開する場合は、十分なディスク容量があることを確認してください。圧縮ファイルは展開すると元のサイズに戻ります。

## よくある質問

#### Q1. `gunzip`と`gzip -d`の違いは何ですか？
A. 機能的には同じです。`gunzip`は`gzip -d`のエイリアスとして実装されていることが多いです。

#### Q2. 展開したファイルと圧縮ファイルの両方を保持するにはどうすればいいですか？
A. `gunzip -k`（または`--keep`）オプションを使用すると、展開後も元の圧縮ファイルが保持されます。

#### Q3. 圧縮ファイルの内容を確認するだけで展開したくない場合はどうすればいいですか？
A. `gunzip -l`（または`--list`）オプションを使用すると、ファイルを展開せずに圧縮ファイルの情報を表示できます。

#### Q4. 標準入力から圧縮データを受け取って展開するにはどうすればいいですか？
A. `gunzip`に引数を指定せずに使用すると、標準入力からデータを読み取り、展開します。例：`cat file.gz | gunzip > extracted_file`

## macOSでの注意点

macOSの`gunzip`はGNU版と若干の違いがあります。特に`-r`（再帰）オプションがない場合があります。代わりに`find`コマンドと組み合わせて使用することができます：

```console
$ find . -name "*.gz" -exec gunzip {} \;
# カレントディレクトリ以下のすべての.gzファイルを再帰的に展開
```

## 参照

https://www.gnu.org/software/gzip/manual/gzip.html

## 改訂履歴

- 2025/04/30 初版作成