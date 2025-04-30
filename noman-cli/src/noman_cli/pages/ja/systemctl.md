# systemctl コマンド

システムとサービスマネージャーを制御するコマンド。

## 概要

`systemctl` は systemd システムとサービスマネージャーを制御するためのコマンドラインツールです。サービスの起動・停止・再起動、システムの状態確認、ブート時の自動起動設定などを管理できます。Linux システムの基本的なサービス管理に不可欠なツールです。

## オプション

### **status**

指定したユニット（サービス、ソケット、デバイスなど）の状態を表示します。

```console
$ systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2025-04-30 10:15:23 JST; 2h 30min ago
     Docs: man:nginx(8)
  Process: 1234 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
  Process: 1235 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
 Main PID: 1236 (nginx)
    Tasks: 2 (limit: 4915)
   Memory: 3.0M
   CGroup: /system.slice/nginx.service
           ├─1236 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─1237 nginx: worker process
```

### **start**

サービスを起動します。

```console
$ sudo systemctl start nginx
# 出力なし（成功時）
```

### **stop**

サービスを停止します。

```console
$ sudo systemctl stop nginx
# 出力なし（成功時）
```

### **restart**

サービスを再起動します。

```console
$ sudo systemctl restart nginx
# 出力なし（成功時）
```

### **enable**

システム起動時に自動的にサービスが起動するように設定します。

```console
$ sudo systemctl enable nginx
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /lib/systemd/system/nginx.service.
```

### **disable**

システム起動時のサービスの自動起動を無効にします。

```console
$ sudo systemctl disable nginx
Removed /etc/systemd/system/multi-user.target.wants/nginx.service.
```

## 使用例

### サービスの状態確認

```console
$ systemctl status sshd
● ssh.service - OpenBSD Secure Shell server
   Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
   Active: active (running) since Wed 2025-04-30 09:45:12 JST; 3h 5min ago
  Process: 845 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
 Main PID: 875 (sshd)
    Tasks: 1 (limit: 4915)
   Memory: 6.2M
   CGroup: /system.slice/ssh.service
           └─875 /usr/sbin/sshd -D
```

### 複数サービスの一覧表示

```console
$ systemctl list-units --type=service
UNIT                               LOAD   ACTIVE SUB     DESCRIPTION
accounts-daemon.service            loaded active running Accounts Service
apparmor.service                   loaded active exited  AppArmor initialization
apport.service                     loaded active exited  LSB: automatic crash report generation
avahi-daemon.service               loaded active running Avahi mDNS/DNS-SD Stack
bluetooth.service                  loaded active running Bluetooth service
...
```

### 失敗したサービスの確認

```console
$ systemctl --failed
UNIT           LOAD   ACTIVE SUB    DESCRIPTION
mysql.service  loaded failed failed MySQL Database Server

LOAD   = Reflects whether the unit definition was properly loaded.
ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
SUB    = The low-level unit activation state, values depend on unit type.

1 loaded units listed.
```

## ヒント:

### サービスの再読み込み

設定ファイルを変更した後、サービスを再起動せずに設定を反映させたい場合は `systemctl reload サービス名` を使用します。すべてのサービスがこの機能をサポートしているわけではありません。

### ジャーナルログの確認

特定のサービスのログを確認するには `journalctl -u サービス名` を使用します。これはトラブルシューティングに非常に役立ちます。

### システム全体の状態確認

`systemctl` を引数なしで実行すると、システム上のすべてのアクティブなユニットのリストが表示されます。これは全体像を把握するのに便利です。

## よくある質問

#### Q1. systemctl と service コマンドの違いは何ですか？
A. `systemctl` は systemd システムの一部であり、より多くの機能を提供します。`service` コマンドは古い SysV init システム用のコマンドで、互換性のために残されています。最新の Linux ディストリビューションでは `systemctl` の使用が推奨されています。

#### Q2. サービスが自動起動するように設定されているか確認するには？
A. `systemctl is-enabled サービス名` を使用します。「enabled」または「disabled」が返されます。

#### Q3. systemd ユニットファイルはどこにありますか？
A. 主に `/lib/systemd/system/` または `/etc/systemd/system/` ディレクトリにあります。カスタムユニットファイルは通常 `/etc/systemd/system/` に配置します。

#### Q4. systemctl コマンドを実行するとき「Failed to connect to bus」エラーが出る場合は？
A. このエラーは通常、権限不足が原因です。多くの `systemctl` コマンドは root 権限が必要なため、`sudo` を付けて実行してください。

## 参考資料

https://www.freedesktop.org/software/systemd/man/systemctl.html

## Revisions

- 2025/04/30 First revision