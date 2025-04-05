# `ip` コマンド概要

`ip` コマンドは、ネットワークインターフェース、ルーティングテーブル、IPアドレスなどのネットワーク設定を表示・管理するための強力なツールです。従来の `ifconfig` や `route` コマンドの代替として使用されます。

## 主なオプション

- **`ip addr`**: ネットワークインターフェースとそのIPアドレスを表示します
  - 例: `ip addr show`

- **`ip link`**: ネットワークインターフェースの状態を表示・変更します
  - 例: `ip link show`

- **`ip route`**: ルーティングテーブルを表示・管理します
  - 例: `ip route show`

- **`ip neigh`**: ARPテーブル（近隣探索キャッシュ）を表示・管理します
  - 例: `ip neigh show`

## 使用例

### IPアドレスの表示

```bash
# すべてのインターフェースのIPアドレスを表示
ip addr show
# 出力例
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0
       valid_lft forever preferred_lft forever
```

### 特定のインターフェースの情報表示

```bash
# eth0インターフェースの情報のみ表示
ip addr show dev eth0
```

### IPアドレスの追加と削除

```bash
# eth0インターフェースに新しいIPアドレスを追加
sudo ip addr add 192.168.1.200/24 dev eth0

# eth0インターフェースからIPアドレスを削除
sudo ip addr del 192.168.1.200/24 dev eth0
```

### インターフェースの有効化/無効化

```bash
# eth0インターフェースを有効化
sudo ip link set eth0 up

# eth0インターフェースを無効化
sudo ip link set eth0 down
```

### ルーティングテーブルの表示と管理

```bash
# ルーティングテーブルを表示
ip route show
# 出力例
default via 192.168.1.1 dev eth0 proto static 
192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100

# デフォルトゲートウェイの追加
sudo ip route add default via 192.168.1.1 dev eth0

# 特定のネットワークへのルートを追加
sudo ip route add 10.0.0.0/24 via 192.168.1.254 dev eth0
```

### ARPテーブルの表示

```bash
# ARPテーブル（近隣探索キャッシュ）を表示
ip neigh show
# 出力例
192.168.1.1 dev eth0 lladdr aa:bb:cc:dd:ee:ff REACHABLE
```

## 追加情報

- `ip` コマンドは、`-c` オプションを使用してカラー出力を有効にできます（例: `ip -c addr show`）
- 出力を簡潔にするには `-br`（brief）オプションを使用できます（例: `ip -br addr show`）
- `ip` コマンドは非常に多機能なため、`man ip` で詳細なマニュアルを参照することをお勧めします
- 多くのLinuxディストリビューションでは、`ip` コマンドを使用するために `iproute2` パッケージのインストールが必要です
- 従来の `ifconfig` や `route` コマンドは古いとされ、最新のLinuxディストリビューションでは `ip` コマンドの使用が推奨されています