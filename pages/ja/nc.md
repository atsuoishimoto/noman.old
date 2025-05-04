# nc コマンド

ネットワーク接続を作成・管理し、データ転送、ポートスキャン、ネットワークデバッグを行います。

## 概要

`nc`（netcat）は、TCPまたはUDPプロトコルを使用してネットワーク接続間でデータを読み書きする多目的ネットワークユーティリティです。サーバーやクライアントの作成、ファイル転送、ポートスキャン、ネットワーク問題のデバッグなどができる「ネットワークのスイスアーミーナイフ」として機能します。シンプルで柔軟性があるため、システム管理者やセキュリティ専門家にとって不可欠なツールとなっています。

## オプション

### **-l, --listen**

接続を開始するのではなく、着信接続をリッスンします。

```console
$ nc -l 8080
Hello, world!
```

### **-p, --port**

ncが使用すべきソースポートを指定します（権限制限と可用性に依存）。

```console
$ nc -p 31337 example.com 80
```

### **-v, --verbose**

詳細な出力を有効にして、より多くの接続詳細を表示します。

```console
$ nc -v example.com 80
Connection to example.com 80 port [tcp/http] succeeded!
```

### **-z**

データを送信せずにリスニングデーモンをスキャンします（ポートスキャンモード）。

```console
$ nc -zv example.com 20-30
Connection to example.com 22 port [tcp/ssh] succeeded!
```

### **-u, --udp**

デフォルトのTCPプロトコルの代わりにUDPを使用します。

```console
$ nc -u 192.168.1.100 53
```

### **-w, --timeout**

接続試行のタイムアウトを設定します。

```console
$ nc -w 5 example.com 80
```

## 使用例

### シンプルなチャットサーバーの作成

```console
$ nc -l 1234
```

### チャットサーバーへの接続

```console
$ nc 192.168.1.100 1234
Hello, are you there?
```

### ファイル転送

サーバー側:
```console
$ nc -l 1234 > received_file.txt
```

クライアント側:
```console
$ nc 192.168.1.100 1234 < file_to_send.txt
```

### ポートスキャン

```console
$ nc -zv example.com 20-30
Connection to example.com 22 port [tcp/ssh] succeeded!
Connection to example.com 25 port [tcp/smtp] succeeded!
```

### バナーグラビング

```console
$ nc -v example.com 22
Connection to example.com 22 port [tcp/ssh] succeeded!
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
```

## ヒント:

### シンプルなWebサーバーとして使用

基本的なHTTPサーバーを作成してファイルを提供できます：
```console
$ while true; do nc -l 8080 < response.html; done
```

### 出力をファイルにリダイレクト

トラブルシューティング時に、後で分析するために出力を保存します：
```console
$ nc example.com 80 > output.txt
```

### ポートが開いているか確認

特定のポートがアクセス可能かどうかを素早く確認する方法：
```console
$ nc -zv example.com 443
```

### パイプと組み合わせて使用

ncはUnixパイプと組み合わせて複雑な操作を行うことができます：
```console
$ echo -e "GET / HTTP/1.0\r\n\r\n" | nc example.com 80
```

## よくある質問

#### Q1. ncとtelnetの違いは何ですか？
A. どちらもリモートサービスに接続できますが、`nc`はポートスキャン、UDPサポート、より優れたスクリプト機能など、より多機能です。telnetは主に対話型ターミナルセッション用に設計されています。

#### Q2. クライアントが切断した後もnetcatリスナーを実行し続けるにはどうすればよいですか？
A. バージョンによってサポートされている場合は、`-k`オプションを使用してクライアント切断後もサーバーをリスニング状態に保ちます。それ以外の場合は、ループで囲みます：`while true; do nc -l 8080; done`

#### Q3. netcatは機密データの転送に安全ですか？
A. いいえ、netcatはデータを平文で送信します。安全な転送には、`scp`、`sftp`、またはSSH経由でnetcatをトンネリングするツールの使用を検討してください。

#### Q4. Webサーバーが動作しているかをテストするにはどうすればよいですか？
A. 次のコマンドを使用します：`echo -e "GET / HTTP/1.0\r\n\r\n" | nc example.com 80`

## macOSに関する注意点

macOSでは、デフォルトの`nc`実装はGNU netcatよりも機能が少ない場合があります。`-k`（リスニングを継続する）などの一部のオプションは利用できない可能性があります。Homebrewを通じて代替バージョンをインストールすることを検討してください：`brew install netcat`

## 参考資料

https://man7.org/linux/man-pages/man1/nc.1.html

## 改訂履歴

- 2025/05/04 初版作成