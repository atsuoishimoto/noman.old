# curl コマンド

URLを使用してサーバーとの間でデータを転送するツールで、HTTP、HTTPS、FTP、SFTPなど多数のプロトコルをサポートします。

## 概要

`curl`はURLを使ってデータを転送するためのコマンドラインツールです。HTTP、HTTPS、FTP、FTPS、SCP、SFTP、LDAPなど、多くのプロトコルをサポートしています。ファイルのダウンロード、APIのテスト、HTTPリクエストの送信、ネットワーク問題のデバッグなどによく使用されます。`curl`は非対話式で、ユーザーの介入なしに動作するように設計されているため、スクリプトや自動化に最適です。

## オプション

### **-o, --output \<file>**

出力を画面に表示せずにファイルに保存します

```console
$ curl -o example.html https://example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0   9664      0 --:--:-- --:--:-- --:--:--  9663
```

### **-O, --remote-name**

URLからリモートファイル名を使用して出力を保存します

```console
$ curl -O https://example.com/sample.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.2M  100 10.2M    0     0  5.1MB/s      0 --:--:-- 0:00:02 --:--:-- 5.1MB
```

### **-L, --location**

HTTPリダイレクト（3XXレスポンス）に従います

```console
$ curl -L http://github.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   142  100   142    0     0    573      0 --:--:-- --:--:-- --:--:--   573
100  5891    0  5891    0     0  13090      0 --:--:-- --:--:-- --:--:-- 13090
```

### **-s, --silent**

サイレントモード；進行状況メーターやエラーメッセージを表示しません

```console
$ curl -s https://example.com > example.html
```

### **-I, --head**

HTTPヘッダーのみを取得します（HEADリクエスト）

```console
$ curl -I https://example.com
HTTP/2 200 
content-type: text/html; charset=UTF-8
date: Tue, 04 May 2025 12:00:00 GMT
expires: Tue, 11 May 2025 12:00:00 GMT
cache-control: public, max-age=604800
server: ECS (dcb/7F84)
content-length: 1256
```

### **-X, --request \<command>**

使用するHTTPリクエストメソッドを指定します（GET、POST、PUT、DELETEなど）

```console
$ curl -X POST https://api.example.com/data
```

### **-H, --header \<header>**

リクエストにカスタムヘッダーを追加します

```console
$ curl -H "Content-Type: application/json" https://api.example.com
```

### **-d, --data \<data>**

リクエストボディにデータを送信します（通常POSTで使用）

```console
$ curl -X POST -d "name=John&age=30" https://api.example.com/users
```

### **-A, --user-agent \<agent string>**

サーバーに送信するUser-Agent文字列を指定します

```console
$ curl -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" https://example.com
```

## 使用例

### ファイルをダウンロードして特定の名前で保存する

```console
$ curl -o linux-distro.iso https://example.com/downloads/linux.iso
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1500M  100 1500M    0     0  10.2M/s      0  0:02:27  0:02:27 --:--:-- 10.5M
```

### JSONデータを使用したPOSTリクエストの作成

```console
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"John","age":30}' https://api.example.com/users
{"id": 123, "status": "created"}
```

### 認証を使用した複数ファイルのダウンロード

```console
$ curl -u username:password -O https://example.com/file1.txt -O https://example.com/file2.txt
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0  12560      0 --:--:-- --:--:-- --:--:-- 12560
100  2048  100  2048    0     0  20480      0 --:--:-- --:--:-- --:--:-- 20480
```

### ファイルのアップロード

```console
$ curl -F "file=@localfile.jpg" https://example.com/upload
{"status": "success", "url": "https://example.com/uploads/image123.jpg"}
```

## ヒント:

### デバッグ用の詳細モードを使用する

トラブルシューティングの際は、`-v`（詳細）または`-vv`（非常に詳細）を使用して、リクエストとレスポンスに関する詳細情報を確認できます：

```console
$ curl -v https://example.com
```

### Cookieを保存して後で使用する

Cookieが必要なセッションを処理するには：

```console
$ curl -c cookies.txt https://example.com/login -d "user=name&password=secret"
$ curl -b cookies.txt https://example.com/protected-area
```

### ダウンロード速度を制限する

利用可能な帯域幅をすべて消費しないようにするには：

```console
$ curl --limit-rate 1M -O https://example.com/large-file.zip
```

### 中断されたダウンロードを再開する

ダウンロードが中断された場合、再開できます：

```console
$ curl -C - -O https://example.com/large-file.zip
```

### APIエンドポイントを素早くテストする

素早いAPIテストのために、`jq`などのツールと組み合わせてJSONレスポンスをフォーマットできます：

```console
$ curl -s https://api.example.com/users | jq
```

## よくある質問

#### Q1. curlでファイルをダウンロードするにはどうすればよいですか？
A. 元のファイル名で保存するには`curl -O URL`を使用し、異なるファイル名を指定するには`curl -o ファイル名 URL`を使用します。

#### Q2. curlでPOSTリクエストを作成するにはどうすればよいですか？
A. フォームデータの場合は`curl -X POST -d "key=value" URL`を、JSONデータの場合は`curl -X POST -H "Content-Type: application/json" -d '{"key":"value"}' URL`を使用します。

#### Q3. curlでリダイレクトに従うにはどうすればよいですか？
A. HTTPリダイレクトに従うには、`-L`または`--location`オプションを使用します。

#### Q4. レスポンスのHTTPヘッダーを確認するにはどうすればよいですか？
A. ヘッダーのみを表示するには`curl -I URL`を、ヘッダーと本文の両方を表示するには`curl -v URL`を使用します。

#### Q5. curlで認証するにはどうすればよいですか？
A. 基本認証には`curl -u ユーザー名:パスワード URL`を使用します。OAuthやトークンベースの認証には`curl -H "Authorization: Bearer あなたのトークン" URL`を使用します。

## macOSに関する考慮事項

macOSでは、デフォルトの`curl`はLinuxディストリビューションよりも古いバージョンであることが一般的です。新しい機能の一部が利用できない場合があります。また、macOSの`curl`はOpenSSLではなくSecure Transport（AppleのSSL/TLS実装）でビルドされているため、特にSSL証明書に関して、動作に微妙な違いが生じることがあります。

すべての機能を備えた最新バージョンが必要な場合は、Homebrewを通じて`curl`をインストールすることを検討してください：

```console
$ brew install curl
```

インストール後、システムバージョンではなくHomebrewバージョンを使用するために、`/usr/local/opt/curl/bin/curl`を使用するか、PATHに追加する必要があるかもしれません。

## 参考資料

https://curl.se/docs/manpage.html

## 改訂履歴

- 2025/05/04 初版作成