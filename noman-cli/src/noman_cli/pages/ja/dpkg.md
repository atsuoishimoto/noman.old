# dpkg コマンド

Debian ベースのシステム（Ubuntu など）でパッケージの管理を行うコマンドラインツール。

## 概要

dpkg（Debian Package）は、Debian ベースの Linux ディストリビューション（Ubuntu など）で使用されるパッケージ管理システムの中核ツールです。.deb 形式のパッケージのインストール、削除、情報表示などの基本的なパッケージ管理操作を行います。apt コマンドの基盤となるツールですが、依存関係の解決は自動で行いません。

## オプション

### **-i, --install**

パッケージをインストールまたはアップグレードします。

```console
$ sudo dpkg -i firefox_115.0+build2-0ubuntu0.20.04.1_amd64.deb
(Reading database ... 200000 files and directories currently installed.)
Preparing to unpack firefox_115.0+build2-0ubuntu0.20.04.1_amd64.deb ...
Unpacking firefox (115.0+build2-0ubuntu0.20.04.1) over (114.0.2+build1-0ubuntu0.20.04.1) ...
Setting up firefox (115.0+build2-0ubuntu0.20.04.1) ...
Processing triggers for mime-support (3.64ubuntu1) ...
```

### **-r, --remove**

パッケージを削除します（設定ファイルは残ります）。

```console
$ sudo dpkg -r firefox
(Reading database ... 200000 files and directories currently installed.)
Removing firefox (115.0+build2-0ubuntu0.20.04.1) ...
```

### **-P, --purge**

パッケージを完全に削除します（設定ファイルも含めて削除）。

```console
$ sudo dpkg -P firefox
(Reading database ... 200000 files and directories currently installed.)
Purging configuration files for firefox (115.0+build2-0ubuntu0.20.04.1) ...
```

### **-l, --list [パターン]**

インストールされているパッケージを一覧表示します。パターンを指定すると、そのパターンに一致するパッケージのみを表示します。

```console
$ dpkg -l | grep firefox
ii  firefox                            115.0+build2-0ubuntu0.20.04.1        amd64        Safe and easy web browser from Mozilla
```

### **-s, --status パッケージ名**

指定したパッケージの状態を表示します。

```console
$ dpkg -s firefox
Package: firefox
Status: install ok installed
Priority: optional
Section: web
Installed-Size: 240000
Maintainer: Ubuntu Mozilla Team <ubuntu-mozilla@lists.ubuntu.com>
Architecture: amd64
Version: 115.0+build2-0ubuntu0.20.04.1
Depends: [依存関係のリスト]
Description: Safe and easy web browser from Mozilla
 Firefox delivers safe, easy web browsing. A familiar user interface,
 enhanced security features including protection from online identity theft,
 and integrated search let you get the most out of the web.
```

### **-L, --listfiles パッケージ名**

パッケージによってインストールされたファイルを一覧表示します。

```console
$ dpkg -L firefox
/.
/usr
/usr/bin
/usr/bin/firefox
/usr/lib
/usr/lib/firefox
[その他のファイル...]
```

## 使用例

### パッケージのインストールと依存関係の解決

```console
$ sudo dpkg -i mypackage.deb
dpkg: dependency problems prevent configuration of mypackage:
 mypackage depends on libsomething; however:
  Package libsomething is not installed.

$ sudo apt-get install -f
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following packages will be installed:
  libsomething
0 upgraded, 1 newly installed, 0 to remove and 0 not upgraded.
```

### システムにインストールされているすべてのパッケージを表示

```console
$ dpkg --get-selections
accountsservice                                install
acl                                            install
adduser                                        install
[その他のパッケージ...]
```

### 特定のファイルがどのパッケージに属しているか確認

```console
$ dpkg -S /usr/bin/firefox
firefox: /usr/bin/firefox
```

## ヒント:

### apt と dpkg の違いを理解する

apt は dpkg のフロントエンドで、依存関係の解決やリポジトリからのダウンロードを自動で行います。dpkg は単一パッケージの操作に特化しています。通常は apt を使用し、ローカルの .deb ファイルを直接インストールする場合に dpkg を使用するとよいでしょう。

### 壊れたパッケージの修復

パッケージのインストールが途中で失敗した場合は、`sudo dpkg --configure -a` を実行して未設定のパッケージを設定し、その後 `sudo apt-get install -f` で依存関係の問題を解決できます。

### パッケージの状態を理解する

dpkg -l の出力の最初の2文字はパッケージの状態を示します：
- `ii`: 正常にインストールされている
- `rc`: 削除されたが設定ファイルが残っている
- `un`: 未インストール

## よくある質問

#### Q1. apt と dpkg の違いは何ですか？
A. dpkg は単一パッケージの管理ツールで依存関係を自動解決しません。apt は dpkg のフロントエンドで、依存関係の解決やリポジトリからのダウンロードを自動で行います。

#### Q2. インストールに失敗したパッケージを修復するにはどうすればよいですか？
A. `sudo dpkg --configure -a` を実行して未設定のパッケージを設定し、その後 `sudo apt-get install -f` で依存関係の問題を解決します。

#### Q3. パッケージの設定ファイルだけを残して削除するにはどうすればよいですか？
A. `sudo dpkg -r パッケージ名` を使用します。設定ファイルも含めて完全に削除するには `sudo dpkg -P パッケージ名` を使用します。

#### Q4. あるファイルがどのパッケージに属しているか調べるにはどうすればよいですか？
A. `dpkg -S /path/to/file` コマンドを使用します。

## 参考文献

https://manpages.debian.org/buster/dpkg/dpkg.1.en.html

## 改訂履歴

- 2025/04/30 初版作成