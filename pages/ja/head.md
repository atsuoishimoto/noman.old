# head コマンド

ファイルの先頭部分を表示します。

## 概要

`head` コマンドはファイルの先頭部分を標準出力に出力します。デフォルトでは、指定された各ファイルの最初の10行を表示します。複数のファイルが指定された場合、各ファイルの内容の前にファイル名を示すヘッダーが表示されます。

## オプション

### **-n, --lines=[-]NUM**

デフォルトの10行ではなく、最初のNUM行を表示します。先頭に「-」をつけると、各ファイルの最後のNUM行を除くすべての行を表示します。

```console
$ head -n 5 file.txt
Line 1
Line 2
Line 3
Line 4
Line 5
```

### **-c, --bytes=[-]NUM**

行数ではなく、最初のNUMバイトを表示します。先頭に「-」をつけると、各ファイルの最後のNUMバイトを除くすべてのバイトを表示します。

```console
$ head -c 20 file.txt
This is the first 20
```

### **-q, --quiet, --silent**

ファイル名を示すヘッダーを表示しません。

```console
$ head -q file1.txt file2.txt
(file1.txtの内容)
(file2.txtの内容)
```

### **-v, --verbose**

常にファイル名を示すヘッダーを表示します。

```console
$ head -v file.txt
==> file.txt <==
Line 1
Line 2
...
```

## 使用例

### ログファイルの先頭部分を確認する

```console
$ head /var/log/syslog
May  3 14:22:01 hostname systemd[1]: Starting Daily apt download activities...
May  3 14:22:01 hostname systemd[1]: apt-daily.service: Succeeded.
May  3 14:22:01 hostname systemd[1]: Finished Daily apt download activities.
...
```

### 複数のファイルを一度に表示する

```console
$ head -n 2 file1.txt file2.txt
==> file1.txt <==
First line of file1
Second line of file1

==> file2.txt <==
First line of file2
Second line of file2
```

### 最後のN行を除くすべての行を表示する

```console
$ head -n -2 file.txt
Line 1
Line 2
Line 3
...
(最後の2行を除くすべての行)
```

## ヒント:

### 他のコマンドと組み合わせる

`head`をパイプと組み合わせて、他のコマンドの出力を制限できます：

```console
$ ls -l | head -n 5
```

これにより、ディレクトリリストの最初の5エントリのみが表示される。

### 大きなファイルの先頭部分を確認する

非常に大きなファイルの場合、ファイル全体をロードせずに内容をプレビューするために`head`を使用できます：

```console
$ head -n 20 huge_log.txt
```

### tailと組み合わせて中間部分を抽出する

`head`と`tail`を組み合わせて、ファイルの中間部分を抽出できます：

```console
$ head -n 20 file.txt | tail -n 10
```

これにより、ファイルの11〜20行目が表示される。

## よくある質問

#### Q1. ファイルから特定の行数を表示するにはどうすればよいですか？
A. `head -n 数字 ファイル名`を使用して、最初の指定した行数を表示できます。

#### Q2. headで複数のファイルを一度に表示できますか？
A. はい、すべてのファイル名をリストするだけです：`head file1.txt file2.txt file3.txt`

#### Q3. 行ではなく最初の数バイトを表示するにはどうすればよいですか？
A. `head -c 数字 ファイル名`を使用して、最初の指定したバイト数を表示できます。

#### Q4. 最後の数行を除くすべての行を表示するにはどうすればよいですか？
A. `head -n -数字 ファイル名`を使用して、最後の指定した行数を除くすべての行を表示できます。

#### Q5. 複数のファイルを表示する際にファイル名のヘッダーを非表示にするにはどうすればよいですか？
A. `-q`オプションを使用します：`head -q file1.txt file2.txt`

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html

## 改訂履歴

2025/05/04 初版作成