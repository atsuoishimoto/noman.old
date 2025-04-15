# ip コマンド概要

`ip` コマンドは、ネットワークインターフェース、ルーティングテーブル、IPアドレスなどのネットワーク設定を表示・管理するための強力なツールです。`ifconfig` や `route` コマンドの後継として設計されています。

## オプション

### **ip addr (address)**

ネットワークインターフェースのIPアドレス情報を表示・管理します。

```bash
$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:3d:5e:7a brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
       valid_lft forever preferred_lft forever
```

### **ip link**

ネットワークインターフェースの状態を表示・管理します。

```bash
$ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:3d:5e:7a brd ff:ff:ff:ff:ff:ff
```

### **ip route**

ルーティングテーブルを表示・管理します。

```bash
$ ip route show
default via 192.168.1.1 dev eth0 proto static 
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```

### **ip neigh (neighbour)**

ARPテーブル（ネイバーテーブル）を表示・管理します。

```bash
$ ip neigh show
192.168.1.1 dev eth0 lladdr 00:11:22:33:44:55 REACHABLE
192.168.1.5 dev eth0 lladdr aa:bb:cc:dd:ee:ff STALE
```

## 使用例

### インターフェースの有効化/無効化

```bash
# eth0インターフェースを有効化
$ sudo ip link set eth0 up

# eth0インターフェースを無効化
$ sudo ip link set eth0 down
```

### IPアドレスの追加/削除

```bash
# eth0にIPアドレスを追加
$ sudo ip addr add 192.168.1.200/24 dev eth0

# eth0からIPアドレスを削除
$ sudo ip addr del 192.168.1.200/24 dev eth0
```

### ルートの追加/削除

```bash
# デフォルトゲートウェイの設定
$ sudo ip route add default via 192.168.1.1 dev eth0

# 特定のネットワークへのルートを追加
$ sudo ip route add 10.0.0.0/24 via 192.168.1.254 dev eth0

# ルートの削除
$ sudo ip route del 10.0.0.0/24
```

## よくある質問

### Q1. `ip` コマンドと `ifconfig` の違いは何ですか？
A. `ip` コマンドは `ifconfig` の後継として開発され、より多くの機能を持ち、最新のネットワーク技術に対応しています。`ifconfig` は多くのディストリビューションで非推奨となっています。

### Q2. 自分のIPアドレスを確認するには？
A. `ip addr show` コマンドを使用します。各インターフェースに割り当てられたIPアドレスが表示されます。

### Q3. デフォルトゲートウェイを確認するには？
A. `ip route show` コマンドを実行し、「default via」で始まる行を探します。

### Q4. ネットワークインターフェースの名前を確認するには？
A. `ip link show` コマンドを使用すると、システム上のすべてのネットワークインターフェースが表示されます。

## 追加情報

- `ip` コマンドは出力が色分けされていることがあり、読みやすくなっています。
- `-s` オプションを追加すると、より詳細な統計情報が表示されます（例：`ip -s link show`）。
- `-br`（brief）オプションを使うと、より簡潔な出力が得られます（例：`ip -br addr show`）。
- `ip` コマンドはサブコマンドを省略形で指定できます（例：`ip a` は `ip addr`、`ip r` は `ip route` と同じ）。
- ほとんどの `ip` コマンドの操作には管理者権限（sudo）が必要です。