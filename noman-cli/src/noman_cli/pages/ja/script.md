# script コマンド

ターミナルセッションの全入出力を記録し、タイプスクリプトファイルに保存します。

## 概要

`script` コマンドは、ターミナルでの操作内容（コマンドの入力と出力）を全て記録し、ファイルに保存するためのツールです。デフォルトでは「typescript」という名前のファイルに記録されますが、別のファイル名を指定することも可能です。このコマンドはトレーニング資料の作成、問題のデバッグ、操作手順の文書化などに役立ちます。

## オプション

### **-a, --append**

既存のファイルに追記します（上書きではなく）

```console
$ script -a session.log
Script started, output log file is 'session.log'.
$ ls
Documents  Downloads  Pictures
$ exit
Script done.
```

### **-f, --flush**

各コマンドの実行後、すぐにログファイルに書き込みます（バッファリングなし）

```console
$ script -f realtime.log
Script started, output log file is 'realtime.log'.
$ echo "このコマンドはすぐにログに書き込まれます"
このコマンドはすぐにログに書き込まれます
$ exit
Script done.
```

### **-q, --quiet**

開始・終了メッセージを表示しません

```console
$ script -q quiet.log
$ ls
Documents  Downloads  Pictures
$ exit
```

### **-t, --timing=ファイル**

タイミング情報を別ファイルに記録します

```console
$ script -t timing.log session.log
Script started, output log file is 'session.log'.
$ ls
Documents  Downloads  Pictures
$ exit
Script done.
```

## 使用例

### 基本的な使用方法

```console
$ script my_session.log
Script started, output log file is 'my_session.log'.
$ ls -la
total 20
drwxr-xr-x  2 user user 4096 Apr 30 10:00 .
drwxr-xr-x 20 user user 4096 Apr 30 09:50 ..
-rw-r--r--  1 user user  123 Apr 30 10:00 file.txt
$ echo "これはログに記録されます"
これはログに記録されます
$ exit
Script done.
```

### 記録したセッションの再生

```console
$ script -t timing.data recording.log
Script started, output log file is 'recording.log'.
$ ls
Documents  Downloads  Pictures
$ echo "Hello World"
Hello World
$ exit
Script done.

$ scriptreplay timing.data recording.log
# 記録されたセッションが再生されます
```

## ヒント:

### セッション記録の終了方法

`script` コマンドを終了するには、`exit` コマンドを入力するか、Ctrl+D を押します。これにより記録が停止し、ファイルが保存されます。

### 記録ファイルの確認

記録されたファイルは通常のテキストファイルとして `cat`、`less` などで確認できますが、エスケープシーケンスなどの制御文字が含まれているため、読みにくい場合があります。

### 自動化スクリプトでの利用

`script` コマンドは自動化スクリプトでも利用できますが、インタラクティブなプロンプトが必要な場合は `expect` などのツールと組み合わせると効果的です。

## よくある質問

#### Q1. `script` コマンドで記録したファイルのサイズが大きくなりすぎる場合はどうすればよいですか？
A. 必要な操作だけを記録するように計画し、長時間の記録は避けましょう。また、`-q` オプションを使用して開始・終了メッセージを省略することでファイルサイズを少し削減できます。

#### Q2. カラー出力も記録されますか？
A. はい、ターミナルのカラー出力を含むANSIエスケープシーケンスも記録されます。ただし、表示するときは対応するビューアが必要です。

#### Q3. 記録中に特定のコマンドだけ記録したくない場合はどうすればよいですか？
A. 一時的に `script` を終了し、記録したくないコマンドを実行した後、`script -a` で記録を再開することができます。

#### Q4. macOSでの注意点はありますか？
A. macOSの `script` コマンドはLinuxバージョンと若干異なり、一部のオプション（特に `-t` や `scriptreplay` との連携）が利用できない場合があります。詳細は `man script` で確認してください。

## 参考情報

https://man7.org/linux/man-pages/man1/script.1.html

## 改訂履歴

- 2025/04/30 初版作成