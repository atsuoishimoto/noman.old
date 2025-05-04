# ls コマンド

ディレクトリの内容を一覧表示します。

## 概要

`ls` コマンドは、指定した場所のファイルとディレクトリを表示します。デフォルトでは、現在のディレクトリの内容をアルファベット順に表示します。ファイルシステムを操作する際に最も頻繁に使用されるコマンドの一つです。

## オプション

### **-l** (ロングフォーマット)

各ファイルの詳細情報（権限、リンク数、所有者、グループ、サイズ、更新日時など）を表示します。

```console
$ ls -l
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-a** (すべて)

隠しファイル（ドットで始まるファイル）を含むすべてのファイルを表示します。

```console
$ ls -a
.  ..  .hidden  document.txt  projects
```

### **-h** (人間が読みやすい形式)

`-l` と組み合わせて使用すると、ファイルサイズを人間が読みやすい形式（KB、MB、GB）で表示します。

```console
$ ls -lh
total 16K
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

### **-d** (ディレクトリ)

ディレクトリの内容ではなく、ディレクトリ自体を一覧表示します。

```console
$ ls -d */
projects/  documents/  downloads/
```

### **-s** (サイズ)

各ファイルに割り当てられたブロックサイズを表示します。

```console
$ ls -s
total 16
8 document.txt  8 projects
```

### **-t** (時間)

ファイルを更新時間順（最新のものが最初）にソートします。

```console
$ ls -lt
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### **-r** (逆順)

ソート順を逆にします。

```console
$ ls -lr
total 16
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
```

## 使用例

### 複数のオプションを組み合わせる

```console
$ ls -lha
total 20K
drwxr-xr-x  4 user  staff  128B Apr 10 15:35 .
drwxr-xr-x 18 user  staff  576B Apr 10 14:00 ..
-rw-r--r--  1 user  staff   74B Apr 10 15:32 .hidden
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

### パターンによるファイルの一覧表示

```console
$ ls *.txt
document.txt  notes.txt  readme.txt
```

### サイズ順にファイルをソート（最大のものから）

```console
$ ls -lhS
total 16K
-rw-r--r--  1 user  staff  1.0K Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96B Apr 9  14:22 projects
```

## ヒント:

### カラーコード出力

多くのシステムでは、`ls` が異なるファイルタイプを異なる色で表示するように設定されています。Linuxでは `ls --color=auto`、macOSでは `ls -G` で強制的に色付けできます。

### 再帰的な一覧表示

`ls -R` を使用すると、サブディレクトリを再帰的に一覧表示し、ディレクトリツリー全体を表示できます。

### ソートオプションの組み合わせ

`-t`（時間順）と `-r`（逆順）などのソートオプションを組み合わせる場合、`-r` は常に現在のソート順を逆にすることを覚えておきましょう。例えば、`ls -ltr` は最も古いファイルを最初に表示します。

### エイリアス

多くのユーザーは、シェル設定ファイルで `ls -l` を `ll`、`ls -la` を `la` などのエイリアスを作成して、一般的な組み合わせのタイピングを省略しています。

## よくある質問

#### Q1. ディレクトリのみを一覧表示するにはどうすればよいですか？
A. 現在の場所のディレクトリのみを一覧表示するには `ls -d */` を使用します。

#### Q2. ファイルサイズを読みやすい形式で表示するにはどうすればよいですか？
A. `ls -lh` を使用すると、バイト単位ではなく KB、MB、GB でファイルサイズを表示できます。

#### Q3. ファイルをサイズ順にソートするにはどうすればよいですか？
A. `ls -lS` を使用すると、ファイルをサイズ順（最大のものが最初）にソートできます。順序を逆にするには `-r`（`ls -lSr`）を追加します。

#### Q4. 最近変更されたファイルを最初に表示するにはどうすればよいですか？
A. `ls -lt` を使用すると、最新のファイルが最初に表示されるように更新時間順にソートできます。

#### Q5. ファイルをiノード番号と一緒に表示するにはどうすればよいですか？
A. `ls -i` を使用すると、各ファイルのインデックス番号（iノード）が表示されます。

## macOSに関する注意点

macOSでは、一部のGNU lsオプションが利用できなかったり、動作が異なる場合があります：
- カラー出力を有効にするには、`--color` の代わりに `-G` を使用します
- `-h` オプションはLinuxと同じように動作します
- 拡張属性を表示するには、macOS固有の `ls -@` を使用します

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/ls-invocation.html

## 改訂履歴

- 2025/05/04 -d, -s, -t, -r オプションとmacOSに関する注意点を追加しました。