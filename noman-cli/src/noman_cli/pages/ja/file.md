# file コマンド

ファイルの内容を調べてファイルタイプを判定します。

## 概要

`file` コマンドは指定された各ファイルを調査し、そのタイプを分類します。テキスト、実行可能ファイル、データ、その他の形式かどうかを判断するために一連のテストを実行します。多くのコマンドがファイル拡張子に依存するのとは異なり、`file` はファイルの実際の内容を調べてタイプを識別します。

## オプション

### **-b, --brief**

ファイル名の接頭辞なしで結果を表示します。

```console
$ file -b document.txt
ASCII text
```

### **-i, --mime**

従来の説明の代わりにMIMEタイプ文字列を表示します。

```console
$ file -i document.txt
document.txt: text/plain; charset=us-ascii
```

### **-z, --uncompress**

圧縮ファイルの中身を調べます。

```console
$ file -z archive.gz
archive.gz: ASCII text (gzip compressed data, was "notes.txt", last modified: Wed Apr 28 15:30:45 2021, from Unix)
```

### **-L, --dereference**

シンボリックリンクをたどります。

```console
$ file -L symlink
symlink: ASCII text
```

### **-s, --special-files**

ブロックまたはキャラクタ特殊ファイルを読み込みます。

```console
$ file -s /dev/sda1
/dev/sda1: Linux rev 1.0 ext4 filesystem data (extents) (large files)
```

## 使用例

### 基本的なファイル識別

```console
$ file document.txt image.png script.sh
document.txt: ASCII text
image.png:    PNG image data, 1920 x 1080, 8-bit/color RGB, non-interlaced
script.sh:    Bourne-Again shell script, ASCII text executable
```

### 複数ファイルの調査

```console
$ file *
document.txt:  ASCII text
image.png:     PNG image data, 1920 x 1080, 8-bit/color RGB, non-interlaced
script.sh:     Bourne-Again shell script, ASCII text executable
archive.tar:   POSIX tar archive (GNU)
binary:        ELF 64-bit LSB executable, x86-64
```

### ディレクトリの調査

```console
$ file projects/
projects/: directory
```

## ヒント:

### パイプとの使用

特殊な引数 `-` を使用して、他のコマンドからの出力を `file` にパイプで渡し、標準入力から読み取ることができます：

```console
$ cat unknown_file | file -
/dev/stdin: ASCII text
```

### 再帰的なファイルタイプ識別

`find` と組み合わせて、再帰的にファイルタイプを識別できます：

```console
$ find . -type f -exec file {} \;
```

### 実行可能ファイルの識別

`file` コマンドは、バイナリが32ビットか64ビットか、どのアーキテクチャ用にコンパイルされているかを判断するのに役立ちます：

```console
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32
```

## よくある質問

#### Q1. `file` コマンドはどのようにファイルタイプを判定しますか？
A. `file` は「マジック」テストを使用します - ファイルの最初の数バイトを調べ、データベース（通常は `/usr/share/file/magic` にあります）の既知のパターンと比較します。

#### Q2. `file` はすべてのファイルタイプを識別できますか？
A. `file` は多くの一般的なファイルタイプを識別できますが、専門的または独自の形式は認識できない場合があります。ファイルの内容に基づいて最善の推測を提供します。

#### Q3. なぜ `file` はテキストファイルを特定のエンコーディングとして報告することがありますか？
A. `file` は文字パターンを分析して、UTF-8、ASCII、その他の文字セットなどのテキストエンコーディングを検出します。

#### Q4. ファイル名なしでMIMEタイプだけを取得するにはどうすればよいですか？
A. `file -b -i ファイル名` を使用すると、ファイル名の接頭辞なしでMIMEタイプのみを取得できます。

## macOSに関する考慮事項

macOSでは、`file` コマンドはLinuxバージョンと同様に動作しますが、出力形式や検出機能が若干異なる場合があります。マジックデータベースの場所は通常 `/usr/share/file/magic` または `/etc/magic` にあります。

## 参考資料

https://man7.org/linux/man-pages/man1/file.1.html

## 改訂履歴

- 2025/05/04 初版作成