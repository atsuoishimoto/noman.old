# docker run コマンド

指定したイメージから新しいコンテナを作成して起動します。

## 概要

`docker run` コマンドは、Dockerイメージからコンテナを作成して起動します。このコマンドは `docker create` と `docker start` の機能を1つのコマンドに統合したものです。コンテナを起動する際に、ランタイムパラメータ、環境変数、ネットワーク設定、ボリュームマウントなどの設定オプションを指定することができます。

## オプション

### **-d, --detach**

コンテナをバックグラウンド（デタッチモード）で実行し、コンテナIDを表示します

```console
$ docker run -d nginx
3a41f9da42324b98a5f34d8c5c09c319f7e8e99cf24c573fc603ed52b11c42e7
```

### **-i, --interactive**

アタッチされていなくても標準入力（STDIN）を開いたままにし、対話型セッションを可能にします

```console
$ docker run -i ubuntu /bin/bash
root@7c3bfd21a2a4:/#
```

### **-t, --tty**

疑似TTYを割り当てます。通常は対話型ターミナルセッション用に `-i` と一緒に使用します

```console
$ docker run -it ubuntu
root@7c3bfd21a2a4:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

### **-p, --publish [ホストポート]:[コンテナポート]**

コンテナのポートをホストに公開します

```console
$ docker run -p 8080:80 nginx
```

### **-v, --volume [ホストパス]:[コンテナパス]**

ホストからコンテナにボリュームをバインドマウントします

```console
$ docker run -v /host/path:/container/path nginx
```

### **-e, --env [キー]=[値]**

コンテナ内に環境変数を設定します

```console
$ docker run -e DB_HOST=localhost -e DB_PORT=5432 postgres
```

### **--name [名前]**

コンテナに名前を割り当てます

```console
$ docker run --name my-web-server nginx
```

### **--rm**

コンテナ終了時に自動的に削除します

```console
$ docker run --rm alpine echo "Hello, World!"
Hello, World!
```

### **--network [ネットワーク]**

コンテナをネットワークに接続します

```console
$ docker run --network my-network nginx
```

## 使用例

### ポートマッピングを行いデタッチモードでコンテナを実行

```console
$ docker run -d -p 8080:80 --name web-server nginx
3a41f9da42324b98a5f34d8c5c09c319f7e8e99cf24c573fc603ed52b11c42e7
```

### コンテナ内で対話型シェルを実行

```console
$ docker run -it --rm ubuntu bash
root@7c3bfd21a2a4:/# echo "I'm in a container"
I'm in a container
root@7c3bfd21a2a4:/# exit
```

### ボリュームマウントと環境変数を使用してコンテナを実行

```console
$ docker run -d \
  --name postgres-db \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_USER=myuser \
  -v pgdata:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

## ヒント:

### 永続データには名前付きボリュームを使用する

特定のホストパスにバインドする代わりに、名前付きボリュームを使用すると移植性が向上します：

```console
$ docker run -v mydata:/app/data nginx
```

### コンテナのリソースを制限する

`--memory` と `--cpus` を使用してコンテナのリソース使用量を制限できます：

```console
$ docker run --memory=512m --cpus=0.5 nginx
```

### 複数の環境変数にはファイルを使用する

多くの環境変数が必要なコンテナには、環境変数ファイルを使用します：

```console
$ docker run --env-file ./env.list nginx
```

### コンテナを自動的にクリーンアップする

短時間だけ実行するコンテナには常に `--rm` を使用して、停止したコンテナが蓄積するのを防ぎましょう。

## よくある質問

#### Q1. `docker run` と `docker start` の違いは何ですか？
A. `docker run` はイメージから新しいコンテナを作成して起動しますが、`docker start` は既に存在する停止中のコンテナを再起動します。

#### Q2. コンテナをバックグラウンドで実行するにはどうすればよいですか？
A. `-d` または `--detach` フラグを使用します：`docker run -d nginx`

#### Q3. 実行中のコンテナのシェルにアクセスするにはどうすればよいですか？
A. 新しいコンテナをシェル付きで起動するには `docker run -it [イメージ] bash` を、既に実行中のコンテナのシェルにアクセスするには `docker exec -it [コンテナID] bash` を使用します。

#### Q4. 複数のポートを公開するにはどうすればよいですか？
A. 複数の `-p` フラグを使用します：`docker run -p 80:80 -p 443:443 nginx`

#### Q5. 特定のユーザーでコンテナを実行するにはどうすればよいですか？
A. `--user` フラグを使用します：`docker run --user 1000:1000 nginx`

## 参考資料

https://docs.docker.com/engine/reference/commandline/run/

## 改訂履歴

- 2025/05/04 初版作成