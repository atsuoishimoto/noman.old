# tar コマンド

ファイルをアーカイブファイルとして作成、抽出、または内容を一覧表示するためのコマンド。

## 概要

`tar`コマンドは、「tarball」と呼ばれるアーカイブファイルの作成、管理、抽出を行います。バックアップ、配布、または圧縮のためにファイルをまとめるのによく使用されます。「tar」という名前は「tape archive（テープアーカイブ）」の略で、元々はテープバックアップ用に設計されましたが、現在は主に通常のファイルで使用されています。

## オプション

### **-c, --create**

新しいアーカイブを作成します

```console
$ tar -c -f archive.tar file1.txt file2.txt
```

### **-x, --extract**

アーカイブからファイルを抽出します

```console
$ tar -x -f archive.tar
```

### **-t, --list**

アーカイブの内容を一覧表示します

```console
$ tar -t -f archive.tar
file1.txt
file2.txt
```

### **-f, --file=ARCHIVE**

アーカイブファイル名を指定します（ほとんどの操作に必須）

```console
$ tar -cf archive.tar directory/
```

### **-v, --verbose**

処理されるファイルを詳細に表示します

```console
$ tar -cvf archive.tar directory/
directory/
directory/file1.txt
directory/file2.txt
directory/subdirectory/
directory/subdirectory/file3.txt
```

### **-z, --gzip**

アーカイブをgzipでフィルタリングします（.tar.gzファイルの作成/抽出）

```console
$ tar -czf archive.tar.gz directory/
```

### **-j, --bzip2**

アーカイブをbzip2でフィルタリングします（.tar.bz2ファイルの作成/抽出）

```console
$ tar -cjf archive.tar.bz2 directory/
```

### **-C, --directory=DIR**

操作を実行する前にディレクトリDIRに移動します

```console
$ tar -xf archive.tar -C /tmp/extract/
```

## 使用例

### ディレクトリの圧縮アーカイブを作成する

```console
$ tar -czf backup.tar.gz /home/user/documents
```

### 圧縮アーカイブを展開する

```console
$ tar -xzf backup.tar.gz
```

### 抽出せずに圧縮アーカイブの内容を表示する

```console
$ tar -tzf backup.tar.gz
home/user/documents/
home/user/documents/file1.txt
home/user/documents/file2.txt
home/user/documents/projects/
home/user/documents/projects/notes.md
```

### アーカイブから特定のファイルを抽出する

```console
$ tar -xf archive.tar file1.txt file2.txt
```

### 既存のアーカイブにファイルを追加する

```console
$ tar -rf archive.tar newfile.txt
```

## ヒント:

### ファイル権限の保持

デフォルトでは、`tar`はファイルの権限、所有権、タイムスタンプを保持します。これはバックアップには便利ですが、非rootユーザーとして抽出する際に問題が発生する可能性があります。権限の問題を避けたい場合は、抽出時に`--no-same-owner`を使用してください。

### 別のディレクトリに抽出する

特定のディレクトリに抽出したい場合は、常に`-C`オプションを使用してください。これにより、ファイルが現在のディレクトリに抽出されるのを防ぎます。

### 進行状況インジケータの使用

大きなアーカイブの場合、作成または抽出中に進行状況を表示するために`--checkpoint=1000 --checkpoint-action=dot`を追加してください。

### ファイルやディレクトリの除外

パターンに一致するファイルやディレクトリを除外するには、`--exclude=PATTERN`を使用します：

```console
$ tar -czf backup.tar.gz --exclude="*.log" --exclude="temp/" /home/user/documents
```

## よくある質問

#### Q1. .tar、.tar.gz、.tar.bz2の違いは何ですか？
A. `.tar`は非圧縮アーカイブ、`.tar.gz`（または`.tgz`）はgzipで圧縮されたもの（速いが圧縮率は低い）、`.tar.bz2`はbzip2で圧縮されたもの（遅いが圧縮率は高い）です。

#### Q2. tarアーカイブから単一のファイルを抽出するにはどうすればよいですか？
A. `tar -xf archive.tar path/to/specific/file`を使用して、そのファイルだけを抽出できます。

#### Q3. 抽出せずにtarファイルの中身を確認するにはどうすればよいですか？
A. `tar -tf archive.tar`を使用すると、抽出せずに内容を一覧表示できます。

#### Q4. ファイル権限を保持するtarアーカイブを作成するにはどうすればよいですか？
A. `tar`はデフォルトで権限を保持します。`tar -cpf archive.tar directory/`を使用すると、`-p`で明示的に権限を保持します。

#### Q5. "Removing leading '/' from member names"という警告にはどう対処すればよいですか？
A. これは絶対パスをアーカイブする際の正常な動作です。`tar`はセキュリティ上の理由から先頭のスラッシュを削除します。可能な限り相対パスを使用してください。

## 参考資料

https://www.gnu.org/software/tar/manual/tar.html

## Revisions

- 2025/05/04 First revision