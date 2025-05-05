# openssl コマンド

暗号化通信、証明書管理、および様々な暗号操作のための暗号機能を提供します。

## 概要

OpenSSLは、Secure Sockets Layer (SSL)およびTransport Layer Security (TLS)プロトコルを実装する強力なツールキットで、汎用の高強度暗号化ライブラリも備えています。コマンドラインから証明書の作成、鍵の管理、ファイルの暗号化/復号化、メッセージダイジェストの生成など、多くの暗号操作を実行できます。

## オプション

OpenSSLはコマンドベースの構造を使用しており、メインコマンドの後にサブコマンドとそのオプションが続きます。

### **s_client** - SSL/TLSクライアント

SSL/TLSを使用してリモートホストに接続する汎用SSL/TLSクライアントを実装します。

```console
$ openssl s_client -connect example.com:443
CONNECTED(00000003)
depth=2 C = US, O = Internet Security Research Group, CN = ISRG Root X1
verify return:1
depth=1 C = US, O = Let's Encrypt, CN = R3
verify return:1
depth=0 CN = example.com
verify return:1
---
Certificate chain
 0 s:CN = example.com
   i:C = US, O = Let's Encrypt, CN = R3
...
```

### **x509** - 証明書表示と署名ユーティリティ

証明書情報の表示、様々な形式への証明書の変換、証明書リクエストの署名を行います。

```console
$ openssl x509 -in certificate.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            04:e5:7b:d2:1d:d5:e5:2c:...
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, O=Let's Encrypt, CN=R3
...
```

### **genrsa** - RSA秘密鍵の生成

RSA秘密鍵を生成します。

```console
$ openssl genrsa -out private.key 2048
Generating RSA private key, 2048 bit long modulus (2 primes)
.....+++++
.....+++++
e is 65537 (0x010001)
```

### **req** - PKCS#10証明書リクエストと証明書生成ユーティリティ

PKCS#10形式の証明書リクエストを作成および処理します。

```console
$ openssl req -new -key private.key -out certificate.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:US
State or Province Name (full name) [Some-State]:California
...
```

### **enc** - 暗号を使用したエンコーディング

様々な暗号アルゴリズムを使用して暗号化または復号化します。

```console
$ openssl enc -aes-256-cbc -salt -in plaintext.txt -out encrypted.txt
enter aes-256-cbc encryption password:
Verifying - enter aes-256-cbc encryption password:
```

## 使用例

### リモートSSL/TLSサーバーの確認

```console
$ openssl s_client -connect example.com:443 -servername example.com
CONNECTED(00000003)
depth=2 C = US, O = Internet Security Research Group, CN = ISRG Root X1
verify return:1
...
```

### 自己署名証明書の作成

```console
$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
Generating a RSA private key
.....++++
.....++++
writing new private key to 'key.pem'
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
...
```

### 証明書チェーンの検証

```console
$ openssl verify -CAfile ca-bundle.crt certificate.crt
certificate.crt: OK
```

### ランダムパスワードの生成

```console
$ openssl rand -base64 12
Ew6Y9RzYxAQeFA==
```

## ヒント:

### 適切な鍵のパーミッションを設定する

秘密鍵には常に制限的なパーミッションを設定して、不正アクセスを防止しましょう：

```console
$ chmod 600 private.key
```

### 証明書の有効期限を確認する

予期しないサービス中断を避けるため、証明書の有効期限を確認しましょう：

```console
$ openssl x509 -enddate -noout -in certificate.crt
notAfter=May 15 12:00:00 2026 GMT
```

### 証明書フォーマットの変換

OpenSSLは異なる証明書フォーマット（PEM、DER、PKCS#12）間の変換ができます：

```console
$ openssl x509 -in cert.pem -inform PEM -out cert.der -outform DER
```

### 自動化には -passin と -passout を使用する

スクリプト作成時には、これらのオプションを使用して非対話的にパスワードを提供できます：

```console
$ openssl rsa -in encrypted.key -out decrypted.key -passin file:password.txt
```

## よくある質問

#### Q1. CSR（証明書署名リクエスト）はどのように作成しますか？
A. `openssl req -new -key private.key -out request.csr` を使用します。証明書情報の入力を求められます。

#### Q2. 証明書の内容を確認するにはどうすればよいですか？
A. `openssl x509 -in certificate.crt -text -noout` を使用して証明書の詳細を表示します。

#### Q3. 証明書をPEM形式からPKCS#12形式に変換するにはどうすればよいですか？
A. `openssl pkcs12 -export -out certificate.pfx -inkey private.key -in certificate.crt -certfile ca-chain.crt` を使用します。

#### Q4. ウェブサイトへのセキュア接続をテストするにはどうすればよいですか？
A. `openssl s_client -connect example.com:443 -servername example.com` を使用して接続を確立し、証明書の詳細を表示します。

#### Q5. 強力なランダムパスワードを生成するにはどうすればよいですか？
A. `openssl rand -base64 16` を使用して、base64でエンコードされた16バイトのランダム文字列を生成します。

## 参考資料

https://www.openssl.org/docs/man1.1.1/man1/

## 改訂履歴

- 2025/05/04 初回改訂