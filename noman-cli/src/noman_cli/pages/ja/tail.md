# tail コマンド

ファイルの末尾部分を表示します。

## 概要

`tail` コマンドはファイルの末尾（tail）部分を出力します。デフォルトでは、指定された各ファイルの最後の10行を標準出力に表示します。ログファイルの最新エントリの確認、ファイルの変更をリアルタイムで監視、またはテキストファイルの末尾を確認するのによく使用されます。

## オプション

### **-n, --lines=NUM**

デフォルトの10行ではなく、最後のNUM行を出力します

```console
$ tail -n 5 /var/log/syslog
May  3 21:45:12 hostname systemd[1]: Started Daily apt download activities.
May  3 21:45:12 hostname systemd[1]: apt-daily.service: Succeeded.
May  3 22:17:01 hostname CRON[12345]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May  3 23:17:01 hostname CRON[12346]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May  4 00:17:01 hostname CRON[12347]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
```

### **-f, --follow**

ファイルが成長するにつれて追加されたデータを出力します。ファイルの末尾を追跡します

```console
$ tail -f /var/log/syslog
May  4 00:17:01 hostname CRON[12347]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May  4 01:17:01 hostname CRON[12348]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
May  4 02:17:01 hostname CRON[12349]: (root) CMD (   cd / && run-parts --report /etc/cron.hourly)
[ファイルに追加されると、新しいエントリがリアルタイムで表示される]
```

### **-c, --bytes=NUM**

最後の10行ではなく、最後のNUMバイトを出力します

```console
$ tail -c 50 file.txt
ファイルの最後の50バイトがここに表示されます。
```

### **-q, --quiet, --silent**

ファイル名を示すヘッダーを出力しません

```console
$ tail -q file1.txt file2.txt
[ヘッダーなしで各ファイルの最後の10行を表示する]
```

## 使用例

### ログファイルをリアルタイムで監視する

```console
$ tail -f /var/log/apache2/access.log
192.168.1.1 - - [04/May/2025:10:15:32 +0000] "GET /index.html HTTP/1.1" 200 1234
192.168.1.2 - - [04/May/2025:10:15:45 +0000] "GET /images/logo.png HTTP/1.1" 200 5678
[新しいエントリが表示され続ける]
```

### 複数ファイルの最後の20行を表示する

```console
$ tail -n 20 file1.txt file2.txt
==> file1.txt <==
[file1.txtの最後の20行]

==> file2.txt <==
[file2.txtの最後の20行]
```

### 複数のファイルを同時に追跡する

```console
$ tail -f /var/log/syslog /var/log/auth.log
==> /var/log/syslog <==
[syslogの最後の10行]

==> /var/log/auth.log <==
[auth.logの最後の10行]
[両方のファイルからの新しいエントリが表示され続ける]
```

## ヒント:

### grepと組み合わせてフィルタリングする

`tail`と`grep`を組み合わせて、ログファイルから特定のエントリをフィルタリングできます：

```console
$ tail -f /var/log/syslog | grep ERROR
```

### ファイルがローテーションされても追跡を続ける

`-f`の代わりに`tail -F`（大文字のF）を使用すると、ファイルがローテーションされたり再作成されたりしても追跡を続けることができます：

```console
$ tail -F /var/log/application.log
```

### 行数を省略形で指定する

`-n`とスペースなしで数字を使用できます：

```console
$ tail -n50 file.txt
```

## よくある質問

#### Q1. `tail -f`と`tail -F`の違いは何ですか？
A. `tail -f`はファイル記述子を追跡するため、ファイルの名前が変更されると停止する場合があります。`tail -F`はファイル名を追跡し、ファイルがローテーションされたり再作成されたりしても内容の表示を継続します。

#### Q2. `tail -f`を終了するにはどうすればよいですか？
A. Ctrl+Cを押すとコマンドが終了し、プロンプトに戻ります。

#### Q3. ファイルの先頭と末尾の両方を見ることはできますか？
A. いいえ、`tail`は末尾のみを表示します。先頭を見るには`head`を使用するか、パイプで組み合わせます：`head -n 5 file.txt && tail -n 5 file.txt`。

#### Q4. 複数のログファイルを一度に監視するにはどうすればよいですか？
A. `tail -f`コマンドの後にすべてのファイルをリストするだけです：`tail -f file1.log file2.log file3.log`。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html

## 改訂履歴

- 2025/05/04 初版作成