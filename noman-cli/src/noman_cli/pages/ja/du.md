# du コマンド

ディスク使用量を表示するコマンドです。

## 概要

`du`（disk usage）コマンドは、ファイルやディレクトリが使用しているディスク容量を表示します。デフォルトでは、指定したディレクトリとそのサブディレクトリのサイズを表示します。ストレージ容量の管理や、大きなファイルやディレクトリを特定するのに役立ちます。

## オプション

### **-h, --human-readable**

サイズを人間が読みやすい形式（K, M, G）で表示します。

```console
$ du -h Documents
4.0K    Documents/notes
8.0K    Documents/projects/old
16K     Documents/projects
24K     Documents
```

### **-s, --summarize**

指定したディレクトリの合計サイズのみを表示します。

```console
$ du -s Documents
24      Documents
```

### **-a, --all**

ディレクトリだけでなく、すべてのファイルのサイズも表示します。

```console
$ du -a Documents
4       Documents/notes/todo.txt
4       Documents/notes
8       Documents/projects/old/backup.zip
8       Documents/projects/old
4       Documents/projects/current.doc
16      Documents/projects
24      Documents
```

### **-c, --total**

全体の合計を最後に表示します。

```console
$ du -c Documents
24      Documents
24      合計
```

### **--max-depth=N**

指定した深さまでのディレクトリのみ表示します。

```console
$ du -h --max-depth=1 Documents
16K     Documents/projects
4.0K    Documents/notes
24K     Documents
```

## 使用例

### 特定のディレクトリの容量を人間が読みやすい形式で確認

```console
$ du -sh /var/log
156M    /var/log
```

### 現在のディレクトリで最も容量を使用しているディレクトリを特定

```console
$ du -h --max-depth=1 | sort -hr
1.2G    .
820M    ./Videos
245M    ./Pictures
98M     ./Documents
42M     ./Music
```

### 特定のファイルタイプの合計サイズを確認

```console
$ find . -name "*.mp4" -exec du -ch {} \; | grep 合計
1.5G    合計
```

## ヒント:

### 大きなファイルを素早く見つける

`du -h | sort -hr | head -10` を使用すると、最も容量を使用している10個のディレクトリを表示できます。

### パイプラインでの活用

`find` コマンドと組み合わせることで、特定のファイルタイプのディスク使用量を計算できます。

### 除外パターンの指定

`du --exclude="*.log"` のように、特定のパターンを除外してディスク使用量を計算できます。

## よくある質問

#### Q1. `du` と `df` の違いは何ですか？
A. `du` は特定のファイルやディレクトリが使用しているディスク容量を表示しますが、`df` はファイルシステム全体の使用状況（総容量、使用量、空き容量など）を表示します。

#### Q2. なぜ `du` と `ls -l` で表示されるサイズが異なるのですか？
A. `ls -l` はファイルの実際のサイズを表示しますが、`du` はファイルが占めるディスクブロックのサイズを表示します。ファイルシステムのブロックサイズにより、小さなファイルでも最小ブロックサイズ分の容量を消費します。

#### Q3. 特定のディレクトリの合計サイズだけを知りたい場合はどうすればよいですか？
A. `du -sh ディレクトリ名` を使用すると、そのディレクトリの合計サイズのみを人間が読みやすい形式で表示できます。

## macOSでの注意点

macOSの`du`コマンドはGNU版と若干異なります。例えば、`--max-depth`オプションの代わりに`-d`を使用します。また、デフォルトのブロックサイズが異なるため、同じファイルでもLinuxとmacOSで表示される数値が異なる場合があります。

```console
$ du -d 1 -h Documents  # macOSでの深さ指定
```

## 参考

https://www.gnu.org/software/coreutils/manual/html_node/du-invocation.html

## 改訂履歴

- 2025/04/30 初版作成