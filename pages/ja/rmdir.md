# rmdir コマンド

ディレクトリを削除します。

## 概要

`rmdir`コマンドは、空のディレクトリを削除するために使用されます。ディレクトリ内にファイルやサブディレクトリが存在する場合は、削除できません。複数のディレクトリを一度に指定することも可能です。

## オプション

### **-p, --parents**

指定されたディレクトリとその親ディレクトリを削除します（空の場合のみ）。

```console
$ mkdir -p dir1/dir2/dir3
$ rmdir -p dir1/dir2/dir3
```

### **-v, --verbose**

削除されるディレクトリごとに処理内容を表示します。

```console
$ mkdir test_dir
$ rmdir -v test_dir
rmdir: 'test_dir' を削除しました
```

### **--ignore-fail-on-non-empty**

ディレクトリが空でない場合のエラーを無視します。

```console
$ mkdir non_empty_dir
$ touch non_empty_dir/file.txt
$ rmdir --ignore-fail-on-non-empty non_empty_dir
```

## 使用例

### 基本的な使い方

```console
$ mkdir empty_dir
$ rmdir empty_dir
```

### 複数のディレクトリを削除

```console
$ mkdir dir1 dir2 dir3
$ rmdir dir1 dir2 dir3
```

### 親ディレクトリも含めて削除

```console
$ mkdir -p parent/child/grandchild
$ rmdir -p parent/child/grandchild
# parent, child, grandchildの全てのディレクトリが削除される
```

## ヒント:

### 空でないディレクトリの削除

`rmdir`は空のディレクトリしか削除できません。ディレクトリ内にファイルがある場合は、`rm -r`コマンドを使用する必要があります。

```console
$ rm -r non_empty_directory
```

### 複数階層のディレクトリ作成と削除

`mkdir -p`でディレクトリ階層を作成した場合、`rmdir -p`を使用すると同様に階層を削除できます。

### 安全な削除

`rmdir`は空のディレクトリしか削除できないため、誤って重要なファイルを削除するリスクが低く、`rm -r`よりも安全です。

## よくある質問

#### Q1. `rmdir`と`rm -r`の違いは何ですか？
A. `rmdir`は空のディレクトリのみを削除できますが、`rm -r`はディレクトリとその中身（ファイルやサブディレクトリ）を再帰的に削除します。

#### Q2. ディレクトリが空でないというエラーが出た場合はどうすればいいですか？
A. そのディレクトリ内のファイルを先に削除するか、`rm -r`コマンドを使用してディレクトリごと削除します。

#### Q3. 複数の空ディレクトリを一度に削除できますか？
A. はい、`rmdir dir1 dir2 dir3`のように複数のディレクトリをスペースで区切って指定できます。

#### Q4. 削除したディレクトリを元に戻すことはできますか？
A. 通常のファイルシステムでは、`rmdir`で削除したディレクトリを元に戻す直接的な方法はありません。バックアップから復元するか、特別なファイル復元ツールを使用する必要があります。

## macOSでの注意点

macOSでは基本的にLinuxと同じように`rmdir`コマンドが動作しますが、一部のオプション（例：`--ignore-fail-on-non-empty`）はGNU版と異なる場合があります。互換性の問題がある場合は、Homebrewを使って`coreutils`パッケージをインストールし、`grmdir`として使用することができます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/rmdir-invocation.html

## 改訂履歴

- 2025/04/30 初版作成