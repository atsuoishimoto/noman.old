# find コマンド

ディレクトリ階層内でファイルを検索します。

## 概要

`find` コマンドは、名前、タイプ、サイズ、更新時間などの様々な条件に基づいて、ディレクトリ階層内のファイルを検索するツールです。ファイルを見つけ出し、一致した結果に対して操作を実行するための強力なツールです。

## オプション

### **-iname パターン**

大文字と小文字を区別せずに、名前がパターンに一致するファイルを検索します。これは `-name` に似ていますが、大文字小文字を区別しない検索を行います。

```console
$ find . -iname "*.txt"
./notes.txt
./Documents/README.txt
./Documents/report.TXT
```

### **-name パターン**

大文字と小文字を区別して、名前がパターンに一致するファイルを検索します。

```console
$ find . -name "*.txt"
./notes.txt
./Documents/README.txt
```

### **-type タイプ**

特定のタイプのファイルを検索します。一般的なタイプには以下があります：
- `f` は通常のファイル
- `d` はディレクトリ
- `l` はシンボリックリンク

```console
$ find . -type d
.
./Documents
./Downloads
./Pictures
```

### **-size n[cwbkMG]**

サイズに基づいてファイルを検索します：
- `c` はバイト単位
- `k` はキロバイト単位
- `M` はメガバイト単位
- `G` はギガバイト単位
- `+` 接頭辞は「より大きい」を意味します
- `-` 接頭辞は「より小さい」を意味します

```console
$ find . -size +10M
./Videos/movie.mp4
./Downloads/installer.iso
```

### **-mtime n**

n日前に変更されたファイルを検索します。`+n` は「n日より前」、`-n` は「n日以内」を意味します。

```console
$ find . -mtime -7
./Documents/recent-report.txt
./Downloads/recent-file.zip
```

## 使用例

### 特定の権限を持つファイルを検索する

```console
$ find /home -type f -perm 644
/home/user/file1.txt
/home/user/file2.txt
```

### 一致するファイルに対してコマンドを実行する

```console
$ find . -name "*.log" -exec rm {} \;
```

### 空のファイルを検索する

```console
$ find /var/log -type f -empty
/var/log/empty.log
```

### 過去24時間以内に変更されたファイルを検索する

```console
$ find /home/user -type f -mtime -1
/home/user/recent-document.txt
/home/user/today-notes.md
```

## ヒント:

### 大文字小文字を区別しない検索には `-iname` を使用する

ファイル名の正確な大文字小文字が不明な場合は、`-name` の代わりに `-iname` を使用して、大文字小文字に関係なくファイルを一致させることができます。

### 論理演算子で複数の条件を組み合わせる

`-and`、`-or`、`-not`（または `!`）を使用して複雑な検索条件を作成できます：
```console
$ find . -type f -name "*.txt" -and -size +1M
```

### `-maxdepth` でディレクトリの深さを制限する

`-maxdepth` を使用して `find` の検索深度を制御できます：
```console
$ find . -maxdepth 2 -name "*.jpg"
```

### エラーメッセージをリダイレクトする

「Permission denied」エラーを非表示にするには `2>/dev/null` を使用します：
```console
$ find / -name "config.xml" 2>/dev/null
```

## よくある質問

#### Q1. 名前でファイルを検索するにはどうすればよいですか？
A. 大文字小文字を区別する検索には `find /検索パス -name "ファイル名"` を、大文字小文字を区別しない検索には `find /検索パス -iname "ファイル名"` を使用します。

#### Q2. 最近変更されたファイルを検索するにはどうすればよいですか？
A. `find /検索パス -mtime -n` を使用します。nは日数です。例えば、`-mtime -7` は過去7日以内に変更されたファイルを検索します。

#### Q3. ファイルを検索して削除するにはどうすればよいですか？
A. `find /検索パス -name "パターン" -delete` または `find /検索パス -name "パターン" -exec rm {} \;` を使用します。

#### Q4. 検索からディレクトリを除外するにはどうすればよいですか？
A. `! -path "*/除外するディレクトリ/*"` または `-not -path "*/除外するディレクトリ/*"` を使用します。

## 参考資料

https://www.gnu.org/software/findutils/manual/html_node/find_html/index.html

## 改訂履歴

- 2025/05/04 初回改訂