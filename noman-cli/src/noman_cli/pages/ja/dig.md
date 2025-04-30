# dig コマンド

DNSサーバーに対してクエリを実行し、ドメイン名の情報を取得します。

## 概要

`dig`（Domain Information Groper）は、DNSサーバーに対してクエリを送信し、ドメイン名の解決情報を取得するためのコマンドラインツールです。ネットワーク管理者やシステム管理者がDNSの問題をトラブルシューティングする際に非常に役立ちます。IPアドレス、メールサーバー、ネームサーバーなどの情報を確認できます。

## オプション

### **+short**

結果を簡潔に表示します。IPアドレスのみなど、最小限の情報を取得したい場合に便利です。

```console
$ dig google.com +short
142.250.207.110
```

### **-t**

特定のレコードタイプを指定します。一般的なタイプには、A（IPv4アドレス）、AAAA（IPv6アドレス）、MX（メールサーバー）、NS（ネームサーバー）、TXT（テキスト情報）などがあります。

```console
$ dig -t MX gmail.com
;; ANSWER SECTION:
gmail.com.		3599	IN	MX	10 alt1.gmail-smtp-in.l.google.com.
gmail.com.		3599	IN	MX	20 alt2.gmail-smtp-in.l.google.com.
gmail.com.		3599	IN	MX	30 alt3.gmail-smtp-in.l.google.com.
gmail.com.		3599	IN	MX	40 alt4.gmail-smtp-in.l.google.com.
gmail.com.		3599	IN	MX	5 gmail-smtp-in.l.google.com.
```

### **@**

特定のDNSサーバーを指定してクエリを実行します。デフォルトでは、システムの設定に従ってDNSサーバーが選択されます。

```console
$ dig @8.8.8.8 example.com
;; ANSWER SECTION:
example.com.		86400	IN	A	93.184.216.34
```

### **+trace**

DNSの委任チェーン全体をたどり、ルートサーバーから始まる解決プロセスを表示します。

```console
$ dig +trace example.com
;; Received 525 bytes from 192.168.1.1#53(192.168.1.1) in 30 ms

example.com.		172800	IN	NS	a.iana-servers.net.
example.com.		172800	IN	NS	b.iana-servers.net.
;; Received 170 bytes from 192.36.148.17#53(i.root-servers.net) in 40 ms
...
```

## 使用例

### 基本的なDNS検索

```console
$ dig example.com
;; ANSWER SECTION:
example.com.		86400	IN	A	93.184.216.34
```

### 複数のドメインを一度に検索

```console
$ dig google.com amazon.com
;; ANSWER SECTION:
google.com.		300	IN	A	142.250.207.110

;; ANSWER SECTION:
amazon.com.		60	IN	A	52.94.236.248
amazon.com.		60	IN	A	54.239.28.85
```

### 逆引きDNS検索

```console
$ dig -x 8.8.8.8
;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.	21599	IN	PTR	dns.google.
```

## ヒント:

### 応答時間の確認

`dig`の出力の最後に表示される「Query time」を確認することで、DNSクエリの応答時間を確認できます。これはネットワークやDNSサーバーのパフォーマンスを評価するのに役立ちます。

### 統計情報の非表示

`+nostats`オプションを使用すると、統計情報を非表示にできます。これにより、出力が簡潔になります。

```console
$ dig google.com +nostats
```

### 特定のセクションのみ表示

`+noall +answer`オプションを使用すると、回答セクションのみを表示できます。これは、必要な情報だけを素早く確認したい場合に便利です。

```console
$ dig google.com +noall +answer
google.com.		300	IN	A	142.250.207.110
```

## よくある質問

#### Q1. digとnslookupの違いは何ですか？
A. `dig`はより詳細な情報を提供し、スクリプトでの使用に適しています。一方、`nslookup`はよりシンプルで対話的な使用に向いています。`dig`は一般的に、より多くのDNS関連の情報を表示します。

#### Q2. 特定のDNSサーバーを使用するにはどうすればよいですか？
A. `@`記号の後にDNSサーバーのIPアドレスを指定します。例：`dig @8.8.8.8 example.com`

#### Q3. TTL（Time To Live）とは何ですか？
A. TTLは、DNSレコードがキャッシュに保存される秒数を示します。この値が小さいほど、DNSの変更が反映されるのが早くなりますが、DNSサーバーへのクエリ数が増加します。

#### Q4. SOAレコードとは何ですか？
A. SOA（Start of Authority）レコードは、ゾーンの管理情報を含むDNSレコードです。ゾーンの権威あるネームサーバー、管理者のメールアドレス、シリアル番号、更新間隔などの情報が含まれています。

## 参考資料

https://linux.die.net/man/1/dig

## Revisions

- 2025/04/30 First revision