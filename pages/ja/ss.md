# ss コマンド

ソケット統計を表示し、ネットワーク接続に関する情報を提供します。

## 概要

`ss` コマンドはソケットを調査するためのユーティリティで、ネットワーク接続、ルーティングテーブル、ネットワークインターフェースに関する情報を表示します。従来の `netstat` コマンドよりも高機能で高速な代替手段であり、システム上のTCP、UDP、およびその他のソケット接続に関する詳細な情報を提供します。

## オプション

### **-a, --all**

リッスン中と非リッスン中の両方のソケットを表示します

```console
$ ss -a
Netid  State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port  Process
u_str  ESTAB   0       0       * 19350               * 19351
u_str  ESTAB   0       0       * 18935               * 18936
tcp    LISTEN  0       4096    127.0.0.1:5432       0.0.0.0:*
tcp    ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
udp    UNCONN  0       0       0.0.0.0:68           0.0.0.0:*
```

### **-l, --listening**

リッスン中のソケットのみを表示します

```console
$ ss -l
Netid  State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port  Process
tcp    LISTEN  0       4096    127.0.0.1:5432       0.0.0.0:*
tcp    LISTEN  0       128     0.0.0.0:22           0.0.0.0:*
tcp    LISTEN  0       511     0.0.0.0:80           0.0.0.0:*
```

### **-t, --tcp**

TCPソケットのみを表示します

```console
$ ss -t
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
ESTAB   0       0       192.168.1.5:49834    151.101.65.69:443
```

### **-u, --udp**

UDPソケットのみを表示します

```console
$ ss -u
State    Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
UNCONN   0       0       0.0.0.0:68           0.0.0.0:*
UNCONN   0       0       0.0.0.0:5353         0.0.0.0:*
```

### **-p, --processes**

ソケットを使用しているプロセスを表示します

```console
$ ss -tp
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port   Process
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721  users:(("sshd",pid=1234,fd=3))
```

### **-n, --numeric**

サービス名を解決せず、ポート番号を表示します

```console
$ ss -tn
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
LISTEN  0       128     0.0.0.0:22           0.0.0.0:*
```

### **-i, --info**

TCP内部情報を表示します

```console
$ ss -ti
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
         cubic wscale:7,7 rto:204 rtt:0.98/0.49 ato:40 mss:1448 cwnd:10 bytes_acked:1448 segs_out:2 segs_in:1
```

## 使用例

### すべてのTCP接続を表示

```console
$ ss -ta
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
LISTEN  0       128     0.0.0.0:22           0.0.0.0:*
LISTEN  0       511     0.0.0.0:80           0.0.0.0:*
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
```

### ポートによる接続のフィルタリング

```console
$ ss -t '( dport = :ssh or sport = :ssh )'
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
```

### ソケット統計の概要を表示

```console
$ ss -s
Total: 187
TCP:   12 (estab 3, closed 0, orphaned 0, timewait 0)
Transport Total     IP        IPv6
RAW       0         0         0
UDP       8         5         3
TCP       12        9         3
INET      20        14        6
FRAG      0         0         0
```

## ヒント:

### オプションを組み合わせて詳細な出力を得る

`ss -tuln` のようにオプションを組み合わせることで、数値ポートを持つTCPとUDPのリッスンソケットを表示できます。これはシステム上で実行中のサービスを素早く確認するのに役立ちます。

### grepと組み合わせてフィルタリングする

`ss` の出力を `grep` にパイプして特定の接続をフィルタリングできます。例えば `ss -ta | grep ESTABLISHED` でアクティブな接続のみを表示できます。

### リアルタイムで接続を監視する

`watch ss -ta` を使用すると、2秒ごとに更新されるリアルタイムで接続を監視できます。ネットワークの問題のトラブルシューティングに役立ちます。

### 接続の問題を確認する

`ss -tan state time-wait` や `ss -tan state close-wait` を使用して、適切に閉じられていない可能性のある問題のある接続を特定できます。

## よくある質問

#### Q1. `ss` と `netstat` の違いは何ですか？
A. `ss` は `netstat` よりも高速で詳細な情報を提供します。`/proc` ファイルからではなく、カーネルから直接情報を読み取るため、特に多数の接続があるシステムでより効率的です。

#### Q2. 特定のポートを使用しているプロセスを確認するにはどうすればよいですか？
A. `ss -tlp` を使用して、関連するプロセスと共にリッスン中のTCPソケットを表示できます。すべてのプロセス情報を表示するには、rootとして実行する必要がある場合があります。

#### Q3. IP アドレスで接続をフィルタリングするにはどうすればよいですか？
A. フィルター式を使用します: `ss -t dst 192.168.1.10` でそのIPアドレスへのTCP接続を表示できます。

#### Q4. 接続のタイミング情報を確認できますか？
A. はい、`ss -ti` を使用すると、往復時間（RTT）や再送タイムアウト（RTO）などの詳細なTCPメトリクスを表示できます。

## 参考資料

https://man7.org/linux/man-pages/man8/ss.8.html

## 改訂履歴

- 2025/05/04 初版作成