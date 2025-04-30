# sudo コマンド

他のユーザー（通常はroot）の権限でコマンドを実行します。

## 概要

`sudo`（superuser do）は、一般ユーザーが管理者（root）権限を一時的に借りてコマンドを実行するためのコマンドです。システム管理タスクやセキュリティ上の理由で制限されている操作を実行する際に使用します。パスワード認証が必要で、実行権限はシステム管理者によって`/etc/sudoers`ファイルで設定されます。

## オプション

### **-u, --user=ユーザー名**

指定したユーザーの権限でコマンドを実行します。

```console
$ sudo -u postgres psql
postgres=# \q
```

### **-i, --login**

ターゲットユーザーのログインシェルを起動します（rootユーザーになります）。

```console
$ sudo -i
# whoami
root
# exit
```

### **-s, --shell**

現在のシェル環境でrootシェルを起動します。

```console
$ sudo -s
# whoami
root
# exit
```

### **-l, --list**

現在のユーザーが実行できる`sudo`コマンドを一覧表示します。

```console
$ sudo -l
User username may run the following commands on hostname:
    (ALL) ALL
```

## 使用例

### パッケージのインストール

```console
$ sudo apt install nginx
[sudo] password for username: 
Reading package lists... Done
Building dependency tree... Done
...
```

### ファイルの編集（rootが所有するファイル）

```console
$ sudo nano /etc/hosts
[sudo] password for username: 
```

### サービスの再起動

```console
$ sudo systemctl restart nginx
[sudo] password for username: 
```

## ヒント:

### パスワード入力の省略

`sudo`コマンドを実行すると、デフォルトで5分間はパスワード入力が不要になります。連続して管理者権限が必要な作業を行う場合は効率的です。

### sudoersファイルの編集

sudoersファイルを編集する場合は、必ず`visudo`コマンドを使用してください。これにより構文エラーを防ぎ、システムがロックされるのを防ぎます。

```console
$ sudo visudo
```

### コマンドの実行履歴

`sudo`で実行したコマンドは通常ログに記録されるため、システム管理者はユーザーのアクションを追跡できます。セキュリティ上重要なコマンドを実行する際は注意しましょう。

## よくある質問

#### Q1. sudoとsuの違いは何ですか？
A. `sudo`は特定のコマンドだけを管理者権限で実行するのに対し、`su`はユーザーを完全に切り替えます。`sudo`はより安全で、実行ログが残り、rootパスワードを共有せずに済みます。

#### Q2. sudoコマンドを実行する権限がないとどうなりますか？
A. 権限がない場合、「username is not in the sudoers file. This incident will be reported.」というメッセージが表示され、コマンドは実行されません。

#### Q3. sudoコマンドでパスワードを間違えるとどうなりますか？
A. 通常3回までパスワード入力のチャンスがあり、それ以上間違えると一定時間`sudo`コマンドが使用できなくなります。

#### Q4. sudoの設定はどこで行いますか？
A. `/etc/sudoers`ファイルで設定します。ただし、直接編集せず`visudo`コマンドを使用してください。

## macOSでの注意点

macOSでは`sudo`コマンドの動作はLinuxと基本的に同じですが、管理者グループは「admin」と呼ばれます。また、macOSではセキュリティ強化のため、一部のシステムディレクトリは「System Integrity Protection (SIP)」によって保護されており、`sudo`でも変更できない場合があります。

## 参考資料

https://www.sudo.ws/docs/man/sudo.man/

## 改訂履歴

- 2025/04/30 初版作成