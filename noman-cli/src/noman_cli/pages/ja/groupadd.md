# groupadd コマンド

新しいグループをシステムに追加します。

## 概要

`groupadd` コマンドは、システムに新しいグループを作成するために使用されます。システム管理者がユーザーアクセス権を管理するために、ユーザーをグループ化する際に役立ちます。このコマンドはルート権限（sudo）が必要です。

## オプション

### **-g GID**

グループIDを指定します。指定しない場合は、利用可能な次のGIDが自動的に割り当てられます。

```console
$ sudo groupadd -g 1001 developers
```

### **-r**

システムグループを作成します。システムグループは通常、デーモンやシステムサービス用に使用されます。

```console
$ sudo groupadd -r webservice
```

### **-f**

グループがすでに存在する場合でもエラーを表示せず、正常終了します（強制モード）。

```console
$ sudo groupadd -f marketing
```

### **-K KEY=VALUE**

デフォルトの設定を上書きします。例えば、`GID_MIN`や`GID_MAX`などを指定できます。

```console
$ sudo groupadd -K GID_MIN=5000 newgroup
```

## 使用例

### 基本的なグループ作成

```console
$ sudo groupadd developers
# 新しいグループ「developers」が作成される
```

### 特定のGIDでグループを作成

```console
$ sudo groupadd -g 2000 designers
# GID 2000で「designers」グループが作成される
```

### システムグループの作成

```console
$ sudo groupadd -r nginx
# システムグループ「nginx」が作成される
```

## ヒント:

### グループ情報の確認

グループが正しく作成されたかを確認するには、`getent group グループ名`または`cat /etc/group | grep グループ名`コマンドを使用します。

```console
$ getent group developers
developers:x:1001:
```

### グループIDの範囲

一般的に、システムグループは低いGID（通常1000未満）を使用し、通常のユーザーグループは1000以上のGIDを使用します。システムによって異なる場合があります。

### グループ削除

不要になったグループを削除するには、`groupdel`コマンドを使用します。

```console
$ sudo groupdel developers
```

## よくある質問

#### Q1. `groupadd`と`useradd -G`の違いは何ですか？
A. `groupadd`は新しいグループを作成するだけです。一方、`useradd -G`は新しいユーザーを作成し、そのユーザーを指定したグループに追加します。既存のユーザーをグループに追加するには`usermod -aG`を使用します。

#### Q2. 作成したグループにユーザーを追加するにはどうすればよいですか？
A. `usermod -aG グループ名 ユーザー名`コマンドを使用します。例：`sudo usermod -aG developers john`

#### Q3. グループのGIDを後から変更できますか？
A. はい、`groupmod -g 新しいGID グループ名`コマンドで変更できます。ただし、すでにそのグループに関連付けられたファイルがある場合は注意が必要です。

#### Q4. グループ作成時にエラーが発生する場合はどうすればよいですか？
A. 多くの場合、権限の問題（sudoを使用していない）か、すでに存在するグループ名やGIDを指定している可能性があります。`-f`オプションを使用するか、別の名前やGIDを選択してください。

## 参考

https://www.man7.org/linux/man-pages/man8/groupadd.8.html

## 改訂

- 2025/04/30 初版作成