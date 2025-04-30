# ln コマンド

ファイルやディレクトリへのリンク（ショートカット）を作成します。

## 概要

`ln` コマンドは、既存のファイルやディレクトリへのリンクを作成するためのコマンドです。Unixシステムでは主に2種類のリンク（ハードリンクとシンボリックリンク）を作成できます。シンボリックリンクは Windows のショートカットに似た機能で、元のファイルへの参照を作成します。ハードリンクは同じファイルに対する別の名前を作成します。

## オプション

### **-s (--symbolic)**

シンボリックリンク（ソフトリンク）を作成します。これが最も一般的な使用方法です。

```console
$ echo "元のファイル" > original.txt
$ ln -s original.txt link.txt
$ ls -l
total 8
lrwxr-xr-x  1 user  staff  12 Apr 30 10:00 link.txt -> original.txt
-rw-r--r--  1 user  staff  15 Apr 30 10:00 original.txt
```

### **-f (--force)**

既存のリンク先ファイルを上書きします。

```console
$ ln -sf original.txt existing_link.txt
```

### **-n (--no-dereference)**

リンク先がシンボリックリンクの場合、それを上書きせずにリンク自体を置き換えます。

```console
$ ln -sfn new_target.txt existing_link.txt
```

### **-v (--verbose)**

作成されるリンクの情報を表示します。

```console
$ ln -sv original.txt verbose_link.txt
'verbose_link.txt' -> 'original.txt'
```

## 使用例

### シンボリックリンクの作成

```console
$ ln -s /path/to/original/file.txt link.txt
```

### ディレクトリへのシンボリックリンクの作成

```console
$ ln -s /path/to/original/directory linkdir
```

### ハードリンクの作成（-sオプションなし）

```console
$ ln original.txt hardlink.txt
$ ls -l
total 16
-rw-r--r--  2 user  staff  15 Apr 30 10:00 hardlink.txt
-rw-r--r--  2 user  staff  15 Apr 30 10:00 original.txt
```

### 複数のファイルを一つのディレクトリにリンク

```console
$ ln -s file1.txt file2.txt destination_directory/
```

## ヒント:

### シンボリックリンクとハードリンクの違い

- シンボリックリンク（`ln -s`）：元のファイルへの参照を作成します。元ファイルが削除されるとリンクは機能しなくなります。
- ハードリンク（`ln`）：同じデータに対する別の名前を作成します。元のファイル名が削除されても、ハードリンクからデータにアクセスできます。

### 相対パスと絶対パス

シンボリックリンクを作成する際、相対パスを使うとリンクの場所を基準にしたパスになります。移動可能性を考慮する場合は絶対パスを使用しましょう。

### リンク切れの確認

```console
$ find /path/to/check -type l -exec test ! -e {} \; -print
```
このコマンドで、リンク切れのシンボリックリンクを見つけることができます。

## よくある質問

#### Q1. シンボリックリンクとハードリンクはどう使い分ければよいですか？
A. ディレクトリへのリンクや、別のファイルシステムへのリンクが必要な場合はシンボリックリンク（`ln -s`）を使います。同一ファイルシステム内で元ファイルが削除されても内容を保持したい場合はハードリンクが適しています。

#### Q2. シンボリックリンクが壊れているかどうかを確認するには？
A. `ls -l`でリンク先が赤色で表示される場合や、`file`コマンドで「broken symbolic link」と表示される場合はリンク切れです。

#### Q3. macOSでシンボリックリンクを作成する際の注意点はありますか？
A. macOSでは基本的にLinuxと同じように動作しますが、HFSやAPFSファイルシステムではハードリンクに一部制限があります。また、Finderでシンボリックリンクを作成・操作する場合は挙動が異なる場合があります。

#### Q4. リンク先のパスを確認するには？
A. `readlink リンク名`コマンドでリンク先のパスを確認できます。

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html

## 改訂履歴

- 2025/04/30 初版作成