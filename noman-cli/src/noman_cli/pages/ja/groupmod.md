# groupmod コマンド

システム上のグループ定義を変更します。

## 概要

`groupmod` コマンドは、Linux や Unix システム上の既存のグループの属性を変更するために使用されます。グループ名（GID）や数値グループ ID を変更することができます。このコマンドは、通常、システム管理者がユーザーとグループアカウントを管理する際に使用されます。

## オプション

### **-g, --gid GID**

グループ ID を指定された値に変更します。

```console
$ sudo groupmod -g 1005 developers
```

### **-n, --new-name 新グループ名**

グループの名前を新しい名前に変更します。

```console
$ sudo groupmod -n programmers developers
```

### **-o, --non-unique**

重複するGIDの使用を許可します（通常、GIDは一意である必要があります）。

```console
$ sudo groupmod -g 1005 -o testers
```

### **-p, --password パスワード**

グループのパスワードを暗号化されたパスワードに変更します。

```console
$ sudo groupmod -p encrypted_password developers
```

### **-R, --root CHROOT_DIR**

CHROOT_DIR ディレクトリ内で変更を適用し、CHROOT_DIR ディレクトリから設定ファイルを使用します。

```console
$ sudo groupmod -R /mnt/system -n programmers developers
```

## 使用例

### グループ名の変更

```console
$ sudo groupmod -n engineering developers
```

これにより、グループ名が「developers」から「engineering」に変更されますが、同じ GID が維持されます。

### グループの GID の変更

```console
$ sudo groupmod -g 2000 engineering
```

これにより、「engineering」グループの GID が 2000 に変更されます。

### 名前と GID の両方を変更

```console
$ sudo groupmod -n tech-team -g 2500 engineering
```

これにより、グループ名が「engineering」から「tech-team」に変更され、GID が 2500 に変更されます。

## ヒント:

### 変更前にグループ情報を確認する

変更を行う前に、`getent group グループ名`を使用して現在のグループ情報を確認し、正しい情報を持っていることを確認しましょう。

### GID 変更後にファイル所有権を更新する

グループの GID を変更した後、`find /path -group 古いgid -exec chgrp 新しいgid {} \;`を使用してファイル所有権を更新し、ファイルへの適切なアクセスを維持する必要があるかもしれません。

### 変更前にバックアップを取る

重要なシステムでは、`groupmod`で変更を行う前に、`/etc/group`と`/etc/gshadow`ファイルをバックアップすることを検討してください。

### 注意して使用する

グループ ID の変更は、システム全体のファイルのアクセス権と権限に影響を与える可能性があります。可能であれば、メンテナンス時間中に変更を行いましょう。

## よくある質問

#### Q1. GID を変更すると、そのグループが所有するファイルはどうなりますか？
A. ファイルは新しい GID ではなく、古い GID 番号を参照し続けます。`chgrp`コマンドを使用して手動でファイルの所有権を更新する必要があります。

#### Q2. グループ名と GID を同時に変更できますか？
A. はい、`-n`と`-g`オプションを1つのコマンドで一緒に使用できます。

#### Q3. グループがユーザーによって使用されているかどうかを確認するにはどうすればよいですか？
A. `grep グループ名 /etc/group /etc/passwd`を使用して、グループが任意のユーザーの主要または二次グループとしてリストされているかどうかを確認できます。

#### Q4. 既に存在する名前にグループの名前を変更しようとするとどうなりますか？
A. コマンドは失敗し、グループがすでに存在することを示すエラーメッセージが表示されます。

## 参考資料

https://www.man7.org/linux/man-pages/man8/groupmod.8.html

## 改訂履歴

- 2025/05/04 初回改訂