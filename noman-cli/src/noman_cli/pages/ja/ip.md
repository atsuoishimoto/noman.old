# ip コマンド

ネットワークインターフェース、ルーティング、トンネルなどのネットワーク設定を表示・管理します。

## 概要

`ip` コマンドは、Linux システムでネットワーク設定を管理するための強力なツールです。ネットワークインターフェースの設定、IPアドレスの割り当て、ルーティングテーブルの管理、ARPテーブルの表示など、さまざまなネットワーク関連のタスクを実行できます。従来の `ifconfig` や `route` コマンドの代替として開発されました。

## オプション

### **ip addr (address)**

ネットワークインターフェースのIPアドレス情報を表示・管理します。

```console
$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:0c:29:b0:xx:xx brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
       valid_lft forever preferred_lft forever
```

### **ip link**

ネットワークインターフェースの状態を表示・管理します。

```console
$ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:b0:xx:xx brd ff:ff:ff:ff:ff:ff
```

### **ip route**

ルーティングテーブルを表示・管理します。

```console
$ ip route show
default via 192.168.1.1 dev eth0 proto static 
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100
```

### **ip neigh (neighbour)**

ARPテーブル（ネイバーテーブル）を表示・管理します。

```console
$ ip neigh show
192.168.1.1 dev eth0 lladdr 00:11:22:33:44:55 REACHABLE
192.168.1.5 dev eth0 lladdr aa:bb:cc:dd:ee:ff STALE
```

## 使用例

### IPアドレスの追加

```console
$ sudo ip addr add 192.168.1.200/24 dev eth0
# eth0インターフェースに192.168.1.200/24のIPアドレスを追加
```

### インターフェースの有効化/無効化

```console
$ sudo ip link set eth0 up
# eth0インターフェースを有効化

$ sudo ip link set eth0 down
# eth0インターフェースを無効化
```

### ルートの追加

```console
$ sudo ip route add 10.0.0.0/24 via 192.168.1.1
# 10.0.0.0/24ネットワークへのルートを192.168.1.1ゲートウェイ経由で追加
```

### 特定のインターフェースの詳細情報表示

```console
$ ip -s link show eth0
# eth0インターフェースの統計情報を含む詳細を表示
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:0c:29:b0:xx:xx brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast   
    1234567    12345    0       0       0       123     
    TX: bytes  packets  errors  dropped carrier collsns 
    7654321    54321    0       0       0       0
```

## ヒント:

### 読みやすい出力形式

`-h` または `--human` オプションを使用すると、数値が読みやすい形式で表示されます。

```console
$ ip -h addr show
# 数値が読みやすい形式で表示される
```

### JSONフォーマットでの出力

`-j` または `--json` オプションを使用すると、出力がJSON形式で表示されます。これはスクリプトでの処理に便利です。

```console
$ ip -j addr show
# JSON形式で出力される
```

### 色付き出力

`-c` または `--color` オプションを使用すると、出力に色が付きます。これにより視認性が向上します。

```console
$ ip -c addr show
# 色付きで出力される
```

### 特定のインターフェースのみ表示

特定のインターフェースに関する情報だけを表示したい場合は、インターフェース名を指定します。

```console
$ ip addr show eth0
# eth0インターフェースの情報のみ表示
```

## よくある質問

#### Q1. `ip` コマンドと `ifconfig` コマンドの違いは何ですか？
A. `ip` コマンドは `ifconfig` の後継として開発され、より多くの機能を持ち、最新のネットワーク技術に対応しています。`ifconfig` は多くのLinuxディストリビューションでは非推奨または廃止されつつあります。

#### Q2. 一時的なIPアドレス変更と永続的な変更の違いは？
A. `ip` コマンドでの変更はシステム再起動後に失われます。永続的な変更を行うには、ディストリビューションに応じたネットワーク設定ファイル（例：`/etc/network/interfaces`、`/etc/sysconfig/network-scripts/`など）を編集する必要があります。

#### Q3. デフォルトゲートウェイを変更するには？
A. `sudo ip route replace default via 新しいゲートウェイIP dev インターフェース名` を使用します。例：`sudo ip route replace default via 192.168.1.254 dev eth0`

#### Q4. ネットワークインターフェースのMACアドレスを変更できますか？
A. はい、`sudo ip link set dev インターフェース名 address 新しいMAC` で変更できます。例：`sudo ip link set dev eth0 address 00:11:22:33:44:55`

## 参考

https://man7.org/linux/man-pages/man8/ip.8.html

## 改訂

- 2025/04/30 初版作成