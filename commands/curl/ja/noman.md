# curlコマンド概要

curlは、URLを使用してデータを転送するためのコマンドラインツールです。WebサイトのHTTPリクエスト、APIの呼び出し、ファイルのダウンロードなど、さまざまなネットワーク操作に使用されます。

## 主なオプション

- **-o, --output \<file\>**: 出力を指定したファイルに保存します
  - 例: `curl -o example.html https://example.com`

- **-O, --remote-name**: リモートファイルと同じ名前でファイルを保存します
  - 例: `curl -O https://example.com/file.zip`

- **-L, --location**: リダイレクトに自動的に従います
  - 例: `curl -L https://github.com`

- **-I, --head**: HTTPヘッダーのみを取得します（本文は取得しません）
  - 例: `curl -I https://example.com`

- **-H, --header \<header\>**: リクエストにカスタムヘッダーを追加します
  - 例: `curl -H "Authorization: Bearer token123" https://api.example.com`

- **-X, --request \<command\>**: 使用するHTTPメソッドを指定します
  - 例: `curl -X POST https://api.example.com/data`

- **-d, --data \<data\>**: POSTリクエストでデータを送信します
  - 例: `curl -X POST -d "name=value" https://api.example.com/form`

- **-s, --silent**: 進行状況や警告メッセージを表示しません
  - 例: `curl -s https://example.com`

## 使用例

### 基本的なWebページの取得
```bash
# Webページの内容を表示
curl https://example.com
# 出力: HTMLコンテンツが標準出力に表示される
```

### ファイルのダウンロード
```bash
# ファイルを指定した名前で保存
curl -o myfile.zip https://example.com/file.zip
# 出力: ファイルがmyfile.zipとして保存される

# リモートと同じファイル名で保存
curl -O https://example.com/file.zip
# 出力: ファイルがfile.zipとして保存される
```

### APIリクエスト
```bash
# JSONデータをPOSTで送信
curl -X POST -H "Content-Type: application/json" -d '{"name":"John","age":30}' https://api.example.com/users
# 出力: APIからのレスポンスが表示される
```

### HTTPヘッダーの確認
```bash
# ヘッダー情報のみを取得
curl -I https://example.com
# 出力:
# HTTP/2 200
# content-type: text/html; charset=UTF-8
# date: Mon, 01 Jan 2023 12:00:00 GMT
# server: ECS (dcb/7F84)
# ...
```

### 進行状況バーの表示
```bash
# 進行状況バーを表示してファイルをダウンロード
curl -# -O https://example.com/largefile.zip
# 出力: [######################] 100%
```

## 追加情報

- curlは非常に多機能で、400以上のオプションがありますが、上記のオプションが日常的な使用で最も一般的です。
- `-k`または`--insecure`オプションを使用すると、SSL証明書の検証をスキップできますが、セキュリティ上のリスクがあるため注意が必要です。
- 複雑なAPIリクエストを行う場合は、`-v`（詳細モード）を使用すると、リクエストとレスポンスの詳細を確認できて便利です。
- ブラウザのようにcookieを扱いたい場合は、`--cookie-jar`と`--cookie`オプションを使用できます。