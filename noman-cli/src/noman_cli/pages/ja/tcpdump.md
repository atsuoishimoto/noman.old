# tcpdump コマンド
ネットワークインターフェイス上のパケットをキャプチャして分析するためのコマンドラインツール。

## 概要
tcpdumpはネットワークトラフィックをリアルタイムでキャプチャし、分析するためのパワフルなツールです。特定のインターフェイス上を流れるパケットをキャプチャし、その内容を表示したり、ファイルに保存したりすることができます。ネットワークの問題診断やセキュリティ監視に非常に役立ちます。

## オプション
### **-i**
キャプチャするネットワークインターフェイスを指定します。
```console
$ tcpdump -i eth0
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:45:22.123456 IP 192.168.1.100.52134 > 192.168.1.1.53: 12345+ A? example.com. (32)
13:45:22.234567 IP 192.168.1.1.53 > 192.168.1.100.52134: 12345 1/0/0 A 93.184.216.34 (48)
```

### **-n**
ホスト名、ポート名などの名前解決を行わず、IPアドレスやポート番号をそのまま表示します。
```console
$ tcpdump -n
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:46:33.123456 IP 192.168.1.100.52134 > 8.8.8.8.53: 12345+ A? example.com. (32)
13:46:33.234567 IP 8.8.8.8.53 > 192.168.1.100.52134: 12345 1/0/0 A 93.184.216.34 (48)
```

### **-w**
キャプチャしたパケットをファイルに保存します。
```console
$ tcpdump -w capture.pcap
tcpdump: listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
^C
45 packets captured
50 packets received by filter
0 packets dropped by kernel
```

### **-r**
保存されたパケットキャプチャファイルを読み込んで表示します。
```console
$ tcpdump -r capture.pcap
reading from file capture.pcap, link-type EN10MB (Ethernet)
13:48:22.123456 IP host1.52134 > host2.53: 12345+ A? example.com. (32)
13:48:22.234567 IP host2.53 > host1.52134: 12345 1/0/0 A 93.184.216.34 (48)
```

## 使用例
### 特定のホストとの通信をキャプチャ
```console
$ tcpdump host 192.168.1.100
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:50:22.123456 IP 192.168.1.100.52134 > dns.google.53: 12345+ A? example.com. (32)
13:50:22.234567 IP dns.google.53 > 192.168.1.100.52134: 12345 1/0/0 A 93.184.216.34 (48)
```

### 特定のポートの通信をキャプチャ
```console
$ tcpdump port 80
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:51:22.123456 IP client.52134 > server.80: Flags [S], seq 1234567890, win 65535, options [mss 1460], length 0
13:51:22.234567 IP server.80 > client.52134: Flags [S.], seq 2345678901, ack 1234567891, win 65535, options [mss 1460], length 0
```

### HTTPトラフィックの内容を表示
```console
$ tcpdump -A -s0 port 80
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on en0, link-type EN10MB (Ethernet), capture size 262144 bytes
13:52:22.123456 IP client.52134 > server.80: Flags [P.], seq 1:165, ack 1, win 65535, length 164
GET / HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Accept: text/html,application/xhtml+xml
Connection: keep-alive

13:52:22.234567 IP server.80 > client.52134: Flags [P.], seq 1:239, ack 165, win 65535, length 238
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 1256
Connection: keep-alive

<!DOCTYPE html>...
```

## ヒント:
### 権限の問題
tcpdumpはパケットキャプチャのために特権が必要なため、通常はroot権限またはsudo経由で実行する必要があります。

### フィルタ式の活用
`host`、`port`、`tcp`、`udp`などのフィルタ式を組み合わせることで、必要なトラフィックだけをキャプチャできます。例えば `tcpdump 'tcp port 80 and host 192.168.1.100'` のように指定できます。

### Wiresharkとの連携
`-w` オプションで保存したキャプチャファイル（.pcap）はWiresharkで開いて詳細に分析することができます。

### パケットサイズの調整
デフォルトでは先頭の数バイトしかキャプチャしないことがあります。完全なパケットをキャプチャするには `-s0` オプションを使用します。

## よくある質問
#### Q1. tcpdumpを実行すると「permission denied」エラーが出ます。どうすればよいですか？
A. tcpdumpはネットワークインターフェイスに直接アクセスするため、root権限が必要です。`sudo tcpdump` のように実行してください。

#### Q2. 利用可能なネットワークインターフェイスを確認するにはどうすればよいですか？
A. `tcpdump -D` コマンドを実行すると、利用可能なインターフェイスの一覧が表示されます。

#### Q3. キャプチャしたパケットの数を制限するにはどうすればよいですか？
A. `-c` オプションを使用します。例えば `tcpdump -c 100` とすると、100パケットをキャプチャした後に自動的に停止します。

#### Q4. 特定のプロトコルだけをキャプチャするにはどうすればよいですか？
A. プロトコル名をフィルタとして指定します。例えば `tcpdump icmp` とすると、ICMPパケットのみをキャプチャします。

## macOSでの注意点
macOSでは、セキュリティ設定によってtcpdumpの実行が制限される場合があります。システム環境設定のセキュリティとプライバシーで許可が必要になることがあります。また、最新のmacOSではパケットキャプチャのためのアクセス許可を明示的に与える必要がある場合があります。

## 参考
https://www.tcpdump.org/manpages/tcpdump.1.html

## 改訂履歴
- 2025/04/29 初版作成