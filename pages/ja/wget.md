# wget コマンド概要

`wget`はウェブサーバーからファイルをダウンロードするためのコマンドラインツールです。HTTPやFTPなどのプロトコルを使用して、インターネット上のファイルを取得できます。

## 主なオプション

- **-O, --output-document=FILE**: ダウンロードしたファイルを指定した名前で保存します
  - 例: `wget -O example.zip https://example.com/file.zip`

- **-c, --continue**: 部分的にダウンロードされたファイルの続きからダウンロードを再開します
  - 例: `wget -c https://example.com/largefile.iso`

- **-b, --background**: バックグラウンドでダウンロードを実行します
  - 例: `wget -b https://example.com/file.zip`

- **-r, --recursive**: ウェブサイトを再帰的にダウンロードします
  - 例: `wget -r https://example.com/docs/`

- **-l, --level=NUMBER**: 再帰的ダウンロードの深さを指定します
  - 例: `wget -r -l 2 https://example.com/`

- **-np, --no-parent**: 親ディレクトリへ移動しないようにします
  - 例: `wget -r -np https://example.com/docs/`

- **-P, --directory-prefix=PREFIX**: ファイルを保存するディレクトリを指定します
  - 例: `wget -P downloads/ https://example.com/file.zip`

- **--limit-rate=RATE**: ダウンロード速度を制限します（例：20k, 1m）
  - 例: `wget --limit-rate=200k https://example.com/largefile.iso`

## 使用例

### 基本的なファイルのダウンロード

```bash
# ウェブサイトからファイルをダウンロード
wget https://example.com/file.zip
# 出力
--2023-04-01 12:00:00--  https://example.com/file.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1024000 (1000K) [application/zip]
Saving to: 'file.zip'

file.zip            100%[===================>]   1000K   256KB/s    in 3.9s    

2023-04-01 12:00:04 (256 KB/s) - 'file.zip' saved [1024000/1024000]
```

### 異なるファイル名で保存

```bash
# ダウンロードしたファイルを別の名前で保存
wget -O custom_name.zip https://example.com/file.zip
# 出力
--2023-04-01 12:01:00--  https://example.com/file.zip
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 1024000 (1000K) [application/zip]
Saving to: 'custom_name.zip'

custom_name.zip     100%[===================>]   1000K   256KB/s    in 3.9s    

2023-04-01 12:01:04 (256 KB/s) - 'custom_name.zip' saved [1024000/1024000]
```

### ウェブサイトの再帰的ダウンロード

```bash
# ウェブサイトの特定のディレクトリを再帰的にダウンロード（深さ2まで）
wget -r -l 2 -np https://example.com/docs/
# 出力
--2023-04-01 12:02:00--  https://example.com/docs/
Resolving example.com... 93.184.216.34
Connecting to example.com|93.184.216.34|:443... connected.
HTTP request sent, awaiting response... 200 OK
Length: 5120 (5.0K) [text/html]
Saving to: 'example.com/docs/index.html'

example.com/docs/index.html    100%[===================>]   5.0K   --.-KB/s    in 0.1s    

2023-04-01 12:02:01 (50.0 KB/s) - 'example.com/docs/index.html' saved [5120/5120]

... (他のファイルのダウンロード情報) ...
```

## 追加情報

- ダウンロードが中断された場合は、`-c`オプションを使用して再開できます。大きなファイルをダウンロードする際に便利です。
- `wget`はプロキシサーバーを通じたダウンロードもサポートしています。環境変数`http_proxy`や`https_proxy`を設定するか、`--proxy`オプションを使用します。
- 認証が必要なサイトからダウンロードする場合は、`--user=USER`と`--password=PASS`オプションを使用できます。
- バックグラウンドでダウンロードを実行する場合（`-b`オプション）、進行状況は`wget-log`ファイルに記録されます。