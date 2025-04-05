# `passwd` コマンドの概要

`passwd`は、ユーザーアカウントのパスワードを変更するためのコマンドです。自分自身のパスワードを変更したり、管理者権限で他のユーザーのパスワードを変更したりすることができます。

## 主なオプション

- **オプションなし**: 自分自身のパスワードを変更します
  - 例: `passwd`

- **-l**: ユーザーアカウントをロック（使用不可）にします（root権限が必要）
  - 例: `sudo passwd -l username`

- **-u**: ロックされたユーザーアカウントのロックを解除します（root権限が必要）
  - 例: `sudo passwd -u username`

- **-d**: ユーザーのパスワードを削除します（パスワードなしでログイン可能になる場合があります）（root権限が必要）
  - 例: `sudo passwd -d username`

- **-e**: ユーザーのパスワードの有効期限を即時に切れた状態にします（次回ログイン時にパスワード変更を強制）（root権限が必要）
  - 例: `sudo passwd -e username`

- **-S**: アカウントのパスワード状態を表示します（root権限が必要）
  - 例: `sudo passwd -S username`

## 使用例

```bash
# 自分のパスワードを変更する
passwd
# 出力例
Current password: （現在のパスワードを入力）
New password: （新しいパスワードを入力）
Retype new password: （新しいパスワードを再入力）
passwd: password updated successfully

# 管理者として他のユーザーのパスワードを変更する
sudo passwd username
# 出力例
New password: （新しいパスワードを入力）
Retype new password: （新しいパスワードを再入力）
passwd: password updated successfully

# ユーザーアカウントをロックする
sudo passwd -l username
# 出力例
passwd: password expiry information changed.

# ユーザーアカウントのパスワード状態を確認する
sudo passwd -S username
# 出力例
username P 04/15/2023 0 99999 7 -1
# P=パスワードあり、L=ロック済み、NP=パスワードなし
```

## 追加情報

- パスワード変更時は、セキュリティのため入力内容は画面に表示されません。
- 一般ユーザーは自分自身のパスワードのみ変更できます。他のユーザーのパスワードを変更するには管理者権限（root）が必要です。
- システムによっては、パスワードの複雑さ（長さ、文字種類など）に関する要件があります。要件を満たさないパスワードは拒否されます。
- パスワードポリシーはシステム管理者によって設定されており、`/etc/security/pwquality.conf`などのファイルで確認できる場合があります。
- パスワードを忘れた場合は、自分で変更することはできません。システム管理者に連絡する必要があります。