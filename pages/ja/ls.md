# ls コマンド

`ls` コマンドは、ディレクトリの内容（ファイルやフォルダ）を一覧表示するための基本的なUNIXコマンドです。デフォルトではカレントディレクトリの内容を表示します。

## オプション

### **-l** (long format)
ファイルの詳細情報（権限、所有者、サイズ、更新日時など）を表示します。

```console
$ ls -l
total 16
-rw-r--r--  1 user  staff  1024 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  4月 9  14:22 projects
```

### **-a** (all)
隠しファイル（ドットで始まるファイル）を含むすべてのファイルを表示します。

```console
$ ls -a
.  ..  .hidden  document.txt  projects
```

### **-h** (human-readable)
ファイルサイズを人間が読みやすい形式（KB、MB、GBなど）で表示します。通常は `-l` と組み合わせて使用します。

```console
$ ls -lh
total 16K
-rw-r--r--  1 user  staff  1.0K 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B 4月 9  14:22 projects
```

### **-d** (directory)
ディレクトリ自体の情報を表示し、その内容は表示しません。ディレクトリの属性を確認したい場合に便利です。

```console
$ ls -ld projects
drwxr-xr-x  3 user  staff  96  4月 9  14:22 projects
```

### **-s** (size)
各ファイルが使用しているブロック数を表示します。ディスク使用量を確認する際に役立ちます。

```console
$ ls -s
total 16
8 document.txt  8 projects
```

### **-t** (time)
ファイルを更新時間順（最新のものが先）に並べ替えます。最近変更されたファイルを素早く見つけるのに便利です。

```console
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  4月 9  14:22 projects
```

### **-r** (reverse)
通常の並び順を逆にします。他のソートオプションと組み合わせて使用できます。例えば `-tr` で古いファイルから表示できます。

```console
$ ls -ltr
total 16
drwxr-xr-x  3 user  staff   96  4月 9  14:22 projects
-rw-r--r--  1 user  staff  1024 4月 10 15:30 document.txt
```

## 使用例

### 特定のディレクトリの内容を表示

```console
$ ls /usr/bin
[/usr/binディレクトリの内容が表示される]
```

### パターンに一致するファイルを表示

```console
$ ls *.txt
document.txt  notes.txt  readme.txt
```

### 最近変更されたファイルを先に表示

```console
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  4月 9  14:22 projects
```

### 複数のオプションを組み合わせる

```console
$ ls -lha
total 24K
drwxr-xr-x   4 user  staff  128B 4月 10 15:35 .
drwxr-xr-x  15 user  staff  480B 4月 8  10:20 ..
-rw-r--r--   1 user  staff   74B 4月 10 14:22 .hidden
-rw-r--r--   1 user  staff  1.0K 4月 10 15:30 document.txt
drwxr-xr-x   3 user  staff   96B 4月 9  14:22 projects
```

## よくある質問

#### Q1. `ls` は何に使用されますか？
A. `ls` はディレクトリ内のファイルとフォルダを一覧表示するために使用されます。

#### Q2. 隠しファイルを表示するにはどうすればよいですか？
A. `ls -a` を使用します。これによりドット（`.`）で始まるファイルも表示されます。

#### Q3. ファイルの詳細情報を見るにはどうすればよいですか？
A. `ls -l` を使用すると、権限、所有者、サイズ、最終更新時間などが表示されます。

#### Q4. ファイルを更新日時順に表示するにはどうすればよいですか？
A. `ls -t` を使用すると、最新のファイルから順に表示されます。

## 追加情報

* `ls` コマンドは、多くのオプションを組み合わせて使用できます（例：`ls -lha`）。
* macOSでは、`ls -G` でカラー表示が可能です（Linuxでは `ls --color=auto`）。
* ディレクトリ内のファイル数が多い場合、`ls | wc -l` でファイル数をカウントできます。
* macOSでは、BSD版の `ls` が使用されているため、GNU/Linuxの `ls` と一部のオプションが異なる場合があります。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html