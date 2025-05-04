# http コマンド

コマンドラインからHTTPリクエストを送信し、レスポンスを表示します。

## 概要

`http`コマンドはHTTPieの一部で、Webサービスとのコマンドライン操作をより人間に優しくするように設計された使いやすいHTTPクライアントです。様々なメソッド（GET、POST、PUTなど）でHTTPリクエストを送信するためのシンプルなインターフェースを提供し、読みやすさを向上させるためにカラー表示された出力を表示します。

## オプション

### **-j, --json**

リクエストボディにJSONデータを送信します。

```console
$ http -j POST example.com name=John age:=30
```

### **-f, --form**

リクエストボディにフォームエンコードされたデータを送信します。

```console
$ http -f POST example.com name=John age=30
```

### **-a, --auth**

認証情報を指定します。

```console
$ http -a username:password example.com
```

### **-h, --headers**

レスポンスヘッダーのみを表示します。

```console
$ http -h example.com
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Date: Sat, 04 May 2025 12:00:00 GMT
Server: nginx
Content-Length: 1256
```

### **-v, --verbose**

HTTPの通信全体（リクエストとレスポンス）を表示します。

```console
$ http -v example.com
GET / HTTP/1.1
Host: example.com
User-Agent: HTTPie/3.2.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive

HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Date: Sat, 04 May 2025 12:00:00 GMT
Server: nginx
Content-Length: 1256

<!doctype html>
<html>
...
```

### **--verify**

SSL検証を制御します。`no`に設定すると検証を無効にできます。

```console
$ http --verify=no https://example.com
```

### **--session**

複数のリクエストでセッションを作成または再利用します。

```console
$ http --session=mysession -a username:password example.com
$ http --session=mysession example.com/api/resource
```

## 使用例

### 基本的なGETリクエスト

```console
$ http example.com
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Date: Sat, 04 May 2025 12:00:00 GMT
Server: nginx
Content-Length: 1256

<!doctype html>
<html>
...
```

### JSONデータを使用したPOST

```console
$ http POST api.example.com/users name=John age:=30 is_active:=true
HTTP/1.1 201 Created
Content-Type: application/json
Location: /users/123
Content-Length: 42

{
    "id": 123,
    "name": "John",
    "age": 30,
    "is_active": true
}
```

### ファイルのダウンロード

```console
$ http --download https://example.com/file.zip
Downloading to "file.zip"
Done. 15.43 MB in 2.32s (6.65 MB/s)
```

### カスタムヘッダー

```console
$ http example.com X-API-Token:abc123 User-Agent:MyApp/1.0
```

## ヒント:

### 一般的なHTTPメソッドのショートカットを使用する

HTTPieは一般的なHTTPメソッドのショートカットを提供しているため、`http GET example.com`の代わりに`http example.com`を使用できます。

### JSONデータの構文

JSONデータを送信する場合、数値とブール値には`:=`を、文字列には`=`を使用します：
- `name=John`は`{"name": "John"}`になる
- `age:=30`は`{"age": 30}`になる
- `active:=true`は`{"active": true}`になる

### 出力を他のツールにパイプする

出力を`jq`などのツールにパイプしてJSON処理を行うことができます：
```console
$ http api.example.com/users | jq '.[] | select(.active==true)'
```

### 出力リダイレクションを使用する

標準出力リダイレクションを使用してレスポンスボディをファイルに保存できます：
```console
$ http example.com/image.jpg > image.jpg
```

## よくある質問

#### Q1. フォームデータを使ってPOSTリクエストを送信するにはどうすればよいですか？
A. `http -f POST example.com name=value`を使用して、フォームエンコードされたデータを送信します。

#### Q2. リクエストに認証情報を含めるにはどうすればよいですか？
A. `-a`または`--auth`オプションを使用します：`http -a username:password example.com`

#### Q3. HTTP通信の全体を確認するにはどうすればよいですか？
A. `-v`または`--verbose`オプションを使用して、リクエストとレスポンスの両方の詳細を確認できます。

#### Q4. リクエストにファイルを送信するにはどうすればよいですか？
A. `@filename`を使用してファイルの内容を含めます：`http POST example.com file@/path/to/file.txt`

#### Q5. リクエストにクッキーを設定するにはどうすればよいですか？
A. `--session`オプションを使用してリクエスト間でクッキーを維持するか、手動でCookieヘッダーを設定します。

## 参考資料

https://httpie.io/docs/cli

## 改訂履歴

- 2025/05/04 初版作成