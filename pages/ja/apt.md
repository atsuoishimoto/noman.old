# apt コマンド

Debian系Linuxディストリビューションでパッケージの検索、インストール、更新、削除を行うパッケージ管理ツール。

## 概要

`apt`（Advanced Package Tool）は、Debian系のLinuxディストリビューション（Ubuntu、Linux Mintなど）でソフトウェアパッケージを管理するためのコマンドラインツールです。`apt-get`や`apt-cache`などの古いコマンドの機能を統合し、より使いやすいインターフェースを提供します。パッケージのインストール、更新、削除、検索などの操作を簡単に行うことができます。

## オプション

### **update**

パッケージリストを更新します。新しいパッケージをインストールする前に実行することをお勧めします。

```console
$ sudo apt update
[sudo] password for user: 
Hit:1 http://jp.archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://jp.archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Get:3 http://jp.archive.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Fetched 229 kB in 2s (114 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
```

### **install**

指定したパッケージをインストールします。

```console
$ sudo apt install firefox
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be upgraded:
  firefox
1 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 65.4 MB of archives.
After this operation, 12.3 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

### **upgrade**

インストール済みのパッケージを最新バージョンにアップグレードします。

```console
$ sudo apt upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  firefox libreoffice-calc libreoffice-writer
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 112 MB of archives.
After this operation, 15.6 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

### **remove**

指定したパッケージを削除します。

```console
$ sudo apt remove firefox
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  firefox
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 212 MB disk space will be freed.
Do you want to continue? [Y/n] y
```

### **search**

パッケージを検索します。

```console
$ apt search text editor
Sorting... Done
Full Text Search... Done
gedit/jammy,now 41.0-1 amd64 [installed]
  GNU Emacs editor for the GNOME desktop

nano/jammy,now 6.2-1 amd64 [installed]
  small, friendly text editor inspired by Pico

vim/jammy 2:8.2.3995-1ubuntu2 amd64
  Vi IMproved - enhanced vi editor
```

## 使用例

### パッケージのインストールと更新

```console
$ sudo apt update && sudo apt upgrade
[sudo] password for user: 
Hit:1 http://jp.archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://jp.archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  firefox libreoffice-calc
2 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Do you want to continue? [Y/n] y
```

### 特定のパッケージに関する情報の表示

```console
$ apt show firefox
Package: firefox
Version: 124.0.1+build1-0ubuntu0.22.04.1
Priority: optional
Section: web
Origin: Ubuntu
Maintainer: Ubuntu Mozilla Team <ubuntu-mozillateam@lists.ubuntu.com>
Installed-Size: 256 MB
Provides: gnome-www-browser, www-browser
Depends: lsb-release, libasound2, libatk1.0-0, ...
Homepage: https://www.mozilla.org/firefox/
Download-Size: 65.4 MB
APT-Sources: http://jp.archive.ubuntu.com/ubuntu jammy-updates/main amd64 Packages
Description: Safe and easy web browser from Mozilla
 Firefox delivers safe, easy web browsing. A familiar user interface,
 enhanced security features including protection from online identity theft,
 and integrated search let you get the most out of the web.
```

### パッケージの完全削除（設定ファイルも含む）

```console
$ sudo apt purge firefox
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  firefox*
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 212 MB disk space will be freed.
Do you want to continue? [Y/n] y
```

## ヒント:

### 自動応答でインストールする

`-y`オプションを使用すると、確認プロンプトに自動的に「yes」と応答します。スクリプト内でaptを使用する場合に便利です。

```console
$ sudo apt install -y firefox
```

### 不要なパッケージの削除

`apt autoremove`を使用すると、依存関係として自動的にインストールされたが、現在は不要になったパッケージを削除できます。

```console
$ sudo apt autoremove
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  libllvm13 linux-headers-5.15.0-60 linux-headers-5.15.0-60-generic
0 upgraded, 0 newly installed, 3 to remove and 0 not upgraded.
After this operation, 122 MB disk space will be freed.
Do you want to continue? [Y/n] y
```

### パッケージリストのクリーンアップ

`apt clean`を使用すると、ダウンロードしたパッケージファイルのローカルリポジトリをクリーンアップできます。ディスク容量を節約したい場合に役立ちます。

```console
$ sudo apt clean
```

## よくある質問

#### Q1. aptとapt-getの違いは何ですか？
A. `apt`は`apt-get`や`apt-cache`などの古いコマンドの機能を統合し、より使いやすいインターフェースを提供します。進行状況バーの表示や色分けされた出力など、ユーザーフレンドリーな機能が追加されています。

#### Q2. パッケージをインストールせずに、ダウンロードだけするにはどうすればいいですか？
A. `apt download パッケージ名`を使用すると、パッケージをインストールせずにダウンロードだけ行えます。

#### Q3. インストール可能なパッケージのバージョンを確認するにはどうすればいいですか？
A. `apt policy パッケージ名`または`apt-cache policy パッケージ名`を使用すると、利用可能なバージョンとインストール候補を確認できます。

#### Q4. 特定のパッケージが依存しているパッケージを確認するにはどうすればいいですか？
A. `apt depends パッケージ名`を使用すると、そのパッケージが依存している他のパッケージを確認できます。

## 参考資料

https://manpages.ubuntu.com/manpages/jammy/man8/apt.8.html

## 改訂履歴

- 2025/04/30 初版作成