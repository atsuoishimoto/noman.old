# getent コマンド

データベースエントリを取得し表示するコマンド。

## 概要

`getent`は、様々なネームサービススイッチ（NSS）データベースからエントリを取得して表示するコマンドです。ユーザー情報、グループ情報、ホスト名、ネットワークサービスなどの情報を簡単に検索できます。これらの情報は、ローカルファイル（/etc/passwd など）や LDAP、NIS などの外部ソースから取得されます。

## オプション

### **データベース**

検索するデータベースを指定します。主なデータベースには passwd, group, hosts, services, protocols などがあります。

```console
$ getent passwd root
root:x:0:0:root:/root:/bin/bash
```

### **-s SOURCE**

特定のソースからのみ情報を取得します。

```console
$ getent -s files passwd root
root:x:0:0:root:/root:/bin/bash
```

### **-i**

大文字小文字を区別せずに検索します。

```console
$ getent -i hosts localhost
127.0.0.1       localhost
```

## 使用例

### ユーザー情報の取得

```console
$ getent passwd username
username:x:1000:1000:Full Name:/home/username:/bin/bash
```

### ホスト名の解決

```console
$ getent hosts example.com
93.184.216.34   example.com
```

### サービスのポート番号確認

```console
$ getent services ssh
ssh                  22/tcp
```

### グループメンバーの確認

```console
$ getent group sudo
sudo:x:27:user1,user2
```

## ヒント:

### 複数のエントリを一度に取得

キーを指定しない場合、データベース内のすべてのエントリが表示されます。これは大量の情報を取得したい場合に便利です。

```console
$ getent hosts | head -3
127.0.0.1       localhost
::1             localhost ip6-localhost ip6-loopback
```

### パイプラインでの活用

`getent`の出力は他のコマンドと組み合わせて使用できます。例えば、特定のユーザーのホームディレクトリを取得するには：

```console
$ getent passwd username | cut -d: -f6
/home/username
```

### ネットワークトラブルシューティング

DNSの問題をデバッグする際に`getent hosts`を使用すると、システムがホスト名をどのように解決しているかを確認できます。

## よくある質問

#### Q1. `getent`と`cat /etc/passwd`の違いは何ですか？
A. `getent passwd`はローカルファイルだけでなく、LDAP、NIS、その他のNSSソースからも情報を取得します。一方、`cat /etc/passwd`はローカルファイルのみを表示します。

#### Q2. 特定のユーザーがシステムに存在するか確認するには？
A. `getent passwd username`を実行し、出力があればそのユーザーは存在します。コマンドの終了ステータスでも確認できます。

#### Q3. ホスト名のIPv4とIPv6両方のアドレスを取得するには？
A. `getent ahosts hostname`を使用すると、IPv4とIPv6の両方のアドレスを取得できます。

#### Q4. `getent`でサポートされているデータベースを確認するには？
A. `getent --help`または`man getent`で確認できます。一般的なデータベースには passwd, group, hosts, services, protocols, networks などがあります。

## 参考資料

https://man7.org/linux/man-pages/man1/getent.1.html

## 改訂履歴

- 2025/04/30 初版作成