# tcpdump コマンド

ネットワークパケットをキャプチャして分析するためのコマンドラインツール。

## 概要

`tcpdump`は、ネットワークインターフェイスを通過するパケットをキャプチャし、表示するためのパワフルなコマンドラインツールです。ネットワークのトラブルシューティングやセキュリティ分析、ネットワークトラフィックの監視に非常に役立ちます。特定のホスト、ポート、プロトコルに基づいてパケットをフィルタリングする機能も備えています。

## オプション

### **-i インターフェイス**

特定のネットワークインターフェイスからパケットをキャプチャします。

```console
$ sudo tcpdump -i eth0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:45:22.123456 IP 192.168.1.100.56789 > 8.8.8.8.53: 12345+ A? example.com. (32)
```

### **-n**

ホスト名、ポート名、サービス名の名前解決を行わず、IPアドレスとポート番号をそのまま表示します。

```console
$ sudo tcpdump -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:45:22.123456 IP 192.168.1.100.56789 > 8.8.8.8.53: 12345+ A? example.com. (32)
```

### **-w ファイル名**

キャプチャしたパケットをファイルに保存します。後で`tcpdump -r`や`Wireshark`で分析できます。

```console
$ sudo tcpdump -w capture.pcap
tcpdump: listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
^C
45 packets captured
50 packets received by filter
0 packets dropped by kernel
```

### **-r ファイル名**

保存されたパケットキャプチャファイルを読み込んで表示します。

```console
$ tcpdump -r capture.pcap
reading from file capture.pcap, link-type EN10MB (Ethernet)
13:45:22.123456 IP host1.56789 > host2.80: Flags [S], seq 1234567890, win 65535, length 0
```

### **-c 数**

指定した数のパケットをキャプチャした後に停止します。

```console
$ sudo tcpdump -c 5
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
5 packets captured
8 packets received by filter
0 packets dropped by kernel
```

## 使用例

### 特定のホストとのトラフィックをキャプチャ

```console
$ sudo tcpdump host 192.168.1.100
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:45:22.123456 IP 192.168.1.100.56789 > 8.8.8.8.53: 12345+ A? example.com. (32)
13:45:22.234567 IP 8.8.8.8.53 > 192.168.1.100.56789: 12345 1/0/0 A 93.184.216.34 (48)
```

### 特定のポートのトラフィックをキャプチャ

```console
$ sudo tcpdump port 80
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:45:22.123456 IP host1.56789 > host2.80: Flags [S], seq 1234567890, win 65535, length 0
13:45:22.234567 IP host2.80 > host1.56789: Flags [S.], seq 9876543210, ack 1234567891, win 65535, length 0
```

### HTTPトラフィックの内容を表示

```console
$ sudo tcpdump -A -s 0 'tcp port 80'
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:45:22.123456 IP host1.56789 > host2.80: Flags [P.], seq 1:165, ack 1, win 65535, length 164
GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml
Connection: keep-alive

```

## ヒント:

### 管理者権限が必要

ほとんどの場合、`tcpdump`を実行するには`sudo`または管理者権限が必要です。これはネットワークインターフェイスに直接アクセスするためです。

### 複雑なフィルタ式

`tcpdump`は強力なフィルタ式をサポートしています。例えば、`tcpdump 'tcp port 80 and (src host 192.168.1.100 or dst host 192.168.1.200)'`のように複数の条件を組み合わせることができます。

### パケットサイズの制限を解除

デフォルトでは、`tcpdump`は各パケットの先頭部分のみをキャプチャします。完全なパケット内容を取得するには、`-s 0`オプションを使用します。

### Wiresharkとの連携

`tcpdump -w file.pcap`でキャプチャしたファイルは、より詳細な分析のためにWiresharkで開くことができます。

## よくある質問

#### Q1. tcpdumpとWiresharkの違いは何ですか？
A. `tcpdump`はコマンドラインツールで、リモートサーバーでも使いやすく、軽量です。Wiresharkはグラフィカルなインターフェイスを持ち、より詳細な分析機能を提供しますが、GUIが必要です。

#### Q2. 特定のIPアドレスとポートのトラフィックだけをキャプチャするにはどうすればよいですか？
A. `sudo tcpdump host 192.168.1.100 and port 80`のようにフィルタを組み合わせて使用します。

#### Q3. キャプチャしたパケットをファイルに保存するにはどうすればよいですか？
A. `sudo tcpdump -w filename.pcap`を使用します。このファイルは後で`tcpdump -r filename.pcap`やWiresharkで分析できます。

#### Q4. パケットの内容を読みやすい形式で表示するにはどうすればよいですか？
A. ASCII形式で表示するには`-A`オプション、16進数とASCII形式で表示するには`-X`オプションを使用します。

## macOSでの注意点

macOSでは、ネットワークインターフェイス名が異なる場合があります。利用可能なインターフェイスを確認するには、`ifconfig`または`networksetup -listallhardwareports`コマンドを使用してください。また、macOSのセキュリティ機能により、初回実行時に権限の承認が求められることがあります。

## 参考資料

https://www.tcpdump.org/manpages/tcpdump.1.html

## 改訂履歴

- 2025/04/30 初版作成