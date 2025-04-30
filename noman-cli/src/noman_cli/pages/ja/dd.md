# dd コマンド

ファイルの変換とコピーを行うユーティリティ。

## 概要

`dd` コマンドは、ファイルをブロック単位でコピー・変換するための低レベルなユーティリティです。主にディスクイメージの作成、バックアップ、データ復旧、ディスクのクローン作成などに使用されます。他のコピーコマンドと異なり、生のデバイスファイルを直接扱うことができるため、システム管理やフォレンジック調査で重宝されます。

## オプション

### **if=ファイル**

入力ファイル（input file）を指定します。指定しない場合は標準入力から読み込みます。

```console
$ dd if=/dev/zero of=zeros.bin count=1 bs=1M
1+0 records in
1+0 records out
1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.00209056 s, 501 MB/s
```

### **of=ファイル**

出力ファイル（output file）を指定します。指定しない場合は標準出力に書き込みます。

```console
$ dd if=/dev/urandom of=random.bin count=1 bs=1M
1+0 records in
1+0 records out
1048576 bytes (1.0 MB, 1.0 MiB) copied, 0.0826016 s, 12.7 MB/s
```

### **bs=バイト数**

一度に読み書きするブロックサイズを指定します。K（キロバイト）、M（メガバイト）、G（ギガバイト）などの単位を使用できます。

```console
$ dd if=/dev/zero of=test.img bs=1M count=10
10+0 records in
10+0 records out
10485760 bytes (10 MB, 10 MiB) copied, 0.0151831 s, 691 MB/s
```

### **count=ブロック数**

コピーするブロック数を指定します。

```console
$ dd if=/dev/urandom of=small.bin bs=512 count=2
2+0 records in
2+0 records out
1024 bytes (1.0 kB, 1.0 KiB) copied, 0.000246534 s, 4.2 MB/s
```

### **status=progress**

コピー処理の進行状況をリアルタイムで表示します。

```console
$ dd if=/dev/zero of=large.bin bs=1M count=100 status=progress
51380224 bytes (51 MB, 49 MiB) copied, 0.0507088 s, 1.0 GB/s
100+0 records in
100+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 0.101418 s, 1.0 GB/s
```

## 使用例

### USBメモリにISOイメージを書き込む

```console
$ sudo dd if=ubuntu.iso of=/dev/sdb bs=4M status=progress
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 85.3209 s, 12.6 MB/s
1324+1 records in
1324+1 records out
5555200000 bytes (5.6 GB, 5.2 GiB) copied, 440.221 s, 12.6 MB/s
```

### ディスクのバックアップを作成する

```console
$ sudo dd if=/dev/sda of=disk_backup.img bs=4M status=progress
8589934592 bytes (8.6 GB, 8.0 GiB) copied, 180.5 s, 47.6 MB/s
2048+0 records in
2048+0 records out
8589934592 bytes (8.6 GB, 8.0 GiB) copied, 190.749 s, 45.0 MB/s
```

### ファイルの一部を抽出する

```console
$ dd if=large_file.bin of=extract.bin bs=1M skip=10 count=5
5+0 records in
5+0 records out
5242880 bytes (5.2 MB, 5.0 MiB) copied, 0.00623305 s, 841 MB/s
```

## ヒント:

### シグナルで進捗状況を確認する

長時間実行中の `dd` コマンドの進捗状況を確認するには、`USR1` シグナルを送信します。

```console
$ # 別のターミナルで以下を実行
$ killall -USR1 dd
```

### データ消去に使用する

ディスクを安全に消去するには、ランダムデータで上書きします。

```console
$ sudo dd if=/dev/urandom of=/dev/sdb bs=4M status=progress
```

### 注意点

`dd` は「データ破壊者（Disk Destroyer）」とも呼ばれるほど危険なコマンドです。特に `of` パラメータには細心の注意を払い、間違ったデバイスを指定しないようにしましょう。

## よくある質問

#### Q1. ddコマンドの名前の由来は何ですか？
A. IBMのメインフレームJCLの「データ定義（Data Definition）」コマンドに由来するとされています。

#### Q2. ddコマンドとcpコマンドの違いは何ですか？
A. `dd` はブロック単位でデータをコピーし、生のデバイスファイルを扱えます。また、コピー中にデータ変換も可能です。一方、`cp` はファイルシステムレベルでのコピーに特化しています。

#### Q3. ddコマンドでUSBにISOを書き込む際の注意点は？
A. 出力先（`of=`）に正しいデバイスを指定することが重要です。間違えると重要なデータを失う可能性があります。また、書き込み前にUSBをアンマウントしておく必要があります。

#### Q4. ddコマンドの実行が遅いのですが、速くする方法はありますか？
A. `bs` パラメータを大きくすると（例：`bs=4M`）、一般的にパフォーマンスが向上します。ただし、あまり大きすぎる値は逆効果になることもあります。

## macOSでの注意点

macOSでは、デバイスパスが異なります。例えば、USBドライブは `/dev/diskN` の形式（Nは数字）で、`diskutil list` コマンドで確認できます。また、書き込み前に `diskutil unmountDisk /dev/diskN` でアンマウントする必要があります。

```console
$ diskutil list
$ diskutil unmountDisk /dev/disk2
$ sudo dd if=image.iso of=/dev/disk2 bs=1m
```

macOSでは、小文字の `m`（`bs=1m`）を使用することに注意してください。大文字の `M` はエラーになります。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html

## 改訂履歴

- 2025/04/30 初版作成