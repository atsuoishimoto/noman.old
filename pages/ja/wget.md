# wget コマンド

wgetはウェブサーバーからファイルをダウンロードするためのコマンドラインツールです。HTTPやFTPなどのプロトコルを使用してコンテンツを取得できます。

## オプション

### **-O, --output-document=FILE**
ダウンロードしたファイルを指定した名前で保存します

```console
$ wget -O example.zip https://example.com/file.zip
--2023-04-01 12:01:00--  https://example.com/file.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1024000 (1000K) [application/zip]
Saving to: 'example.zip'

example.zip     100%[===================>]   1000K   256KB/s    in 3.9s    

2023-04-01 12:01:04 (256 KB/s) - 'example.zip' saved [1024000/1024000]
```

### **-c, --continue**
部分的にダウンロードされたファイルの続きからダウンロードを再開します

```console
$ wget -c https://example.com/largefile.iso
--2023-04-01 12:05:00--  https://example.com/largefile.iso
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 206 Partial Content
Length: 104857600 (100M), 52428800 (50M) remaining [application/octet-stream]
Saving to: 'largefile.iso'

largefile.iso   50%[========>         ]  50.0M   1.2MB/s    eta 41s
```

### **-r, --recursive**
ウェブサイトを再帰的にダウンロードします

```console
$ wget -r https://example.com/docs/
--2023-04-01 12:02:00--  https://example.com/docs/
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5120 (5.0K) [text/html]
Saving to: 'example.com/docs/index.html'

example.com/docs/index.html    100%[===================>]   5.0K   --.-KB/s    in 0.1s
```

### **-P, --directory-prefix=PREFIX**
ファイルを保存するディレクトリを指定します

```console
$ wget -P downloads/ https://example.com/file.zip
--2023-04-01 12:10:00--  https://example.com/file.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1024000 (1000K) [application/zip]
Saving to: 'downloads/file.zip'

downloads/file.zip  100%[===================>]   1000K   256KB/s    in 3.9s
```

## 使用例

### 基本的なファイルのダウンロード

```console
$ wget https://example.com/file.zip
--2023-04-01 12:00:00--  https://example.com/file.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1024000 (1000K) [application/zip]
Saving to: 'file.zip'

file.zip            100%[===================>]   1000K   256KB/s    in 3.9s    

2023-04-01 12:00:04 (256 KB/s) - 'file.zip' saved [1024000/1024000]
```

### ウェブサイトの再帰的ダウンロード（深さと親ディレクトリ制限付き）

```console
$ wget -r -l 2 -np https://example.com/docs/
--2023-04-01 12:02:00--  https://example.com/docs/
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5120 (5.0K) [text/html]
Saving to: 'example.com/docs/index.html'

example.com/docs/index.html    100%[===================>]   5.0K   --.-KB/s    in 0.1s    

2023-04-01 12:02:01 (50.0 KB/s) - 'example.com/docs/index.html' saved [5120/5120]
```

### ダウンロード速度の制限

```console
$ wget --limit-rate=200k https://example.com/largefile.iso
--2023-04-01 12:15:00--  https://example.com/largefile.iso
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 104857600 (100M) [application/octet-stream]
Saving to: 'largefile.iso'

largefile.iso   10%[===>              ]  10.0M   200KB/s    eta 7m 30s
```

## Tips

### バックグラウンドでのダウンロード
`-b`オプションを使用すると、ダウンロードをバックグラウンドで実行できます。進行状況は`wget-log`ファイルに記録されます。

### 複数ファイルのダウンロード
URLリストを含むファイルを作成し、`-i`オプションで指定すると、複数のファイルを一度にダウンロードできます。

### ミラーリング
`--mirror`オプションは、`-r -N -l inf --no-remove-listing`の組み合わせで、サイトの完全なミラーを作成します。

## よくある質問

#### Q1. ダウンロードが途中で中断された場合はどうすればよいですか？
A. `-c`オプションを使用すると、中断されたダウンロードを続きから再開できます。例：`wget -c https://example.com/largefile.iso`

#### Q2. ウェブサイト全体をダウンロードするにはどうすればよいですか？
A. `-r`（再帰的）、`-np`（親ディレクトリに移動しない）、`-l`（深さレベル）オプションを組み合わせて使用します。例：`wget -r -np -l 2 https://example.com/`

#### Q3. ダウンロードをバックグラウンドで実行するにはどうすればよいですか？
A. `-b`オプションを使用します。進行状況は`wget-log`ファイルに記録されます。例：`wget -b https://example.com/file.zip`

#### Q4. 認証が必要なサイトからダウンロードするにはどうすればよいですか？
A. `--user=USER`と`--password=PASS`オプションを使用します。例：`wget --user=username --password=password https://example.com/private/file.zip`

## macOSでの注意点

macOSでは、デフォルトではwgetがインストールされていません。Homebrewを使用して最新版のwgetをインストールできます：

```console
$ brew install wget
```

インストール後は、他のUnixシステムと同様に使用できます。

## 参考資料

https://www.gnu.org/software/wget/manual/wget.html

## 改訂履歴

- 2025/04/26 Tipsセクションを追加し、macOSでの注意点を独立したセクションに移動しました。
- 2025/04/26 コマンドの概要を追加し、ドキュメント形式を改善しました。
- 2025/04/01 ドキュメント形式を統一し、よくある質問と追加情報を整理しました。macOSに関する情報を追加しました。