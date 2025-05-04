# ssh-copy-id コマンド

リモートマシンの authorized keys ファイルに公開鍵をインストールします。

## 概要

`ssh-copy-id` は、SSH 公開鍵をリモートサーバーの `~/.ssh/authorized_keys` ファイルにコピーするユーティリティで、パスワードなしの SSH ログインを可能にします。このツールは、パスワード認証よりも安全な鍵ベースの認証の設定プロセスを簡素化し、ログインごとにパスワードを入力する必要をなくします。

## オプション

### **-i identity_file**

使用するアイデンティティファイル（秘密鍵）を指定します。対応する公開鍵がサーバーにコピーされます。

```console
$ ssh-copy-id -i ~/.ssh/custom_key.pub user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### **-f**

鍵がリモートサーバーに既に存在する場合でも、強制的にインストールします。

```console
$ ssh-copy-id -f user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### **-n**

実際にインストールせずに、どの鍵がインストールされるかを示すドライランを実行します。

```console
$ ssh-copy-id -n user@remote-host
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/user/.ssh/id_rsa.pub"
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
Would have added the following key(s):
ssh-rsa AAAAB3NzaC1yc2EAAA...truncated...user@local-host
```

### **-p port**

リモートホストに接続するポートを指定します。

```console
$ ssh-copy-id -p 2222 user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -p 2222 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

## 使用例

### 基本的な使用法

```console
$ ssh-copy-id user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### 特定のアイデンティティファイルを使用する

```console
$ ssh-copy-id -i ~/.ssh/id_ed25519.pub user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

### 非標準のSSHポートを使用する

```console
$ ssh-copy-id -p 2222 user@remote-host
/usr/bin/ssh-copy-id: INFO: attempting to log in with the new key(s), to filter out any that are already installed
/usr/bin/ssh-copy-id: INFO: 1 key(s) remain to be installed -- if you are prompted now it is to install the new keys
user@remote-host's password: 

Number of key(s) added: 1

Now try logging into the machine, with:   "ssh -p 2222 'user@remote-host'"
and check to make sure that only the key(s) you wanted were added.
```

## ヒント:

### 先にSSH鍵を生成する

`ssh-copy-id` を使用する前に、SSH鍵が生成されていることを確認してください。生成されていない場合は、以下のコマンドで作成できます：

```console
$ ssh-keygen -t rsa -b 4096
```

### 鍵のインストールを確認する

`ssh-copy-id` を実行した後、リモートサーバーにSSH接続を試みて設定を確認してください。パスワードの入力を求められずに接続できるはずです。

### 複数の鍵

複数のSSH鍵がある場合は、`-i` オプションを使用してインストールする公開鍵を指定してください。指定しない場合、`ssh-copy-id` は `~/.ssh` ディレクトリのデフォルトの鍵を使用します。

### リモートサーバーの要件

リモートサーバーにはSSHサーバーが実行されており、最初はパスワード認証を許可している必要があります（鍵ベースの認証を設定するため）。

## よくある質問

#### Q1. ssh-copy-id は実際に何をしますか？
A. リモートサーバーの `~/.ssh/authorized_keys` ファイルに公開SSH鍵をコピーし、鍵ベースの認証を使用したパスワードなしのSSHログインを可能にします。

#### Q2. ssh-copy-id を複数回実行する必要がありますか？
A. サーバーごとに鍵ごとに1回だけ実行する必要があります。新しい鍵を生成したり、新しいサーバーにアクセスしたりする場合は、再度実行する必要があります。

#### Q3. ssh-copy-id が失敗した場合はどうすればよいですか？
A. 一般的な問題には、リモートサーバーに `~/.ssh` ディレクトリがない（作成されます）、リモートの `~/.ssh` ディレクトリの権限が正しくない、またはサーバーでSSHパスワード認証が無効になっているなどがあります。

#### Q4. カスタムSSH設定でssh-copy-idを使用できますか？
A. はい、`ssh-copy-id` はSSH設定を使用します。`~/.ssh/config` にカスタム設定がある場合、それらが適用されます。

#### Q5. ssh-copy-idで追加した鍵を削除するにはどうすればよいですか？
A. リモートサーバーの `~/.ssh/authorized_keys` ファイルを手動で編集し、削除したい鍵を含む行を削除する必要があります。

## macOSでの注意事項

macOSでは、`ssh-copy-id` がデフォルトでインストールされていない場合があります。Homebrewを使用して `brew install ssh-copy-id` でインストールできます。または、公開鍵を手動でリモートサーバーにコピーすることもできます：

```console
$ cat ~/.ssh/id_rsa.pub | ssh user@remote-host "mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys"
```

## 参考資料

https://man.openbsd.org/ssh-copy-id

## 改訂履歴

- 2025/05/04 初版作成