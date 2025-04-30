# gpasswd コマンド

グループのパスワードとメンバーシップを管理します。

## 概要

`gpasswd` コマンドはグループのパスワードを設定したり、グループのメンバーを追加・削除したりするためのツールです。システム管理者やグループ管理者がグループのメンバーシップを管理する際に使用します。

## オプション

### **-a ユーザー**

指定したユーザーをグループに追加します。

```console
$ sudo gpasswd -a username groupname
ユーザー username をグループ groupname に追加しました
```

### **-d ユーザー**

指定したユーザーをグループから削除します。

```console
$ sudo gpasswd -d username groupname
ユーザー username をグループ groupname から削除しました
```

### **-A ユーザー,...**

グループ管理者のリストを設定します。複数の管理者を指定する場合はカンマで区切ります。

```console
$ sudo gpasswd -A admin1,admin2 groupname
```

### **-M ユーザー,...**

グループのメンバーリストを設定します。既存のメンバーリストは上書きされます。

```console
$ sudo gpasswd -M user1,user2,user3 groupname
```

### **-r**

グループのパスワードを削除します。

```console
$ sudo gpasswd -r groupname
```

## 使用例

### グループにユーザーを追加する

```console
$ sudo gpasswd -a john developers
ユーザー john をグループ developers に追加しました
```

### グループからユーザーを削除する

```console
$ sudo gpasswd -d mary designers
ユーザー mary をグループ designers から削除しました
```

### グループ管理者を設定する

```console
$ sudo gpasswd -A teamlead,manager projectgroup
```

### グループメンバーを一括設定する

```console
$ sudo gpasswd -M user1,user2,user3,user4 projectgroup
```

## ヒント:

### グループメンバーシップの確認

グループのメンバーを確認するには、`getent group` コマンドを使用します。

```console
$ getent group developers
developers:x:1001:john,mary,bob
```

### 管理者権限が必要

ほとんどの `gpasswd` 操作には管理者権限（sudo）が必要です。グループ管理者として設定されている場合は、一部の操作が可能です。

### グループ管理者とメンバーの違い

グループ管理者（-A オプションで設定）はグループのメンバーシップを管理できますが、必ずしもそのグループのメンバーである必要はありません。

## よくある質問

#### Q1. 一般ユーザーでも `gpasswd` コマンドを使えますか？
A. 基本的には管理者権限（root）が必要ですが、グループ管理者として設定されているユーザーは、そのグループのメンバーシップを管理できます。

#### Q2. グループのメンバーを確認するにはどうすればいいですか？
A. `getent group グループ名` または `grep グループ名 /etc/group` コマンドで確認できます。

#### Q3. ユーザーが所属しているすべてのグループを確認するには？
A. `groups ユーザー名` コマンドで確認できます。

#### Q4. グループパスワードは何のために使われますか？
A. グループパスワードを使うと、ユーザーが `newgrp` コマンドでそのグループに一時的に切り替える際に認証が必要になります。ただし、セキュリティ上の理由から現代のシステムではあまり使用されません。

## 参考情報

https://linux.die.net/man/1/gpasswd

## 改訂履歴

- 2025/04/30 初版作成