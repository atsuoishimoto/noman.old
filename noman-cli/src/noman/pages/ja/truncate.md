# truncate コマンド

ファイルのサイズを指定したサイズに縮小または拡張します。

## 概要

`truncate` コマンドは、ファイルのサイズを縮小または拡張して指定した長さに変更します。存在しないファイルを新規作成することもでき、複数のファイルを一度に同じサイズに設定できます。特定のサイズのファイルを素早く作成したり、ログファイルを切り詰めたりするのに便利です。

## オプション

### **-s, --size=SIZE**

ファイルサイズを SIZE バイトに設定または調整します

```console
$ truncate -s 100 myfile.txt
$ ls -l myfile.txt
-rw-r--r-- 1 user group 100 May 4 10:15 myfile.txt
```

### **-c, --no-create**

存在しないファイルを作成しません

```console
$ truncate -c -s 50 nonexistent.txt
truncate: cannot open 'nonexistent.txt' for writing: No such file or directory
```

### **-o, --io-blocks**

SIZE をバイト数ではなく IO ブロック数として扱います

```console
$ truncate -o -s 2 blockfile.dat
```

### **-r, --reference=RFILE**

RFILE のサイズに基づいてサイズを設定します

```console
$ truncate -r reference.txt target.txt
```

## 使用例

### 特定のサイズの新しい空ファイルを作成する

```console
$ truncate -s 1M largefile.bin
$ ls -lh largefile.bin
-rw-r--r-- 1 user group 1.0M May 4 10:20 largefile.bin
```

### 既存のファイルを縮小する

```console
$ echo "This is a test file with some content" > testfile.txt
$ truncate -s 10 testfile.txt
$ cat testfile.txt
This is a 
```

### 相対サイズの使用

```console
$ truncate -s 100 myfile.txt    # 正確に100バイトに設定
$ truncate -s +50 myfile.txt    # 50バイト追加（現在150バイト）
$ truncate -s -30 myfile.txt    # 30バイト削除（現在120バイト）
$ truncate -s %64 myfile.txt    # サイズを64の倍数に切り下げ（96バイト）
```

## ヒント:

### ゼロ埋めと切り詰め

ファイルを拡張する場合、`truncate` は新しい領域をゼロやその他のデータで埋めるわけではなく、単にファイルサイズを拡張します。これにより、拡張された部分が実際に書き込まれるまでディスク容量を使用しない「スパースファイル」が作成されます。

### 簡易ログローテーション

`truncate -s 0` を使用すると、ファイルを削除せずにログファイルを素早く空にでき、ファイルのパーミッションと所有権が保持されます：

```console
$ truncate -s 0 /path/to/logfile.log
```

### テストファイルの作成

ディスク容量やファイル転送操作をテストするための特定サイズのテストファイルを作成できます：

```console
$ truncate -s 10M test10mb.bin
$ truncate -s 1G test1gb.bin
```

## よくある質問

#### Q1. `truncate` と `touch` の違いは何ですか？
A. `touch` はタイムスタンプを更新し、空のファイルを作成できますが、`truncate` は特定のサイズのファイルを作成したり、既存のファイルサイズを変更したりできます。

#### Q2. `truncate` は実際にディスク容量を割り当てますか？
A. ファイルを拡張する場合、`truncate` はスパースファイルを作成し、データが書き込まれるまで実際にはディスク容量を消費しません。

#### Q3. `truncate` を使ってファイルにデータを追加できますか？
A. いいえ、`truncate` はコンテンツを追加せずにファイルサイズのみを変更します。データを追加するには、リダイレクション（`>>`）や `echo`、`cat` などのツールを使用してください。

#### Q4. ファイルを削除せずに完全に空にするにはどうすればよいですか？
A. `truncate -s 0 ファイル名` を使用して、ファイル自体を保持したままファイルサイズをゼロに減らします。

## References

https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html

## Revisions

- 2025/05/04 初回リビジョン