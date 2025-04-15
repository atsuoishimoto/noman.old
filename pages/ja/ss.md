# ss コマンド概要

`ss`（Socket Statistics）は、ネットワークソケット情報を表示するコマンドです。`netstat`の代替として開発され、より高速で詳細な情報を提供します。

## オプション

### **-t (--tcp)**

TCPソケットのみを表示します。

```bash
$ ss -t
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
ESTAB    0        0          192.168.1.5:ssh          192.168.1.10:52410
ESTAB    0        0          127.0.0.1:45678          127.0.0.1:http
```

### **-u (--udp)**

UDPソケットのみを表示します。

```bash
$ ss -u
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
UNCONN   0        0          0.0.0.0:bootpc           0.0.0.0:*
UNCONN   0        0          0.0.0.0:mdns             0.0.0.0:*
```

### **-l (--listening)**

リスニング状態のソケットのみを表示します。

```bash
$ ss -l
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
LISTEN   0        128        0.0.0.0:ssh              0.0.0.0:*
LISTEN   0        128        127.0.0.1:http           0.0.0.0:*
```

### **-p (--processes)**

ソケットを使用しているプロセス情報を表示します（root権限が必要）。

```bash
$ sudo ss -p
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
LISTEN   0        128        0.0.0.0:ssh              0.0.0.0:*           users:(("sshd",pid=1234,fd=3))
ESTAB    0        0          192.168.1.5:ssh          192.168.1.10:52410  users:(("sshd",pid=5678,fd=5))
```

### **-n (--numeric)**

ホスト名、サービス名、ユーザー名を数値で表示します。

```bash
$ ss -n
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
ESTAB    0        0          192.168.1.5:22           192.168.1.10:52410
ESTAB    0        0          127.0.0.1:45678          127.0.0.1:80
```

### **-a (--all)**

リスニング状態と非リスニング状態の両方のソケットを表示します。

```bash
$ ss -a
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
LISTEN   0        128        0.0.0.0:ssh              0.0.0.0:*
ESTAB    0        0          192.168.1.5:ssh          192.168.1.10:52410
```

## 使用例

### TCP接続のリスニングポートを確認

```bash
$ ss -tl
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
LISTEN   0        128        0.0.0.0:ssh              0.0.0.0:*
LISTEN   0        128        127.0.0.1:http           0.0.0.0:*
LISTEN   0        128        :::ssh                   :::*
```

### 特定のポートに関連するすべての接続を表示

```bash
$ ss -t state established '( dport = :ssh or sport = :ssh )'
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
ESTAB    0        0          192.168.1.5:ssh          192.168.1.10:52410
ESTAB    0        0          192.168.1.5:ssh          192.168.1.15:33256
```

### プロセス情報を含むすべてのTCP接続を表示

```bash
$ sudo ss -tp
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
LISTEN   0        128        0.0.0.0:ssh              0.0.0.0:*           users:(("sshd",pid=1234,fd=3))
ESTAB    0        0          192.168.1.5:ssh          192.168.1.10:52410  users:(("sshd",pid=5678,fd=5))
```

## よくある質問

### Q1. `ss`と`netstat`の違いは何ですか？
A. `ss`は`netstat`の代替として開発され、より高速で詳細な情報を提供します。`ss`はカーネルから直接情報を取得するため、特に多数の接続がある場合に効率的です。

### Q2. 特定のポートを使用している接続を確認するにはどうすればよいですか？
A. `ss -t '( dport = :80 or sport = :80 )'`のように、フィルタを使用して特定のポート（この例では80番ポート）に関連する接続を表示できます。

### Q3. 確立された接続のみを表示するにはどうすればよいですか？
A. `ss state established`または`ss -o state established`を使用します。

### Q4. IPv4またはIPv6の接続のみを表示するにはどうすればよいですか？
A. IPv4のみの場合は`ss -4`、IPv6のみの場合は`ss -6`を使用します。

## 追加情報

- `ss`コマンドは`iproute2`パッケージの一部です。
- 複雑なフィルタリングが可能で、正規表現や条件式を使用できます。
- メモリ使用量が少なく、大規模なシステムでのネットワーク診断に適しています。
- `ss -s`を使用すると、ソケットの統計情報を確認できます。