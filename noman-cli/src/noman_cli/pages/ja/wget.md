# wget コマンド

リモートサーバーからファイルをダウンロードするためのコマンドラインツールです。

## 概要

`wget`は、HTTP、HTTPS、FTPなどのプロトコルを使用してウェブサーバーからファイルをダウンロードするためのユーティリティです。オフラインでの閲覧のためにウェブサイト全体をミラーリングしたり、スクリプト内でファイルを自動的にダウンロードしたりするのに便利です。ネットワーク接続が不安定な場合でも、ダウンロードを再開する機能があります。

## オプション

### **-O, --output-document=FILE**

ダウンロードしたファイルを指定した名前で保存します。

```console
$ wget -O latest-firefox.dmg https://download.mozilla.org/?product=firefox-latest
--2025-04-30 10:15:23--  https://download.mozilla.org/?product=firefox-latest
ファイル 'latest-firefox.dmg' に保存中
```

### **-c, --continue**

部分的にダウンロードされたファイルの続きからダウンロードを再開します。

```console
$ wget -c https://example.com/largefile.zip
--2025-04-30 10:16:45--  https://example.com/largefile.zip
ファイル 'largefile.zip' の続きからダウンロードを再開します
```

### **-b, --background**

バックグラウンドでダウンロードを実行します。ログは `wget-log` ファイルに保存されます。

```console
$ wget -b https://example.com/largefile.iso
バックグラウンドで実行を継続します。pid 1234
ログは 'wget-log' に出力されます
```

### **-r, --recursive**

リンクを再帰的にたどってダウンロードします。ウェブサイト全体をダウンロードする際に使用します。

```console
$ wget -r -np https://example.com/docs/
--2025-04-30 10:18:12--  https://example.com/docs/
ディレクトリ 'example.com/docs/' を再帰的にダウンロードしています
```

### **-np, --no-parent**

親ディレクトリへのリンクをたどらないようにします。特定のディレクトリ以下のみをダウンロードする場合に便利です。

```console
$ wget -r -np https://example.com/docs/
--2025-04-30 10:19:30--  https://example.com/docs/
親ディレクトリへのリンクは無視されます
```

### **-P, --directory-prefix=PREFIX**

ダウンロードしたファイルを指定したディレクトリに保存します。

```console
$ wget -P downloads/ https://example.com/file.zip
--2025-04-30 10:20:45--  https://example.com/file.zip
ファイルを 'downloads/file.zip' に保存中
```

## 使用例

### 単一ファイルのダウンロード

```console
$ wget https://example.com/file.zip
--2025-04-30 10:22:10--  https://example.com/file.zip
ファイル 'file.zip' に保存中
100%[======================================>] 1,234,567   1.2MB/s   in 1.0s
2025-04-30 10:22:11 (1.2 MB/s) - 'file.zip' へ保存完了 [1234567]
```

### ウェブサイトのミラーリング

```console
$ wget -m -k -p https://example.com/
--2025-04-30 10:23:30--  https://example.com/
ウェブサイトをミラーリングしています
リンクを変換しています...
```

### 認証が必要なサイトからのダウンロード

```console
$ wget --user=username --password=password https://secure-example.com/private/file.pdf
--2025-04-30 10:25:15--  https://secure-example.com/private/file.pdf
ユーザー名/パスワードによる認証中...
```

### 複数URLのダウンロード（ファイルからURLリストを読み込む）

```console
$ wget -i url-list.txt
--2025-04-30 10:26:40--  https://example.com/file1.zip
ファイル 'file1.zip' に保存中
--2025-04-30 10:26:45--  https://example.com/file2.zip
ファイル 'file2.zip' に保存中
```

## ヒント:

### ダウンロード速度の制限

帯域幅を節約したい場合は、`--limit-rate`オプションを使用してダウンロード速度を制限できます。
```console
$ wget --limit-rate=200k https://example.com/largefile.iso
```

### ユーザーエージェントの変更

一部のウェブサイトはブラウザからのアクセスのみを許可しています。`--user-agent`オプションでブラウザのふりをすることができます。
```console
$ wget --user-agent="Mozilla/5.0" https://example.com/restricted-file.zip
```

### 再試行回数の設定

不安定なネットワーク環境では、`--tries`オプションで再試行回数を増やすことができます。
```console
$ wget --tries=10 https://example.com/important-file.zip
```

### ダウンロード履歴の保存

`-o`オプションを使用して、ダウンロードの詳細なログを保存できます。
```console
$ wget -o download.log https://example.com/file.zip
```

## よくある質問

#### Q1. wgetとcurlの違いは何ですか？
A. `wget`は主にファイルのダウンロードに特化しており、再帰的なダウンロードやダウンロードの再開機能があります。一方、`curl`はより多くのプロトコルをサポートし、データの送信にも使用できますが、再帰的なダウンロードは標準では行いません。

#### Q2. ダウンロードが途中で中断された場合、どうすればよいですか？
A. `-c`（または`--continue`）オプションを使用すると、部分的にダウンロードされたファイルの続きからダウンロードを再開できます。

#### Q3. ウェブサイト全体をダウンロードするにはどうすればよいですか？
A. `-m`（または`--mirror`）オプションを使用します。これは`-r -N -l inf --no-remove-listing`の組み合わせと同等です。さらに`-k`（リンク変換）と`-p`（必要なファイルも取得）を追加するとオフライン閲覧に適しています。

#### Q4. HTTPSサイトの証明書エラーを無視するにはどうすればよいですか？
A. `--no-check-certificate`オプションを使用できますが、セキュリティ上のリスクがあるため注意が必要です。

## macOSでの注意点

macOSにはデフォルトで`wget`がインストールされていません。Homebrewを使用してインストールできます：

```console
$ brew install wget
```

また、macOSのセキュリティ設定によっては、ダウンロードしたファイルの実行に追加の許可が必要な場合があります。

## 参考資料

https://www.gnu.org/software/wget/manual/wget.html

## 改訂履歴

- 2025/04/30 初版作成