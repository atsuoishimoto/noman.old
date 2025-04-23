# ls コマンド

`ls` コマンドは、ディレクトリの内容（ファイルやフォルダ）を一覧表示するための基本的なUNIXコマンドです。

## オプション

### **-l**（ロング形式）

ファイルやディレクトリの詳細情報（権限、所有者、サイズ、更新日時など）を表示します。

```bash
$ ls -l
total 16
-rw-r--r--  1 user  staff  1024 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  4月 9  14:22 projects
```

### **-a**（すべて表示）

隠しファイル（ドットで始まるファイル）を含むすべてのファイルを表示します。

```bash
$ ls -a
.  ..  .hidden  document.txt  projects
```

### **-h**（人間が読みやすい形式）

ファイルサイズを読みやすい単位（KB、MB、GBなど）で表示します。`-l`オプションと組み合わせて使用します。

```bash
$ ls -lh
total 16K
-rw-r--r--  1 user  staff  1.0K 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B 4月 9  14:22 projects
```

### **-d**（ディレクトリ自体を表示）

ディレクトリの中身ではなく、ディレクトリ自体の情報を表示します。

```bash
$ ls -ld projects
drwxr-xr-x  3 user  staff  96  4月 9  14:22 projects
```

### **-s**（サイズを表示）

各ファイルが使用しているブロック数を表示します。

```bash
$ ls -s
total 16
8 document.txt  8 projects
```

### **-t**（時間順に並べ替え）

ファイルを最終更新時間の新しい順に並べ替えます。

```bash
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 4月 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  4月 9  14:22 projects
```

### **-r**（逆順に並べ替え）

通常の並び順を逆にします。他のソートオプションと組み合わせて使用できます。

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

隠しファイルを含む詳細情報を、人間が読みやすいサイズ形式で表示します。

```bash
$ ls -lah
total 24K
drwxr-xr-x   4 user  staff   128B 4月 10 15:35 .
drwxr-xr-x  15 user  staff   480B 4月 8  10:20 ..
-rw-r--r--   1 user  staff    74B 4月 10 15:32 .hidden
-rw-r--r--   1 user  staff   1.0K 4月 10 15:30 document.txt
drwxr-xr-x   3 user  staff    96B 4月 9  14:22 projects
```

### 特定のディレクトリの内容を表示

```bash
$ ls -l /usr/bin
# /usr/binディレクトリ内のファイル一覧が表示されます
```

### ファイルタイプでフィルタリング

ワイルドカードを使用して特定のパターンに一致するファイルのみを表示します。

```bash
$ ls *.txt
document.txt  notes.txt  readme.txt
```

## よくある質問

### Q1. `ls`コマンドの基本的な使い方は？
A. 単に`ls`と入力すると、現在のディレクトリ内のファイルとフォルダが表示されます。

### Q2. 隠しファイルを表示するには？
A. `ls -a`を使用します。これにより、ドット(`.`)で始まるファイルも表示されます。

### Q3. ファイルの詳細情報を見るには？
A. `ls -l`を使用すると、権限、所有者、サイズ、最終更新日時などの詳細情報が表示されます。

### Q4. ファイルを更新日時順に表示するには？
A. `ls -t`を使用すると、最新のファイルから順に表示されます。逆順にするには`ls -tr`を使用します。

### Q5. ディレクトリのみ、またはファイルのみを表示するには？
A. 直接的なオプションはありませんが、`ls -l | grep "^d"`でディレクトリのみ、`ls -l | grep "^-"`でファイルのみを表示できます。

## 追加情報

- `ls`コマンドは、多くのオプションを組み合わせて使用できます（例：`ls -lah`）。
- macOSでは、`ls`コマンドはBSD版であり、GNU版（Linux）とは一部の動作が異なります。例えば、色付け表示のオプションは`--color`ではなく`-G`です。
- ファイル名に特殊文字（スペースなど）が含まれる場合、`ls`の出力が予期しない形になることがあります。
- 大量のファイルがあるディレクトリで`ls`を実行すると、画面がスクロールしてしまうことがあります。その場合は`ls | less`のようにパイプを使用すると便利です。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html