# su コマンド

ユーザーIDを切り替えたり、一時的に別のユーザーになったりします。

## 概要

`su` コマンドは、別のユーザーアカウント（最も一般的にはroot）に切り替えることができます。ユーザー名を指定しない場合、`su` はデフォルトでスーパーユーザー（root）になります。対象ユーザーの環境と権限を持つ新しいシェルを作成します。

## オプション

### **-** または **-l**, **--login**

指定したユーザーの直接ログインをシミュレートするログイン環境を提供します

```console
$ su - john
Password: 
john@hostname:~$
```

### **-c**, **--command=COMMAND**

指定したユーザーとして単一のコマンドを実行し、その後終了します

```console
$ su -c "ls -la /root" root
Password: 
total 28
drwx------  4 root root 4096 May  4 10:15 .
drwxr-xr-x 20 root root 4096 Apr 15 09:30 ..
-rw-------  1 root root  982 May  1 14:22 .bash_history
-rw-r--r--  1 root root 3106 Dec  5  2024 .bashrc
drwxr-xr-x  3 root root 4096 Jan 10  2025 .config
-rw-r--r--  1 root root  161 Dec  5  2024 .profile
drwx------  2 root root 4096 Feb 20  2025 .ssh
```

### **-s**, **--shell=SHELL**

ユーザーのデフォルトシェルの代わりに指定したシェルを実行します

```console
$ su -s /bin/zsh john
Password: 
john@hostname:~$
```

### **-p**, **--preserve-environment**

ユーザーを切り替える際に現在の環境変数を保持します

```console
$ su -p john
Password: 
john@hostname:/current/directory$
```

## 使用例

### rootユーザーになる

```console
$ su
Password: 
root@hostname:/home/user#
```

### rootとしてコマンドを実行し、通常のユーザーに戻る

```console
$ su -c "apt update && apt upgrade -y" root
Password: 
[apt updateとupgradeの出力]
$
```

### 別のユーザーに環境ごと切り替える

```console
$ su - john
Password: 
john@hostname:~$
```

## ヒント:

### 可能な限り sudo を使用する

ほとんどの管理タスクでは、`su` よりも `sudo command` を使用する方が望ましいです：
- 実行されたすべてのコマンドが記録される
- rootパスワードの共有が不要
- より細かい権限制御が可能

### スーパーユーザーシェルを安全に終了する

スーパーユーザーシェルの使用が終わったら、必ず `exit` と入力するか Ctrl+D を押して通常のユーザーアカウントに戻りましょう。

### 環境変数の扱いに注意する

単純な `su`（`-` なし）を使用すると、現在の環境変数が保持され、予期しない動作を引き起こす可能性があります。クリーンな環境を得るには `su -` を使用してください。

## よくある質問

#### Q1. `su` と `sudo` の違いは何ですか？
A. `su` はユーザーセッション全体を別のユーザー（通常はroot）に切り替えますが、`sudo` は単一のコマンドを昇格した権限で実行し、その後通常のユーザーに戻ります。

#### Q2. なぜ `su` が「認証失敗」で失敗することがありますか？
A. これは通常、rootアカウントのパスワードが間違っているか、rootアカウントがロックされている（Ubuntuなどsudoを優先するディストリビューションでは一般的）ためです。

#### Q3. suセッションを終了するにはどうすればよいですか？
A. `exit` と入力するか Ctrl+D を押すと、元のユーザーアカウントに戻ります。

#### Q4. `su` と `su -` の違いは何ですか？
A. `su` はユーザーIDのみを変更し、現在の環境変数と作業ディレクトリを保持します。`su -` は新しいユーザーの完全なログイン環境を提供し、そのホームディレクトリに移動してプロファイルを読み込みます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/su-invocation.html

## 改訂履歴

- 2025/05/04 初版作成