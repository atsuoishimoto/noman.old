# ping コマンド

ネットワークホストに ICMP ECHO_REQUEST パケットを送信して接続性を確認します。

## 概要

`ping` コマンドは、IPネットワーク上のホストへの到達性をテストするネットワーク診断ツールです。送信元ホストから宛先コンピュータへのメッセージの往復時間を測定します。pingは、ターゲットホストにインターネット制御メッセージプロトコル（ICMP）エコーリクエストパケットを送信し、ICMPエコー応答を待つことで動作します。

## オプション

### **-c 回数** / **--count=回数**

指定した回数のECHO_REQUESTパケットを送信（および受信）した後に停止します。

```console
$ ping -c 4 google.com
PING google.com (142.250.190.78) 56(84) bytes of data.
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=1 ttl=116 time=15.2 ms
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=2 ttl=116 time=14.8 ms
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=3 ttl=116 time=15.0 ms
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=4 ttl=116 time=14.9 ms

--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3005ms
rtt min/avg/max/mdev = 14.816/14.979/15.201/0.158 ms
```

### **-i 間隔** / **--interval=間隔**

各パケットの送信間隔を秒単位で指定します。デフォルトでは各パケット間に1秒待機します。

```console
$ ping -c 3 -i 2 example.com
PING example.com (93.184.216.34) 56(84) bytes of data.
64 bytes from 93.184.216.34: icmp_seq=1 ttl=56 time=11.8 ms
64 bytes from 93.184.216.34: icmp_seq=2 ttl=56 time=12.1 ms
64 bytes from 93.184.216.34: icmp_seq=3 ttl=56 time=11.9 ms

--- example.com ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 4005ms
rtt min/avg/max/mdev = 11.823/11.941/12.102/0.115 ms
```

### **-t ttl** / **--ttl=ttl**

送信パケットのIP Time to Live（TTL）値を設定します。

```console
$ ping -c 2 -t 64 github.com
PING github.com (140.82.114.3) 56(84) bytes of data.
64 bytes from 140.82.114.3: icmp_seq=1 ttl=64 time=29.7 ms
64 bytes from 140.82.114.3: icmp_seq=2 ttl=64 time=29.5 ms

--- github.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 29.532/29.636/29.741/0.104 ms
```

### **-s パケットサイズ** / **--size=パケットサイズ**

送信するデータバイト数を指定します。デフォルトは56バイトで、8バイトのICMPヘッダーデータと組み合わせると64バイトのICMPデータになります。

```console
$ ping -c 2 -s 100 cloudflare.com
PING cloudflare.com (104.16.132.229) 100(128) bytes of data.
108 bytes from 104.16.132.229: icmp_seq=1 ttl=57 time=10.3 ms
108 bytes from 104.16.132.229: icmp_seq=2 ttl=57 time=10.1 ms

--- cloudflare.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1001ms
rtt min/avg/max/mdev = 10.143/10.245/10.348/0.102 ms
```

## 使用例

### 基本的な接続テスト

```console
$ ping google.com
PING google.com (142.250.190.78) 56(84) bytes of data.
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=1 ttl=116 time=15.2 ms
64 bytes from lga25s74-in-f14.1e100.net (142.250.190.78): icmp_seq=2 ttl=116 time=14.8 ms
^C
--- google.com ping statistics ---
2 packets transmitted, 2 received, 0% packet loss, time 1002ms
rtt min/avg/max/mdev = 14.816/15.008/15.201/0.192 ms
```

### ネットワークの遅延確認

```console
$ ping -c 5 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=116 time=9.82 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=116 time=9.75 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=116 time=9.79 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=116 time=9.86 ms
64 bytes from 8.8.8.8: icmp_seq=5 ttl=116 time=9.80 ms

--- 8.8.8.8 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4006ms
rtt min/avg/max/mdev = 9.752/9.804/9.861/0.039 ms
```

## ヒント:

### 継続的なping

デフォルトでは、pingはCtrl+Cで中断されるまで継続します。`-c`オプションを使用して送信するパケット数を制限できます。

### ネットワーク問題のトラブルシューティング

pingが失敗した場合、ネットワーク接続の問題を示している可能性があります。ネットワーク接続、DNS設定、またはファイアウォールがICMPパケットをブロックしていないか確認してください。

### ネットワーク品質の測定

pingを使用してパケットロスと遅延を測定できます。高い遅延（100ms以上）やパケットロスは、潜在的なネットワーク問題を示しています。

### フラッドping

`-f`（フラッド）オプションを使用すると、可能な限り速くパケットを送信できますが、root権限が必要であり、ネットワークに負荷をかける可能性があるため注意して使用してください。

## よくある質問

#### Q1. 「Request timeout」や「Destination host unreachable」とはどういう意味ですか？
A. これらのメッセージは、ターゲットホストが応答していないことを示しています。ホストがオフラインである、ネットワークに問題がある、またはファイアウォールがICMPパケットをブロックしている可能性があります。

#### Q2. ping結果をどのように解釈すればよいですか？
A. 往復時間（RTT）とパケットロスの割合を確認してください。RTT値が低いほど接続状態が良いことを示します。パケットロスがある場合はネットワークに問題がある可能性があります。

#### Q3. pingで特定のポートが開いているかどうかを確認できますか？
A. いいえ、pingはICMPを使用した基本的な接続テストのみを行います。特定のポートが開いているかテストするには、`telnet`や`nc`（netcat）などのツールを使用してください。

#### Q4. なぜpingが予想とは異なるIPアドレスに解決されることがありますか？
A. これはDNSロードバランシング、CDN（コンテンツ配信ネットワーク）、またはドメイン名に関連付けられた複数のIPアドレスが原因で発生する可能性があります。

## macOSでの注意点

macOSでは、一部のpingオプションがLinuxとは異なります：
- `-i`オプションで1秒未満の間隔を指定するにはroot権限が必要です
- `--count`の長いオプション形式はありません。代わりに`-c`を使用してください
- フラッドping（`-f`）オプションはroot権限が必要で、Linuxとは動作が異なります

## 参考資料

https://linux.die.net/man/8/ping

## 改訂履歴

2025/05/04 初版作成