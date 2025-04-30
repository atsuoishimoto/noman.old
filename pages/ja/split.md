# split コマンド

ファイルを複数の小さなファイルに分割します。

## 概要

`split` コマンドは大きなファイルを複数の小さなファイルに分割するために使用されます。デフォルトでは、元のファイルを1000行ごとに分割し、「xaa」、「xab」などの名前のファイルを作成します。サイズや行数を指定して分割することも可能です。

## オプション

### **-b, --bytes=SIZE**

指定したサイズ（バイト単位）でファイルを分割します。サイズには単位（K, M, G, T, P, E, Z, Y）を付けることができます。

```console
$ split -b 1M large_file.iso
$ ls -lh xa*
-rw-r--r-- 1 user staff 1.0M Apr 30 10:00 xaa
-rw-r--r-- 1 user staff 1.0M Apr 30 10:00 xab
-rw-r--r-- 1 user staff 1.0M Apr 30 10:00 xac
-rw-r--r-- 1 user staff 500K Apr 30 10:00 xad
```

### **-l, --lines=NUMBER**

指定した行数でファイルを分割します。

```console
$ split -l 100 large_text_file.txt
$ wc -l xa*
     100 xaa
     100 xab
      50 xac
     250 合計
```

### **-d, --numeric-suffixes[=FROM]**

数字のサフィックスを使用します（アルファベットの代わりに）。

```console
$ split -d -l 100 large_text_file.txt part_
$ ls part_*
part_00  part_01  part_02
```

### **-a, --suffix-length=N**

サフィックスの長さを指定します（デフォルトは2）。

```console
$ split -a 3 -l 100 large_text_file.txt
$ ls x*
xaaa xaab xaac
```

## 使用例

### 大きなファイルを特定のサイズに分割する

```console
$ split -b 10M large_video.mp4 video_part_
$ ls -lh video_part_*
-rw-r--r-- 1 user staff 10M Apr 30 10:15 video_part_aa
-rw-r--r-- 1 user staff 10M Apr 30 10:15 video_part_ab
-rw-r--r-- 1 user staff 5.2M Apr 30 10:15 video_part_ac
```

### 分割したファイルを再結合する

```console
$ cat video_part_* > restored_video.mp4
$ md5sum large_video.mp4 restored_video.mp4
f7e11a5204fbb73d1a0c2a3cf5a9b3d2  large_video.mp4
f7e11a5204fbb73d1a0c2a3cf5a9b3d2  restored_video.mp4
# ハッシュ値が同じであるため、ファイルは正確に復元されたことがわかる
```

## ヒント:

### 分割と結合のワークフロー

ファイルを分割した後、元のファイルに戻すには `cat` コマンドを使用します。例えば `cat x* > original_file` のように実行します。分割ファイルの順序が重要なので、適切な命名規則を使用することをお勧めします。

### 圧縮と組み合わせる

大きなファイルを分割する前に圧縮すると、全体のサイズを削減できます：
```console
$ gzip -c large_file > large_file.gz
$ split -b 1M large_file.gz gz_part_
```

### 分割ファイルの命名

`-d` オプションと接頭辞を組み合わせると、わかりやすいファイル名を作成できます：
```console
$ split -d -b 10M backup.tar.gz backup_part_
# backup_part_00, backup_part_01 などが作成される
```

## よくある質問

#### Q1. `split` コマンドはバイナリファイルを分割しても安全ですか？
A. はい、`split` はバイナリファイルを安全に分割できます。分割されたファイルを正しい順序で結合すれば、元のファイルを完全に復元できます。

#### Q2. 分割したファイルを元に戻すにはどうすればいいですか？
A. `cat` コマンドを使用します。例：`cat xaa xab xac > original_file`。または、`cat x* > original_file` のようにワイルドカードを使用することもできます。

#### Q3. 特定のファイルサイズで分割する際の単位は何ですか？
A. `-b` オプションでは、デフォルトではバイト単位ですが、K（キロバイト）、M（メガバイト）、G（ギガバイト）などの単位を指定できます。例：`split -b 10M large_file`。

#### Q4. macOSとLinuxの `split` コマンドに違いはありますか？
A. 基本的な機能は同じですが、一部のオプションやデフォルト値が異なる場合があります。macOSの `split` は BSD 由来で、Linux の `split` は GNU 由来です。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/split-invocation.html

## 改訂履歴

- 2025/04/30 初版作成