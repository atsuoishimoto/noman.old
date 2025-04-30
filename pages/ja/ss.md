# ss コマンド

ネットワークソケット情報を表示するユーティリティです。

## 概要

`ss`コマンドは、ネットワークソケットの状態を調査するためのツールです。従来の`netstat`コマンドの代替として開発され、より高速で詳細な情報を提供します。TCP、UDP、UNIXドメインソケットなどの接続状態、ポート番号、プロセス情報を確認できます。

## オプション

### **-a (--all)**

すべてのソケット（リスニング中と非リスニング中の両方）を表示します。

```console
$ ss -a
Netid  State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port  Process
u_str  ESTAB   0       0       * 19347              * 19348
u_str  ESTAB   0       0       * 19348              * 19347
tcp    LISTEN  0       4096    127.0.0.1:5432       0.0.0.0:*
tcp    ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
```

### **-l (--listening)**

リスニング中のソケットのみを表示します。

```console
$ ss -l
Netid  State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port  Process
tcp    LISTEN  0       128     0.0.0.0:ssh          0.0.0.0:*
tcp    LISTEN  0       4096    127.0.0.1:postgresql 0.0.0.0:*
tcp    LISTEN  0       128     [::]:ssh             [::]:*
```

### **-t (--tcp)**

TCPソケットのみを表示します。

```console
$ ss -t
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:ssh      192.168.1.10:49721
```

### **-u (--udp)**

UDPソケットのみを表示します。

```console
$ ss -u
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
UNCONN  0       0       0.0.0.0:mdns         0.0.0.0:*
UNCONN  0       0       0.0.0.0:bootpc       0.0.0.0:*
```

### **-p (--processes)**

ソケットを使用しているプロセス情報を表示します。

```console
$ ss -tp
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port   Process
ESTAB   0       0       192.168.1.5:ssh      192.168.1.10:49721  users:(("sshd",pid=1234,fd=3))
```

### **-n (--numeric)**

ホスト名、サービス名、ユーザー名を数値で表示します。

```console
$ ss -tn
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
```

## 使用例

### 特定のポートに関連するソケットを表示

```console
$ ss -t state established '( dport = :ssh or sport = :ssh )'
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
```

### 特定のIPアドレスに関連するソケットを表示

```console
$ ss -t dst 192.168.1.10
State   Recv-Q  Send-Q  Local Address:Port   Peer Address:Port
ESTAB   0       0       192.168.1.5:22       192.168.1.10:49721
```

### 統計情報を表示

```console
$ ss -s
Total: 187
TCP:   6 (estab 1, closed 0, orphaned 0, timewait 0)
Transport Total     IP        IPv6
RAW       0         0         0
UDP       5         3         2
TCP       6         3         3
INET      11        6         5
FRAG      0         0         0
```

## ヒント:

### フィルタリング構文を活用する

`ss`コマンドは強力なフィルタリング構文をサポートしています。例えば、`ss dst 192.168.1.1`は特定の宛先IPに関連するソケットを表示します。

### 状態によるフィルタリング

`ss state established`のように、特定の状態（established、syn-sent、syn-recv、fin-wait-1など）のソケットだけを表示できます。

### メモリ使用量の確認

`ss -m`オプションを使用すると、ソケットのメモリ使用量を確認できます。これはメモリリークの調査に役立ちます。

### 定期的な監視

`watch -n 1 'ss -t'`のように、watchコマンドと組み合わせることで、ネットワーク接続の変化をリアルタイムで監視できます。

## よくある質問

#### Q1. `ss`と`netstat`の違いは何ですか？
A. `ss`は`netstat`の代替として開発され、より高速で詳細な情報を提供します。`ss`はカーネルから直接情報を取得するため、特に多数の接続がある場合に効率的です。

#### Q2. 特定のポートがリスニング状態かどうかを確認するには？
A. `ss -ln sport = :ポート番号`を使用します。例えば、ポート80をチェックするには`ss -ln sport = :80`と入力します。

#### Q3. 特定のプロセスが使用しているソケットを確認するには？
A. `ss -p '( pid = プロセスID )'`を使用します。例えば、PID 1234のプロセスが使用しているソケットを確認するには`ss -p '( pid = 1234 )'`と入力します。

#### Q4. TCPの接続状態の意味は何ですか？
A. 主な状態には、LISTEN（接続待機中）、ESTABLISHED（接続確立済み）、TIME-WAIT（接続終了後の待機状態）、CLOSE-WAIT（相手からの切断待ち）などがあります。

## 参考文献

https://man7.org/linux/man-pages/man8/ss.8.html

## Revisions

- 2025/04/30 初版作成