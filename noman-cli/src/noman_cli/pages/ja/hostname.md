# hostname コマンド

システムのホスト名を表示または設定します。

## 概要

`hostname` コマンドは、システムの現在のホスト名を表示または設定します。ホスト名とは、ネットワーク上でデバイスが認識される名前のことです。このコマンドは、スクリプト内で現在のマシンを識別する場合や、複数のシステムで作業する際に役立ちます。

## オプション

### **-s, --short**

ドメイン情報を除いた短いホスト名を表示します。

```console
$ hostname -s
mycomputer
```

### **-f, --fqdn, --long**

完全修飾ドメイン名（FQDN）を表示します。

```console
$ hostname -f
mycomputer.example.com
```

### **-d, --domain**

DNSドメイン名を表示します。

```console
$ hostname -d
example.com
```

### **-i, --ip-address**

ホストのIPアドレスを表示します。

```console
$ hostname -i
192.168.1.100
```

### **-I, --all-ip-addresses**

ホストのすべてのネットワークアドレスを表示します。

```console
$ hostname -I
192.168.1.100 10.0.0.1 172.16.0.1
```

## 使用例

### 現在のホスト名の表示

```console
$ hostname
mycomputer.example.com
```

### 新しいホスト名の設定（root権限が必要）

```console
$ sudo hostname newname
$ hostname
newname
```

### スクリプト内で現在のマシンを識別するためにホスト名を使用

```console
$ echo "バックアップスクリプトを $(hostname) で実行中"
バックアップスクリプトを mycomputer.example.com で実行中
```

## ヒント:

### 永続的なホスト名の変更

`hostname` コマンドは次の再起動までホスト名を一時的に変更するだけです。永続的な変更には：
- systemdベースのシステム：`hostnamectl set-hostname newname` を使用
- Debian/Ubuntu：`/etc/hostname` を編集
- RHEL/CentOS：`/etc/sysconfig/network` を編集

### ネットワーク設定

ホスト名を変更する場合、適切な名前解決を確保するために `/etc/hosts` などの他のファイルも更新する必要があるかもしれません。

### ホスト名の制限

ホスト名はRFC 1178のガイドラインに従うべきです：文字、数字、ハイフンのみを使用し、63文字を超えないようにしましょう。

## よくある質問

#### Q1. ホスト名とFQDNの違いは何ですか？
A. ホスト名はマシンの名前だけ（例：「mycomputer」）であるのに対し、FQDNはドメインを含みます（例：「mycomputer.example.com」）。

#### Q2. 再起動後にホスト名がリセットされるのはなぜですか？
A. `hostname` コマンドは一時的な変更のみを行います。永続的な変更を行うには、システム設定ファイルを変更するか、`hostnamectl` などのツールを使用する必要があります。

#### Q3. ホスト名に特殊文字を使用できますか？
A. すべてのネットワークサービスとの互換性を確保するために、ホスト名には文字、数字、ハイフンのみを使用することが推奨されています。

#### Q4. スクリプト内でホスト名を取得するにはどうすればよいですか？
A. スクリプト内で `$(hostname)` を使用するだけで、現在のホスト名を取得できます。

## macOSに関する注意点

macOSでは、hostname コマンドは同様に機能しますが、永続的な変更は以下を使用して行うべきです：
- ホスト名の場合は `sudo scutil --set HostName newname`
- Bonjourホスト名の場合は `sudo scutil --set LocalHostName newname`
- ユーザーフレンドリーなコンピュータ名の場合は `sudo scutil --set ComputerName "新しい名前"`

## 参考資料

https://man7.org/linux/man-pages/man1/hostname.1.html

## 改訂履歴

2025/05/04 初版作成