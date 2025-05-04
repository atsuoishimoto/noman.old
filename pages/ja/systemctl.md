# systemctl コマンド

システムとサービスマネージャーである systemd を制御します。

## 概要

`systemctl` は、Linux のシステムおよびサービスマネージャーである systemd を制御・管理するためのコマンドラインユーティリティです。このコマンドを使用して、システムサービスの起動、停止、再起動、有効化、無効化、状態確認などを行うことができます。systemd は、ほとんどの最新の Linux ディストリビューションで使用されている init システムで、ユーザースペースの起動とシステムプロセスの管理を担当しています。

## オプション

### **-t, --type=TYPE**

ユニットをタイプ（service、socket、timerなど）でフィルタリングします

```console
$ systemctl -t service
UNIT                               LOAD   ACTIVE SUB     DESCRIPTION
accounts-daemon.service            loaded active running Accounts Service
apparmor.service                   loaded active exited  AppArmor initialization
avahi-daemon.service               loaded active running Avahi mDNS/DNS-SD Stack
bluetooth.service                  loaded active running Bluetooth service
...
```

### **-a, --all**

非アクティブなものを含む、読み込まれたすべてのユニットを表示します

```console
$ systemctl -a
UNIT                                  LOAD      ACTIVE   SUB     DESCRIPTION
proc-sys-fs-binfmt_misc.automount     loaded    active   running Arbitrary Executable File Formats File System
sys-devices-pci0000:00-0000:00:14.0-usb1-1\x2d1-1\x2d1.1-1\x2d1.1:1.0-bluetooth-hci0.device loaded active plugged /sys/devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1.1/1-1.1:1.0/bluetooth/hci0
...
```

### **--state=STATE**

ユニットを状態（active、failedなど）でフィルタリングします

```console
$ systemctl --state=failed
UNIT                  LOAD   ACTIVE SUB    DESCRIPTION
mysql.service         loaded failed failed MySQL Database Server
docker.service        loaded failed failed Docker Application Container Engine
```

### **--failed**

失敗したユニットのみを表示します

```console
$ systemctl --failed
UNIT                  LOAD   ACTIVE SUB    DESCRIPTION
mysql.service         loaded failed failed MySQL Database Server
docker.service        loaded failed failed Docker Application Container Engine
```

### **-l, --full**

ユニット名、ステータステキスト、ユニットの説明を省略せずに表示します

```console
$ systemctl status sshd.service -l
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2025-05-04 10:15:23 UTC; 2h 30min ago
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 1190 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
   Main PID: 1226 (sshd)
      Tasks: 1 (limit: 4611)
     Memory: 6.5M
        CPU: 236ms
     CGroup: /system.slice/ssh.service
             └─1226 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"
```

## 使用例

### サービスの起動

```console
$ sudo systemctl start nginx.service
```

### サービスの停止

```console
$ sudo systemctl stop nginx.service
```

### サービスの再起動

```console
$ sudo systemctl restart nginx.service
```

### サービスの状態確認

```console
$ systemctl status nginx.service
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2025-05-04 12:34:56 UTC; 2h ago
       Docs: man:nginx(8)
   Main PID: 1234 (nginx)
      Tasks: 5 (limit: 4611)
     Memory: 6.2M
        CPU: 123ms
     CGroup: /system.slice/nginx.service
             ├─1234 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             ├─1235 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             ├─1236 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" 
             ├─1237 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             └─1238 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
```

### サービスをブート時に自動起動するよう設定

```console
$ sudo systemctl enable nginx.service
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /lib/systemd/system/nginx.service.
```

### サービスのブート時自動起動を無効化

```console
$ sudo systemctl disable nginx.service
Removed /etc/systemd/system/multi-user.target.wants/nginx.service.
```

### システムブートログの表示

```console
$ systemctl list-jobs
JOB UNIT                      TYPE  STATE  
423 systemd-backlight@backlight:acpi_video0.service start running
425 systemd-rfkill.service    start running
426 systemd-update-utmp-runlevel.service start running
427 multi-user.target         start running
```

## ヒント:

### タブ補完を活用する

systemctl はユニット名のタブ補完をサポートしているため、正確な名前を覚えていなくてもサービスを簡単に管理できます。

### サービスの依存関係を確認する

`systemctl list-dependencies [ユニット]` を使用して、特定のサービスが依存している他のサービスや、それに依存しているサービスを確認できます。

### サービスをマスクする

サービスが（手動でも）起動されないようにしたい場合は、`systemctl mask [サービス]` を使用します。これにより /dev/null へのシンボリックリンクが作成され、サービスの起動が不可能になります。

### reload と restart の違い

設定ファイルだけを再読み込みしてサービスを中断したくない場合は `systemctl reload [サービス]` を使用します。サービスを完全に停止して再起動する必要がある場合は `restart` を使用します。

### サービスログの表示

systemctl と journalctl を組み合わせて特定のサービスのログを表示できます: `journalctl -u [サービス]`

## よくある質問

#### Q1. 「enable」と「start」の違いは何ですか？
A. `enable` はサービスをブート時に自動的に起動するよう設定し、`start` はサービスを即座に起動します。サービスは有効化されていても現在実行されていない場合や、実行中でも有効化されていない場合があります。

#### Q2. 利用可能なすべてのサービスを確認するにはどうすればよいですか？
A. `systemctl list-unit-files --type=service` を使用すると、利用可能なすべてのサービスユニットとその有効/無効状態を確認できます。

#### Q3. サービスがブート時に起動するよう設定されているかを確認するにはどうすればよいですか？
A. `systemctl is-enabled [サービス]` を使用すると、「enabled」または「disabled」が返されます。

#### Q4. サービスの「masked」ステータスとは何ですか？
A. マスクされたサービスは、手動でも自動でも完全に起動が防止されています。これは「disabled」よりも強力な形態です。

#### Q5. 特定のサービスに依存するすべてのサービスを再起動するにはどうすればよいですか？
A. `systemctl restart --all [サービス]` を使用すると、そのサービスとそれに依存するすべてのサービスが再起動します。

## 参考資料

https://www.freedesktop.org/software/systemd/man/systemctl.html

## 改訂履歴

- 2025/05/04 初版作成