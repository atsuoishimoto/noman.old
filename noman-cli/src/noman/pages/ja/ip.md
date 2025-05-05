# ip コマンド

Linuxシステム上のネットワークインターフェース、ルーティング、トンネルを表示および操作します。

## 概要

`ip` コマンドは、Linux でネットワークインターフェース、ルーティングテーブル、トンネルを設定するための強力なユーティリティです。iproute2 パッケージの一部であり、`ifconfig` や `route` などの古いネットワークコマンドよりも多くの機能を提供します。このコマンドは階層構造を使用しており、オブジェクト（link、address、route など）の後にコマンドとオプションが続きます。

## オプション

### **-s, --stats, --statistics**

より詳細な情報や統計を表示します

```console
$ ip -s link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    RX: bytes  packets  errors  dropped overrun mcast   
    3500       35       0       0       0       0      
    TX: bytes  packets  errors  dropped carrier collsns 
    3500       35       0       0       0       0      
```

### **-c, --color**

読みやすさを向上させるためにカラー出力を使用します

```console
$ ip -c addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
```

### **-br, --brief**

簡潔な出力（オブジェクトごとに1行）を表示します

```console
$ ip -br addr show
lo               UNKNOWN        127.0.0.1/8 ::1/128 
eth0             UP             192.168.1.10/24 fe80::1234:5678:abcd:ef01/64
```

### **-d, --details**

詳細情報を表示します

```console
$ ip -d link show dev eth0
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff promiscuity 0 
    altname enp0s3
    vlan protocol 802.1Q
    vlan id 1 <REORDER_HDR> 
```

## 使用例

### ネットワークインターフェースの表示

```console
$ ip link show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
```

### IPアドレスの表示

```console
$ ip addr show
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.10/24 brd 192.168.1.255 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::1234:5678:abcd:ef01/64 scope link 
       valid_lft forever preferred_lft forever
```

### IPアドレスの設定

```console
$ sudo ip addr add 192.168.1.100/24 dev eth0
```

### インターフェースの有効化または無効化

```console
$ sudo ip link set eth0 up
$ sudo ip link set eth0 down
```

### ルーティングテーブルの表示

```console
$ ip route show
default via 192.168.1.1 dev eth0 proto static 
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.10
```

### 静的ルートの追加

```console
$ sudo ip route add 10.0.0.0/24 via 192.168.1.254
```

## ヒント:

### 一般的なコマンドのショートカットを使用する

`ip` コマンドはサブコマンドの短縮版を使用できます：
- `ip a` は `ip addr show` の代わりに
- `ip l` は `ip link show` の代わりに
- `ip r` は `ip route show` の代わりに

### 設定の保存と復元

現在のIP設定を保存し、後で復元することができます：

```console
$ ip addr save > ip-config.txt
$ ip addr restore < ip-config.txt
```

### 一時的な変更と永続的な変更

`ip` コマンドで行った変更は再起動後には保持されません。永続的な変更を行うには、ディストリビューションのネットワーク設定ファイルを変更する必要があります。

### ネットワーク分離のための名前空間の使用

ネットワーク名前空間を使用すると、分離されたネットワーク環境を作成できます：

```console
$ sudo ip netns add mynetwork
$ sudo ip netns exec mynetwork ip addr
```

## よくある質問

#### Q1. `ip` と `ifconfig` の違いは何ですか？
A. `ip` はより新しく、強力で、`ifconfig` よりも多くの機能を提供します。ルーティング、トンネリング、ポリシーベースのルーティングを管理できますが、`ifconfig` は基本的なインターフェース設定に限られています。

#### Q2. IPアドレスを確認するにはどうすればよいですか？
A. `ip addr show` または短縮形の `ip a` を使用して、システム上のすべてのIPアドレスを表示します。

#### Q3. 一時的なIPアドレスを追加するにはどうすればよいですか？
A. `sudo ip addr add IPアドレス/ネットマスク dev インターフェース` を使用します。例：`sudo ip addr add 192.168.1.100/24 dev eth0`。

#### Q4. ルーティングテーブルを確認するにはどうすればよいですか？
A. `ip route show` または短縮形の `ip r` を使用して、ルーティングテーブルを表示します。

#### Q5. インターフェースからIPアドレスを削除するにはどうすればよいですか？
A. `sudo ip addr flush dev インターフェース` を使用します。例：`sudo ip addr flush dev eth0`。

## 参考資料

https://man7.org/linux/man-pages/man8/ip.8.html

## 改訂履歴

2025/05/04 初回改訂