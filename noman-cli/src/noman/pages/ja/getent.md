# getent コマンド

管理データベース（ホスト、ユーザー、グループなど）からエントリを取得します。

## 概要

`getent` は、Name Service Switch (NSS) ライブラリによってサポートされている様々な管理データベースからエントリを取得します。ユーザー、グループ、ホスト、ネットワーク、サービス、プロトコルなどの情報をローカルまたはリモートに保存されているかに関わらず、システムデータベースから検索するために一般的に使用されます。

## オプション

### **-s, --service=CONFIG**

使用するサービスプロバイダを指定します

```console
$ getent -s files passwd root
root:x:0:0:root:/root:/bin/bash
```

### **-i, --no-idn**

hostsデータベースに対するIDNエンコーディングを無効にします

```console
$ getent -i hosts example.com
93.184.216.34    example.com
```

### **-h, --help**

ヘルプ情報を表示して終了します

```console
$ getent --help
Usage: getent [OPTION...] database [key ...]
Get entries from administrative database.

  -i, --no-idn               Disable IDN encoding
  -s, --service=CONFIG       Service configuration to be used
  -?, --help                 Give this help list
      --usage                Give a short usage message
  -V, --version              Print program version
```

## 使用例

### ユーザー情報の検索

```console
$ getent passwd username
username:x:1000:1000:John Doe:/home/username:/bin/bash
```

### ホストのIPアドレスを検索

```console
$ getent hosts github.com
140.82.121.4     github.com
```

### すべてのグループを一覧表示

```console
$ getent group
root:x:0:
daemon:x:1:
bin:x:2:
sys:x:3:
adm:x:4:syslog,username
[追加のグループ...]
```

### サービスポートの検索

```console
$ getent services ssh
ssh                  22/tcp
```

## ヒント:

### ユーザーの存在確認

`getent passwd username` を使用して、システム内にユーザーが存在するかどうかを確認できます。コマンドが出力を返せばユーザーは存在し、何も返さなければ存在しません。

### グループのすべてのメンバーを見つける

`getent group groupname` を使用して、特定のグループに所属するすべてのユーザーを確認できます。

### 名前解決のテスト

`getent hosts hostname` を使用して、ホスト名が解決できるかテストできます。これはDNSからでもローカルのhostsファイルからでも解決元に関わらず機能します。

### 利用可能なデータベース

クエリできる一般的なデータベースには、`passwd`、`group`、`hosts`、`services`、`protocols`、`networks`、`netgroup` などがあります。正確なリストはシステム構成によって異なります。

## よくある質問

#### Q1. `getent hosts` と `ping` の違いは何ですか？
A. `getent hosts` はパケットを送信せずに名前解決のみを実行しますが、`ping` は実際にICMPパケットをホストに送信します。`getent` はホスト名がIPアドレスに解決できるかどうかを確認するだけに便利です。

#### Q2. `getent` をスクリプトで使用できますか？
A. はい、`getent` はユーザー、グループ、ホストが存在するかどうかを確認してから操作を実行するために、シェルスクリプトでよく使用されます。

#### Q3. なぜ `getent passwd username` が `/etc/passwd` を見るのと異なる結果を示すことがありますか？
A. `getent` は設定されたすべてのNSSソースをクエリするため、ローカルの `/etc/passwd` ファイルだけでなく、LDAP、NIS、その他のネットワーク認証システムも含まれる可能性があります。

#### Q4. 利用可能なすべてのデータベースを確認するにはどうすればよいですか？
A. 利用可能なデータベースはシステム構成によって異なります。一般的なものには passwd、group、hosts、services、protocols、networks、netgroup などがあります。

## 参考資料

https://man7.org/linux/man-pages/man1/getent.1.html

## 改訂履歴

- 2025/05/04 初版作成