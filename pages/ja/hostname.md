# hostname コマンド

システムのホスト名を表示または設定します。

## 概要

`hostname` コマンドは、現在のシステムのホスト名（コンピュータ名）を表示したり、管理者権限で実行した場合はホスト名を変更したりするために使用します。ホスト名はネットワーク上でコンピュータを識別するために使用される名前です。

## オプション

### **-s (--short)**

短いホスト名のみを表示します（ドメイン名を含まない）。

```console
$ hostname -s
macbook
```

### **-f (--fqdn, --long)**

完全修飾ドメイン名（FQDN）を表示します。

```console
$ hostname -f
macbook.local
```

### **-i (--ip-address)**

ホスト名に関連付けられたIPアドレスを表示します。

```console
$ hostname -i
192.168.1.5
```

### **-d (--domain)**

DNSドメイン名のみを表示します。

```console
$ hostname -d
local
```

## 使用例

### 現在のホスト名を表示する

```console
$ hostname
macbook.local
```

### ホスト名を変更する（管理者権限が必要）

```console
$ sudo hostname new-hostname
[sudo] password for user: 
$ hostname
new-hostname
```

### すべてのネットワーク情報を表示する

```console
$ hostname -a
macbook.local
```

## ヒント:

### ホスト名の永続的な変更

`hostname` コマンドでの変更は一時的なものです。システムの再起動後も変更を維持するには、システム固有の設定ファイルを編集する必要があります。

- Linux: `/etc/hostname` ファイルを編集
- macOS: システム環境設定 > 共有 > コンピュータ名

### ホスト名とDNS

ホスト名はローカルマシンの識別子であり、必ずしもDNSに登録されているわけではありません。完全なネットワーク接続性のためには、DNSの設定も確認してください。

### ホスト名の命名規則

ホスト名には英数字とハイフン（-）のみを使用し、スペースや特殊文字は避けるのがベストプラクティスです。

## よくある質問

#### Q1. ホスト名とは何ですか？
A. ホスト名はネットワーク上でコンピュータを識別するための名前です。これによりIPアドレスを覚える代わりに名前でマシンを参照できます。

#### Q2. ホスト名を永続的に変更するにはどうすればよいですか？
A. システムによって異なります。Linuxでは通常 `/etc/hostname` ファイルを編集し、macOSではシステム環境設定から変更します。

#### Q3. FQDNとは何ですか？
A. 完全修飾ドメイン名（Fully Qualified Domain Name）は、ホスト名とドメイン名を含む完全なコンピュータ名です（例：server.example.com）。

#### Q4. ホスト名を変更した後、他のサービスを再起動する必要がありますか？
A. はい、多くの場合、ネットワークサービスやアプリケーションは起動時にホスト名を読み込むため、変更後は再起動が必要な場合があります。

## macOSでの注意点

macOSでは、`hostname` コマンドでホスト名を変更しても、「システム環境設定 > 共有」に表示されるコンピュータ名は変更されません。永続的な変更のためには、システム環境設定から変更するか、以下のコマンドを使用します：

```console
$ sudo scutil --set HostName new-hostname
$ sudo scutil --set LocalHostName new-hostname
$ sudo scutil --set ComputerName new-hostname
```

## 参考情報

https://linux.die.net/man/1/hostname

## 改訂履歴

- 2025/04/30 初版作成