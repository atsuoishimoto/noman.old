# OpenSSL コマンド概要

OpenSSLは暗号化、SSL/TLS通信、証明書管理などのセキュリティ機能を提供するオープンソースのツールキットです。データの暗号化、ハッシュ生成、証明書の作成・管理などに使用されます。

## 主なオプション

- **s_client**: SSLサーバーに接続してテストを行います
  - 例: `openssl s_client -connect example.com:443`

- **s_server**: テスト用のSSLサーバーを起動します
  - 例: `openssl s_server -cert server.crt -key server.key -port 4433`

- **req**: 証明書署名要求(CSR)や自己署名証明書を作成します
  - 例: `openssl req -new -key private.key -out request.csr`

- **x509**: 証明書の管理や情報表示を行います
  - 例: `openssl x509 -in certificate.crt -text -noout`

- **genrsa**: RSA秘密鍵を生成します
  - 例: `openssl genrsa -out private.key 2048`

- **rsa**: RSA鍵の処理や変換を行います
  - 例: `openssl rsa -in private.key -pubout -out public.key`

- **enc**: ファイルやデータの暗号化・復号を行います
  - 例: `openssl enc -aes-256-cbc -in file.txt -out file.enc`

- **dgst**: メッセージダイジェスト（ハッシュ値）を計算します
  - 例: `openssl dgst -sha256 file.txt`

## 使用例

### SSL/TLS接続のテスト
```bash
# サーバーへのSSL接続をテスト
openssl s_client -connect example.com:443

# 出力例（一部）
CONNECTED(00000003)
depth=2 C = US, O = DigiCert Inc, OU = www.digicert.com, CN = DigiCert Global Root CA
verify return:1
...
```

### 証明書の情報表示
```bash
# 証明書の詳細情報を表示
openssl x509 -in certificate.crt -text -noout

# 出力例（一部）
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number: 12345678 (0xbc614e)
    Signature Algorithm: sha256WithRSAEncryption
    Issuer: C=US, O=Let's Encrypt, CN=Let's Encrypt Authority X3
...
```

### 秘密鍵と証明書署名要求(CSR)の作成
```bash
# 2048ビットのRSA秘密鍵を生成
openssl genrsa -out private.key 2048

# CSRを作成
openssl req -new -key private.key -out request.csr
# 対話式プロンプトが表示され、証明書情報を入力する
```

### ファイルの暗号化と復号
```bash
# ファイルをAES-256-CBCで暗号化
openssl enc -aes-256-cbc -salt -in secret.txt -out secret.enc

# 暗号化されたファイルを復号
openssl enc -d -aes-256-cbc -in secret.enc -out secret_decrypted.txt
```

### ハッシュ値の計算
```bash
# SHA-256ハッシュを計算
openssl dgst -sha256 file.txt

# 出力例
SHA256(file.txt)= e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

## 追加情報

- 証明書や鍵の形式変換（PEM、DER、PKCS#12など）も行えます。例えば：
  ```bash
  # PEM形式からDER形式への変換
  openssl x509 -in cert.pem -outform DER -out cert.der
  ```

- パスワード保護された鍵ファイルを作成する場合は `-passout` オプションを使用できます：
  ```bash
  openssl genrsa -des3 -out private.key 2048
  ```

- 自己署名証明書を一度に作成するには：
  ```bash
  openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365
  ```

- 最新のバージョンでは、より安全なアルゴリズム（例：Ed25519）もサポートしています。

- 実際の運用環境では、適切な鍵長や暗号化アルゴリズムの選択が重要です。セキュリティ要件に応じて適切なオプションを選択してください。