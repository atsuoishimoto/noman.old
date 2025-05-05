# chgrp コマンド

ファイルやディレクトリのグループ所有権を変更します。

## 概要

`chgrp` コマンドはファイルやディレクトリのグループ所有権を変更するために使用されます。適切な権限を持つユーザーが、特定のファイルやディレクトリにどのグループがアクセスできるかを変更できるようにするもので、Unixファイルパーミッション管理の重要な側面です。

## オプション

### **-c, --changes**

グループ所有権が変更された場合に報告します。

```console
$ chgrp -c staff document.txt
changed group of 'document.txt' from 'users' to 'staff'
```

### **-f, --silent, --quiet**

ほとんどのエラーメッセージを抑制します。

```console
$ chgrp -f nonexistent_group document.txt
```

### **-v, --verbose**

処理されるすべてのファイルについて詳細な情報を出力します。

```console
$ chgrp -v staff *.txt
group of 'document.txt' retained as 'staff'
group of 'notes.txt' changed from 'users' to 'staff'
```

### **-R, --recursive**

ファイルとディレクトリを再帰的に処理します。

```console
$ chgrp -R developers project_folder/
```

### **-h, --no-dereference**

参照先のファイルではなくシンボリックリンク自体に影響を与えます。

```console
$ chgrp -h staff symlink_file
```

### **--reference=RFILE**

グループ値を指定する代わりに、RFILEのグループを使用します。

```console
$ chgrp --reference=template.txt document.txt
```

## 使用例

### 単一ファイルのグループ所有権を変更する

```console
$ ls -l document.txt
-rw-r--r-- 1 user users 1024 May 4 10:30 document.txt
$ chgrp staff document.txt
$ ls -l document.txt
-rw-r--r-- 1 user staff 1024 May 4 10:30 document.txt
```

### 再帰的にグループ所有権を変更する

```console
$ chgrp -R developers project/
$ ls -l project/
total 8
drwxr-xr-x 2 user developers 4096 May 4 10:35 src/
-rw-r--r-- 1 user developers 2048 May 4 10:32 README.md
```

### 参照ファイルを使用してグループ所有権を変更する

```console
$ ls -l template.txt document.txt
-rw-r--r-- 1 user developers 1024 May 4 10:30 template.txt
-rw-r--r-- 1 user users 2048 May 4 10:32 document.txt
$ chgrp --reference=template.txt document.txt
$ ls -l document.txt
-rw-r--r-- 1 user developers 2048 May 4 10:32 document.txt
```

## ヒント:

### 先にグループメンバーシップを確認する

ファイルのグループを変更する前に、`groups`コマンドを使用して対象グループのメンバーであることを確認してください。自分が所属しているグループにのみファイルのグループを変更できます（rootユーザーを除く）。

### 数値グループIDを使用する

グループIDの番号を知っている場合は、グループ名の代わりに番号を使用できます：

```console
$ chgrp 1000 document.txt
```

### chmodと組み合わせる

グループ所有権を変更した後、`chmod`でグループのパーミッションを調整する必要があるかもしれません：

```console
$ chgrp developers project/
$ chmod g+w project/
```

## よくある質問

#### Q1. 誰がファイルのグループを変更できますか？
A. ファイルの所有者は、自分が所属しているグループにのみファイルのグループを変更できます。rootユーザーは任意のファイルのグループを任意のグループに変更できます。

#### Q2. 自分がどのグループに所属しているか確認するには？
A. `groups`コマンドを使用すると、自分が所属するすべてのグループを確認できます。

#### Q3. 所有者とグループを一度に変更できますか？
A. いいえ、`chgrp`はグループのみを変更します。所有者とグループを同時に変更するには、`chown user:group file`という構文で`chown`を使用してください。

#### Q4. 「Operation not permitted」エラーが出る理由は？
A. これは通常、ファイルの所有者でない場合、対象グループのメンバーでない場合、またはファイルに不変フラグなどの特別なパーミッションが設定されている場合に発生します。

## 参照

https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html

## 改訂履歴

- 2025/05/04 初版作成