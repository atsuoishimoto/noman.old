# touch コマンド

ファイルのタイムスタンプを更新したり、新しい空のファイルを作成したりします。

## 概要

`touch`コマンドは、指定したファイルのアクセス時刻と更新時刻を現在の時刻に変更します。指定したファイルが存在しない場合は、新しい空のファイルを作成します。このコマンドは、ファイルの存在確認や、単純な空ファイルの作成によく使われます。

## オプション

### **-a**

ファイルのアクセス時刻のみを変更します。更新時刻は変更されません。

```console
$ ls -l file.txt
-rw-r--r--  1 user  staff  0 Apr 29 10:00 file.txt
$ touch -a file.txt
$ ls -l file.txt
-rw-r--r--  1 user  staff  0 Apr 29 10:00 file.txt  # 更新時刻は変わっていない
```

### **-m**

ファイルの更新時刻のみを変更します。アクセス時刻は変更されません。

```console
$ ls -l file.txt
-rw-r--r--  1 user  staff  0 Apr 29 10:00 file.txt
$ touch -m file.txt
$ ls -l file.txt
-rw-r--r--  1 user  staff  0 Apr 30 15:30 file.txt  # 更新時刻が変更された
```

### **-c**

ファイルが存在しない場合でも新しいファイルを作成しません。

```console
$ touch -c nonexistent.txt
$ ls nonexistent.txt
ls: nonexistent.txt: No such file or directory  # ファイルは作成されていない
```

### **-t**

指定した時刻にタイムスタンプを設定します。形式は「[[CC]YY]MMDDhhmm[.ss]」です。

```console
$ touch -t 202504291200 file.txt
$ ls -l file.txt
-rw-r--r--  1 user  staff  0 Apr 29 12:00 file.txt  # 指定した時刻に設定された
```

### **-r**

参照ファイルと同じタイムスタンプに設定します。

```console
$ ls -l reference.txt
-rw-r--r--  1 user  staff  0 Apr 28 09:30 reference.txt
$ touch -r reference.txt file.txt
$ ls -l file.txt
-rw-r--r--  1 user  staff  0 Apr 28 09:30 file.txt  # reference.txtと同じタイムスタンプになった
```

## 使用例

### 新しいファイルの作成

```console
$ touch newfile.txt
$ ls -l newfile.txt
-rw-r--r--  1 user  staff  0 Apr 30 15:35 newfile.txt  # 新しい空ファイルが作成された
```

### 複数ファイルの作成

```console
$ touch file1.txt file2.txt file3.txt
$ ls
file1.txt  file2.txt  file3.txt  # 3つのファイルが作成された
```

### ワイルドカードを使用して複数ファイルのタイムスタンプを更新

```console
$ touch *.txt
$ ls -l *.txt
-rw-r--r--  1 user  staff  0 Apr 30 15:40 file1.txt
-rw-r--r--  1 user  staff  0 Apr 30 15:40 file2.txt
-rw-r--r--  1 user  staff  0 Apr 30 15:40 file3.txt  # すべての.txtファイルのタイムスタンプが更新された
```

## ヒント:

### ディレクトリの作成と同時に空ファイルを作成

```console
$ mkdir -p new_dir && touch new_dir/empty_file.txt
$ ls -l new_dir/
-rw-r--r--  1 user  staff  0 Apr 30 15:45 empty_file.txt  # ディレクトリと空ファイルが作成された
```

### ファイルの内容を変更せずにタイムスタンプだけを更新

ファイルの内容を変更せずに「最終更新日時」だけを更新したい場合に`touch`は便利です。これはビルドシステムやMakefileで依存関係を制御する際に役立ちます。

### 複数のファイルを一度に作成

```console
$ touch file{1..10}.txt
$ ls
file1.txt  file2.txt  file3.txt  file4.txt  file5.txt  file6.txt  file7.txt  file8.txt  file9.txt  file10.txt
```

## よくある質問

#### Q1. touchコマンドの主な用途は何ですか？
A. 空のファイルを新規作成することと、既存ファイルのタイムスタンプ（アクセス時刻・更新時刻）を更新することです。

#### Q2. すでに存在するファイルにtouchを使うとどうなりますか？
A. ファイルの内容は変更されず、タイムスタンプ（アクセス時刻と更新時刻）のみが現在の時刻に更新されます。

#### Q3. 特定の日時にタイムスタンプを設定するにはどうすればよいですか？
A. `-t`オプションを使用して、`touch -t YYYYMMDDhhmm.ss filename`の形式で指定できます。例えば、`touch -t 202504291200 file.txt`とします。

#### Q4. 既存のファイルと同じタイムスタンプを別のファイルに設定するには？
A. `-r`オプションを使用します。例：`touch -r reference.txt target.txt`

## macOSでの注意点

macOSのtouchコマンドはGNU版と若干の違いがありますが、基本的な機能は同じです。ただし、一部のGNUオプション（例：`--date`）はmacOSでは使用できない場合があります。また、macOSでは`-A`オプションを使用して相対的な時間調整が可能です。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/touch-invocation.html

## 改訂履歴

- 2025/04/30 初版作成