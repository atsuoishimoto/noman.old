# systemctl コマンドの概要

systemctl は、systemd システムとサービスマネージャーを制御するためのコマンドです。サービスの起動・停止、状態確認、自動起動の設定などを行うことができます。

## 主なオプション

- **status**: サービスの現在の状態を確認します
  - 例: `systemctl status nginx`

- **start**: サービスを起動します
  - 例: `systemctl start nginx`

- **stop**: サービスを停止します
  - 例: `systemctl stop nginx`

- **restart**: サービスを再起動します
  - 例: `systemctl restart nginx`

- **reload**: サービスの設定を再読み込みします（可能な場合）
  - 例: `systemctl reload nginx`

- **enable**: システム起動時に自動的にサービスを起動するよう設定します
  - 例: `systemctl enable nginx`

- **disable**: システム起動時の自動起動を無効にします
  - 例: `systemctl disable nginx`

- **is-active**: サービスが実行中かどうかを確認します
  - 例: `systemctl is-active nginx`

- **is-enabled**: サービスが自動起動に設定されているかを確認します
  - 例: `systemctl is-enabled nginx`

- **list-units**: 読み込まれたユニット（サービスなど）を一覧表示します
  - 例: `systemctl list-units --type=service`

## 使用例

### サービスの状態確認

```bash
# Nginxの状態を確認
systemctl status nginx
# 出力例
● nginx.service - A high performance web server and a reverse proxy server
   Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
   Active: active (running) since Mon 2023-04-03 12:34:56 JST; 2h ago
     Docs: man:nginx(8)
  Process: 1234 ExecStartPre=/usr/sbin/nginx -t -q -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
  Process: 1235 ExecStart=/usr/sbin/nginx -g daemon on; master_process on; (code=exited, status=0/SUCCESS)
 Main PID: 1236 (nginx)
    Tasks: 2 (limit: 4915)
   CGroup: /system.slice/nginx.service
           ├─1236 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
           └─1237 nginx: worker process
```

### サービスの起動と停止

```bash
# サービスを起動
systemctl start nginx
# 特に成功時は出力なし

# サービスを停止
systemctl stop nginx
# 特に成功時は出力なし
```

### 自動起動の設定

```bash
# 自動起動を有効化
systemctl enable nginx
# 出力例
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /lib/systemd/system/nginx.service.

# 自動起動を無効化
systemctl disable nginx
# 出力例
Removed /etc/systemd/system/multi-user.target.wants/nginx.service.
```

### 実行中のサービス一覧表示

```bash
# 実行中のサービスを一覧表示
systemctl list-units --type=service --state=running
# 出力例（一部）
UNIT                  LOAD   ACTIVE SUB     DESCRIPTION
nginx.service         loaded active running A high performance web server and a reverse proxy server
ssh.service           loaded active running OpenSSH server daemon
systemd-journald.service loaded active running Journal Service
```

## 追加情報

- `sudo` が必要：多くの systemctl コマンドは管理者権限が必要なため、`sudo` を付けて実行する必要があります。
- システム全体の再起動・シャットダウンも可能です：`systemctl reboot` や `systemctl poweroff` などのコマンドがあります。
- ユニットファイル：各サービスの設定は `/etc/systemd/system/` や `/lib/systemd/system/` ディレクトリにあるユニットファイルで定義されています。
- 設定変更後は `systemctl daemon-reload` を実行すると、systemd が設定を再読み込みします。