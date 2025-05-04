# host コマンド

ドメインネームサーバーに対してDNS検索を行うユーティリティです。

## 概要

`host`コマンドはDNS検索を実行するためのシンプルなユーティリティです。ドメイン名をIPアドレスに変換したり、その逆を行ったり、DNSレコードを照会したりするために使用されます。`dig`や`nslookup`よりもシンプルで、素早いDNS検索に適しています。

## オプション

### **-a, --all**

利用可能なすべての情報を表示します（-v -t ANYと同等）

```console
$ host -a example.com
Trying "example.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;example.com.                   IN      ANY

;; ANSWER SECTION:
example.com.            86400   IN      A       93.184.216.34
example.com.            86400   IN      AAAA    2606:2800:220:1:248:1893:25c8:1946
example.com.            86400   IN      NS      a.iana-servers.net.
example.com.            86400   IN      NS      b.iana-servers.net.
example.com.            86400   IN      SOA     ns.icann.org. noc.dns.icann.org. 2023050101 7200 3600 1209600 3600
```

### **-t, --type=TYPE**

クエリタイプを指定します（例：A, MX, NSなど）

```console
$ host -t MX gmail.com
gmail.com mail is handled by 10 alt1.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 20 alt2.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 30 alt3.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 40 alt4.gmail-smtp-in.l.google.com.
gmail.com mail is handled by 5 gmail-smtp-in.l.google.com.
```

### **-v, --verbose**

より詳細な情報を含む詳細出力を有効にします

```console
$ host -v example.com
Trying "example.com"
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 12345
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 0

;; QUESTION SECTION:
;example.com.                   IN      A

;; ANSWER SECTION:
example.com.            86400   IN      A       93.184.216.34

Received 56 bytes from 8.8.8.8#53 in 28 ms
```

### **-4, -6**

IPv4（-4）またはIPv6（-6）トランスポートのみを使用します

```console
$ host -4 example.com
example.com has address 93.184.216.34

$ host -6 example.com
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
```

### **-C, --checking**

DNSサーバーの応答の一貫性をチェックします

```console
$ host -C example.com
Host example.com is consistent
```

## 使用例

### 基本的なドメイン検索

```console
$ host example.com
example.com has address 93.184.216.34
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
example.com mail is handled by 0 .
```

### 逆引きDNS検索

```console
$ host 93.184.216.34
34.216.184.93.in-addr.arpa domain name pointer example.com.
```

### 特定のDNSサーバーに対する照会

```console
$ host example.com 8.8.8.8
Using domain server:
Name: 8.8.8.8
Address: 8.8.8.8#53
Aliases: 

example.com has address 93.184.216.34
example.com has IPv6 address 2606:2800:220:1:248:1893:25c8:1946
```

### ネームサーバーの検索

```console
$ host -t NS google.com
google.com name server ns1.google.com.
google.com name server ns2.google.com.
google.com name server ns3.google.com.
google.com name server ns4.google.com.
```

## ヒント:

### 簡易フォーマットを使用した素早い検索

素早い検索には、オプションなしで `host domain.com` を使用しましょう。これにより、最も重要な情報が簡潔な形式で表示されます。

### トラブルシューティングのためのDNSサーバー指定

DNS問題のトラブルシューティングを行う場合は、別のDNSサーバー（GoogleのDNSサーバー 8.8.8.8など）を指定して、デフォルトのDNSサーバーに問題があるかどうかを確認できます。

### grepと組み合わせたフィルタリング

`host`を`grep`と組み合わせて特定の情報をフィルタリングできます。例えば、`host -t ANY example.com | grep MX`とすると、メール交換レコードのみを表示できます。

### 完全なレコードには-t ANYを使用

ドメインのすべてのDNSレコードを確認する必要がある場合は、異なるレコードタイプに対して複数のクエリを実行するのではなく、`host -t ANY domain.com`を使用しましょう。

## よくある質問

#### Q1. `host`、`dig`、`nslookup`の違いは何ですか？
A. `host`は`dig`よりもシンプルでユーザーフレンドリーです。`dig`はより詳細な出力を提供します。`nslookup`は古い対話型ツールです。素早い検索には`host`が好まれることが多く、詳細なDNSトラブルシューティングには`dig`が適しています。

#### Q2. ドメインが適切なメールサーバー設定を持っているかどうかを確認するにはどうすればよいですか？
A. `host -t MX domain.com`を使用してメール交換レコードを確認します。

#### Q3. DNSの伝播を確認するために`host`を使用できますか？
A. はい、異なるDNSサーバーで`host domain.com dns-server-ip`を使用して、DNS変更が伝播しているかどうかを確認できます。

#### Q4. ドメインのすべてのDNSレコードを検索するにはどうすればよいですか？
A. `host -a domain.com`または`host -t ANY domain.com`を使用して、利用可能なすべてのDNSレコードを確認できます。

## 参考資料

https://linux.die.net/man/1/host

## 改訂履歴

- 2025/05/04 初回改訂