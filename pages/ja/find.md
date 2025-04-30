# find コマンド

ファイルシステム内でファイルやディレクトリを検索します。

## 概要

`find`コマンドは、指定したディレクトリ階層内でファイルやディレクトリを検索するための強力なツールです。名前、サイズ、更新日時、パーミッションなど、様々な条件に基づいて検索できます。また、検索結果に対して追加のアクションを実行することも可能です。

## オプション

### **-name パターン**

ファイル名でファイルを検索します。ワイルドカード（*、?など）が使用できます。

```console
$ find . -name "*.txt"
./documents/note.txt
./readme.txt
```

### **-iname パターン**

ファイル名で大文字・小文字を区別せずに検索します。`-name`と同様にワイルドカードが使用できます。

```console
$ find . -iname "readme*"
./README.md
./docs/readme.txt
./projects/ReadMe.rst
```

### **-type タイプ**

ファイルタイプで検索します。一般的な値は `f`（通常ファイル）、`d`（ディレクトリ）、`l`（シンボリックリンク）です。

```console
$ find . -type d
.
./documents
./images
./projects
```

### **-mtime 日数**

指定した日数以内に変更されたファイルを検索します。`-mtime -7` は7日以内に変更されたファイルを検索します。

```console
$ find . -mtime -3
./documents/report.docx
./projects/script.py
```

### **-size サイズ**

特定のサイズのファイルを検索します。`+`は「より大きい」、`-`は「より小さい」を意味します。

```console
$ find . -size +1M
./images/photo.jpg
./videos/clip.mp4
```

### **-exec コマンド {} \;**

検索結果の各ファイルに対してコマンドを実行します。`{}`は検索されたファイル名に置き換えられます。

```console
$ find . -name "*.txt" -exec cat {} \;
これはnote.txtの内容です。
これはreadme.txtの内容です。
```

## 使用例

### 大文字小文字を区別せずにファイルを検索

```console
$ find ~/Documents -iname "*report*"
/home/user/Documents/annual_Report.docx
/home/user/Documents/reports/weekly_report.pdf
/home/user/Documents/REPORT_template.xlsx
```

### 特定の拡張子を持つファイルを検索

```console
$ find /home/user -name "*.jpg"
/home/user/pictures/vacation.jpg
/home/user/documents/scan.jpg
```

### 最近変更されたファイルを検索して詳細表示

```console
$ find /var/log -mtime -1 -exec ls -l {} \;
-rw-r--r-- 1 root root 15340 4月 30 10:23 /var/log/syslog
-rw-r--r-- 1 root root 7823 4月 30 09:15 /var/log/auth.log
```

### 空のファイルを検索して削除

```console
$ find /tmp -type f -size 0 -delete
```

## ヒント:

### 大文字小文字を区別しない検索の活用

ファイル名の大文字小文字が不確かな場合は、`-iname`を使用すると便利です。特にチーム作業や異なるOSからのファイル転送時に役立ちます。

### パフォーマンスの向上

大きなディレクトリ構造を検索する場合は、検索範囲を制限するか、`-type`や`-name`などのフィルターを早めに指定すると処理が速くなります。

### 複数条件の組み合わせ

`-a`（AND、デフォルト）や`-o`（OR）、`!`（NOT）を使用して複数の検索条件を組み合わせることができます。例：`find . -name "*.txt" -a -size +1k`

### 権限エラーの回避

権限エラーを無視するには、`2>/dev/null`を追加します。例：`find / -name "config.xml" 2>/dev/null`

## よくある質問

#### Q1. `-name`と`-iname`の違いは何ですか？
A. `-name`は大文字と小文字を区別しますが、`-iname`は区別しません。例えば、`-iname "readme*"`は「README.md」や「readme.txt」などにマッチします。

#### Q2. findコマンドの基本的な構文は？
A. 基本構文は `find [検索開始パス] [検索条件] [アクション]` です。例えば `find . -name "*.txt"` は現在のディレクトリから始めて、.txtで終わるファイルを検索します。

#### Q3. 特定の日付範囲内のファイルを検索するには？
A. `-mtime`や`-newer`オプションを使用します。例えば、`find . -mtime -7 -a -mtime +1`は1日以上7日以内に変更されたファイルを検索します。

#### Q4. 検索結果を別のコマンドに渡すにはどうすればいいですか？
A. `-exec`オプションを使用するか、パイプとxargsを組み合わせます。例：`find . -name "*.txt" | xargs grep "keyword"`

## macOSでの注意点

macOSのfindコマンドはGNU findとは若干異なります。特に、`-delete`オプションの動作や正規表現の扱いが異なる場合があります。また、macOSでは`-path`オプションの代わりに`-not -path`を使用することが多いです。`-iname`オプションは両方のバージョンで同様に動作しますが、複雑な正規表現パターンを使用する場合は注意が必要です。

## 参考文献

https://www.gnu.org/software/findutils/manual/html_mono/find.html

## 改訂履歴

- 2025/04/30 -iname オプションの説明を追加し、使用例と関連するFAQを更新
- 2025/04/30 初版作成