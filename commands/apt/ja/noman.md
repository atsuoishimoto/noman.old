# apt コマンド概要

`apt`（Advanced Package Tool）は、Debian系Linuxディストリビューション（UbuntuやLinux Mintなど）でソフトウェアパッケージの検索、インストール、アップデート、削除を行うためのコマンドラインツールです。

## 主なオプション

- **apt update**: パッケージリストを更新します
  - 例: `sudo apt update`

- **apt upgrade**: インストール済みのパッケージを最新バージョンにアップグレードします
  - 例: `sudo apt upgrade`

- **apt install**: 新しいパッケージをインストールします
  - 例: `sudo apt install パッケージ名`

- **apt remove**: パッケージを削除します（設定ファイルは残ります）
  - 例: `sudo apt remove パッケージ名`

- **apt purge**: パッケージを設定ファイルごと完全に削除します
  - 例: `sudo apt purge パッケージ名`

- **apt search**: パッケージを検索します
  - 例: `apt search キーワード`

- **apt show**: パッケージの詳細情報を表示します
  - 例: `apt show パッケージ名`

- **apt list**: パッケージのリストを表示します
  - 例: `apt list --installed`（インストール済みのパッケージを表示）

- **apt autoremove**: 不要になった依存パッケージを自動的に削除します
  - 例: `sudo apt autoremove`

## 使用例

```bash
# システムのパッケージリストを更新する
sudo apt update
# 出力例
Hit:1 http://archive.ubuntu.com/ubuntu focal InRelease
Get:2 http://security.ubuntu.com/ubuntu focal-security InRelease [114 kB]
Reading package lists... Done
Building dependency tree... Done
All packages are up to date.

# Firefoxをインストールする
sudo apt install firefox
# 出力例
Reading package lists... Done
Building dependency tree... Done
The following packages will be installed:
  firefox
Do you want to continue? [Y/n] y
Setting up firefox (115.0+build2-0ubuntu0.20.04.1) ...
Processing triggers for desktop-file-utils (0.24-1ubuntu3) ...

# インストール済みのパッケージをアップグレードする
sudo apt upgrade
# 出力例
Reading package lists... Done
Building dependency tree... Done
Calculating upgrade... Done
The following packages will be upgraded:
  firefox libc6 python3-apt
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Do you want to continue? [Y/n] y

# VLCメディアプレーヤーに関連するパッケージを検索する
apt search vlc
# 出力例
Sorting... Done
Full Text Search... Done
vlc/focal 3.0.9.2-1 amd64
  multimedia player and streamer

vlc-bin/focal 3.0.9.2-1 amd64
  binaries for VLC

# Firefoxを削除する
sudo apt remove firefox
# 出力例
Reading package lists... Done
Building dependency tree... Done
The following packages will be REMOVED:
  firefox
Do you want to continue? [Y/n] y
Removing firefox (115.0+build2-0ubuntu0.20.04.1) ...
```

## 追加メモ

- ほとんどの`apt`コマンドは管理者権限が必要なため、`sudo`を付けて実行する必要があります。
- `apt`は古い`apt-get`や`apt-cache`コマンドの機能を統合し、よりユーザーフレンドリーなインターフェースを提供しています。
- システムを最新の状態に保つには、定期的に`sudo apt update && sudo apt upgrade`を実行することをお勧めします。
- 大規模なアップグレードを行う前に`sudo apt dist-upgrade`を使用すると、依存関係の変更も含めて処理できます。
- パッケージのインストール時に`-y`オプションを追加すると（例：`sudo apt install -y パッケージ名`）、確認プロンプトをスキップできます。