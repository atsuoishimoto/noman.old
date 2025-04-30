# groupmod コマンド

既存のグループの属性を変更します。

## 概要

`groupmod`コマンドは、システム上の既存のグループアカウントの設定を変更するために使用されます。グループ名やグループIDなどの属性を変更できます。システム管理者がユーザーグループを管理する際に役立ちます。

## オプション

### **-g, --gid GID**

グループのIDを変更します。

```console
$ sudo groupmod -g 1001 developers
# developersグループのGIDを1001に変更
```

### **-n, --new-name 新しいグループ名**

グループの名前を変更します。

```console
$ sudo groupmod -n programmers developers
# developersグループの名前をprogrammersに変更
```

### **-p, --password パスワード**

グループのパスワードを変更します（暗号化された形式で指定）。

```console
$ sudo groupmod -p encrypted_password developers
# developersグループのパスワードを変更
```

### **-o, --non-unique**

重複するGIDを許可します。

```console
$ sudo groupmod -g 1001 -o testers
# testersグループのGIDを1001に変更（既に他のグループが使用していても許可）
```

## 使用例

### グループ名とGIDを同時に変更

```console
$ sudo groupmod -g 2000 -n engineering developers
# developersグループの名前をengineeringに変更し、GIDを2000に設定
```

### グループ情報の確認

```console
$ grep developers /etc/group
developers:x:1001:user1,user2,user3
# 変更前のグループ情報を確認

$ sudo groupmod -n programmers developers
# グループ名を変更

$ grep programmers /etc/group
programmers:x:1001:user1,user2,user3
# 変更後のグループ情報を確認
```

## ヒント:

### 変更前にバックアップを作成

グループ情報を変更する前に、/etc/groupファイルのバックアップを作成しておくと安全です。

```console
$ sudo cp /etc/group /etc/group.bak
# グループファイルのバックアップを作成
```

### 変更の影響を確認

グループ名やGIDを変更すると、そのグループに関連付けられたファイルやプロセスに影響する可能性があります。変更前に影響範囲を確認しましょう。

### rootユーザーで実行

`groupmod`コマンドはシステム設定を変更するため、通常はroot権限（sudoを使用）で実行する必要があります。

## よくある質問

#### Q1. `groupmod`コマンドを実行するために必要な権限は？
A. rootユーザー権限が必要です。一般ユーザーは`sudo`を使用して実行する必要があります。

#### Q2. グループIDを変更した場合、ファイルの所有権はどうなりますか？
A. ファイルシステム上の古いGIDを参照しているファイルは自動的に更新されません。`find`と`chgrp`コマンドを使用して手動で更新する必要があります。

#### Q3. 存在しないグループを変更しようとするとどうなりますか？
A. エラーメッセージが表示され、コマンドは失敗します。例：「groupmod: group 'nonexistent' does not exist」

#### Q4. システムグループ（GID 1-999）の変更に制限はありますか？
A. 多くのシステムでは、システムグループの変更は可能ですが、システムの動作に影響を与える可能性があるため注意が必要です。

## macOSでの注意点

macOSでは`groupmod`コマンドは標準では利用できません。代わりに`dscl`コマンドを使用してグループ属性を変更します：

```console
$ sudo dscl . -change /Groups/developers PrimaryGroupID 1000 1001
# developersグループのGIDを1000から1001に変更

$ sudo dscl . -change /Groups/developers RealName "Developers" "Programmers"
# developersグループの表示名を変更
```

## 参考資料

https://man7.org/linux/man-pages/man8/groupmod.8.html

## 改訂履歴

- 2025/04/30 初版作成