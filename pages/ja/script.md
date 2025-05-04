# script コマンド

ターミナルセッションの全アクティビティを記録し、タイプスクリプトを作成します。

## 概要

`script` コマンドはターミナルセッション中に表示されるすべての内容を記録します。すべての入力と出力をキャプチャし、ファイル（デフォルトでは「typescript」という名前）に保存します。これは手順の文書化、チュートリアルの作成、またはターミナルセッションのログを保持するのに役立ちます。

## オプション

### **-a, --append**

指定したファイルまたはデフォルトの typescript ファイルに出力を上書きではなく追記します。

```console
$ script -a session_log.txt
Script started, output file is session_log.txt
$ ls
Documents Downloads Pictures
$ exit
Script done, output file is session_log.txt
```

### **-f, --flush**

各書き込み後に出力をフラッシュして、リアルタイム記録を確保します。記録中に typescript ファイルを監視する場合に便利です。

```console
$ script -f realtime_log.txt
Script started, output file is realtime_log.txt
$ echo "これはすぐにフラッシュされます"
これはすぐにフラッシュされます
$ exit
Script done, output file is realtime_log.txt
```

### **-q, --quiet**

静かモードで実行し、開始および終了メッセージを表示しません。

```console
$ script -q quiet_log.txt
$ echo "開始メッセージは表示されていません"
開始メッセージは表示されていません
$ exit
```

### **-t, --timing[=FILE]**

タイミングデータを FILE に出力します。FILE が指定されていない場合は標準エラーに出力します。これは scriptreplay でセッションを再生する際に使用できます。

```console
$ script -t timing.log session.log
Script started, output file is session.log
$ echo "このセッションは時間計測されています"
このセッションは時間計測されています
$ exit
Script done, output file is session.log
```

### **-c, --command COMMAND**

対話型シェルの代わりに指定されたコマンドを実行します。

```console
$ script -c "ls -la" command_output.txt
Script started, output file is command_output.txt
total 32
drwxr-xr-x  5 user  staff   160 May  4 10:15 .
drwxr-xr-x  3 user  staff    96 May  4 10:10 ..
-rw-r--r--  1 user  staff  1024 May  4 10:12 file1.txt
-rw-r--r--  1 user  staff  2048 May  4 10:14 file2.txt
Script done, output file is command_output.txt
```

## 使用例

### 基本的なセッション記録

```console
$ script my_session.txt
Script started, output file is my_session.txt
$ ls
Documents Downloads Pictures
$ pwd
/home/user
$ exit
Script done, output file is my_session.txt
```

### 記録されたセッションの表示

```console
$ cat my_session.txt
Script started on Sun May  4 10:20:00 2025
$ ls
Documents Downloads Pictures
$ pwd
/home/user
$ exit

Script done on Sun May  4 10:21:30 2025
```

### セッションの記録と再生

```console
$ script --timing=timing.log session.log
Script started, output file is session.log
$ echo "こんにちは、これはデモです"
こんにちは、これはデモです
$ ls
Documents Downloads Pictures
$ exit
Script done, output file is session.log

$ scriptreplay timing.log session.log
# セッションが元のタイミングで再生されます
```

## ヒント:

### scriptreplay との併用

`-t` オプションを使用してタイミング情報を記録すると、後で `scriptreplay` コマンドでセッションを再生できます。これにより、元々入力されたのと同じペースで出力が表示されます。

### 制御文字のクリーンアップ

typescript ファイルには読みにくい制御文字が含まれている場合があります。`col -b` のようなツールを使用してクリーンアップできます：

```console
$ col -b < my_session.txt > clean_session.txt
```

### 複雑な手順の文書化

複雑なシステム管理タスクやソフトウェアインストールを文書化する際に `script` を使用すると、後で参照したり同僚と共有したりできる完全な記録を作成できます。

## よくある質問

#### Q1. script セッションの記録を停止するにはどうすればよいですか？
A. `exit` と入力するか、Ctrl+D を押してセッションを終了し、記録を停止します。

#### Q2. 開始と終了のメッセージを表示せずにセッションを記録できますか？
A. はい、`-q` または `--quiet` オプションを使用してこれらのメッセージを抑制できます。

#### Q3. 記録されたセッションを再生するにはどうすればよいですか？
A. `-t` を使用してタイミング情報を記録した場合、`scriptreplay` コマンドを使用してセッションを再生できます。

#### Q4. 入力したパスワードは記録されますか？
A. いいえ、適切に設計されたパスワードプロンプトは文字をターミナルにエコーしないため、通常パスワードは typescript ファイルに表示されません。

#### Q5. 既存の typescript ファイルに追記できますか？
A. はい、`-a` または `--append` オプションを使用して、既存のファイルを上書きするのではなく追加できます。

## 参考資料

https://man7.org/linux/man-pages/man1/script.1.html

## 改訂履歴

- 2025/05/04 初版作成