# find コマンド

ファイルシステム内でファイルやディレクトリを検索し、条件に基づいて見つけ出します。

## 概要

`find`コマンドは、ファイルシステム内でファイルやディレクトリを検索するための強力なツールです。ファイル名、サイズ、更新日時などの様々な条件に基づいて検索でき、さらに見つかったファイルに対して操作を実行することもできます。日常的なファイル管理から複雑なシステム管理まで幅広く活用できます。

## オプション

### **-name**

ファイル名で検索します（大文字小文字を区別）

```console
$ find . -name "*.txt"
./documents/memo.txt
./notes.txt
./archive/old_notes.txt
```

### **-iname**

ファイル名で検索します（大文字小文字を区別しない）

```console
$ find . -iname "README*"
./README.md
./projects/readme.txt
./docs/ReadMe.rst
```

### **-type**

ファイルタイプで検索します

```console
$ find . -type d
.
./documents
./photos
./projects
```

### **-size**

ファイルサイズで検索します

```console
$ find . -size +1M
./videos/tutorial.mp4
./images/background.png
./archives/backup.zip
```

### **-mtime**

更新時間に基づいて検索します

```console
$ find . -mtime -7
./documents/recent_report.pdf
./notes.txt
./downloads/latest.zip
```

### **-exec**

見つかったファイルに対してコマンドを実行します

```console
$ find . -name "*.log" -exec rm {} \;
```

### **-maxdepth**

検索する深さを制限します

```console
$ find . -maxdepth 1 -name "*.txt"
./notes.txt
./todo.txt
```

## 使用例

### 複数条件での検索

```console
$ find /home/user -type f -size +5M -mtime -30
/home/user/videos/family.mp4
/home/user/documents/presentation.pptx
```

### 検索結果に対する操作

```console
$ find . -name "*.jpg" -exec convert {} {}.png \;
```

### 権限に基づく検索

```console
$ find /etc -type f -perm 644
/etc/hosts
/etc/resolv.conf
```

### 空のファイルやディレクトリの検索

```console
$ find /tmp -empty
/tmp/empty_dir
/tmp/test.log
```

## ヒント:

### エラーメッセージを非表示にする

権限のないディレクトリでの検索エラーを無視するには、`2>/dev/null`を追加します。これにより、エラーメッセージが表示されなくなります。

```console
$ find / -name "config.xml" 2>/dev/null
```

### 効率的な-execの使用

大量のファイルを扱う場合、`-exec command {} \;`の代わりに`-exec command {} \+`を使用すると効率的です。これにより、複数のファイルを一度にコマンドに渡すことができます。

```console
$ find . -name "*.txt" -exec grep "keyword" {} \+
```

### 複雑な条件の組み合わせ

論理演算子（`-and`、`-or`、`-not`）を使って複雑な検索条件を作成できます。

```console
$ find . -name "*.log" -size +1M -and -mtime +30
```

## よくある質問

#### Q1. findコマンドの基本的な構文は？

A. 基本構文は `find [検索開始パス] [検索条件] [アクション]` です。例えば `find . -name "*.txt"` はカレントディレクトリ以下の全ての.txtファイルを検索します。

#### Q2. 特定の日付範囲内のファイルを検索するには？

A. `-mtime`オプションを使用します。例えば、7日以内に更新されたファイルは `find . -mtime -7`、7日以上前に更新されたファイルは `find . -mtime +7` で検索できます。

#### Q3. 検索結果をファイルに保存するには？

A. リダイレクトを使用します：`find . -name "*.jpg" > image_files.txt`

#### Q4. 特定のディレクトリを検索から除外するには？

A. `-path`と`-prune`を組み合わせます：`find . -path "./node_modules" -prune -o -name "*.js" -print`

## macOSでの注意点

macOSのfindコマンドはGNU findとは若干異なります。特に、`-path`や`-regex`の動作が異なる場合があります。また、macOSでは`-maxdepth`などの一部のオプションが標準でサポートされていない場合があります。代わりに`brew install findutils`でGNU findをインストールし、`gfind`として使用することも検討してください。

## 参考資料

https://www.gnu.org/software/findutils/manual/html_node/find_html/index.html

## 改訂履歴

- 2025/04/30 macOSでの注意点を追加、よくある質問を拡充、ヒントセクションを改善
- 2025/01/01 初版作成