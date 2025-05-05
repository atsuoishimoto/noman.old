# apt コマンド

Debian系Linuxディストリビューション（Ubuntuなど）用のパッケージ管理ユーティリティです。

## 概要

`apt`（Advanced Package Tool）は、Debian系Linuxディストリビューションでソフトウェアパッケージのインストール、更新、削除、管理を行うためのコマンドラインユーティリティです。依存関係を自動的に処理し、`dpkg`などの低レベルツールと比較してユーザーフレンドリーなインターフェースを提供することで、パッケージ管理を簡素化します。

## オプション

### **-y, --yes, --assume-yes**

プロンプトに自動的に「yes」と答え、非対話的な使用を可能にします

```console
$ sudo apt install firefox -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
firefox is already the newest version (115.0+build2-0ubuntu0.22.04.1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

### **-q, --quiet**

進行状況インジケータを省略し、ログ記録に適した出力を生成します

```console
$ sudo apt update -q
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Fetched 110 kB in 1s (110 kB/s)
Reading package lists...
Building dependency tree...
Reading state information...
All packages are up to date.
```

### **--no-install-recommends**

推奨パッケージのインストールをスキップし、必須の依存関係のみをインストールします

```console
$ sudo apt install gimp --no-install-recommends
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be installed:
  gimp gimp-data libbabl-0.1-0 libgegl-0.4-0 [...]
```

### **-s, --simulate, --just-print, --dry-run, --recon, --no-act**

アクションをシミュレートしますが、実際にはシステムを変更しません

```console
$ sudo apt remove firefox -s
NOTE: This is only a simulation!
      apt needs root privileges for real execution.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  firefox
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
Remv firefox [115.0+build2-0ubuntu0.22.04.1]
```

## 使用例

### パッケージのインストール

```console
$ sudo apt install vlc
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libvlc-bin libvlc5 libvlccore9 vlc-bin vlc-data vlc-plugin-base
Suggested packages:
  vlc-plugin-access-extra vlc-plugin-video-output vlc-plugin-video-splitter
  vlc-plugin-visualization
The following NEW packages will be installed:
  libvlc-bin libvlc5 libvlccore9 vlc vlc-bin vlc-data vlc-plugin-base
0 upgraded, 7 newly installed, 0 to remove and 0 not upgraded.
Need to get 7,192 kB of archives.
After this operation, 32.8 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

### パッケージリストの更新

```console
$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Fetched 229 kB in 2s (114 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
```

### インストール済みパッケージのアップグレード

```console
$ sudo apt upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  firefox libnss3 python3-software-properties software-properties-common
4 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 75.8 MB of archives.
After this operation, 1,024 B of additional disk space will be used.
Do you want to continue? [Y/n] y
```

### パッケージの削除

```console
$ sudo apt remove gimp
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  gimp
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 20.5 MB disk space will be freed.
Do you want to continue? [Y/n] y
```

### パッケージの検索

```console
$ apt search text-editor
Sorting... Done
Full Text Search... Done
gedit/jammy,now 41.0-3 amd64 [installed]
  GNU text editor for the GNOME desktop environment

mousepad/jammy 0.5.8-1 amd64
  simple Xfce oriented text editor

nano/jammy,now 6.2-1 amd64 [installed]
  small, friendly text editor inspired by Pico
```

## ヒント:

### apt-getの代わりにaptを使用する

`apt`は古い`apt-get`コマンドと比較して、プログレスバーやカラー出力を備えたよりユーザーフレンドリーなインターフェースを提供しながら、最も一般的に使用される機能を提供します。

### 未使用パッケージのクリーンアップ

`sudo apt autoremove`を定期的に実行して、依存関係として自動的にインストールされたが、もはや必要とされないパッケージを削除しましょう。

### 壊れたパッケージの修復

パッケージのインストールに問題が発生した場合は、`sudo apt --fix-broken install`を試して依存関係の問題を解決してください。

### 利用可能なディスク容量の確認

大規模なインストールやアップグレードの前に、`df -h`で利用可能なディスク容量を確認しましょう。容量不足になるとパッケージ操作が失敗する可能性があります。

### apt-markでパッケージを保護する

`sudo apt-mark hold パッケージ名`を使用して、パッケージが自動的にアップグレード、削除、またはインストールされるのを防ぐことができます。

## よくある質問

#### Q1. aptとapt-getの違いは何ですか？
A. `apt`は、`apt-get`と`apt-cache`の最も一般的に使用される機能を組み合わせた、より使いやすい新しいコマンドで、出力フォーマットと進行状況の情報が改善されています。

#### Q2. 設定ファイルを含めてパッケージを完全に削除するにはどうすればよいですか？
A. `remove`の代わりに`sudo apt purge パッケージ名`を使用します。不要になった依存関係も削除するには、`autoremove`を追加します：`sudo apt purge パッケージ名 && sudo apt autoremove`。

#### Q3. 特定のバージョンのパッケージをインストールするにはどうすればよいですか？
A. `sudo apt install パッケージ名=バージョン`を使用します。例：`sudo apt install nginx=1.18.0-0ubuntu1`。

#### Q4. 「Unable to lock the administration directory」エラーを修正するにはどうすればよいですか？
A. これは通常、別のパッケージマネージャーが実行中であることを意味します。終了するのを待つか、`ps aux | grep apt`で停止したプロセスを確認し、必要に応じて終了させてください。また、`sudo rm /var/lib/apt/lists/lock /var/cache/apt/archives/lock /var/lib/dpkg/lock*`でロックファイルを削除する必要がある場合もあります。

#### Q5. 単一のパッケージを更新するにはどうすればよいですか？
A. `sudo apt install --only-upgrade パッケージ名`を使用します。

## 参考資料

https://manpages.ubuntu.com/manpages/jammy/man8/apt.8.html

## 改訂履歴

- 2025/05/04 初回改訂