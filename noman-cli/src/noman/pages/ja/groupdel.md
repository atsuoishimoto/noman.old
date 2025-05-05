# groupdel コマンド

システムからグループを削除します。

## 概要

`groupdel` は、指定されたグループをシステムから削除するコマンドラインユーティリティです。システムのグループデータベース（通常は `/etc/group` と `/etc/gshadow`）からグループのエントリを削除します。このコマンドは、主にシステム管理者が Linux や Unix 系システム上のグループアカウントを管理するために使用されます。

## オプション

### **-f, --force**

ユーザーの主グループであっても、グループの削除を強制します。

```console
$ sudo groupdel -f developers
```

### **-h, --help**

ヘルプメッセージを表示して終了します。

```console
$ groupdel --help
Usage: groupdel [options] GROUP

Options:
  -h, --help                    display this help message and exit
  -R, --root CHROOT_DIR         directory to chroot into
  -P, --prefix PREFIX_DIR       prefix directory where are located the /etc/* files
  -f, --force                   delete group even if it is the primary group of a user
```

### **-R, --root CHROOT_DIR**

CHROOT_DIR ディレクトリ内で変更を適用し、CHROOT_DIR ディレクトリから設定ファイルを使用します。

```console
$ sudo groupdel -R /mnt/system developers
```

### **-P, --prefix PREFIX_DIR**

/etc/* ファイルが配置されているプレフィックスディレクトリを使用します。

```console
$ sudo groupdel -P /mnt/etc developers
```

## 使用例

### 基本的なグループ削除

```console
$ sudo groupdel developers
```

### 主グループの強制削除

```console
$ sudo groupdel -f projectteam
```

## ヒント:

### 削除前にグループの依存関係を確認する

グループを削除する前に、`grep groupname /etc/passwd` を使用して、そのグループを主グループとしているユーザーがいないか確認しましょう。ユーザーがそのグループに依存している場合は、先に主グループを変更するか、`-f` オプションを使用する必要があるかもしれません。

### グループの存在を確認する

`getent group groupname` を使用して、削除しようとするグループが存在することを確認しましょう。

### グループ情報のバックアップ

特に本番環境では、グループ構造を変更する前に `/etc/group` と `/etc/gshadow` ファイルをバックアップしておくことをお勧めします。

## よくある質問

#### Q1. 削除されたグループが所有していたファイルはどうなりますか？
A. 以前削除されたグループが所有していたファイルは引き続き存在しますが、グループ名の代わりにグループIDの数字が表示されます。削除前にこれらのファイルを別のグループに再割り当てすることをお勧めします。

#### Q2. ユーザーが所属しているグループを削除できますか？
A. はい、できますが、ファイルアクセス権限に影響します。このグループを補助グループとしていたユーザーは、そのグループに制限されていたファイルへのアクセス権を失います。

#### Q3. 一部のユーザーの主グループであるグループを削除するにはどうすればよいですか？
A. `groupdel -f groupname` を使用します。ただし、影響を受ける各ユーザーに対して先に `usermod -g newgroup username` でユーザーの主グループを変更する方が良い方法です。

#### Q4. 削除したグループを復元できますか？
A. いいえ、一度削除すると、グループを手動で再作成する必要があります。そのため、変更を加える前にシステムファイルをバックアップすることが重要です。

## 参考資料

https://man7.org/linux/man-pages/man8/groupdel.8.html

## 改訂履歴

- 2025/05/04 初版作成