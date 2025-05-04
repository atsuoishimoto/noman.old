# dpkg コマンド

Debian ベースのシステム（Ubuntu など）で Debian パッケージファイル（.deb）を管理する。

## 概要

`dpkg` は Debian ベースの Linux ディストリビューション向けのパッケージ管理システムです。.deb パッケージのインストール、削除、情報表示などを処理します。`apt` のような高レベルのパッケージマネージャとは異なり、`dpkg` は .deb ファイルを直接扱い、依存関係を自動的に解決しません。

## オプション

### **-i, --install**

.deb ファイルからパッケージをインストールします

```console
$ sudo dpkg -i firefox_115.0+build2-0ubuntu0.20.04.1_amd64.deb
Selecting previously unselected package firefox.
(Reading database ... 186342 files and directories currently installed.)
Preparing to unpack firefox_115.0+build2-0ubuntu0.20.04.1_amd64.deb ...
Unpacking firefox (115.0+build2-0ubuntu0.20.04.1) ...
Setting up firefox (115.0+build2-0ubuntu0.20.04.1) ...
Processing triggers for mime-support (3.64ubuntu1) ...
```

### **-r, --remove**

インストール済みのパッケージを削除します（設定ファイルは保持）

```console
$ sudo dpkg -r firefox
(Reading database ... 186342 files and directories currently installed.)
Removing firefox (115.0+build2-0ubuntu0.20.04.1) ...
```

### **-P, --purge**

インストール済みのパッケージを完全に削除します（設定ファイルも含む）

```console
$ sudo dpkg -P firefox
(Reading database ... 186342 files and directories currently installed.)
Removing firefox (115.0+build2-0ubuntu0.20.04.1) ...
Purging configuration files for firefox ...
```

### **-l, --list [パターン]**

オプションのパターンに一致するインストール済みパッケージを一覧表示します

```console
$ dpkg -l firefox
| Status=Not/Inst/Conf-files/Unpacked/halF-conf/Half-inst/trig-aWait/Trig-pend
|/ Err?=(none)/Reinst-required (Status,Err: uppercase=bad)
||/ Name           Version      Architecture Description
+++-==============-============-============-=================================
ii  firefox        115.0+build2 amd64        Safe and easy web browser from Mozilla
```

### **-L, --listfiles**

パッケージによってインストールされたファイルを一覧表示します

```console
$ dpkg -L firefox
/.
/usr
/usr/bin
/usr/bin/firefox
/usr/lib
/usr/lib/firefox
...
```

### **-S, --search**

特定のファイルを所有するパッケージを検索します

```console
$ dpkg -S /usr/bin/firefox
firefox: /usr/bin/firefox
```

### **-s, --status**

パッケージの詳細なステータス情報を表示します

```console
$ dpkg -s firefox
Package: firefox
Status: install ok installed
Priority: optional
Section: web
Installed-Size: 256348
Maintainer: Ubuntu Mozilla Team <ubuntu-mozillateam@lists.ubuntu.com>
Architecture: amd64
Version: 115.0+build2-0ubuntu0.20.04.1
Depends: lsb-release, libatk1.0-0 (>= 1.12.4), libc6 (>= 2.28), ...
Description: Safe and easy web browser from Mozilla
 Firefox delivers safe, easy web browsing. A familiar user interface,
 enhanced security features including protection from online identity theft,
 and integrated search let you get the most out of the web.
```

### **--configure**

セットアップが必要な展開済みパッケージを設定します

```console
$ sudo dpkg --configure firefox
Setting up firefox (115.0+build2-0ubuntu0.20.04.1) ...
```

## 使用例

### パッケージをインストールして依存関係を修正する

```console
$ sudo dpkg -i package.deb
$ sudo apt-get install -f
```

### インストール済みのすべてのパッケージを一覧表示する

```console
$ dpkg -l
```

### ファイルがどのパッケージに属しているかを調べる

```console
$ dpkg -S /usr/bin/python3
python3-minimal: /usr/bin/python3
```

## ヒント:

### 壊れた依存関係を修正する

`dpkg` が依存関係の不足により失敗した場合は、`sudo apt-get install -f` を実行して解決します。これは .deb ファイルを直接インストールする際の一般的なワークフローです。

### パッケージリストのバックアップ

システムの大きな変更を行う前に、`dpkg --get-selections > packages.list` でインストール済みパッケージのリストを保存しておきましょう。後で `sudo dpkg --set-selections < packages.list && sudo apt-get dselect-upgrade` で復元できます。

### パッケージの整合性を検証する

インストール前に `dpkg-deb --info package.deb` でパッケージを検査し、`dpkg -V パッケージ名` でインストール済みファイルをパッケージデータベースと照合して検証できます。

### パッケージの再設定

パッケージを再設定する必要がある場合（設定を変更するなど）、`sudo dpkg-reconfigure パッケージ名` を使用すると設定スクリプトを再実行できます。

## よくある質問

#### Q1. `dpkg` と `apt` の違いは何ですか？
A. `dpkg` は .deb ファイルを直接扱い、依存関係を自動的に処理しません。`apt` はより高レベルのツールで、依存関係を解決し、リポジトリからパッケージをダウンロードできます。

#### Q2. 「依存関係の問題」エラーを修正するにはどうすればよいですか？
A. `dpkg -i` が失敗した後に `sudo apt-get install -f` を実行して、不足している依存関係を解決します。

#### Q3. インストール前に .deb パッケージがどのファイルをインストールするか確認するにはどうすればよいですか？
A. `dpkg-deb --contents package.deb` を使用して、パッケージに含まれるファイルを一覧表示します。

#### Q4. パッケージを再インストールするにはどうすればよいですか？
A. `sudo dpkg -i --force-reinstall package.deb` または apt を使用して `sudo apt-get install --reinstall パッケージ名` を実行します。

#### Q5. パッケージが自動的にアップグレードされないようにするにはどうすればよいですか？
A. `sudo apt-mark hold パッケージ名` を使用して、自動アップグレードを防止します。

## 参考資料

https://manpages.debian.org/buster/dpkg/dpkg.1.en.html

## 改訂履歴

- 2025/05/04 初版作成