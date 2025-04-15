# ss コマンド概要

`ss`（Socket Statistics）は、ネットワークソケットの状態を表示するコマンドです。`netstat`の代替として開発され、より高速で詳細な情報を提供します。

## オプション

### **-t (--tcp)**

TCPソケットのみを表示します。

```bash
$ ss -t
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
ESTAB    0        0          192.168.1.5:ssh          192.168.1.10:52414
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
Netid    State     Recv-Q    Send-Q       Local Address:Port        Peer Address:Port   Process
tcp      LISTEN    0         128          0.0.0.0:ssh               0.0.0.0:*
tcp      LISTEN    0         128          127.0.0.1:http            0.0.0.0:*
```

### **-a (--all)**

すべてのソケット（リスニング状態と非リスニング状態の両方）を表示します。

```bash
$ ss -a
Netid    State     Recv-Q    Send-Q       Local Address:Port        Peer Address:Port   Process
tcp      LISTEN    0         128          0.0.0.0:ssh               0.0.0.0:*
tcp      ESTAB     0         0            192.168.1.5:ssh           192.168.1.10:52414
udp      UNCONN    0         0            0.0.0.0:bootpc            0.0.0.0:*
```

### **-n (--numeric)**

ホスト名、サービス名、ユーザー名を数値で表示します。

```bash
$ ss -tn
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port
ESTAB    0        0          192.168.1.5:22           192.168.1.10:52414
ESTAB    0        0          127.0.0.1:45678          127.0.0.1:80
```

### **-p (--processes)**

ソケットを使用しているプロセス情報を表示します。

```bash
$ ss -tp
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
ESTAB    0        0          192.168.1.5:ssh          192.168.1.10:52414  users:(("sshd",pid=1234,fd=3))
ESTAB    0        0          127.0.0.1:45678          127.0.0.1:http      users:(("curl",pid=5678,fd=3))
```

## 使用例

### 特定のポートに関連するすべての接続を表示

```bash
$ ss -t state established '( dport = :http or sport = :http )'
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
ESTAB    0        0          127.0.0.1:45678          127.0.0.1:http
ESTAB    0        0          192.168.1.5:http         192.168.1.10:56789
```

### リスニング中のTCPポートとそのプロセスを表示

```bash
$ ss -tlp
State    Recv-Q   Send-Q     Local Address:Port       Peer Address:Port   Process
LISTEN   0        128        0.0.0.0:ssh              0.0.0.0:*           users:(("sshd",pid=1234,fd=3))
LISTEN   0        128        127.0.0.1:http           0.0.0.0:*           users:(("nginx",pid=2345,fd=6))
```

### 接続の統計情報を表示

```bash
$ ss -s
Total: 182
TCP:   6 (estab 1, closed 0, orphaned 0, timewait 0)
Transport Total     IP        IPv6
RAW       0         0         0
UDP       5         3         2
TCP       6         4         2
INET      11        7         4
FRAG      0         0         0
```

## よくある質問

### Q1. `ss`と`netstat`の違いは何ですか？
A. `ss`は`netstat`の代替として開発され、より高速で詳細な情報を提供します。`ss`はカーネルから直接情報を取得するため、特に多数の接続がある場合に効率的です。

### Q2. 特定のポートをリスニングしているプロセスを確認するにはどうすればよいですか？
A. `ss -tlp | grep <ポート番号>` を使用します。例えば、HTTPポート（80）をリスニングしているプロセスを確認するには `ss -tlp | grep :http` または `ss -tlp | grep :80` を実行します。

### Q3. 確立された接続のみを表示するにはどうすればよいですか？
A. `ss -t state established` を使用します。これにより、現在アクティブなTCP接続のみが表示されます。

### Q4. 特定のIPアドレスとの接続を表示するにはどうすればよいですか？
A. `ss dst <IPアドレス>` または `ss src <IPアドレス>` を使用します。例えば、`ss dst 192.168.1.10` は宛先が192.168.1.10の接続を表示します。

## 追加情報

- `ss`コマンドは`iproute2`パッケージの一部であり、ほとんどの最新のLinuxディストリビューションにデフォルトでインストールされています。
- フィルタリングオプションを組み合わせることで、非常に具体的な条件に一致する接続を検索できます。
- 大規模なサーバーでは、`-n`オプションを使用すると名前解決を省略するため、コマンドの実行が高速化されます。
- `ss`コマンドはroot権限がなくても基本的な情報を表示できますが、`-p`オプションなど一部の詳細情報を表示するにはroot権限が必要な場合があります。