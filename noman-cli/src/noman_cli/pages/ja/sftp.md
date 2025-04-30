# sftp コマンド

セキュアなファイル転送プロトコル（SSH File Transfer Protocol）を使用してファイルを転送します。

## 概要

`sftp`は、SSHプロトコルを使用してリモートサーバーとの間でファイルを安全に転送するためのコマンドです。FTPと似た操作性を持ちながら、通信が暗号化されるため、セキュリティが確保されます。ファイルのアップロード、ダウンロード、リモートディレクトリの操作などが可能です。

## オプション

### **-P port**

接続先のポート番号を指定します。

```console
$ sftp -P 2222 user@example.com
Connected to example.com.
sftp>
```

### **-i identity_file**

SSH認証に使用する秘密鍵ファイルを指定します。

```console
$ sftp -i ~/.ssh/my_key user@example.com
Connected to example.com.
sftp>
```

### **-b batchfile**

バッチファイルからコマンドを読み込んで実行します。

```console
$ cat commands.txt
cd /remote/dir
get important.txt
bye

$ sftp -b commands.txt user@example.com
# コマンドが自動実行される
```

### **-r**

ディレクトリを再帰的にコピーします（get/putコマンドと組み合わせて使用）。

```console
sftp> get -r remote_directory
Fetching /remote_directory/ to remote_directory
...
sftp>
```

## 使用例

### リモートサーバーへの接続

```console
$ sftp user@example.com
Connected to example.com.
sftp>
```

### ファイルのダウンロード

```console
sftp> get remote_file.txt
Fetching /home/user/remote_file.txt to remote_file.txt
/home/user/remote_file.txt                        100%  1234     1.2KB/s   00:01
sftp>
```

### ファイルのアップロード

```console
sftp> put local_file.txt
Uploading local_file.txt to /home/user/local_file.txt
local_file.txt                                    100%  2345     2.3KB/s   00:01
sftp>
```

### リモートディレクトリの操作

```console
sftp> pwd
Remote working directory: /home/user
sftp> cd documents
sftp> ls
file1.txt    file2.txt    projects/
sftp> mkdir new_folder
sftp>
```

## ヒント:

### 対話モードでのコマンド補完

sftpの対話モードでは、Tabキーを使ってコマンドやファイル名を補完できます。長いファイル名を入力する手間が省けます。

### ローカルコマンドの実行

コマンドの前に「!」をつけると、ローカルシェルでコマンドを実行できます。例えば、`!ls`でローカルディレクトリの内容を表示できます。

### 複数ファイルの転送

ワイルドカードを使用して複数のファイルを一度に転送できます。例：`get *.txt`

### 対話モードでのヘルプ表示

`help`または`?`コマンドを使用すると、利用可能なコマンドの一覧が表示されます。

## よくある質問

#### Q1. sftpとscpの違いは何ですか？
A. sftpは対話的なセッションを提供し、複数の操作を連続して行えます。一方、scpは単一のファイル転送操作に特化しています。sftpはより多機能ですが、scpはシンプルな転送には便利です。

#### Q2. sftpセッション内でファイルの権限を変更できますか？
A. はい、`chmod`コマンドを使用してリモートファイルの権限を変更できます。例：`chmod 644 file.txt`

#### Q3. 転送速度を向上させる方法はありますか？
A. `-C`オプションを使用して圧縮を有効にすると、低速ネットワークでの転送速度が向上する場合があります。また、適切な暗号化アルゴリズムを選択することも効果的です。

#### Q4. sftpセッションを終了するにはどうすればよいですか？
A. `exit`、`quit`、または`bye`コマンドを使用するか、Ctrl+Dを押すことでセッションを終了できます。

## macOSでの注意点

macOSでは、OpenSSHのバージョンが古い場合があります。最新の機能を利用するには、Homebrewなどのパッケージマネージャーを使用してOpenSSHを更新することをお勧めします。また、macOSのキーチェーンとの連携により、パスフレーズの入力を省略できる場合があります。

## 参考

https://man.openbsd.org/sftp.1

## 改訂

- 2025/04/30 初版作成