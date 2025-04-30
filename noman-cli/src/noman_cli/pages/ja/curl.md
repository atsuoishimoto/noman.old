# curl コマンド

URLで指定されたリソースをダウンロードまたは操作するためのコマンドラインツール。

## 概要

`curl`はURLを使用してデータを転送するためのコマンドラインツールです。HTTP、HTTPS、FTP、FTPS、SFTPなど多くのプロトコルをサポートしています。Webページの取得、APIとの対話、ファイルのダウンロード、フォームデータの送信など、ネットワーク操作に広く使用されています。

## オプション

### **-o, --output \<file\>**

指定したファイルに出力を保存します。

```console
$ curl -o example.html https://example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0  12560      0 --:--:-- --:--:-- --:--:-- 12686
```

### **-O, --remote-name**

リモートファイルと同じ名前でローカルに保存します。

```console
$ curl -O https://example.com/sample.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.2M  100 10.2M    0     0  5.1MB/s      0 --:--:-- 0:00:02 --:--:-- 5.1MB/s
```

### **-s, --silent**

進行状況やエラーメッセージを表示せず、静かに実行します。

```console
$ curl -s https://example.com > /dev/null
```

### **-I, --head**

HTTPヘッダーのみを取得します（ボディは取得しません）。

```console
$ curl -I https://example.com
HTTP/2 200 
content-type: text/html; charset=UTF-8
date: Tue, 30 Apr 2025 12:34:56 GMT
expires: Tue, 07 May 2025 12:34:56 GMT
cache-control: public, max-age=604800
server: ECS (dcb/7F84)
content-length: 1256
```

### **-X, --request \<command\>**

使用するHTTPメソッドを指定します（GET、POST、PUT、DELETEなど）。

```console
$ curl -X POST https://api.example.com/data
```

### **-H, --header \<header\>**

HTTPリクエストに追加のヘッダーを設定します。

```console
$ curl -H "Content-Type: application/json" -H "Authorization: Bearer token123" https://api.example.com
```

### **-d, --data \<data\>**

HTTPリクエストにデータを送信します（POSTリクエストなど）。

```console
$ curl -X POST -d "name=John&age=30" https://api.example.com/users
```

## 使用例

### JSONデータをPOSTする

```console
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"John","age":30}' https://api.example.com/users
{"id": 123, "status": "created"}
```

### ファイルをダウンロードして進行状況を表示

```console
$ curl -# -O https://example.com/largefile.zip
######################################################################## 100.0%
```

### 複数のファイルを一度にダウンロード

```console
$ curl -O https://example.com/file1.txt -O https://example.com/file2.txt
```

### リダイレクトに従う

```console
$ curl -L https://short-url.example
```

## ヒント:

### 証明書の検証をスキップ

開発環境やテスト時に自己署名証明書を使用する場合は、`-k`または`--insecure`オプションを使用できますが、本番環境では使用しないでください。

```console
$ curl -k https://localhost:8443
```

### ユーザーエージェントの設定

一部のウェブサイトはユーザーエージェントをチェックするため、ブラウザのように振る舞いたい場合は`-A`オプションを使用します。

```console
$ curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" https://example.com
```

### クッキーの使用

クッキーを保存して再利用するには、`-b`と`-c`オプションを使用します。

```console
$ curl -c cookies.txt https://example.com/login -d "user=name&password=secret"
$ curl -b cookies.txt https://example.com/protected-area
```

## よくある質問

#### Q1. curlとwgetの違いは何ですか？
A. curlはより多くのプロトコルをサポートし、より多くのオプションを提供しますが、wgetは再帰的なダウンロードに優れています。curlはスクリプトでの使用に適しており、wgetはシンプルなダウンロードタスクに適しています。

#### Q2. curlでHTTPSサイトにアクセスする際に証明書エラーが発生する場合はどうすればよいですか？
A. 開発環境では`-k`オプションを使用して証明書検証をスキップできますが、本番環境では適切な証明書を設定するか、`--cacert`オプションで信頼できる証明書を指定してください。

#### Q3. curlでPOSTリクエストを送信する方法は？
A. `-X POST`でメソッドを指定し、`-d`オプションでデータを送信します。JSONデータを送信する場合は、`-H "Content-Type: application/json"`ヘッダーも追加してください。

#### Q4. curlでファイルをアップロードするには？
A. `-F "file=@ファイルパス"`オプションを使用します。例：`curl -F "file=@document.pdf" https://example.com/upload`

## macOSでの注意点

macOSのcurlはOpenSSLではなくSecure Transport（macOSのネイティブTLSライブラリ）を使用していることがあります。これにより、一部のSSL/TLS機能が異なる動作をする場合があります。最新のTLSプロトコルを使用するには、Homebrewなどでcurlを再インストールすることを検討してください。

```console
$ brew install curl
```

## 参考資料

https://curl.se/docs/

## 改訂履歴

- 2025/04/30 初版作成