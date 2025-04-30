# openssl コマンド

暗号化、証明書管理、ハッシュ計算などの暗号操作を実行するためのツールです。

## 概要

OpenSSLは、SSL/TLS暗号化プロトコルの実装を提供するオープンソースのツールキットです。このコマンドを使用して、証明書の生成・管理、暗号化・復号化、ハッシュ値の計算、SSL/TLS接続のテストなど、さまざまな暗号操作を実行できます。

## オプション

OpenSSLは多くのサブコマンドを持つ複合コマンドです。主要なサブコマンドとその使い方を紹介します。

### **s_client**

サーバーへのSSL/TLS接続をテストするためのクライアントです。

```console
$ openssl s_client -connect example.com:443
CONNECTED(00000003)
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
...
---
Certificate chain
 0 s:CN = *.example.org
   i:C = US, O = Let's Encrypt, CN = R3
...
```

### **x509**

X.509証明書の表示、変換、署名などを行います。

```console
$ openssl x509 -in certificate.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            12:34:56:78:9a:bc:de:f0
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=US, O=Let's Encrypt, CN=R3
...
```

### **genrsa**

RSA秘密鍵を生成します。

```console
$ openssl genrsa -out private.key 2048
Generating RSA private key, 2048 bit long modulus
.....+++
.....+++
e is 65537 (0x10001)
```

### **req**

証明書署名要求(CSR)の作成や自己署名証明書の生成を行います。

```console
$ openssl req -new -key private.key -out request.csr
You are about to be asked to enter information that will be incorporated
into your certificate request.
...
Country Name (2 letter code) []:JP
State or Province Name []:Tokyo
...
```

### **dgst**

ファイルのハッシュ値（ダイジェスト）を計算します。

```console
$ openssl dgst -sha256 file.txt
SHA256(file.txt)= 8c17424f2e26d971060a5a82c5a1d7851e0c4bc8e0e347f223f95bb4a0d766af
```

## 使用例

### SSL証明書の情報を表示する

```console
$ openssl x509 -in certificate.crt -text -noout
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 12345678 (0xbc614e)
    # 証明書の詳細情報が表示される
```

### 自己署名証明書を生成する

```console
$ openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
Generating a 4096 bit RSA private key
...
writing new private key to 'key.pem'
Enter PEM pass phrase: ******
Verifying - Enter PEM pass phrase: ******
# 対話形式で証明書情報を入力
```

### リモートサーバーのSSL/TLS設定を確認する

```console
$ openssl s_client -connect example.com:443 -servername example.com
CONNECTED(00000003)
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
# 接続情報と証明書チェーンが表示される
```

### ファイルのSHA-256ハッシュを計算する

```console
$ openssl dgst -sha256 document.pdf
SHA256(document.pdf)= a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t0u1v2w3x4y5z6
```

## ヒント:

### 証明書情報の確認

証明書ファイルの内容を確認する際は、`-text -noout`オプションを使用すると読みやすい形式で表示されます。

```console
$ openssl x509 -in cert.pem -text -noout
```

### パスワード入力の自動化

スクリプト内でOpenSSLを使用する場合、`-passin`オプションでパスワードを指定できます。ただし、セキュリティ上の理由から本番環境では注意が必要です。

```console
$ openssl rsa -in encrypted.key -out decrypted.key -passin pass:mypassword
```

### 証明書チェーンの検証

証明書チェーンを検証するには、`verify`コマンドを使用します。

```console
$ openssl verify -CAfile ca-bundle.crt certificate.crt
```

## よくある質問

#### Q1. OpenSSLで自己署名証明書を作成するにはどうすればよいですか？
A. `openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365`コマンドを使用します。これにより、2048ビットのRSA鍵と365日間有効な自己署名証明書が生成されます。

#### Q2. リモートサーバーのSSL/TLS設定を確認するにはどうすればよいですか？
A. `openssl s_client -connect example.com:443`コマンドを使用します。これにより、サーバーの証明書情報やSSL/TLS設定が表示されます。

#### Q3. 証明書の有効期限を確認するにはどうすればよいですか？
A. `openssl x509 -in certificate.crt -noout -dates`コマンドを使用します。これにより、証明書の開始日と終了日が表示されます。

#### Q4. 暗号化されたRSA秘密鍵のパスワードを削除するにはどうすればよいですか？
A. `openssl rsa -in encrypted.key -out decrypted.key`コマンドを使用します。パスワードを入力すると、パスワードなしの秘密鍵が生成されます。

## macOSでの注意点

macOSに搭載されているOpenSSLは、LibreSSLという別の実装に置き換えられている場合があります。一部のコマンドやオプションが標準のOpenSSLと異なる可能性があるため、最新のOpenSSLが必要な場合はHomebrewなどでインストールすることをお勧めします。

```console
$ brew install openssl
```

インストール後は、`/usr/local/opt/openssl/bin/openssl`または`/opt/homebrew/bin/openssl`にインストールされます。

## 参考資料

https://www.openssl.org/docs/

## 改訂履歴

- 2025/04/30 初版作成