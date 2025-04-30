# host コマンド

DNS（ドメインネームシステム）の検索を実行し、ドメイン名からIPアドレスへの変換や、その逆の変換を行います。

## 概要

`host` コマンドは、ドメイン名からIPアドレスへの変換（正引き）や、IPアドレスからドメイン名への変換（逆引き）を行うためのDNSルックアップユーティリティです。シンプルなインターフェースで、ネットワークの問題診断やDNS情報の確認に役立ちます。

## オプション

### **-t type**

特定のDNSレコードタイプを指定して検索します。

```console
$ host -t MX example.com
example.com mail is handled by 10 mail.example.com.
```

### **-a**

すべてのDNSレコードを表示します（ANY検索を実行）。

```console
$ host -a example.com
Trying "example.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;example.com.                   IN      ANY

;; ANSWER SECTION:
example.com.            86400   IN      A       93.184.216.34
example.com.            86400   IN      NS      a.iana-servers.net.
example.com.            86400   IN      NS      b.iana-servers.net.
...
```

### **-v**

詳細な出力を表示します（冗長モード）。

```console
$ host -v example.com
Trying "example.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 54321
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;example.com.                   IN      A

;; ANSWER SECTION:
example.com.            86400   IN      A       93.184.216.34
```

### **-4**

IPv4アドレスのみを使用します。

```console
$ host -4 example.com
example.com has address 93.184.216.34
```

### **-6**

IPv6アドレスのみを使用します。

```console
$ host -6 example.com
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
```

## 使用例

### 基本的なドメイン名の検索

```console
$ host example.com
example.com has address 93.184.216.34
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
example.com mail is handled by 0 .
```

### IPアドレスの逆引き

```console
$ host 93.184.216.34
34.216.184.93.in-addr.arpa domain name pointer example.com.
```

### MXレコード（メールサーバー）の検索

```console
$ host -t MX gmail.com
gmail.com mail is handled by 10 alt1.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 20 alt2.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 30 alt3.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 40 alt4.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 5 gmail-smtp-in.l.google.com.
```

### NSレコード（ネームサーバー）の検索

```console
$ host -t NS example.com
example.com name server a.iana-servers.net.
example.com name server b.iana-servers.net.
```

## ヒント:

### 特定のDNSサーバーを指定する

特定のDNSサーバーを使用して検索したい場合は、コマンドの最後にDNSサーバーのIPアドレスを指定できます。

```console
$ host example.com 8.8.8.8
Using domain server:
Name: 8.8.8.8
Address: 8.8.8.8#53
Aliases: 

example.com has address 93.184.216.34
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
```

### TTL（Time To Live）値の確認

`-v`（詳細表示）オプションを使用すると、DNSレコードのTTL値を確認できます。これはキャッシュの有効期間を示しています。

### 複数のドメインを一度に検索

複数のドメインを一度に検索する場合は、スペースで区切って指定できます。

```console
$ host google.com yahoo.com
google.com has address 142.250.207.110
google.com has IPv6 address 2404:6800:4004:80a::200e
google.com mail is handled by 10 smtp.google.com.
yahoo.com has address 74.6.231.20
yahoo.com has address 74.6.143.25
yahoo.com has IPv6 address 2001:4998:124:1507::f000
yahoo.com has IPv6 address 2001:4998:44:3507::8000
yahoo.com mail is handled by 1 mta7.am0.yahoodns.net.
yahoo.com mail is handled by 1 mta6.am0.yahoodns.net.
```

## よくある質問

#### Q1. `host`コマンドと`dig`コマンドの違いは何ですか？
A. `host`はシンプルで読みやすい出力を提供し、基本的なDNS検索に適しています。一方、`dig`はより詳細な情報を提供し、DNSのトラブルシューティングや高度な分析に向いています。

#### Q2. 特定のDNSサーバーを使って検索するにはどうすればいいですか？
A. コマンドの最後にDNSサーバーのIPアドレスを指定します。例：`host example.com 8.8.8.8`

#### Q3. すべてのDNSレコードタイプを一度に表示するにはどうすればいいですか？
A. `-a`オプションを使用します：`host -a example.com`

#### Q4. macOSでホスト名を変更するのに`host`コマンドは使えますか？
A. いいえ、`host`コマンドはDNS検索のみを行います。macOSでホスト名を変更するには、システム環境設定またはコマンドラインの`scutil`コマンドを使用します。

## macOSでの注意点

macOSでは、`host`コマンドはデフォルトでインストールされています。macOSの`host`コマンドはBIND（Berkeley Internet Name Domain）の実装に基づいており、Linuxのものとほぼ同じ動作をします。ただし、一部のオプションや出力形式に若干の違いがある場合があります。

## 参考資料

https://linux.die.net/man/1/host

## 改訂履歴

- 2025/04/30 初版作成