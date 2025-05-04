# unlink コマンド

ファイルシステムから単一のファイルを削除します。

## 概要

`unlink`コマンドは、ファイルシステムからリンクを削除することで単一のファイルを削除するために使用されます。1つのファイルだけを削除する場合には、`rm`コマンドよりもシンプルな代替手段です。`rm`と異なり、`unlink`は複数のファイルやディレクトリを削除することができず、オプションも少なくなっています。

## オプション

### **-h, --help**

ヘルプ情報を表示して終了します。

```console
$ unlink --help
Usage: unlink FILE
  or:  unlink OPTION
Call the unlink function to remove the specified FILE.

      --help     display this help and exit
      --version  output version information and exit
```

### **--version**

バージョン情報を出力して終了します。

```console
$ unlink --version
unlink (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Michael Stone.
```

## 使用例

### ファイルの削除

```console
$ touch temp_file.txt
$ ls
temp_file.txt
$ unlink temp_file.txt
$ ls
$
```

### ディレクトリの削除を試みる（失敗します）

```console
$ mkdir test_dir
$ unlink test_dir
unlink: cannot unlink 'test_dir': Is a directory
```

## ヒント:

### 複数ファイルには`rm`を使用する

複数のファイルを削除する必要がある場合は、`unlink`ではなく`rm`を使用してください。`unlink`コマンドは一度に1つのファイルしか削除できません。

### シンボリックリンク

シンボリックリンクに対して`unlink`を使用すると、リンク先のファイルではなくリンク自体が削除されます。

### 復元不可

`unlink`で削除されたファイルはゴミ箱やリサイクルビンに送られません。完全に削除され、バックアップからしか復元できません。

### 確認なし

`rm`コマンドは`-i`オプションで削除前に確認を求めることができますが、`unlink`はファイル削除前の確認プロンプトを提供しません。

## よくある質問

#### Q1. `unlink`と`rm`の違いは何ですか？
A. `unlink`は単一のファイルのみを削除でき、オプションも最小限ですが、`rm`は複数のファイル、ディレクトリ（`-r`オプション使用時）を削除でき、多くの追加オプションがあります。

#### Q2. `unlink`でディレクトリを削除できますか？
A. いいえ、`unlink`はディレクトリを削除できません。空のディレクトリには`rmdir`を、内容のあるディレクトリには`rm -r`を使用してください。

#### Q3. `unlink`はファイルをゴミ箱に移動しますか？
A. いいえ、`unlink`は永久にファイルを削除します。ゴミ箱やリサイクルビンから復元することはできません。

#### Q4. 存在しないファイルを`unlink`しようとするとどうなりますか？
A. `unlink`はファイルが存在しないというエラーメッセージを返します。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/unlink-invocation.html

## 改訂履歴

- 2025/05/04 初版作成