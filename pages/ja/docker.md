# docker コマンド

コンテナの作成、管理、実行を行うためのコマンドラインツール。

## 概要

Docker は、アプリケーションをコンテナとして実行するためのプラットフォームです。コンテナは軽量な仮想環境で、アプリケーションとその依存関係をパッケージ化し、どこでも同じように実行できます。`docker` コマンドを使用して、イメージの作成・管理、コンテナの起動・停止、ネットワークやボリュームの管理などを行うことができます。

## オプション

### **docker run**

コンテナを作成して起動します。

```console
$ docker run -d -p 80:80 --name webserver nginx
b1a0dc2f37e9e48c5dfcbed288a3d38f42ce70cd75bce1005b3a4972e0d3a5a5
```

### **docker ps**

実行中のコンテナを一覧表示します。

```console
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                               NAMES
b1a0dc2f37e9   nginx     "/docker-entrypoint.…"   10 seconds ago   Up 9 seconds    0.0.0.0:80->80/tcp, :::80->80/tcp   webserver
```

### **docker images**

ローカルに保存されているイメージを一覧表示します。

```console
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    605c77e624dd   3 weeks ago    141MB
ubuntu       latest    ba6acccedd29   4 weeks ago    72.8MB
```

### **docker build**

Dockerfileからイメージを構築します。

```console
$ docker build -t myapp:1.0 .
[+] Building 25.3s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 215B                                       0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/node:14                 1.2s
 => [1/5] FROM docker.io/library/node:14@sha256:fcb6...                    0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 3.25kB                                        0.0s
 => [2/5] WORKDIR /app                                                     0.1s
 => [3/5] COPY package*.json ./                                            0.1s
 => [4/5] RUN npm install                                                 20.5s
 => [5/5] COPY . .                                                         0.1s
 => exporting to image                                                     3.2s
 => => exporting layers                                                    3.1s
 => => writing image sha256:d8f...                                         0.0s
 => => naming to docker.io/library/myapp:1.0                               0.0s
```

## 使用例

### コンテナの対話的実行

```console
$ docker run -it ubuntu bash
root@7b8b7c5c8e6a:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

### バックグラウンドでのコンテナ実行とポート転送

```console
$ docker run -d -p 8080:80 --name webserver nginx
a72df3b3b5b7e48c5dfcbed288a3d38f42ce70cd75bce1005b3a4972e0d3a5a5

$ curl localhost:8080
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

### コンテナの停止と削除

```console
$ docker stop webserver
webserver

$ docker rm webserver
webserver
```

### ボリュームマウント

```console
$ docker run -d -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html --name webserver nginx
c1b0dc2f37e9e48c5dfcbed288a3d38f42ce70cd75bce1005b3a4972e0d3a5a5
```

## ヒント:

### コンテナのシェルに接続する

実行中のコンテナに接続するには `docker exec -it コンテナ名 bash` を使用します。これはデバッグやトラブルシューティングに役立ちます。

```console
$ docker exec -it webserver bash
root@b1a0dc2f37e9:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

### 不要なリソースのクリーンアップ

使用していないコンテナ、イメージ、ネットワーク、ボリュームを削除するには `docker system prune` を使用します。

```console
$ docker system prune
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all dangling images
  - all dangling build cache

Are you sure you want to continue? [y/N] y
Deleted Containers:
f9a3...

Total reclaimed space: 1.2GB
```

### Dockerfileのベストプラクティス

- マルチステージビルドを使用して最終イメージのサイズを小さくする
- キャッシュを効率的に利用するため、変更頻度の低いレイヤーを先に配置する
- 必要最小限のファイルだけをコピーする（.dockerignoreファイルを活用）

## よくある質問

#### Q1. Dockerとは何ですか？
A. Dockerはコンテナ化技術を使用して、アプリケーションとその依存関係を一緒にパッケージ化し、どの環境でも同じように実行できるようにするプラットフォームです。

#### Q2. DockerとVMの違いは何ですか？
A. VMは完全なOSを仮想化しますが、DockerコンテナはホストOSのカーネルを共有し、アプリケーションの実行に必要な部分だけを含むため、より軽量で起動が速いです。

#### Q3. Docker Hubとは何ですか？
A. Docker Hubは、Dockerの公式イメージリポジトリで、様々なアプリケーションやOSのイメージを公開・共有できるプラットフォームです。`docker pull` コマンドでイメージをダウンロードできます。

#### Q4. コンテナ内のデータを永続化するにはどうすればよいですか？
A. ボリュームを使用します。`docker run -v ホストパス:コンテナパス` または `docker volume create` と `docker run --mount` を使用してデータを永続化できます。

## macOSでの注意点

macOSでDockerを実行する場合、以下の点に注意してください：

1. macOSではDocker Desktopをインストールする必要があります
2. リソース制限：CPUやメモリなどのリソース割り当てはDocker Desktopの設定から調整できます
3. ファイル共有：デフォルトでは `/Users` ディレクトリのみがDockerコンテナからアクセス可能です。他のディレクトリを使用する場合は、Docker Desktopの設定で「File sharing」を設定する必要があります
4. パフォーマンス：macOSでのDockerはLinuxと比較して若干パフォーマンスが低下する場合があります

## 参考

https://docs.docker.com/engine/reference/commandline/cli/

## 改訂

- 2025/04/30 初版作成