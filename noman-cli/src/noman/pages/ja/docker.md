# docker コマンド

Dockerコンテナ、イメージ、ネットワーク、その他のDockerオブジェクトを管理します。

## 概要

Dockerはアプリケーションをコンテナで開発、配布、実行できるプラットフォームです。`docker`コマンドはDockerとやり取りするための主要なインターフェースであり、コンテナ、イメージ、ネットワーク、ボリュームなどのDockerリソースを構築、実行、管理することができます。ホストシステムに関係なく、アプリケーションが一貫した環境で実行できるようにします。

## オプション

### **docker run**

イメージから新しいコンテナを作成して起動します

```console
$ docker run -d --name web nginx
e7cc5d2c8cdc5b05a4f37ce6cf15e9f0e0a5bd2bec30cc5415917d669de12857
```

### **docker ps**

実行中のコンテナを一覧表示します（`-a`を追加すると停止したものも含めすべてのコンテナを表示）

```console
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
e7cc5d2c8cdc   nginx     "/docker-entrypoint.…"   10 seconds ago   Up 9 seconds    80/tcp    web
```

### **docker images**

ローカルシステム上の利用可能なイメージを一覧表示します

```console
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    a6bd71f48f68   2 weeks ago    187MB
ubuntu       latest    3b418d7b466a   4 weeks ago    77.8MB
```

### **docker build**

Dockerfileからイメージをビルドします

```console
$ docker build -t myapp:1.0 .
[+] Building 25.6s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 215B                                       0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/node:14                 1.2s
 => [1/5] FROM docker.io/library/node:14@sha256:fcb6...                    0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 1.25kB                                        0.0s
 => [2/5] WORKDIR /app                                                     0.5s
 => [3/5] COPY package*.json ./                                            0.1s
 => [4/5] RUN npm install                                                 20.5s
 => [5/5] COPY . .                                                         0.1s
 => exporting to image                                                     3.1s
 => => exporting layers                                                    3.1s
 => => writing image sha256:a1b2c3d4e5f6...                                0.0s
 => => naming to docker.io/library/myapp:1.0                               0.0s
```

### **docker stop/start**

既存のコンテナを停止または起動します

```console
$ docker stop web
web

$ docker start web
web
```

### **docker exec**

実行中のコンテナでコマンドを実行します

```console
$ docker exec -it web bash
root@e7cc5d2c8cdc:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@e7cc5d2c8cdc:/# exit
```

## 使用例

### ポートマッピングを使用したコンテナの実行

```console
$ docker run -d -p 8080:80 --name webserver nginx
f499cc406d7e9d92537dec4182f2d0f9f9dbf74e2d9651c3c4c94a7b8a023c15

$ curl http://localhost:8080
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

### カスタムアプリケーションのビルドと実行

```console
$ docker build -t myapp:latest .
[+] Building 15.3s (10/10) FINISHED
...

$ docker run -d -p 3000:3000 --name myapplication myapp:latest
a72f4623b8bfb647e8b108f770e5758eed96a37638e929278169a105ea86c912
```

### ボリュームを使用したコンテナデータの管理

```console
$ docker volume create mydata
mydata

$ docker run -d --name database -v mydata:/var/lib/mysql mysql:8.0
b8a1c375e3c2a9c0293bb9d4f9a6b1e7f2d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9
```

## ヒント:

### Docker Composeを使用して複数コンテナアプリケーションを管理する

複雑な`docker run`コマンドで複数のコンテナを管理する代わりに、Docker Composeと`docker-compose.yml`ファイルを使用して、複数コンテナアプリケーションを定義・実行しましょう。

```console
$ docker-compose up -d
```

### 未使用リソースをクリーンアップする

Dockerは時間とともに未使用のコンテナ、イメージ、ボリュームが蓄積されます。以下のコマンドでクリーンアップできます：

```console
$ docker system prune  # 停止したコンテナ、未使用ネットワーク、ダングリングイメージを削除
$ docker system prune -a  # ダングリングイメージだけでなく未使用イメージも削除
$ docker volume prune  # 未使用ボリュームを削除
```

### マルチステージビルドで小さなイメージを作成する

Dockerfileでマルチステージビルドを使用すると、ビルド時の依存関係と実行時の依存関係を分離して、より小さな本番イメージを作成できます。

```dockerfile
FROM node:14 AS build
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

### .dockerignoreを使用する

`.gitignore`と同様に`.dockerignore`ファイルを作成して、不要なファイルがDockerビルドコンテキストに含まれないようにしましょう。これによりビルドが高速化され、イメージサイズも削減できます。

## よくある質問

#### Q1. `docker run`と`docker start`の違いは何ですか？
A. `docker run`はイメージから新しいコンテナを作成して起動しますが、`docker start`は既に存在する停止中のコンテナを再起動します。

#### Q2. コンテナからログにアクセスするにはどうすればよいですか？
A. `docker logs [コンテナ名]`を使用してログを表示できます。リアルタイムでログを追跡するには`-f`を追加します。

#### Q3. ホストとコンテナ間でファイルをコピーするにはどうすればよいですか？
A. `docker cp [ソース] [宛先]`を使用します。例：`docker cp ./file.txt mycontainer:/app/`または`docker cp mycontainer:/app/file.txt ./`

#### Q4. コンテナとイメージを削除するにはどうすればよいですか？
A. コンテナを削除するには`docker rm [コンテナID]`を、イメージを削除するには`docker rmi [イメージID]`を使用します。強制削除するには`-f`を追加します。

#### Q5. コンテナのリソース使用状況を確認するにはどうすればよいですか？
A. `docker stats`を使用すると、実行中のコンテナのCPU、メモリ、ネットワーク、ディスク使用量を確認できます。

## 参考資料

https://docs.docker.com/engine/reference/commandline/cli/

## 改訂履歴

- 2025/05/04 初回作成