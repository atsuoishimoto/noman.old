# tcpdump コマンド

ネットワークトラフィックをキャプチャして分析するツール。

## 概要

`tcpdump` は強力なコマンドラインパケットアナライザで、ネットワークインターフェースを通じて送受信されるネットワークパケットをキャプチャして表示することができます。ネットワークのトラブルシューティング、セキュリティ分析、ネットワークアクティビティの監視によく使用されます。このツールは様々な条件でパケットをフィルタリングし、パケットの内容を異なる形式で表示することができます。

## オプション

### **-i インターフェース**

パケットをキャプチャするネットワークインターフェースを指定します

```console
$ tcpdump -i eth0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:45:22.357928 IP host1.ssh > host2.52986: Flags [P.], seq 196:392, ack 1, win 501, options [nop,nop,TS val 1089067 ecr 1089067], length 196
```

### **-n**

アドレス（ホストアドレス、ポート番号など）を名前に変換しません

```console
$ tcpdump -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:46:15.123456 IP 192.168.1.100.22 > 192.168.1.101.52986: Flags [P.], seq 196:392, ack 1, win 501, length 196
```

### **-c カウント**

指定した数のパケットをキャプチャした後に終了します

```console
$ tcpdump -c 5
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:47:01.123456 IP host1.ssh > host2.52986: Flags [P.], seq 196:392, ack 1, win 501, length 196
13:47:01.234567 IP host2.52986 > host1.ssh: Flags [.], ack 392, win 501, length 0
13:47:01.345678 IP host1.ssh > host2.52986: Flags [P.], seq 392:588, ack 1, win 501, length 196
13:47:01.456789 IP host2.52986 > host1.ssh: Flags [.], ack 588, win 501, length 0
13:47:01.567890 IP host1.ssh > host2.52986: Flags [P.], seq 588:784, ack 1, win 501, length 196
5 packets captured
10 packets received by filter
0 packets dropped by kernel
```

### **-w ファイル**

パケットを解析・表示する代わりに、生のパケットをファイルに書き込みます

```console
$ tcpdump -w capture.pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
^C
45 packets captured
50 packets received by filter
0 packets dropped by kernel
```

### **-r ファイル**

ファイル（以前に -w で作成したもの）からパケットを読み込みます

```console
$ tcpdump -r capture.pcap
reading from file capture.pcap, link-type EN10MB (Ethernet)
13:50:01.123456 IP host1.ssh > host2.52986: Flags [P.], seq 196:392, ack 1, win 501, length 196
13:50:01.234567 IP host2.52986 > host1.ssh: Flags [.], ack 392, win 501, length 0
```

### **-v, -vv, -vvv**

詳細レベルを上げます（より多くのパケット情報を表示）

```console
$ tcpdump -vv
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:51:22.357928 IP (tos 0x10, ttl 64, id 12345, offset 0, flags [DF], proto TCP (6), length 240) host1.ssh > host2.52986: Flags [P.], cksum 0x1234 (correct), seq 196:392, ack 1, win 501, options [nop,nop,TS val 1089067 ecr 1089067], length 196
```

## 使用例

### ポート80（HTTP）のTCPトラフィックをキャプチャする

```console
$ tcpdump -i eth0 tcp port 80
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:55:01.123456 IP host1.52986 > webserver.http: Flags [S], seq 123456789, win 64240, options [mss 1460,sackOK,TS val 1089067 ecr 0,nop,wscale 7], length 0
13:55:01.234567 IP webserver.http > host1.52986: Flags [S.], seq 987654321, ack 123456790, win 65535, options [mss 1460,sackOK,TS val 1089067 ecr 1089067,nop,wscale 7], length 0
```

### 特定のホストからのトラフィックをキャプチャする

```console
$ tcpdump -i eth0 host 192.168.1.100
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:56:01.123456 IP 192.168.1.100.22 > 192.168.1.101.52986: Flags [P.], seq 196:392, ack 1, win 501, length 196
13:56:01.234567 IP 192.168.1.101.52986 > 192.168.1.100.22: Flags [.], ack 392, win 501, length 0
```

### タイムスタンプ付きでパケットをキャプチャして保存する

```console
$ tcpdump -i eth0 -w capture_$(date +%Y%m%d_%H%M%S).pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
^C
120 packets captured
125 packets received by filter
0 packets dropped by kernel
```

## ヒント:

### 管理者権限で実行する

ほとんどのシステムではパケットをキャプチャするために管理者権限が必要です。必要な権限を確保するために `sudo tcpdump` を使用しましょう。

### 式を使用してトラフィックをフィルタリングする

`and`、`or`、`not` を組み合わせて複雑なフィルタを作成できます：
```console
$ tcpdump -i eth0 'tcp port 80 and not host 192.168.1.5'
```

### パケットキャプチャサイズを制限する

`-s snaplen` を使用して、パケットごとにキャプチャするバイト数を制限できます。ヘッダーのみの場合は `-s 96` を使用します：
```console
$ tcpdump -i eth0 -s 96 -c 100
```

### 名前解決を無効にして出力を高速化する

`-n` を使用してホスト名の解決を無効にし、`-nn` を使用してホスト名とポート名の両方の解決を無効にすると、tcpdumpの実行が速くなります：
```console
$ tcpdump -i eth0 -nn
```

## よくある質問

#### Q1. すべてのインターフェースでパケットをキャプチャするにはどうすればよいですか？
A. `tcpdump -i any` を使用して、すべてのインターフェースでキャプチャできます。

#### Q2. パケットの内容をASCIIで見るにはどうすればよいですか？
A. `-A` フラグを使用して各パケットをASCIIで表示するか、`-X` を使用して16進数とASCII両方の出力を表示できます。

#### Q3. キャプチャしたパケットを後で分析するために保存するにはどうすればよいですか？
A. `tcpdump -w ファイル名.pcap` を使用して生のパケットを保存し、後で `tcpdump -r ファイル名.pcap` またはWiresharkなどのツールで分析できます。

#### Q4. IPアドレスでパケットをフィルタリングするにはどうすればよいですか？
A. `tcpdump host 192.168.1.100` を使用して、そのIPとの間のトラフィックをキャプチャするか、`src host` または `dst host` を使用して方向を指定できます。

#### Q5. TCP SYNパケットのみをキャプチャするにはどうすればよいですか？
A. `tcpdump 'tcp[tcpflags] & (tcp-syn) != 0'` を使用してTCP SYNパケットをキャプチャできます。

## 参考文献

https://www.tcpdump.org/manpages/tcpdump.1.html

## Revisions

- 2025/05/04 初回リビジョン