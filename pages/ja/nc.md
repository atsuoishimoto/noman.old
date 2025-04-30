# nc コマンド

ネットワーク接続を読み書きするためのユーティリティ。

## 概要

`nc`（netcat）は、TCP や UDP プロトコルを使用してネットワーク接続を確立し、データを送受信するためのシンプルなコマンドラインツールです。ポートスキャン、ファイル転送、チャット、サーバーのテストなど、さまざまなネットワーク関連タスクに使用できます。

## オプション

### **-l**：リッスンモード

サーバーとして動作し、指定したポートで接続を待ち受けます。

```console
$ nc -l 1234
```

### **-p**：ポート指定

使用するローカルポート番号を指定します。

```console
$ nc -p 12345 example.com 80
```

### **-v**：詳細表示

接続の詳細情報を表示します。デバッグに役立ちます。

```console
$ nc -v example.com 80
Connection to example.com 80 port [tcp/http] succeeded!
```

### **-z**：スキャンモード

接続を確立せずにポートスキャンを行います。

```console
$ nc -z -v example.com 20-30
Connection to example.com 22 port [tcp/ssh] succeeded!
Connection to example.com 25 port [tcp/smtp] succeeded!
```

### **-u**：UDP モード

デフォルトの TCP の代わりに UDP プロトコルを使用します。

```console
$ nc -u -l 1234
```

## 使用例

### 簡易チャットサーバーの作成

```console
# サーバー側
$ nc -l 1234
こんにちは！
元気ですか？

# クライアント側
$ nc localhost 1234
こんにちは！
元気ですか？
```

### ファイル転送

```console
# 受信側
$ nc -l 1234 > received_file.txt

# 送信側
$ nc 192.168.1.100 1234 < file_to_send.txt
```

### ポートスキャン

```console
$ nc -z -v example.com 20-100
Connection to example.com 22 port [tcp/ssh] succeeded!
Connection to example.com 80 port [tcp/http] succeeded!
Connection to example.com 443 port [tcp/https] succeeded!
```

### HTTP リクエストの送信

```console
$ echo -e "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n" | nc example.com 80
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Date: Wed, 30 Apr 2025 12:00:00 GMT
...
```

## ヒント:

### タイムアウトの設定

`-w` オプションを使用して接続のタイムアウト時間を秒単位で設定できます。これはスクリプト内で使用する際に特に便利です。

```console
$ nc -w 5 example.com 80
```

### バナー情報の取得

サーバーのバナー情報を取得するには、単純に接続するだけで十分な場合があります。

```console
$ nc -v example.com 22
SSH-2.0-OpenSSH_8.2p1 Ubuntu-4ubuntu0.5
```

### 永続的なリスニングサーバー

`-k` オプションを使用すると、クライアントが切断した後もリスニングを継続します。

```console
$ nc -k -l 1234
```

## よくある質問

#### Q1. nc と telnet の違いは何ですか？
A. `nc` は `telnet` よりも多機能で、TCP/UDP の両方をサポートし、ポートスキャンやファイル転送などの機能も提供します。`telnet` は主に対話型のリモート接続に使用されます。

#### Q2. nc でファイアウォールをバイパスできますか？
A. `nc` 自体はファイアウォールをバイパスする機能はありませんが、さまざまなポートやプロトコルを使用して接続を試みることができます。ただし、セキュリティ上の理由から、許可されたネットワークでのみ使用してください。

#### Q3. nc の代替コマンドはありますか？
A. `socat`、`ncat`（Nmap プロジェクトの一部）、`telnet`（基本的な機能のみ）などがあります。`socat` は特に高度な機能を提供します。

#### Q4. macOS と Linux の nc コマンドに違いはありますか？
A. はい、macOS の `nc` は BSD バージョンで、Linux の多くのディストリビューションで使用される GNU バージョンとは一部のオプションが異なります。例えば、macOS の `nc` では `-k` オプション（接続後もリスニングを継続する）がサポートされていない場合があります。

## macOS での注意点

macOS に搭載されている `nc` は BSD バージョンであり、Linux の GNU バージョンとは一部の機能やオプションが異なります。特に以下の点に注意してください：

- `-e` オプション（コマンド実行）は macOS の `nc` ではサポートされていません
- 永続的なリスニング（`-k`）は macOS の一部のバージョンではサポートされていない場合があります
- macOS で同様の機能が必要な場合は、Homebrew などを使用して GNU バージョンの netcat をインストールすることを検討してください

## 参考資料

https://man.openbsd.org/nc.1

## 改訂履歴

- 2025/04/30 初版作成