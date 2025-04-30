# docker run コマンド

コンテナを作成して実行するためのコマンド。

## 概要

`docker run` コマンドは、新しいコンテナを作成し、指定されたイメージから起動します。このコマンドは、イメージのダウンロード（必要な場合）、コンテナの作成、起動、そして指定されたコマンドの実行までを一度に行います。開発環境の構築、アプリケーションのテスト、本番環境へのデプロイなど、Dockerを使用する際の基本的なコマンドです。

## オプション

### **-d, --detach**

コンテナをバックグラウンドで実行し、コンテナIDを表示します。

```console
$ docker run -d nginx
3a53a5724d6b9f25b85222e4c2c9b8c455d4f3909a7d8f74c6c9cb9d94d6f4a2
```

### **-p, --publish**

ホストとコンテナ間のポートマッピングを設定します。

```console
$ docker run -p 8080:80 nginx
```

### **-v, --volume**

ホストとコンテナ間のボリュームマウントを設定します。

```console
$ docker run -v /host/path:/container/path nginx
```

### **-e, --env**

環境変数を設定します。

```console
$ docker run -e MYSQL_ROOT_PASSWORD=password mysql
```

### **--name**

コンテナに名前を付けます。

```console
$ docker run --name my-nginx nginx
```

### **--rm**

コンテナ終了時に自動的に削除します。

```console
$ docker run --rm alpine echo "Hello, World!"
Hello, World!
```

## 使用例

### Webサーバーの起動

```console
$ docker run -d -p 8080:80 --name my-web-server nginx
b8a5f8d9c9e8f7d6e5c4b3a2
```

このコマンドはnginxコンテナをバックグラウンドで起動し、ホストの8080ポートをコンテナの80ポートにマッピングしている。

### データベースの起動

```console
$ docker run -d --name my-db -e POSTGRES_PASSWORD=mysecretpassword -v pgdata:/var/lib/postgresql/data postgres
7c6b5a4d3e2f1g0h9i8j7k6l
```

このコマンドはPostgreSQLコンテナを起動し、パスワードを設定し、データを永続化するためのボリュームをマウントしている。

### 対話型シェルの起動

```console
$ docker run -it ubuntu bash
root@f8d9c7b6a5:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

このコマンドはUbuntuコンテナを対話モードで起動し、bashシェルを実行している。

## ヒント:

### コンテナのリソース制限

`--memory` や `--cpus` オプションを使用して、コンテナが使用できるリソースを制限できます。

```console
$ docker run --memory=512m --cpus=0.5 nginx
```

### ネットワーク設定

`--network` オプションを使用して、コンテナを特定のネットワークに接続できます。

```console
$ docker run --network=my-network nginx
```

### ヘルスチェックの設定

`--health-cmd` オプションを使用して、コンテナの健全性をチェックするコマンドを設定できます。

```console
$ docker run --health-cmd="curl -f http://localhost/ || exit 1" nginx
```

## よくある質問

#### Q1. `docker run` と `docker create` + `docker start` の違いは何ですか？
A. `docker run` は `docker create`（コンテナの作成）と `docker start`（コンテナの起動）を一度に行うコマンドです。より細かい制御が必要な場合は、個別のコマンドを使用することもできます。

#### Q2. コンテナを一時的に使用するにはどうすればよいですか？
A. `--rm` オプションを使用すると、コンテナが停止した後に自動的に削除されます。一時的な作業やテストに便利です。

#### Q3. コンテナ内で実行されるデフォルトのコマンドを上書きするにはどうすればよいですか？
A. `docker run` コマンドの最後にコマンドを指定することで、イメージのデフォルトコマンドを上書きできます。例：`docker run ubuntu echo "Hello"`

#### Q4. macOSでボリュームマウントが遅い場合はどうすればよいですか？
A. macOSでは、特に大量のファイルを扱う場合、ボリュームマウントのパフォーマンスが低下することがあります。Docker Desktop for Macの設定で、ファイル共有の最適化オプションを確認するか、Docker Volumeを使用することを検討してください。

## 参考文献

https://docs.docker.com/engine/reference/commandline/run/

## 改訂履歴

- 2025/04/30 初版作成