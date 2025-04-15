# curl コマンド概要

`curl`はURLを使用してデータを転送するためのコマンドラインツールです。WebサイトのコンテンツのダウンロードやAPIとの通信など、HTTPやその他のプロトコルを介したデータのやり取りに使用されます。

## オプション

### **-o, --output**

指定したファイル名にダウンロードしたデータを保存します。

```bash
$ curl -o example.html https://example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0   7975      0 --:--:-- --:--:-- --:--:--  8034
```

### **-O, --remote-name**

リモートファイルと同じ名前でローカルに保存します。

```bash
$ curl -O https://example.com/sample.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.2M  100 10.2M    0     0  5215k      0  0:00:02  0:00:02 --:--:-- 5216k
```

### **-s, --silent**

進行状況やエラーメッセージを表示せず、静かに実行します。

```bash
$ curl -s https://example.com > example.html
```

### **-I, --head**

HTTPヘッダー情報のみを取得します（コンテンツ本体は取得しません）。

```bash
$ curl -I https://example.com
HTTP/2 200 
content-type: text/html; charset=UTF-8
date: Mon, 15 May 2023 12:34:56 GMT
expires: Mon, 22 May 2023 12:34:56 GMT
cache-control: public, max-age=604800
server: ECS (dcb/7F83)
content-length: 1256
```

### **-X, --request**

HTTPリクエストメソッド（GET、POST、PUT、DELETEなど）を指定します。

```bash
$ curl -X POST https://api.example.com/data
```

### **-H, --header**

HTTPリクエストヘッダーを追加します。

```bash
$ curl -H "Content-Type: application/json" -H "Authorization: Bearer token123" https://api.example.com
```

### **-d, --data**

POSTリクエストでデータを送信します。

```bash
$ curl -X POST -d "name=John&age=30" https://api.example.com/users
```

### **-L, --location**

リダイレクトに自動的に従います。

```bash
$ curl -L https://example.com/redirect
```

## 使用例

### JSONデータをPOSTする

```bash
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"山田太郎","email":"yamada@example.com"}' https://api.example.com/users
{"id": 123, "status": "created"}
```

### ファイルをダウンロードして進捗状況を表示

```bash
$ curl -# -O https://example.com/largefile.zip
######################################################################## 100.0%
```

### 複数のファイルを一度にダウンロード

```bash
$ curl -O https://example.com/file1.txt -O https://example.com/file2.txt
```

### APIからJSONデータを取得して整形表示（jqと組み合わせ）

```bash
$ curl -s https://api.example.com/users | jq
{
  "users": [
    {
      "id": 1,
      "name": "山田太郎"
    },
    {
      "id": 2,
      "name": "佐藤花子"
    }
  ]
}
```

## よくある質問

### Q1. curlとwgetの違いは何ですか？
A. curlはより多くのプロトコルとオプションをサポートし、スクリプト内での使用に適しています。wgetは再帰的なダウンロードに優れています。curlはデフォルトで標準出力に結果を表示しますが、wgetはファイルに保存します。

### Q2. curlでHTTPSサイトの証明書エラーを無視するには？
A. `-k`または`--insecure`オプションを使用します。ただし、セキュリティ上のリスクがあるため注意が必要です。

### Q3. curlでリクエストのタイムアウトを設定するには？
A. `--connect-timeout <秒数>`でコネクションタイムアウト、`--max-time <秒数>`で全体のタイムアウトを設定できます。

### Q4. curlでクッキーを使用するには？
A. `-b`または`--cookie`オプションでクッキーを送信、`-c`または`--cookie-jar`オプションでクッキーを保存できます。

## 追加情報

- `-v`（verbose）オプションを使用すると、リクエストとレスポンスの詳細情報が表示され、デバッグに役立ちます。
- `curl`は多くのプロトコル（HTTP、HTTPS、FTP、SFTP、SMTPなど）をサポートしています。
- 大きなファイルをダウンロードする場合は、`-C -`オプションを使用すると、中断したダウンロードを再開できます。
- APIテストやWebスクレイピングのスクリプトでよく使用されるコマンドです。
- 複雑なリクエストは、`--data-binary @file.json`のようにファイルからデータを読み込むと便利です。