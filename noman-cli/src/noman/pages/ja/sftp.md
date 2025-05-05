# sftp コマンド

暗号化された接続を介してホスト間でファイルを安全に転送します。

## 概要

SFTP（Secure File Transfer Protocol）は、コンピュータ間でファイルを安全に転送するためのネットワークプロトコルです。SSH上で動作し、暗号化と認証を提供します。`sftp`コマンドはFTPに似た対話型のファイル転送プログラムですが、SSH暗号化を使用しています。

## オプション

### **-b** / **--batch** *バッチファイル*

対話的に実行する代わりに、sftpコマンドのバッチファイルを処理します。

```console
$ sftp -b commands.txt user@remote.server
Connecting to remote.server...
Batch file commands.txt processed
```

### **-P** / **--port** *ポート*

リモートホストに接続するポートを指定します。

```console
$ sftp -P 2222 user@remote.server
Connecting to remote.server port 2222...
sftp>
```

### **-i** / **--identity** *アイデンティティファイル*

公開鍵認証に使用するアイデンティティ（秘密鍵）を読み込むファイルを選択します。

```console
$ sftp -i ~/.ssh/my_key user@remote.server
Connecting to remote.server...
sftp>
```

### **-r** / **--recursive**

アップロードまたはダウンロード時にディレクトリ全体を再帰的にコピーします。

```console
$ sftp user@remote.server
sftp> get -r remote_directory
Fetching /remote_directory/ to remote_directory
sftp>
```

### **-v** / **--verbose**

ログレベルを上げ、詳細なデバッグ出力を提供します。

```console
$ sftp -v user@remote.server
OpenSSH_8.9p1, LibreSSL 3.3.6
debug1: Reading configuration data /etc/ssh/ssh_config
debug1: Connecting to remote.server port 22.
...
sftp>
```

## 使用例

### リモートサーバーへの接続

```console
$ sftp user@remote.server
Connected to remote.server.
sftp>
```

### ファイルのダウンロード

```console
$ sftp user@remote.server
sftp> get remote_file.txt
Fetching /home/user/remote_file.txt to remote_file.txt
sftp>
```

### ファイルのアップロード

```console
$ sftp user@remote.server
sftp> put local_file.txt
Uploading local_file.txt to /home/user/local_file.txt
sftp>
```

### ディレクトリの移動

```console
$ sftp user@remote.server
sftp> pwd
Remote working directory: /home/user
sftp> cd documents
sftp> lpwd
Local working directory: /Users/localuser
sftp> lcd Downloads
```

## ヒント:

### タブ補完を使用する

SFTPはローカルとリモートの両方のファイルに対してタブ補完をサポートしており、完全なパスを入力せずに簡単にナビゲートできます。

### 対話的なコマンド

- `ls` - リモートファイルを一覧表示する
- `lls` - ローカルファイルを一覧表示する
- `cd` - リモートディレクトリを変更する
- `lcd` - ローカルディレクトリを変更する
- `mkdir` - リモートディレクトリを作成する
- `rmdir` - リモートディレクトリを削除する
- `rm` - リモートファイルを削除する
- `help`または`?` - 利用可能なコマンドを表示する

### 自動化のためのバッチモード

sftpコマンドを含むテキストファイルを作成し、スクリプトでの自動転送には`-b`オプションを使用します。

### 複数のファイルにワイルドカードを使用する

```console
sftp> get *.txt
```

## よくある質問

#### Q1. SFTPとSCPの違いは何ですか？
A. SFTPはSSH上で動作する対話型のファイル転送プロトコルであるのに対し、SCPは安全なコピーのための非対話型コマンドです。SFTPは転送の再開やディレクトリ一覧表示などの機能を提供します。

#### Q2. ディレクトリ全体を転送するにはどうすればよいですか？
A. getまたはputコマンドで`-r`（再帰的）オプションを使用します：`get -r remote_directory`または`put -r local_directory`。

#### Q3. スクリプトでSFTPを使用できますか？
A. はい、SFTPコマンドを含むバッチファイルと共に`-b`オプションを使用します：`sftp -b commands.txt user@remote.server`。

#### Q4. リモートファイルの権限を変更するにはどうすればよいですか？
A. SFTPセッション内で`chmod`コマンドを使用します：`chmod 644 remote_file.txt`。

#### Q5. 中断されたファイル転送を再開するにはどうすればよいですか？
A. ファイルのダウンロードを再開するには`reget`コマンドを、アップロードを再開するには`reput`コマンドを使用します。

## 参考文献

https://man.openbsd.org/sftp.1

## 改訂履歴

- 2025/05/04 初回改訂