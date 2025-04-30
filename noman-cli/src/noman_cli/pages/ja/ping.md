# ping コマンド

ネットワーク上のホストに対して接続性をテストし、応答時間を測定します。

## 概要

`ping`コマンドは、指定したホストやIPアドレスに対してICMP（Internet Control Message Protocol）エコーリクエストパケットを送信し、応答を確認するためのツールです。ネットワーク接続の確認、応答時間（レイテンシー）の測定、ホストの到達可能性の診断に使用されます。デフォルトでは、中断されるまで継続的にパケットを送信します。

## オプション

### **-c (count)**

送信するパケット数を指定します。指定した数のパケットを送信した後、自動的に終了します。

```console
$ ping -c 4 google.com
PING google.com (142.250.196.110): 56 data bytes
64 bytes from 142.250.196.110: icmp_seq=0 ttl=116 time=5.127 ms
64 bytes from 142.250.196.110: icmp_seq=1 ttl=116 time=5.834 ms
64 bytes from 142.250.196.110: icmp_seq=2 ttl=116 time=5.418 ms
64 bytes from 142.250.196.110: icmp_seq=3 ttl=116 time=5.283 ms

--- google.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 5.127/5.416/5.834/0.255 ms
```

### **-i (interval)**

パケットを送信する間隔を秒単位で指定します。デフォルトは1秒です。

```console
$ ping -i 2 -c 3 example.com
PING example.com (93.184.216.34): 56 data bytes
64 bytes from 93.184.216.34: icmp_seq=0 ttl=56 time=15.321 ms
64 bytes from 93.184.216.34: icmp_seq=1 ttl=56 time=15.189 ms
64 bytes from 93.184.216.34: icmp_seq=2 ttl=56 time=15.244 ms

--- example.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 15.189/15.251/15.321/0.055 ms
```

### **-t (ttl)**

送信パケットのTTL（Time To Live）値を設定します。これはパケットが通過できるルーターの最大数を制限します。

```console
$ ping -t 64 -c 2 github.com
PING github.com (140.82.121.4): 56 data bytes
64 bytes from 140.82.121.4: icmp_seq=0 ttl=64 time=120.321 ms
64 bytes from 140.82.121.4: icmp_seq=1 ttl=64 time=119.189 ms

--- github.com ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 119.189/119.755/120.321/0.566 ms
```

### **-s (size)**

送信するパケットのサイズをバイト単位で指定します。デフォルトは56バイトです。

```console
$ ping -s 100 -c 2 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 100 data bytes
108 bytes from 8.8.8.8: icmp_seq=0 ttl=116 time=4.127 ms
108 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=4.834 ms

--- 8.8.8.8 ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 4.127/4.481/4.834/0.354 ms
```

## 使用例

### 基本的な接続テスト

```console
$ ping google.com
PING google.com (142.250.196.110): 56 data bytes
64 bytes from 142.250.196.110: icmp_seq=0 ttl=116 time=5.127 ms
64 bytes from 142.250.196.110: icmp_seq=1 ttl=116 time=5.834 ms
64 bytes from 142.250.196.110: icmp_seq=2 ttl=116 time=5.418 ms
^C
--- google.com ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 5.127/5.460/5.834/0.294 ms
```

### IPアドレスへのping

```console
$ ping -c 3 8.8.8.8
PING 8.8.8.8 (8.8.8.8): 56 data bytes
64 bytes from 8.8.8.8: icmp_seq=0 ttl=116 time=4.127 ms
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=4.834 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=4.418 ms

--- 8.8.8.8 ping statistics ---
3 packets transmitted, 3 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 4.127/4.460/4.834/0.294 ms
```

### パケットロスの確認

```console
$ ping -c 10 unstable-server.example
PING unstable-server.example (192.168.1.100): 56 data bytes
64 bytes from 192.168.1.100: icmp_seq=0 ttl=64 time=2.127 ms
64 bytes from 192.168.1.100: icmp_seq=1 ttl=64 time=2.834 ms
Request timeout for icmp_seq 2
64 bytes from 192.168.1.100: icmp_seq=3 ttl=64 time=2.418 ms
Request timeout for icmp_seq 4

--- unstable-server.example ping statistics ---
10 packets transmitted, 8 packets received, 20.0% packet loss
round-trip min/avg/max/stddev = 2.127/2.460/2.834/0.294 ms
```

## ヒント:

### Ctrl+Cで終了

pingは指定した回数（-cオプション）がない場合、手動で停止するまで実行され続けます。Ctrl+Cを押すことで実行を中断できます。

### パケットロスの確認

パケットロスの割合は、ネットワークの安定性を示す重要な指標です。0%が理想的で、高いパケットロスはネットワークの問題を示しています。

### 応答時間の解釈

一般的に、ローカルネットワークでは1ms未満、同じ地域内のサーバーでは10-20ms、国際的な接続では100ms以上の応答時間が一般的です。応答時間が長いほど、接続が遅いことを意味します。

### macOSでの注意点

macOSでは、pingコマンドのオプションがLinuxとは若干異なる場合があります。例えば、永続的にpingを実行する`-t`オプション（Windowsで使用）はmacOSでは使用できず、代わりに`-c`オプションで回数を指定するか、オプションなしで実行して手動で停止する必要があります。

## よくある質問

#### Q1. pingが通らない場合は何を意味していますか？
A. ホストが応答していない、ファイアウォールがICMPパケットをブロックしている、ネットワーク接続に問題がある、またはホストが存在しない可能性があります。

#### Q2. pingの応答時間は何を示していますか？
A. 応答時間（ミリ秒単位）は、パケットが送信先に到達して戻ってくるまでの時間を示します。これはネットワークの遅延（レイテンシー）の指標となります。

#### Q3. pingコマンドを永続的に実行するにはどうすればよいですか？
A. macOSやLinuxでは、オプションなしで`ping`を実行すると、Ctrl+Cで停止するまで継続的に実行されます。特定の回数だけ実行するには`-c`オプションを使用します。

#### Q4. pingでIPv6アドレスをテストするにはどうすればよいですか？
A. macOSでは`ping6`コマンドまたは`ping -6`を使用してIPv6アドレスをテストできます。

## 参考

https://linux.die.net/man/8/ping

## 改訂履歴

- 2025/04/30 初版作成