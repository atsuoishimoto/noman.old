# tail コマンド

ファイルの末尾部分を表示します。

## 概要

`tail` コマンドはファイルの末尾（最後の部分）を表示するためのコマンドです。デフォルトでは、ファイルの最後の10行を表示します。ログファイルの最新エントリの確認や、ファイルの更新をリアルタイムで監視する場合に特に便利です。

## オプション

### **-n, --lines=N**

表示する行数を指定します。

```console
$ tail -n 5 /var/log/syslog
Apr 30 10:15:22 hostname service[1234]: 処理を完了しました
Apr 30 10:15:30 hostname service[1234]: 新しいリクエストを受信しました
Apr 30 10:15:35 hostname service[1234]: 処理を開始します
Apr 30 10:15:40 hostname service[1234]: データを処理中です
Apr 30 10:15:45 hostname service[1234]: 処理が完了しました
```

### **-f, --follow**

ファイルの末尾を継続的に監視し、新しく追加された行をリアルタイムで表示します。

```console
$ tail -f /var/log/apache2/access.log
192.168.1.100 - - [30/Apr/2025:10:20:15 +0900] "GET /index.html HTTP/1.1" 200 2326
192.168.1.101 - - [30/Apr/2025:10:20:18 +0900] "GET /images/logo.png HTTP/1.1" 200 4532
192.168.1.102 - - [30/Apr/2025:10:20:20 +0900] "POST /login HTTP/1.1" 302 0
```

### **-c, --bytes=N**

最後のN バイトを表示します。

```console
$ tail -c 20 example.txt
の最後の20バイトです
```

## 使用例

### 複数ファイルの末尾を表示

```console
$ tail -n 2 file1.txt file2.txt
==> file1.txt <==
file1の最後から2行目
file1の最後の行

==> file2.txt <==
file2の最後から2行目
file2の最後の行
```

### バイト数指定で表示

```console
$ tail -c 50 large_file.txt
...ファイルの最後の50バイト分のテキストが表示される...
```

### ファイルの更新を監視

```console
$ tail -f -n 0 /var/log/syslog
# 新しく追加される行だけをリアルタイムで表示する
```

## ヒント:

### ログ監視の効率化

`tail -f` と `grep` を組み合わせることで、特定のパターンを含む新しいログエントリだけを監視できます。
```console
$ tail -f /var/log/syslog | grep ERROR
```

### 複数ファイルの監視

`tail -f` で複数のファイルを同時に監視できます。各ファイルからの出力には、そのファイル名のヘッダーが付きます。
```console
$ tail -f /var/log/syslog /var/log/auth.log
```

### 行数の代わりにプラス記号を使用

`tail +N` を使うと、N行目から最後までを表示できます。
```console
$ tail -n +100 large_file.txt
# 100行目から最後までを表示する
```

## よくある質問

#### Q1. `tail` と `head` の違いは何ですか？
A. `tail` はファイルの末尾（最後の部分）を表示するのに対し、`head` はファイルの先頭（最初の部分）を表示します。

#### Q2. `tail -f` を終了するにはどうすればいいですか？
A. `Ctrl+C` キーを押すことで、`tail -f` の実行を終了できます。

#### Q3. 特定の行から最後までを表示するにはどうすればいいですか？
A. `tail -n +N` を使用します。例えば、`tail -n +100` は100行目から最後までを表示します。

#### Q4. `tail -f` でファイルが削除されたり名前が変更されたりした場合はどうなりますか？
A. デフォルトでは監視を続けますが、`--follow=name` オプションを使うと、ファイル名に基づいて追跡するため、ログローテーションなどで名前が変わった場合に新しいファイルを追跡できます。

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html

## Revisions

- 2025/04/30 First revision