# chgrp コマンド

ファイルやディレクトリのグループ所有権を変更します。

## 概要

`chgrp`コマンドは、ファイルやディレクトリのグループ所有権を変更するために使用します。Unixシステムでは、各ファイルとディレクトリは所有者とグループに関連付けられており、このコマンドを使用することでグループの割り当てを変更できます。

## オプション

### **-R, --recursive**

指定したディレクトリ内のファイルとサブディレクトリを再帰的に処理します。

```console
$ chgrp -R developers project/
# project/ディレクトリとその中のすべてのファイルとサブディレクトリのグループを「developers」に変更
```

### **-v, --verbose**

処理されるファイルごとに詳細な情報を表示します。

```console
$ chgrp -v staff document.txt
changed group of 'document.txt' from 'users' to 'staff'
```

### **-c, --changes**

変更が行われた場合のみ、verboseモードと同様の出力を表示します。

```console
$ chgrp -c admin config.ini
changed group of 'config.ini' from 'users' to 'admin'
```

### **-h, --no-dereference**

シンボリックリンクそのものを変更し、リンク先のファイルは変更しません。

```console
$ chgrp -h developers symlink.txt
# symlink.txtというシンボリックリンク自体のグループを変更
```

## 使用例

### 基本的な使用方法

```console
$ ls -l file.txt
-rw-r--r--  1 user users 1024 Apr 30 10:00 file.txt
$ chgrp staff file.txt
$ ls -l file.txt
-rw-r--r--  1 user staff 1024 Apr 30 10:00 file.txt
```

### 複数のファイルのグループを変更

```console
$ chgrp developers file1.txt file2.txt file3.txt
# file1.txt、file2.txt、file3.txtのグループを「developers」に変更
```

### 数値グループIDを使用

```console
$ chgrp 1000 document.txt
# document.txtのグループをグループID 1000に変更
```

## ヒント:

### グループ名とグループIDの確認

グループ名とそのIDを確認するには、`/etc/group`ファイルを参照するか、`getent group`コマンドを使用できます。

```console
$ getent group developers
developers:x:1001:user1,user2,user3
```

### 権限の確認

グループを変更した後、適切なグループ権限が設定されているか確認しましょう。`chmod`コマンドでグループ権限を調整できます。

```console
$ chmod g+rw file.txt
# ファイルにグループの読み書き権限を追加
```

### 所有者とグループを同時に変更

ファイルの所有者とグループを同時に変更する場合は、`chown`コマンドを使用します。

```console
$ chown user:group file.txt
# file.txtの所有者を「user」に、グループを「group」に変更
```

## よくある質問

#### Q1. `chgrp`を実行するために必要な権限は何ですか？
A. ファイルの所有者であるか、root（スーパーユーザー）権限を持っている必要があります。

#### Q2. 存在しないグループに変更しようとするとどうなりますか？
A. エラーメッセージが表示され、グループの変更は行われません。例：`chgrp: invalid group: 'nonexistentgroup'`

#### Q3. シンボリックリンクのグループを変更するには？
A. `-h`オプションを使用して、リンク自体のグループを変更できます。デフォルトでは、リンク先のファイルのグループが変更されます。

#### Q4. 数値グループIDと名前のどちらを使うべきですか？
A. 通常はグループ名を使用する方が分かりやすいですが、システム間で一貫性を保つ必要がある場合は数値IDが便利です。

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html

## Revisions

- 2025/04/30 First revision