# wget コマンド

ウェブからHTTP、HTTPS、またはFTPプロトコルを使用してファイルをダウンロードします。

## 概要

`wget`はウェブからファイルをダウンロードするための非対話型コマンドラインユーティリティです。HTTP、HTTPS、FTPプロトコルをサポートし、バックグラウンドで動作したり、中断されたダウンロードを再開したり、ウェブページ上のリンクをたどったりすることができます。ブラウザが利用できない場合やダウンロードを自動化する必要がある場合に特に便利です。

## オプション

### **-O, --output-document=FILE**

ダウンロードしたファイルに別のファイル名を指定します

```console
$ wget -O カスタム名.zip https://example.com/download/file.zip
--2025-05-04 10:15:30--  https://example.com/download/file.zip
example.com (example.com) をDNSに問いあわせています... 93.184.216.34
example.com (example.com)|93.184.216.34|:443 に接続しています... 接続しました。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 1024000 (1000K) [application/zip]
'カスタム名.zip' に保存中

カスタム名.zip       100%[===================>]  1000K  1.2MB/s    in 0.8s    

2025-05-04 10:15:31 (1.2 MB/s) - 'カスタム名.zip' へ保存完了 [1024000/1024000]
```

### **-c, --continue**

部分的にダウンロードされたファイルを再開します

```console
$ wget -c https://example.com/large-file.iso
--2025-05-04 10:20:45--  https://example.com/large-file.iso
example.com (example.com) をDNSに問いあわせています... 93.184.216.34
example.com (example.com)|93.184.216.34|:443 に接続しています... 接続しました。
HTTP による接続要求を送信しました、応答を待っています... 206 Partial Content
長さ: 1073741824 (1.0G), 残り 536870912 (512M) [application/octet-stream]
'large-file.iso' に保存中

large-file.iso      50%[====>           ]  512M  5.2MB/s    残り 1m 40s
```

### **-b, --background**

起動後にwgetをバックグラウンドで実行します

```console
$ wget -b https://example.com/large-file.iso
バックグラウンドで継続します、pid 12345。
出力は 'wget-log' に書き込まれます。
```

### **-r, --recursive**

再帰的にダウンロードします（ウェブサイトのミラーリングに便利）

```console
$ wget -r -np https://example.com/docs/
--2025-05-04 10:30:15--  https://example.com/docs/
example.com (example.com) をDNSに問いあわせています... 93.184.216.34
example.com (example.com)|93.184.216.34|:443 に接続しています... 接続しました。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 5120 (5.0K) [text/html]
'example.com/docs/index.html' に保存中

example.com/docs/index.html    100%[===================>]   5.0K  --.-KB/s    in 0.001s  

2025-05-04 10:30:16 (5.0 MB/s) - 'example.com/docs/index.html' へ保存完了 [5120/5120]

--2025-05-04 10:30:16--  https://example.com/docs/page1.html
example.com:443 への接続を再利用します。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 4096 (4.0K) [text/html]
'example.com/docs/page1.html' に保存中

example.com/docs/page1.html    100%[===================>]   4.0K  --.-KB/s    in 0.001s  
```

### **-np, --no-parent**

再帰的に取得する際に親ディレクトリに上がらないようにします

```console
$ wget -r -np https://example.com/docs/
```

### **-q, --quiet**

静かなモード（出力なし）

```console
$ wget -q https://example.com/file.txt
```

### **-P, --directory-prefix=PREFIX**

指定したディレクトリにファイルを保存します

```console
$ wget -P downloads/ https://example.com/file.txt
--2025-05-04 10:40:20--  https://example.com/file.txt
example.com (example.com) をDNSに問いあわせています... 93.184.216.34
example.com (example.com)|93.184.216.34|:443 に接続しています... 接続しました。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 2048 (2.0K) [text/plain]
'downloads/file.txt' に保存中

downloads/file.txt  100%[===================>]   2.0K  --.-KB/s    in 0.001s  

2025-05-04 10:40:21 (2.0 MB/s) - 'downloads/file.txt' へ保存完了 [2048/2048]
```

## 使用例

### プログレスバー付きでファイルをダウンロード

```console
$ wget https://example.com/file.zip
--2025-05-04 10:45:30--  https://example.com/file.zip
example.com (example.com) をDNSに問いあわせています... 93.184.216.34
example.com (example.com)|93.184.216.34|:443 に接続しています... 接続しました。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 10485760 (10M) [application/zip]
'file.zip' に保存中

file.zip            100%[===================>]  10.0M  1.5MB/s    in 6.7s    

2025-05-04 10:45:37 (1.5 MB/s) - 'file.zip' へ保存完了 [10485760/10485760]
```

### ウェブサイトのミラーリング

```console
$ wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com/docs/
--2025-05-04 10:50:15--  https://example.com/docs/
example.com (example.com) をDNSに問いあわせています... 93.184.216.34
example.com (example.com)|93.184.216.34|:443 に接続しています... 接続しました。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 5120 (5.0K) [text/html]
'example.com/docs/index.html' に保存中

example.com/docs/index.html    100%[===================>]   5.0K  --.-KB/s    in 0.001s  

2025-05-04 10:50:16 (5.0 MB/s) - 'example.com/docs/index.html' へ保存完了 [5120/5120]
```

### 認証付きでダウンロード

```console
$ wget --user=username --password=password https://example.com/protected/file.pdf
--2025-05-04 10:55:45--  https://example.com/protected/file.pdf
example.com (example.com) をDNSに問いあわせています... 93.184.216.34
example.com (example.com)|93.184.216.34|:443 に接続しています... 接続しました。
HTTP による接続要求を送信しました、応答を待っています... 401 Unauthorized
認証方式が選択されました: Basic realm="Restricted Area"
example.com:443 への接続を再利用します。
HTTP による接続要求を送信しました、応答を待っています... 200 OK
長さ: 1048576 (1.0M) [application/pdf]
'file.pdf' に保存中

file.pdf            100%[===================>]   1.0M  1.2MB/s    in 0.8s    

2025-05-04 10:55:46 (1.2 MB/s) - 'file.pdf' へ保存完了 [1048576/1048576]
```

## ヒント:

### ダウンロード速度の制限

`--limit-rate=RATE`を使用してダウンロード速度を制限できます（例：`--limit-rate=200k`で200KB/秒）。これは、wgetが利用可能な帯域幅をすべて消費しないようにしたい場合に便利です。

### タイムアウトの処理

不安定な接続の場合は、`--timeout=SECONDS`と`--tries=NUMBER`でタイムアウト値を増やし、wgetがダウンロードを完了するまでより粘り強く試行するようにします。

### ユーザーエージェントの使用

一部のウェブサイトはwgetのデフォルトのユーザーエージェントをブロックします。`--user-agent="Mozilla/5.0"`を使用してブラウザを模倣し、ブロックされるのを避けることができます。

### ログファイルの作成

`--output-file=logfile.txt`を使用して、wgetの出力を画面に表示する代わりにファイルに保存します。長時間のダウンロードを追跡するのに便利です。

## よくある質問

#### Q1. 複数のファイルを一度にダウンロードするにはどうすればよいですか？
A. URLを1行に1つずつ記載したテキストファイルを作成し、`wget -i urls.txt`を使用します。

#### Q2. 進行状況の出力を表示せずにファイルをダウンロードするにはどうすればよいですか？
A. 静かなモードには`wget -q URL`を使用するか、バックグラウンドで実行するには`wget -b URL`を使用します。

#### Q3. 中断されたダウンロードを再開するにはどうすればよいですか？
A. `wget -c URL`を使用して、部分的にダウンロードされたファイルを中断された箇所から続行します。

#### Q4. wgetでウェブサイト全体をダウンロードできますか？
A. はい、`wget --mirror --convert-links --adjust-extension --page-requisites --no-parent https://example.com/`を使用してウェブサイトのローカルコピーを作成できます。

#### Q5. FTPサーバーからファイルをダウンロードするにはどうすればよいですか？
A. `wget ftp://username:password@ftp.example.com/path/to/file`または`wget --ftp-user=username --ftp-password=password ftp://ftp.example.com/path/to/file`を使用します。

## 参考資料

https://www.gnu.org/software/wget/manual/wget.html

## 改訂履歴

- 2025/05/04 初版作成