# groupadd コマンド

システムに新しいグループを作成します。

## 概要

`groupadd` コマンドはシステムに新しいグループアカウントを作成します。指定されたグループ名でシステムのグループファイル（通常は `/etc/group`）にエントリを追加し、一意のグループID（GID）を割り当てます。

## オプション

### **-f, --force**

グループがすでに存在する場合でも正常終了し、GIDがすでに使用されている場合は -g オプションをキャンセルします。

```console
$ sudo groupadd -f developers
```

### **-g, --gid GID**

グループのID（GID）の数値を指定します。この値は -o オプションを使用しない限り、一意である必要があります。

```console
$ sudo groupadd -g 1500 project-team
```

### **-K, --key KEY=VALUE**

/etc/login.defs のデフォルト値（GID_MIN、GID_MAX など）を上書きします。

```console
$ sudo groupadd -K GID_MIN=5000 new-group
```

### **-o, --non-unique**

一意でないGIDを持つグループの作成を許可します。

```console
$ sudo groupadd -o -g 1500 another-group
```

### **-p, --password PASSWORD**

新しいグループの暗号化されたパスワードを設定します。

```console
$ sudo groupadd -p encrypted_password finance
```

### **-r, --system**

システムGID範囲内のGIDを持つシステムグループを作成します。

```console
$ sudo groupadd -r sysgroup
```

## 使用例

### 基本的なグループの作成

```console
$ sudo groupadd developers
```

### システムグループの作成

```console
$ sudo groupadd -r docker
```

### 特定のGIDを持つグループの作成

```console
$ sudo groupadd -g 2000 project-team
```

### すでに存在する可能性のあるグループの作成

```console
$ sudo groupadd -f webadmins
```

## ヒント:

### グループ作成の確認

グループを作成した後、`getent group` コマンドを使用して正しく追加されたことを確認できます：

```console
$ getent group developers
developers:x:1001:
```

### グループIDの範囲

システムグループは通常、低いGID（多くの場合1000未満）を使用し、ユーザーグループはより高いGIDを使用します。特定の範囲については、システムの `/etc/login.defs` ファイルを確認してください。

### グループ管理

`groupadd` はグループの作成のみを行うことを覚えておいてください。既存のグループを変更するには `groupmod` を、削除するには `groupdel` を使用します。

### グループメンバーシップ

グループを作成した後、`usermod -aG グループ名 ユーザー名` を使用してユーザーをグループに追加できます。

## よくある質問

#### Q1. 新しいグループを作成するにはどうすればよいですか？
A. `sudo groupadd グループ名` を使用して、指定した名前の新しいグループを作成します。

#### Q2. グループを作成する際にカスタムGIDを指定するにはどうすればよいですか？
A. `sudo groupadd -g GID グループ名` を使用します。GIDは割り当てたい数値のグループIDです。

#### Q3. システムグループと通常のグループの違いは何ですか？
A. システムグループ（`-r` で作成）は通常、システムサービスやデーモン用に使用され、通常のグループは人間のユーザー用です。システムグループは通常、より低いGIDを持ちます。

#### Q4. グループがすでに存在するかどうかを確認するにはどうすればよいですか？
A. `getent group グループ名` を使用してグループが存在するかどうかを確認します。

#### Q5. 既存のグループと同じGIDを持つグループを作成できますか？
A. はい、ただし `-o`（非一意）オプションを使用する必要があります：`sudo groupadd -o -g 既存のgid 新しいグループ`

## 参考資料

https://man7.org/linux/man-pages/man8/groupadd.8.html

## 改訂履歴

- 2025/05/04 初版作成