# head コマンド

ファイルの先頭部分を表示します。

## 概要

`head` コマンドはファイルの先頭から指定した行数（デフォルトでは10行）を表示するためのコマンドです。大きなファイルの内容を確認する際や、ファイルの構造を素早く把握したい場合に便利です。複数のファイルを指定すると、それぞれのファイルの先頭部分を順番に表示します。

## オプション

### **-n, --lines=N**

表示する行数を指定します。Nは表示したい行数です。

```console
$ head -n 3 /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
```

### **-c, --bytes=N**

表示するバイト数を指定します。Nは表示したいバイト数です。

```console
$ head -c 20 /etc/passwd
root:x:0:0:root:/ro
```

### **-q, --quiet, --silent**

複数ファイルを処理する際にファイル名のヘッダーを表示しません。

```console
$ head -q -n 1 file1.txt file2.txt
これはfile1.txtの1行目です
これはfile2.txtの1行目です
```

## 使用例

### 基本的な使用方法

```console
$ head /etc/passwd
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
```

### 複数ファイルの先頭を表示

```console
$ head -n 2 file1.txt file2.txt
==> file1.txt <==
これはfile1.txtの1行目です
これはfile1.txtの2行目です

==> file2.txt <==
これはfile2.txtの1行目です
これはfile2.txtの2行目です
```

### パイプラインでの使用

```console
$ ls -l | head -n 5
total 120
drwxr-xr-x  2 user user 4096 Apr 30 10:00 Desktop
drwxr-xr-x  2 user user 4096 Apr 30 10:00 Documents
drwxr-xr-x  2 user user 4096 Apr 30 10:00 Downloads
drwxr-xr-x  2 user user 4096 Apr 30 10:00 Music
```

## ヒント:

### 負の行数を指定する

`head -n -N` を使用すると、ファイルの最後のN行を除いた全ての行を表示できます。

```console
$ head -n -2 file.txt
# file.txtの最後の2行を除いた全ての行が表示される
```

### 大きなログファイルの確認

ログファイルの最新の状態を確認するには、`tail` コマンドの方が適していますが、ログの初期部分を確認するには `head` が便利です。

```console
$ head /var/log/syslog
# システムログの先頭10行が表示される
```

### 複数ファイルの処理

複数のファイルを処理する際、各ファイルの先頭にファイル名が表示されます。これを抑制するには `-q` オプションを使用します。

## よくある質問

#### Q1. `head` と `tail` の違いは何ですか？
A. `head` はファイルの先頭部分を表示し、`tail` はファイルの末尾部分を表示します。

#### Q2. デフォルトで表示される行数を変更できますか？
A. はい、`-n` オプションで行数を指定できます。例えば `head -n 20` は先頭20行を表示します。

#### Q3. 標準入力からデータを読み取ることはできますか？
A. はい、パイプラインを使用して標準入力からデータを読み取ることができます。例：`cat file.txt | head -n 5`

#### Q4. macOSとLinuxで `head` コマンドに違いはありますか？
A. 基本的な機能は同じですが、一部のオプションや動作が異なる場合があります。特に `-c` オプションの解釈が異なることがあります。

## 参考

https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html

## 改訂履歴

- 2025/04/30 初版作成