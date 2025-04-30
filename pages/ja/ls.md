# ls コマンド

ファイルやディレクトリの情報を表示します。

## 概要

`ls` コマンドは、指定したディレクトリ内のファイルやディレクトリの一覧を表示します。オプションなしで実行すると、現在のディレクトリ内の非隠しファイルとディレクトリを表示します。様々なオプションを使用することで、表示形式や表示する情報を変更できます。

## オプション

### **-l（ロング形式）**

ファイルやディレクトリの詳細情報（権限、所有者、サイズ、更新日時など）を表示します。

```console
$ ls -l
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-a（すべて表示）**

隠しファイル（ドットで始まるファイル）を含むすべてのファイルを表示します。

```console
$ ls -a
.  ..  .hidden  document.txt  projects
```

### **-h（人間が読みやすい形式）**

ファイルサイズを読みやすい単位（K、M、Gなど）で表示します。通常は `-l` オプションと組み合わせて使用します。

```console
$ ls -lh
total 16K
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

### **-d（ディレクトリ自体）**

ディレクトリの内容ではなく、ディレクトリ自体の情報を表示します。

```console
$ ls -ld projects
drwxr-xr-x  3 user  staff  96 Apr 9 14:22 projects
```

### **-s（サイズ表示）**

各ファイルが使用しているブロック数を表示します。

```console
$ ls -s
total 16
8 document.txt  8 projects
```

### **-t（時間順）**

ファイルを更新時間順（最新のものが先）にソートして表示します。

```console
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-r（逆順）**

通常の表示順序を逆にします。他のソートオプションと組み合わせて使用できます。

```console
$ ls -ltr
total 16
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
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

### 複数のオプションを組み合わせる

```console
$ ls -lha
total 24K
drwxr-xr-x  4 user  staff  128B Apr 10 15:30 .
drwxr-xr-x 10 user  staff  320B Apr 8  12:15 ..
-rw-r--r--  1 user  staff   74B Apr 10 15:25 .hidden
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

## ヒント:

### 読みやすいサイズ表示

`ls -lh` を使用すると、ファイルサイズが「1K」や「5M」のような読みやすい単位で表示されます。大きなファイルをすぐに見つけたいときに便利です。

### 更新時間順にソート

`ls -lt` を使用すると、ファイルが最終更新時間順にソートされ、最新のファイルが最初に表示されます。最近更新されたファイルを探すのに役立ちます。

### 隠しファイルの表示

`ls -a` を使用すると、`.bashrc` のような隠しドットファイルを含むすべてのファイルが表示されます。設定ファイルやシステムファイルを確認する際に便利です。

### カラー表示

多くのシステムでは `ls --color=auto` または macOS では `ls -G` を使用することで、ファイルタイプごとに色分けされた出力が得られます。

## よくある質問

#### Q1. `ls` は何に使われますか？
A. `ls` はディレクトリ内のファイルとディレクトリを一覧表示するために使用されます。

#### Q2. 隠しファイルを表示するにはどうすればよいですか？
A. `ls -a` を使用します。これによりドット（`.`）で始まるファイルも表示されます。

#### Q3. ファイルの詳細情報を表示するにはどうすればよいですか？
A. `ls -l` を使用すると、権限、所有者、サイズ、最終更新時間などが表示されます。

#### Q4. ファイルを更新日時の古い順に表示するにはどうすればよいですか？
A. `ls -ltr` を使用します。`-t` で時間順、`-r` で逆順にソートします。

## macOSでの注意点

macOSの `ls` コマンドは GNU バージョンとは若干異なります。例えば、カラー表示には `--color` ではなく `-G` オプションを使用します。また、一部の GNU 固有のオプションは利用できない場合があります。Homebrew などのパッケージマネージャを使って GNU coreutils をインストールすると、`gls` コマンドとして GNU バージョンの ls を使用できます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html

## 改訂履歴

- 2025/04/30 初版作成