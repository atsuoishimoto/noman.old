# http command

HTTP リクエストを送信し、レスポンスを表示するコマンドラインツールです。

## 概要

`http` コマンドは HTTPie というツールの一部で、コマンドラインから HTTP リクエストを簡単に作成、送信し、レスポンスを見やすく表示します。cURL よりも使いやすく設計されており、JSONデータの送信、ヘッダーの設定、認証など、Web APIとの対話に便利な機能を提供します。

## オプション

### **-v, --verbose**

リクエストとレスポンスの詳細情報を表示します。

```console
$ http -v example.com
GET / HTTP/1.1
Host: example.com
User-Agent: HTTPie/3.2.1
Accept-Encoding: gzip, deflate
Accept: */*
Connection: keep-alive

HTTP/1.1 200 OK
Age: 595469
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Tue, 30 Apr 2025 10:00:00 GMT
...
```

### **-j, --json**

JSONデータを送信するためのショートカットです。Content-Type ヘッダーを application/json に設定します。

```console
$ http -j POST api.example.com/users name=John age:=30
POST /users HTTP/1.1
Host: api.example.com
Content-Type: application/json
...

{
    "name": "John",
    "age": 30
}
```

### **-f, --form**

フォームデータを送信するためのショートカットです。Content-Type ヘッダーを application/x-www-form-urlencoded に設定します。

```console
$ http -f POST api.example.com/submit name=John age=30
POST /submit HTTP/1.1
Host: api.example.com
Content-Type: application/x-www-form-urlencoded
...

name=John&age=30
```

### **-a, --auth**

Basic認証のための認証情報を指定します。

```console
$ http -a username:password api.example.com/secure
GET /secure HTTP/1.1
Host: api.example.com
Authorization: Basic dXNlcm5hbWU6cGFzc3dvcmQ=
...
```

### **-h, --headers**

レスポンスヘッダーのみを表示します。

```console
$ http -h example.com
HTTP/1.1 200 OK
Age: 595469
Cache-Control: max-age=604800
Content-Type: text/html; charset=UTF-8
Date: Tue, 30 Apr 2025 10:00:00 GMT
...
```

## 使用例

### 基本的なGETリクエスト

```console
$ http example.com
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
...

<!doctype html>
<html>
...
</html>
```

### JSONデータを送信するPOSTリクエスト

```console
$ http POST api.example.com/users name=John age:=30 is_active:=true
HTTP/1.1 201 Created
Content-Type: application/json
...

{
    "id": 123,
    "name": "John",
    "age": 30,
    "is_active": true
}
```

### カスタムヘッダーの追加

```console
$ http example.com X-API-Key:abc123 User-Agent:MyApp/1.0
HTTP/1.1 200 OK
...

[レスポンス本文]
```

### ファイルのアップロード

```console
$ http POST api.example.com/upload file@/path/to/file.jpg
HTTP/1.1 200 OK
...

{
    "success": true,
    "file_id": "f123"
}
```

## ヒント:

### JSONデータの書き方

- `name=value` は文字列として扱われます
- `name:=value` は JSON として解釈されます（数値、ブール値、null など）
- `name:=@file.json` はファイルから JSON を読み込みます

### 出力のカラー表示

HTTPie はデフォルトでカラー表示を行いますが、パイプやリダイレクトを使用する場合は `--pretty=all` オプションを使用すると強制的にカラー表示されます。

### セッションの保存と再利用

`--session=NAME` オプションを使用すると、クッキーやその他のセッション情報を保存して再利用できます。ログインが必要なAPIをテストする際に便利です。

### リダイレクトの追跡

`--follow` オプションを使用すると、HTTPリダイレクト（301、302など）を自動的に追跡します。

## よくある質問

#### Q1. HTTPieとcURLの違いは何ですか？
A. HTTPieはcURLよりも使いやすく設計されており、JSONの扱いが簡単で、カラフルな出力、直感的な構文などの特徴があります。cURLはより多機能ですが、HTTPieは日常的なAPI操作により適しています。

#### Q2. HTTPieをインストールするにはどうすればよいですか？
A. `pip install httpie`（Python）、`brew install httpie`（macOS）、`apt install httpie`（Ubuntu/Debian）などでインストールできます。

#### Q3. HTTPSリクエストで証明書検証をスキップするにはどうすればよいですか？
A. `--verify=no` オプションを使用します。ただし、セキュリティ上の理由から本番環境では推奨されません。

#### Q4. リクエストのタイムアウトを設定するにはどうすればよいですか？
A. `--timeout=SECONDS` オプションを使用します。例：`http --timeout=5 example.com`

## macOSでの注意点

macOSでは、Homebrewを使用して簡単にインストールできます：

```console
$ brew install httpie
```

macOSのセキュリティ設定によっては、一部の証明書検証に関する問題が発生する場合があります。その場合は `--verify=no` オプションを使用するか、Python の証明書ストアを更新することで解決できることがあります。

## 参考

https://httpie.io/docs

## 改訂履歴

- 2025/04/30 初版作成