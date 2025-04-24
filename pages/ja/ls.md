# ls コマンド

`ls` コマンドは、ディレクトリの内容（ファイルやフォルダ）を一覧表示するための基本的なUnixコマンドです。

## オプション

### **-l**（ロングフォーマット）
ファイルの詳細情報（権限、所有者、サイズ、更新日時など）を表示します。

```console
$ ls -l
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-a**（すべて表示）
隠しファイル（ドットで始まるファイル）を含むすべてのファイルを表示します。

```console
$ ls -a
.  ..  .hidden  document.txt  projects
```

### **-h**（人間が読みやすい形式）
ファイルサイズを読みやすい単位（KB、MB、GBなど）で表示します。`-l`オプションと組み合わせて使用します。

```console
$ ls -lh
total 16K
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

### **-d**（ディレクトリ自体）
ディレクトリの中身ではなく、ディレクトリ自体の情報を表示します。

```console
$ ls -ld projects
drwxr-xr-x  3 user  staff  96 Apr 9 14:22 projects
```

### **-s**（サイズ表示）
各ファイルが使用しているブロック数を表示します。

```console
$ ls -s
total 16
8 document.txt  8 projects
```

### **-t**（時間順）
ファイルを最終更新時間の新しい順に表示します。

```console
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-r**（逆順）
表示順序を逆にします。他のオプションと組み合わせて使用できます。

```console
$ ls -ltr
total 16
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
```

## 使用例

### 基本的な使用法
```console
$ ls
document.txt  projects
```

### 複数のオプションを組み合わせる
隠しファイルを含む詳細情報を人間が読みやすい形式で表示します。

```console
$ ls -lah
total 24K
drwxr-xr-x   4 user  staff   128B Apr 10 15:35 .
drwxr-xr-x  15 user  staff   480B Apr 10 15:00 ..
-rw-r--r--   1 user  staff    74B Apr 10 15:20 .hidden
-rw-r--r--   1 user  staff   1.0K Apr 10 15:30 document.txt
drwxr-xr-x   3 user  staff    96B Apr 9  14:22 projects
```

### 特定のディレクトリの内容を表示
```console
$ ls -l projects
total 8
-rw-r--r--  1 user  staff  512 Apr 9 14:20 README.md
```

### 最新のファイルを先に表示
```console
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

## よくある質問

### Q1. `ls` コマンドの基本的な使い方は？
A. 引数なしで `ls` を実行すると、現在のディレクトリ内のファイルとフォルダが表示されます。

### Q2. 隠しファイルを表示するには？
A. `ls -a` を使用します。これにより、ドット（`.`）で始まるファイルも表示されます。

### Q3. ファイルの詳細情報を見るには？
A. `ls -l` を使用すると、権限、所有者、サイズ、最終更新日時などの詳細情報が表示されます。

### Q4. ファイルを更新日時順に並べるには？
A. `ls -t` を使用すると最新のファイルから順に表示され、`ls -tr` を使用すると古いファイルから順に表示されます。

### Q5. ディレクトリのサイズを確認するには？
A. `ls -ld ディレクトリ名` を使用します。ただし、これはディレクトリ自体のサイズであり、中身の合計サイズではありません。

## 追加情報

- カラー表示を有効にするには `ls --color=auto`（LinuxなどのGNU系）または `ls -G`（macOS）を使用します。
- 多くのシステムでは、`ls` コマンドに対するエイリアスが設定されており、自動的にカラー表示などが有効になっていることがあります。
- macOSでは、`ls` コマンドの動作がLinuxとは若干異なる場合があります。例えば、GNU版の `ls` では `--color` オプションが使えますが、macOSでは `-G` を使います。

## macOSでの注意点

- macOSの `ls` コマンドはBSD由来であり、GNU版とは一部オプションが異なります。
- カラー表示には `-G` オプションを使用します（GNU版では `--color`）。
- macOSでGNU版の `ls` を使いたい場合は、Homebrewなどのパッケージマネージャで `coreutils` をインストールし、`gls` コマンドを使用できます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html