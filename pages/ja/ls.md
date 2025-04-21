# ls コマンド

`ls` は、ディレクトリの内容を一覧表示するコマンドです。ファイル名やディレクトリ名、およびそれらの属性情報を確認することができます。

## オプション

### **-l（ロング形式）**

ファイルやディレクトリの詳細情報（権限、所有者、サイズ、更新日時など）を表示します。

```bash
$ ls -l
total 16
-rw-r--r--  1 user  staff  1024 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  4月 9  14:22 projects
```

### **-a（すべて表示）**

隠しファイル（ドットで始まるファイル）を含むすべてのファイルを表示します。

```bash
$ ls -a
.  ..  .hidden  document.txt  projects
```

### **-h（人間が読みやすい形式）**

ファイルサイズを読みやすい単位（KB、MB、GBなど）で表示します。`-l`オプションと組み合わせて使用します。

```bash
$ ls -lh
total 16K
-rw-r--r--  1 user  staff  1.0K 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B 4月 9  14:22 projects
```

### **-d（ディレクトリ自体）**

ディレクトリの中身ではなく、ディレクトリ自体の情報を表示します。

```bash
$ ls -ld projects
drwxr-xr-x  3 user  staff  96  4月 9  14:22 projects
```

### **-s（サイズ表示）**

各ファイルが使用しているブロック数を表示します。

```bash
$ ls -s
total 16
8 document.txt  8 projects
```

### **-t（時間順）**

ファイルを更新時間順（新しい順）に並べ替えて表示します。

```bash
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  4月 9  14:22 projects
```

### **-r（逆順）**

表示順序を逆にします。他のソートオプションと組み合わせて使用できます。

```bash
$ ls -ltr
total 16
drwxr-xr-x  3 user  staff   96  4月 9  14:22 projects
-rw-r--r--  1 user  staff  1024 4月 10 15:30 document.txt
```

## 使用例

### 基本的な使い方

```bash
$ ls
document.txt  projects
```

### 複数のオプションを組み合わせる

```bash
$ ls -lha
total 20K
drwxr-xr-x   4 user  staff  128B 4月 10 15:35 .
drwxr-xr-x  15 user  staff  480B 4月 8  10:20 ..
-rw-r--r--   1 user  staff   12B 4月 10 15:32 .hidden
-rw-r--r--   1 user  staff  1.0K 4月 10 15:30 document.txt
drwxr-xr-x   3 user  staff   96B 4月 9  14:22 projects
```

### 特定のディレクトリの内容を表示

```bash
$ ls -l projects
total 8
-rw-r--r--  1 user  staff  512 4月 9 14:20 README.md
```

## よくある質問

### Q1. `ls` コマンドの基本的な使い方は？
A. 引数なしで実行すると、現在のディレクトリ内のファイルとディレクトリを表示します。

### Q2. 隠しファイルを表示するには？
A. `ls -a` を使用します。ドット（`.`）で始まるファイルも表示されます。

### Q3. ファイルを更新日時の古い順に表示するには？
A. `ls -ltr` を使用します。`-t`で時間順、`-r`で逆順にソートします。

### Q4. ファイルの種類を区別するには？
A. `ls -F` を使用すると、ディレクトリには `/`、実行可能ファイルには `*` などの記号が付きます。

## 追加情報

- macOSでは、`ls` コマンドはBSD版が使用されており、GNU版（Linux）とは一部の動作が異なります。
- カラー表示をするには、macOSでは `ls -G` を使用します（Linuxでは `ls --color`）。
- ファイル名に特殊文字や空白が含まれる場合は、`ls -b` オプションを使うとエスケープシーケンスで表示されます。
- `ls` コマンドの出力を `grep` などと組み合わせてフィルタリングすると、特定のファイルを検索できます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html