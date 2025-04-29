# curl コマンド

curlは、さまざまなプロトコル（HTTP、HTTPS、FTP等）を使用してデータを転送するためのコマンドラインツールです。Webページの取得、APIとの通信、ファイルのダウンロードなどに使用されます。

## オプション

### **-o, --output**
指定したファイル名にダウンロードしたデータを保存します。

```console
$ curl -o example.html https://example.com
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  1256  100  1256    0     0   7975      0 --:--:-- --:--:-- --:--:--  8034
```

### **-O, --remote-name**
リモートファイルと同じ名前でローカルに保存します。

```console
$ curl -O https://example.com/sample.zip
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 10.2M  100 10.2M    0     0  5215k      0  0:00:02  0:00:02 --:--:-- 5216k
```

### **-s, --silent**
進行状況やエラーメッセージを表示せず、静かに実行します。

```console
$ curl -s https://example.com > example.html
```

### **-I, --head**
HTTPヘッダー情報のみを取得します（コンテンツ本体は取得しません）。

```console
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

```console
$ curl -X POST https://api.example.com/data
```

### **-H, --header**
HTTPリクエストヘッダーを追加します。

```console
$ curl -H "Content-Type: application/json" -H "Authorization: Bearer token123" https://api.example.com
```

### **-d, --data**
POSTリクエストでデータを送信します。

```console
$ curl -X POST -d "name=John&age=30" https://api.example.com/users
```

### **-L, --location**
リダイレクトに自動的に従います。

```console
$ curl -L https://example.com/redirect
```

## 使用例

### JSONデータをPOSTする

```console
$ curl -X POST -H "Content-Type: application/json" -d '{"name":"山田太郎","email":"yamada@example.com"}' https://api.example.com/users
{"id": 123, "status": "created"}
```

### ファイルをダウンロードして進捗状況を表示

```console
$ curl -# -O https://example.com/largefile.zip
######################################################################## 100.0%
```

### 複数のファイルを一度にダウンロード

```console
$ curl -O https://example.com/file1.txt -O https://example.com/file2.txt
```

### APIからJSONデータを取得して整形表示（jqと組み合わせ）

```console
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

#### Q1. curlとwgetの違いは何ですか？
A. curlはより多くのプロトコルをサポートし、データの送信に強みがあります。wgetは再帰的なダウンロードに適しています。

#### Q2. curlでPOSTリクエストを送る基本的な方法は？
A. `curl -X POST -d "データ" URL` の形式で送信できます。JSONデータを送る場合は `-H "Content-Type: application/json"` ヘッダーも追加します。

#### Q3. ダウンロードが中断された場合、続きからダウンロードするには？
A. `-C -` オプションを使用すると、中断したところから再開できます。例: `curl -C - -O URL`

## 追加情報

* `-v`（verbose）オプションを使用すると、リクエストとレスポンスの詳細情報が表示され、デバッグに役立ちます。
* `curl`は多くのプロトコル（HTTP、HTTPS、FTP、SFTP、SMTPなど）をサポートしています。
* 大きなファイルをダウンロードする場合は、`-C -`オプションを使用すると、中断したダウンロードを再開できます。
* APIテストやWebスクレイピングのスクリプトでよく使用されるコマンドです。
* 複雑なリクエストは、`--data-binary @file.json`のようにファイルからデータを読み込むと便利です。
* macOSでは標準でインストールされていますが、最新バージョンが必要な場合はHomebrewで `brew install curl` としてアップデートできます。

## References

https://curl.se/docs/manpage.html

## Revisions

- 2025/04/26 コマンドの概要を冒頭に追加。フォーマットを指定された形式に変更。コードブロックの言語指定を`bash`から`console`に変更。「よくある質問」セクションを追加。macOSに関する情報を追加。
