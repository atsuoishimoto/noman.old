# ss コマンド概要

`ss`（Socket Statistics）は、ネットワークソケット情報を表示するコマンドです。`netstat`の代替として開発され、より高速で詳細な情報を提供します。

## オプション

### **-t (--tcp)**

TCPソケットのみを表示します。

```bash
$ ss -t
State     Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
ESTAB     0          0              192.168.1.5:ssh             192.168.1.10:52414
ESTAB     0          0              192.168.1.5:42004           151.101.65.69:https
```

### **-u (--udp)**

UDPソケットのみを表示します。

```bash
$ ss -u
State     Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
UNCONN    0          0              0.0.0.0:bootpc             0.0.0.0:*
UNCONN    0          0              0.0.0.0:mdns               0.0.0.0:*
```

### **-l (--listening)**

リスニング状態のソケットのみを表示します。

```bash
$ ss -l
Netid     State      Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
tcp       LISTEN     0          128            0.0.0.0:ssh                 0.0.0.0:*
tcp       LISTEN     0          128            127.0.0.1:smtp              0.0.0.0:*
```

### **-a (--all)**

リスニング状態と非リスニング状態の両方のソケットを表示します。

```bash
$ ss -a
Netid     State      Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
tcp       LISTEN     0          128            0.0.0.0:ssh                 0.0.0.0:*
tcp       ESTAB      0          0              192.168.1.5:ssh             192.168.1.10:52414
```

### **-n (--numeric)**

ホスト名、ポート名、ユーザー名を数値で表示します。

```bash
$ ss -tn
State     Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
ESTAB     0          0              192.168.1.5:22              192.168.1.10:52414
ESTAB     0          0              192.168.1.5:42004           151.101.65.69:443
```

### **-p (--processes)**

ソケットを使用しているプロセス情報を表示します。

```bash
$ ss -tp
State     Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
ESTAB     0          0              192.168.1.5:ssh             192.168.1.10:52414    users:(("sshd",pid=1234,fd=3))
```

## 使用例

### 特定のポートに関連するすべての接続を表示

```bash
$ ss -t state established '( dport = :ssh or sport = :ssh )'
State     Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
ESTAB     0          0              192.168.1.5:ssh             192.168.1.10:52414
```

### HTTPSの接続を表示

```bash
$ ss -tn state established '( dport = :443 or sport = :443 )'
State     Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
ESTAB     0          0              192.168.1.5:42004           151.101.65.69:443
```

### リスニング中のTCPポートとそのプロセスを表示

```bash
$ ss -tlp
State     Recv-Q     Send-Q         Local Address:Port          Peer Address:Port     Process
LISTEN    0          128            0.0.0.0:ssh                 0.0.0.0:*             users:(("sshd",pid=1234,fd=3))
LISTEN    0          128            127.0.0.1:smtp              0.0.0.0:*             users:(("postfix",pid=5678,fd=13))
```

## よくある質問

### Q1. `ss`と`netstat`の違いは何ですか？
A. `ss`は`netstat`の代替として開発され、より高速で詳細な情報を提供します。`ss`はカーネルから直接情報を取得するため、特に多数の接続がある場合に効率的です。

### Q2. 特定のポートをリスニングしているプロセスを確認するにはどうすればよいですか？
A. `ss -tlp | grep <ポート番号>` を使用します。例えば、HTTPポート(80)をリスニングしているプロセスを確認するには `ss -tlp | grep :http` または `ss -tlp | grep :80` を実行します。

### Q3. 確立された接続のみを表示するにはどうすればよいですか？
A. `ss -t state established` を使用します。これにより、現在アクティブなTCP接続のみが表示されます。

### Q4. 特定のIPアドレスとの接続を表示するにはどうすればよいですか？
A. `ss dst <IPアドレス>` または `ss src <IPアドレス>` を使用します。例えば、`ss dst 192.168.1.10` は、192.168.1.10に向けたすべての接続を表示します。

## 追加情報

- `ss`コマンドは`iproute2`パッケージの一部であり、多くの現代的なLinuxディストリビューションにデフォルトでインストールされています。
- 複雑なフィルタリングが可能で、正規表現や条件式を使用して特定の接続を検索できます。
- 大量の接続がある環境（サーバーなど）では、`-n`オプションを使用すると名前解決を行わないため処理が高速化します。
- `ss`の出力は非常に詳細なため、`grep`と組み合わせて使用すると特定の情報を簡単に抽出できます。