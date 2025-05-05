# egrep コマンド

テキスト内で拡張正規表現を使用してパターンを検索します。

## 概要

`egrep` はパターンマッチングツールで、ファイルや標準入力から指定されたパターンに一致する行を検索します。機能的には `grep -E` と同等で、基本的な grep よりも強力なパターンマッチング機能を提供する拡張正規表現を使用します。このコマンドは、コード、ログ、テキストファイルの検索によく使用されます。

## オプション

### **-i, --ignore-case**

大文字と小文字を区別せずにマッチングを行います

```console
$ egrep -i "error" logfile.txt
ERROR: Connection failed
error: file not found
Warning: Some errors were detected
```

### **-v, --invert-match**

一致しない行を選択します

```console
$ egrep -v "success" logfile.txt
ERROR: Connection failed
Warning: operation incomplete
Process terminated unexpectedly
```

### **-c, --count**

一致する行の数だけを表示します

```console
$ egrep -c "error" logfile.txt
3
```

### **-n, --line-number**

出力の各行の前に入力ファイル内の行番号を付けます

```console
$ egrep -n "error" logfile.txt
5:error: file not found
12:error: permission denied
27:error: timeout occurred
```

### **-l, --files-with-matches**

一致を含むファイル名のみを表示します

```console
$ egrep -l "error" *.log
app.log
system.log
error.log
```

### **-r, --recursive**

各ディレクトリ下のすべてのファイルを再帰的に読み込みます

```console
$ egrep -r "password" /home/user/
/home/user/config.txt:password=12345
/home/user/notes/secret.txt:my password hint
```

## 使用例

### 拡張正規表現の使用

```console
$ egrep "(error|warning)" logfile.txt
error: file not found
warning: disk space low
error: permission denied
```

### 複数のパターンのマッチング

```console
$ egrep "user[0-9]+" users.txt
user123 logged in at 14:30
user456 account created
user789 password changed
```

### オプションの組み合わせ

```console
$ egrep -in "fail(ed|ure)" *.log
app.log:15:Connection failed to server
system.log:42:System failure detected
network.log:7:Authentication failed for user admin
```

## ヒント:

### 単語境界を使用して正確なマッチングを行う

より正確な結果を得るために `\b` を使用して単語境界にマッチさせます：

```console
$ egrep "\berror\b" logfile.txt
```

これは "error" にマッチしますが、"errors" や "errorless" にはマッチしません。

### マッチを色付けして視認性を向上させる

最近の egrep の実装では自動的にマッチを色付けしますが、以下のコマンドで確実に色付けできます：

```console
$ egrep --color "pattern" file.txt
```

### egrep は grep -E と同等であることを覚えておく

`egrep` は一部のシステムでは非推奨となり、代わりに `grep -E` が推奨されています。両者は同じ機能を持ちますが、`grep -E` の方が移植性が高いです。

## よくある質問

#### Q1. grep と egrep の違いは何ですか？
A. `egrep` はデフォルトで拡張正規表現を使用し、これは `grep -E` と同等です。拡張正規表現の構文では、`+`、`?`、`|`、`()` などの特殊文字をエスケープせずに使用できます。

#### Q2. 複数のファイルでパターンを検索するにはどうすればよいですか？
A. パターンの後にファイルを列挙するだけです：`egrep "pattern" file1.txt file2.txt` またはワイルドカードを使用します：`egrep "pattern" *.txt`。

#### Q3. 検索から特定のパターンを除外するにはどうすればよいですか？
A. `-v` オプションを使用します：`egrep -v "除外するパターン" file.txt`。

#### Q4. egrep は圧縮ファイルを検索できますか？
A. 直接はできません。圧縮ファイルの場合、gzip 圧縮ファイル用の `zgrep` などの専用ツールを使用してください。

## 参照

https://www.gnu.org/software/grep/manual/grep.html

## 改訂履歴

- 2025/05/04 初版作成