# sudo コマンド

別のユーザー（通常は管理者権限を持つユーザー）として、コマンドを実行します。

## 概要

`sudo`（superuser do）は、認可されたユーザーが別のユーザー（デフォルトではスーパーユーザー/root）のセキュリティ権限でコマンドを実行できるようにします。これにより、rootユーザーとしてログインせずに管理タスクを実行でき、特権アクセスを制限することでシステムセキュリティを向上させます。

## オプション

### **-u, --user=USER**

デフォルトのターゲットユーザー（root）以外のユーザーとしてコマンドを実行します

```console
$ sudo -u postgres psql
psql (14.5)
Type "help" for help.

postgres=#
```

### **-i, --login**

ターゲットユーザーとしてログインシェルを実行します。完全なログインをシミュレートします

```console
$ sudo -i
[root@hostname ~]#
```

### **-s, --shell**

ターゲットユーザーのパスワードデータベースエントリで指定されたシェルを実行します

```console
$ sudo -s
root@hostname:/home/user#
```

### **-l, --list**

呼び出しユーザーに許可された（および禁止された）コマンドを一覧表示します

```console
$ sudo -l
User user may run the following commands on hostname:
    (ALL : ALL) ALL
```

### **-v, --validate**

ユーザーのキャッシュされた認証情報を更新し、sudoのタイムアウトを延長します

```console
$ sudo -v
[sudo] password for user: 
```

### **-k, --reset-timestamp**

ユーザーのキャッシュされた認証情報を無効にします

```console
$ sudo -k
```

## 使用例

### root権限でコマンドを実行する

```console
$ sudo apt update
[sudo] password for user: 
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
...
```

### システム設定ファイルを編集する

```console
$ sudo nano /etc/hosts
[sudo] password for user:
```

### 別のユーザーとしてコマンドを実行する

```console
$ sudo -u www-data ls -la /var/www/html
total 16
drwxr-xr-x 2 www-data www-data 4096 May  4 10:15 .
drwxr-xr-x 3 root     root     4096 May  4 10:14 ..
-rw-r--r-- 1 www-data www-data  612 May  4 10:15 index.html
```

## ヒント:

### `sudo !!` を使用して前のコマンドをsudoで繰り返す

sudoが必要なコマンドを実行する際にsudoを付け忘れた場合、`sudo !!`と入力すると、前のコマンドをsudo権限で繰り返すことができます。

### 特定のコマンドに対してパスワードなしでsudoを設定する

`sudo visudo`でsudoersファイルを編集し、特定のコマンドをパスワードプロンプトなしで実行できるようにします。例：
```
username ALL=(ALL) NOPASSWD: /usr/bin/apt update
```

### `sudo -E`を使用して環境変数を保持する

sudoでコマンドを実行する際に現在の環境変数を保持する必要がある場合は、`-E`オプションを使用します。

### sudoersファイルの編集には常に`visudo`を使用する

`/etc/sudoers`を直接編集しないでください。常に`sudo visudo`を使用してください。これは保存前に構文エラーをチェックし、sudo権限へのアクセスをロックしてしまうことを防ぎます。

## よくある質問

#### Q1. `sudo -i`と`sudo -s`の違いは何ですか？
A. `sudo -i`は完全なログインをシミュレートし、ターゲットユーザーのホームディレクトリに移動して環境を設定します。`sudo -s`はターゲットユーザーとしてシェルを起動するだけで、現在の環境と作業ディレクトリを保持します。

#### Q2. sudo認証はどれくらいの期間有効ですか？
A. デフォルトでは、sudoは認証情報を15分間キャッシュします。`sudo -v`で延長したり、`sudo -k`でリセットしたりできます。

#### Q3. 複数のコマンドをsudoで実行するにはどうすればよいですか？
A. `sudo sh -c "command1 && command2"`を使用するか、`sudo -i`でrootシェルを起動してからコマンドを実行します。

#### Q4. ユーザーをsudoersに追加するにはどうすればよいですか？
A. Debian/Ubuntuでは`usermod -aG sudo username`でユーザーをsudoグループに追加します。RHEL/CentOSシステムではwheelグループに追加します。

## 参考資料

https://www.sudo.ws/docs/man/sudo.man/

## Revisions

- 2025/05/04 初回リビジョン