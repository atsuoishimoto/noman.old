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

### 特定のユーザーが所有するファイルを検索

```console
$ find /home -user username
/home/username
/home/username/.bashrc
/home/username/documents
```

## ヒント:

### パフォーマンスの向上

大きなディレクトリ構造を検索する場合は、検索範囲を制限するか、`-type`や`-name`などのフィルターを早めに指定すると処理が速くなります。

### 複数条件の組み合わせ

`-a`（AND、デフォルト）や`-o`（OR）、`!`（NOT）を使用して複数の検索条件を組み合わせることができます。例：`find . -name "*.txt" -a -size +1k`

### 権限エラーの回避

権限エラーを無視するには、`2>/dev/null`を追加します。例：`find / -name "config.xml" 2>/dev/null`

### 検索結果の処理

`-exec`の代わりに、パイプとxargsを使用することもできます：`find . -name "*.log" | xargs grep "error"`

## よくある質問

#### Q1. findコマンドの基本的な構文は？
A. 基本構文は `find [検索開始パス] [検索条件] [アクション]` です。例えば `find . -name "*.txt"` は現在のディレクトリから始めて、.txtで終わるファイルを検索します。

#### Q2. 特定の日付範囲内のファイルを検索するには？
A. `-mtime`や`-newer`オプションを使用します。例えば、`find . -mtime -7 -a -mtime +1`は1日以上7日以内に変更されたファイルを検索します。

#### Q3. 検索結果を別のコマンドに渡すにはどうすればいいですか？
A. `-exec`オプションを使用するか、パイプとxargsを組み合わせます。例：`find . -name "*.txt" | xargs grep "keyword"`

#### Q4. 検索から特定のディレクトリを除外するには？
A. `-path "./dir" -prune -o`を使用します。例：`find . -path "./node_modules" -prune -o -name "*.js" -print`

## macOSでの注意点

macOSのfindコマンドはGNU findとは若干異なります。特に、`-delete`オプションの動作や正規表現の扱いが異なる場合があります。また、macOSでは`-path`オプションの代わりに`-not -path`を使用することが多いです。

## 参考文献

https://www.gnu.org/software/findutils/manual/html_mono/find.html

## 改訂履歴

- 2025/04/30 初版作成