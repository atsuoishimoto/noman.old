# systemctl コマンド
systemdシステムとサービスマネージャーを制御するためのコマンドラインツールです。

## 概要
systemctlは、Linuxシステムでサービスの起動・停止、状態確認、自動起動設定などを管理するためのコマンドです。systemdを採用したLinuxディストリビューションで使用され、システム全体の管理も行えます。

## オプション
### **status**
サービスの現在の状態を詳細に表示します。
```console
$ sudo systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2023-04-03 12:34:56 JST; 2h ago
     Docs: man:nginx(8)
  Process: 1234 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
 Main PID: 1236 (nginx)
    Tasks: 2 (limit: 4915)
   CGroup: /system.slice/nginx.service
           ├─1236 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─1237 nginx: worker process
```

### **start/stop**
サービスを起動または停止します。
```console
$ sudo systemctl start nginx
$ sudo systemctl stop nginx
```

### **restart/reload**
サービスを再起動、または設定を再読み込みします。
```console
$ sudo systemctl restart nginx
$ sudo systemctl reload nginx  # 設定のみ再読み込み（サービスによっては未対応）
```

### **enable/disable**
システム起動時のサービス自動起動を設定・解除します。
```console
$ sudo systemctl enable nginx
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /lib/systemd/system/nginx.service.

$ sudo systemctl disable nginx
Removed /etc/systemd/system/multi-user.target.wants/nginx.service.
```

### **list-units**
読み込まれたユニット（サービスなど）を一覧表示します。
```console
$ systemctl list-units --type=service
UNIT                  LOAD   ACTIVE SUB     DESCRIPTION
nginx.service         loaded active running A high performance web server and a reverse proxy server
ssh.service           loaded active running OpenSSH server daemon
systemd-journald.service loaded active running Journal Service
...
```

## 使用例
### システム全体の再起動とシャットダウン
```console
$ sudo systemctl reboot    # システムを再起動
$ sudo systemctl poweroff  # システムをシャットダウン
```

### サービスの状態確認と自動起動チェック
```console
$ systemctl is-active nginx
active

$ systemctl is-enabled nginx
enabled
```

### 失敗したサービスの確認
```console
$ systemctl --failed
UNIT           LOAD   ACTIVE SUB    DESCRIPTION
mysql.service  loaded failed failed MySQL Database Server
```

## ヒント:
### 設定変更後はdaemon-reloadを実行する
ユニットファイルを変更した後は、systemdに変更を認識させるために以下のコマンドを実行します。
```console
$ sudo systemctl daemon-reload
```

### ジャーナルログの確認
特定のサービスのログを確認するには、journalctlコマンドと組み合わせて使用します。
```console
$ sudo journalctl -u nginx
```

### マスクによるサービスの完全無効化
サービスを完全に無効化し、手動でも起動できないようにするには、maskオプションを使用します。
```console
$ sudo systemctl mask bluetooth
Created symlink /etc/systemd/system/bluetooth.service → /dev/null.
```

## Frequently Asked Questions
#### Q1. systemctlとservice/chkconfigコマンドの違いは何ですか？
A. systemctlはsystemdベースのシステム用のコマンドで、古いSysVinit用のserviceやchkconfigコマンドを置き換えるものです。より多機能で一貫性のある管理インターフェースを提供します。

#### Q2. サービスの設定ファイルはどこにありますか？
A. 主に`/etc/systemd/system/`や`/lib/systemd/system/`ディレクトリにユニットファイル（.serviceファイル）として保存されています。

#### Q3. 「Failed to connect to bus」エラーが出る場合はどうすればよいですか？
A. このエラーは通常、rootユーザー権限がない場合に発生します。`sudo`を付けてコマンドを実行してください。

#### Q4. systemctlコマンドはmacOSで使えますか？
A. いいえ、systemctlはLinux特有のコマンドで、macOSでは使用できません。macOSではlaunchdシステムを使用し、`launchctl`コマンドで同様の機能を実現します。

## References
https://www.freedesktop.org/software/systemd/man/systemctl.html

## Revisions
- 2025/04/27 ドキュメント全体を改訂し、フォーマットを統一。FAQセクションとヒントセクションを追加。macOSに関する注意事項を追加。