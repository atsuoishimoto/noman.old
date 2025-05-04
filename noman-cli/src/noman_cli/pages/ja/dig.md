# dig コマンド

DNSネームサーバーにドメイン情報を問い合わせます。

## 概要

`dig`（Domain Information Groper）は柔軟なDNS検索ユーティリティで、ドメイン名、IPアドレス、メール交換、その他のDNSレコードに関する情報をDNSサーバーに問い合わせることができます。DNS問題のトラブルシューティング、DNS設定の確認、DNS変更のテストによく使用されます。

## オプション

### **-t, --type=TYPE**

問い合わせるDNSレコードの種類を指定します（例：A, MX, NS, ANY）

```console
$ dig -t MX google.com
;; ANSWER SECTION:
google.com.		300	IN	MX	10 smtp.google.com.
# MXレコード（メールサーバー情報）を表示している
```

### **-x, --reverse**

逆引きDNS検索を実行します（IPアドレスからホスト名への変換）

```console
$ dig -x 8.8.8.8
;; ANSWER SECTION:
8.8.8.8.in-addr.arpa.	7200	IN	PTR	dns.google.
# 8.8.8.8のIPアドレスに対応するホスト名を表示している
```

### **@server**

デフォルトの代わりに特定のDNSサーバーに問い合わせます

```console
$ dig @1.1.1.1 example.com
;; ANSWER SECTION:
example.com.		86400	IN	A	93.184.216.34
# Cloudflareの1.1.1.1 DNSサーバーを使用して問い合わせている
```

### **+short**

簡潔な回答を表示します（ヘッダーや追加情報なしで結果のみ）

```console
$ dig +short google.com
142.250.190.78
# 結果のIPアドレスのみを表示している
```

### **+noall, +answer**

応答のどのセクションを表示するかを制御します

```console
$ dig +noall +answer google.com
google.com.		300	IN	A	142.250.190.78
# 回答セクションのみを表示している
```

## 使用例

### 基本的なドメイン検索

```console
$ dig example.com
;; QUESTION SECTION:
;example.com.			IN	A

;; ANSWER SECTION:
example.com.		86400	IN	A	93.184.216.34
# example.comのAレコード（IPアドレス）を問い合わせている
```

### 複数のレコードタイプの検索

```console
$ dig example.com ANY
;; ANSWER SECTION:
example.com.		86400	IN	A	93.184.216.34
example.com.		86400	IN	NS	a.iana-servers.net.
example.com.		86400	IN	NS	b.iana-servers.net.
example.com.		86400	IN	SOA	ns.icann.org. noc.dns.icann.org. 2023080794 7200 3600 1209600 3600
# example.comの全タイプのレコードを表示している
```

### DNS解決パスのトレース

```console
$ dig +trace example.com
;; Received 13 bytes from 192.168.1.1#53 in 10 ms

. 			518400	IN	NS	a.root-servers.net.
...
;; Received 811 bytes from 192.5.6.30#53 in 40 ms

com. 			172800	IN	NS	a.gtld-servers.net.
...
;; Received 1173 bytes from 192.41.162.30#53 in 160 ms

example.com.		86400	IN	NS	a.iana-servers.net.
...
;; Received 97 bytes from 199.43.135.53#53 in 100 ms

example.com.		86400	IN	A	93.184.216.34
# ルートサーバーからの完全な解決パスを表示している
```

## ヒント:

### +nocommentsでより見やすい出力を得る

`+nocomments`オプションを使用すると、出力からコメント行が削除され、必要な情報だけを見たい場合に読みやすくなります。

### DNS伝播の確認

DNS変更を行った場合、`dig @server domain.com`を異なるDNSサーバーで使用して、変更が伝播しているかを確認できます。

### 1つのコマンドで複数のクエリを指定

複数のドメインやレコードタイプを1つのコマンドで問い合わせることができます：`dig example.com mx google.com a`

### +statsでパフォーマンス分析

`+stats`オプションを使用すると、クエリにかかった時間などのクエリ統計が表示され、DNS解決の遅延を診断するのに役立ちます。

## よくある質問

#### Q1. `dig`と`nslookup`の違いは何ですか？
A. `dig`はより詳細な情報を提供し、DNS問い合わせのためのオプションが多くあります。その包括的な出力と柔軟性から、一般的にネットワーク管理者に好まれています。

#### Q2. DNS変更が伝播したかどうかを確認するにはどうすればよいですか？
A. `dig @different-dns-servers your-domain.com`を使用して複数のDNSサーバーに問い合わせ、結果を比較します。

#### Q3. ドメインの権威ネームサーバーを見つけるにはどうすればよいですか？
A. `dig NS domain.com`を使用して、ドメインを担当するネームサーバーを見つけることができます。

#### Q4. DNSレコードのTTL（Time To Live）を確認するにはどうすればよいですか？
A. TTLは`dig`の標準出力に表示されます。回答セクションの最初のINの前にある数字（秒単位）です。

## 参考資料

https://linux.die.net/man/1/dig

## 改訂履歴

- 2025/05/04 初版作成