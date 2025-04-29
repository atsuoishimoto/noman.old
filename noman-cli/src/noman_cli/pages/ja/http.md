# `http` コマンド概要

`http` コマンドは、HTTPリクエストを簡単に送信し、レスポンスを見やすく表示するためのコマンドラインツールです。主に開発者がAPIのテストやデバッグに使用します。

## 主なオプション

- **`GET`/`POST`/`PUT`/`DELETE` など**: HTTPメソッドを指定します
  - 例: `http GET example.com`

- **`-v`, `--verbose`**: 詳細な情報（リクエストヘッダーやレスポンスヘッダーなど）を表示します
  - 例: `http -v GET example.com`

- **`-j`, `--json`**: JSONデータを送信する際に使用します
  - 例: `http -j POST example.com/api name=value`

- **`-f`, `--form`**: フォームデータを送信する際に使用します
  - 例: `http -f POST example.com/upload file@/path/to/file.jpg`

- **`-a`, `--auth`**: 基本認証情報を指定します
  - 例: `http -a username:password example.com`

- **`-h`, `--headers`**: カスタムヘッダーを追加します
  - 例: `http example.com X-API-Key:abc123`

## 使用例

### 基本的なGETリクエスト
```bash
# シンプルなGETリクエスト
http get httpbin.org/get
# 出力例
{
  "args": {}, 
  "headers": {
    "Accept": "*/*", 
    "Host": "httpbin.org", 
    "User-Agent": "HTTPie/2.6.0"
  }, 
  "url": "https://httpbin.org/get"
}
```

### クエリパラメータの送信
```bash
# クエリパラメータを含むGETリクエスト
http get httpbin.org/get name=value id=123
# 出力例
{
  "args": {
    "id": "123", 
    "name": "value"
  }, 
  "headers": {
    "Accept": "*/*", 
    "Host": "httpbin.org", 
    "User-Agent": "HTTPie/2.6.0"
  }, 
  "url": "https://httpbin.org/get?name=value&id=123"
}
```

### JSONデータを送信するPOSTリクエスト
```bash
# JSONデータを送信するPOSTリクエスト
http post httpbin.org/post name=John age:=30 skills:='["python", "javascript"]'
# 出力例
{
  "args": {}, 
  "data": "{\"name\": \"John\", \"age\": 30, \"skills\": [\"python\", \"javascript\"]}", 
  "files": {}, 
  "form": {}, 
  "headers": {
    "Accept": "application/json", 
    "Content-Length": "60", 
    "Content-Type": "application/json", 
    "Host": "httpbin.org", 
    "User-Agent": "HTTPie/2.6.0"
  }, 
  "json": {
    "age": 30, 
    "name": "John", 
    "skills": [
      "python", 
      "javascript"
    ]
  }, 
  "url": "https://httpbin.org/post"
}
```

### ファイルのアップロード
```bash
# ファイルをアップロードする例
http -f POST httpbin.org/post file@/path/to/document.pdf
# 出力例
{
  "args": {}, 
  "data": "", 
  "files": {
    "file": "ファイルの内容（バイナリデータ）"
  }, 
  "form": {}, 
  "headers": {
    "Accept": "*/*", 
    "Content-Length": "12345", 
    "Content-Type": "multipart/form-data; boundary=---", 
    "Host": "httpbin.org", 
    "User-Agent": "HTTPie/2.6.0"
  }, 
  "url": "https://httpbin.org/post"
}
```

## 追加情報

- `:=` を使うと数値や真偽値などのJSONデータ型を指定できます（例: `count:=42`）
- `:=[]` や `:={}` を使って配列やオブジェクトを指定できます
- `@` を使ってファイルの内容を送信できます（例: `data@file.json`）
- カラー出力がデフォルトで有効になっており、レスポンスが見やすく表示されます
- HTTPSリクエストの場合、証明書の検証に問題があれば警告が表示されます
- `--offline` オプションを使用すると、実際にリクエストを送信せずにリクエスト内容を確認できます