# dd コマンド

ファイルのブロックレベル操作によるコピーと変換を行います。

## 概要

`dd`はデータのコピーと変換を行うコマンドラインユーティリティです。標準的なコピーコマンドとは異なり、ブロックサイズ、バイト順序、データ変換を精密に制御できます。ディスクイメージの作成、パーティションのバックアップ、ファイル形式の変換、低レベルデータ操作によく使用されます。

## オプション

### **if=FILE, --input=FILE**

読み込み元の入力ファイルを指定します（デフォルトは標準入力）

```console
$ dd if=/dev/sda
```

### **of=FILE, --output=FILE**

書き込み先の出力ファイルを指定します（デフォルトは標準出力）

```console
$ dd if=/dev/sda of=/dev/sdb
```

### **bs=BYTES, --block-size=BYTES**

入力と出力の両方のブロックサイズをBYTESに設定します

```console
$ dd if=/dev/zero of=testfile bs=1M count=10
10+0 records in
10+0 records out
10485760 bytes (10 MB, 10 MiB) copied, 0.0119631 s, 876 MB/s
```

### **count=N, --count=N**

N個の入力ブロックだけをコピーします

```console
$ dd if=/dev/urandom of=random.dat bs=1M count=5
5+0 records in
5+0 records out
5242880 bytes (5.2 MB, 5.0 MiB) copied, 0.0452266 s, 116 MB/s
```

### **status=LEVEL, --status=LEVEL**

表示される情報のレベルを制御します（none, noxfer, progress）

```console
$ dd if=/dev/zero of=testfile bs=1M count=100 status=progress
51380224 bytes (51 MB, 49 MiB) copied, 0.0519088 s, 990 MB/s
100+0 records in
100+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 0.105822 s, 991 MB/s
```

### **conv=CONVS, --conv=CONVS**

カンマ区切りの記号リストに従ってファイルを変換します

```console
$ dd if=input.txt of=output.txt conv=ucase
```

## 使用例

### ディスクイメージの作成

```console
$ dd if=/dev/sda of=disk.img bs=4M status=progress
8589934592 bytes (8.6 GB, 8.0 GiB) copied, 126 s, 68.2 MB/s
2048+0 records in
2048+0 records out
8589934592 bytes (8.6 GB, 8.0 GiB) copied, 126.453 s, 67.9 MB/s
```

### ブート可能なUSBドライブの作成

```console
$ sudo dd if=ubuntu.iso of=/dev/sdb bs=4M status=progress conv=fsync
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 35.6279 s, 30.1 MB/s
256+0 records in
256+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 35.6423 s, 30.1 MB/s
```

### ゼロで埋められたファイルの作成

```console
$ dd if=/dev/zero of=zeros.bin bs=1M count=100
100+0 records in
100+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 0.101822 s, 1.0 GB/s
```

## ヒント:

### 長時間の操作にはstatus=progressを使用する

時間のかかる操作では、`status=progress`を使用してコピー処理のリアルタイム情報を確認できます。

### ブロックデバイスの取り扱いに注意

`/dev/sda`のようなブロックデバイスを扱う場合は、実行前にコマンドを二重チェックしてください。間違えると重要なデータが上書きされる可能性があります。

### ブロックサイズでパフォーマンスを最適化

大きな転送には大きなブロックサイズ（`bs=4M`や`bs=8M`など）を使用するとパフォーマンスが向上しますが、非常に大きな値が常に良いとは限りません。

### USBドライブにはfsyncを使用

USBドライブに書き込む場合は、`conv=fsync`を追加して、ddが完了する前にすべてのデータがデバイスに書き込まれるようにしましょう。

### MBRのバックアップ

マスターブートレコードだけをバックアップするには：`sudo dd if=/dev/sda of=mbr.bin bs=512 count=1`

## よくある質問

#### Q1. ハードドライブ全体をクローンするにはどうすればよいですか？
A. `dd if=/dev/source_drive of=/dev/destination_drive bs=4M status=progress`を使用します。コピー先のドライブがコピー元と同じかそれ以上のサイズであることを確認してください。

#### Q2. なぜddは「ディスクデストロイヤー」と呼ばれるのですか？
A. この愛称は、誤って使用するとデータ損失を引き起こす可能性があることに由来します。ddコマンドを実行する前に、必ずデバイス名を二重確認してください。

#### Q3. ddを高速化するにはどうすればよいですか？
A. ブロックサイズ（bs）パラメータを4Mや8Mなどの値に増やし、不要な変換を避けてください。

#### Q4. 特定のサイズのファイルを作成するにはどうすればよいですか？
A. `dd if=/dev/zero of=ファイル名 bs=1M count=X`を使用します。Xは希望するサイズ（メガバイト単位）です。

#### Q5. ddの進行状況を監視するにはどうすればよいですか？
A. 新しいバージョンでは`status=progress`オプションを使用します。古いバージョンでは、ddプロセスにUSR1シグナルを送信できます：`kill -USR1 $(pgrep dd)`

## References

https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html

## Revisions

- 2025/05/04 初回リビジョン