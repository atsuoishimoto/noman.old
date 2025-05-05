# gpasswd コマンド

グループのメンバーシップと認証情報を `/etc/group` および `/etc/gshadow` ファイルで管理します。

## 概要

`gpasswd` は Linux システムでグループを管理するためのコマンドです。管理者はこのコマンドを使用して、ユーザーをグループに追加または削除したり、グループパスワードを設定したり、グループ管理者とメンバーを指定したりすることができます。このコマンドは `/etc/group` および `/etc/gshadow` ファイルに保存されている情報を管理します。

## オプション

### **-a, --add** *ユーザー名*

指定したグループにユーザーを追加します。

```console
$ sudo gpasswd -a john developers
Adding user john to group developers
```

### **-d, --delete** *ユーザー名*

指定したグループからユーザーを削除します。

```console
$ sudo gpasswd -d john developers
Removing user john from group developers
```

### **-r, --remove-password**

指定したグループからパスワードを削除します。

```console
$ sudo gpasswd -r developers
Removing password from group developers
```

### **-R, --restrict**

グループへのアクセスをそのメンバーのみに制限します。

```console
$ sudo gpasswd -R developers
```

### **-A, --administrators** *ユーザー1,ユーザー2,...*

グループの管理者リストを設定します。

```console
$ sudo gpasswd -A jane,mike developers
```

### **-M, --members** *ユーザー1,ユーザー2,...*

グループのメンバーリストを設定します。

```console
$ sudo gpasswd -M john,jane,mike developers
```

## 使用例

### ユーザーをグループに追加する

```console
$ sudo gpasswd -a username groupname
Adding user username to group groupname
```

### グループパスワードを設定する

```console
$ sudo gpasswd developers
Changing the password for group developers
New Password: 
Re-enter new password: 
```

### グループに複数の管理者を設定する

```console
$ sudo gpasswd -A user1,user2,user3 groupname
```

### グループからすべてのメンバーを削除する

```console
$ sudo gpasswd -M "" groupname
```

## ヒント:

### グループメンバーシップの確認

`groups` コマンドを使用して、ユーザーがどのグループに所属しているかを確認できます：

```console
$ groups username
```

### グループ情報の表示

`/etc/group` ファイルにはグループ情報が含まれています。以下のコマンドで確認できます：

```console
$ cat /etc/group | grep groupname
```

### グループ管理のワークフロー

新しいプロジェクトチームを設定する場合、まず `groupadd` でグループを作成し、次に `gpasswd -a` でメンバーを追加するか、`gpasswd -M` ですべてのメンバーを一度に設定します。

## よくある質問

#### Q1. `gpasswd` と `usermod -G` の違いは何ですか？
A. `gpasswd` はグループ管理専用に設計されており、グループ管理者やパスワードを設定できます。`usermod -G` はユーザーをグループに追加できますが、`-a` オプションを使用しない限り、既存のすべてのグループメンバーシップが置き換えられます。

#### Q2. 一般ユーザーは `gpasswd` を使用できますか？
A. 一般ユーザーは `-A` オプションでグループ管理者に指定された場合のみ `gpasswd` を使用できますが、その場合でも機能は制限されています。

#### Q3. グループパスワードを削除するにはどうすればよいですか？
A. `gpasswd -r グループ名` を使用してグループからパスワードを削除できます。

#### Q4. グループパスワードを設定するとどうなりますか？
A. グループにパスワードが設定されている場合、そのグループのメンバーでないユーザーは `newgrp` コマンドを使用して正しいパスワードを入力することで、セッション中に一時的にそのグループに参加できます。

## 参考資料

https://man7.org/linux/man-pages/man1/gpasswd.1.html

## 改訂履歴

- 2025/05/04 初版作成