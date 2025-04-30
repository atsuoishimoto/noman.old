# docker build コマンド

Dockerイメージを構築するためのコマンドです。

## 概要

`docker build` コマンドは、Dockerfileと呼ばれる指示ファイルからDockerイメージを作成します。このコマンドは、アプリケーションとその依存関係を含む一貫した実行環境を構築するために使用されます。

## オプション

### **-t, --tag**

イメージに名前とオプションでタグを付けます。

```console
$ docker build -t myapp:1.0 .
[+] Building 10.5s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 215B                                       0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/node:14                 1.2s
 => [1/5] FROM docker.io/library/node:14@sha256:fcb6...                    0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 3.25kB                                        0.0s
 => CACHED [2/5] WORKDIR /app                                              0.0s
 => [3/5] COPY package*.json ./                                            0.1s
 => [4/5] RUN npm install                                                  8.2s
 => [5/5] COPY . .                                                         0.1s
 => exporting to image                                                     0.7s
 => => exporting layers                                                    0.7s
 => => writing image sha256:a1b2c3...                                      0.0s
 => => naming to docker.io/library/myapp:1.0                               0.0s
```

### **-f, --file**

Dockerfileの名前と場所を指定します。デフォルトは現在のディレクトリの `Dockerfile` です。

```console
$ docker build -f Dockerfile.dev -t myapp:dev .
[+] Building 8.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile.dev                   0.1s
 => => transferring dockerfile: 240B                                       0.0s
...
```

### **--no-cache**

ビルド時にキャッシュを使用しないようにします。

```console
$ docker build --no-cache -t myapp:latest .
[+] Building 25.3s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
...
```

### **--build-arg**

Dockerfile内のARG命令で定義された変数に値を渡します。

```console
$ docker build --build-arg VERSION=2.0 -t myapp:2.0 .
[+] Building 12.1s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
...
```

## 使用例

### 基本的なイメージのビルド

```console
$ docker build .
[+] Building 15.2s (10/10) FINISHED
...
```

カレントディレクトリのDockerfileを使用してイメージをビルドしています。

### タグ付きイメージのビルド

```console
$ docker build -t mycompany/myapp:1.0 -t mycompany/myapp:latest .
[+] Building 14.7s (10/10) FINISHED
...
```

複数のタグを付けてイメージをビルドしています。

### 特定のコンテキストからのビルド

```console
$ docker build -t myapp:1.0 https://github.com/user/repo.git#main
[+] Building 18.3s (10/10) FINISHED
...
```

GitリポジトリからDockerfileとビルドコンテキストを取得してビルドしています。

## ヒント:

### .dockerignoreファイルを使用する

`.dockerignore` ファイルを作成して、ビルドコンテキストから除外するファイルやディレクトリを指定できます。これによりビルド速度が向上し、イメージサイズも小さくなります。

### マルチステージビルドを活用する

本番環境用のイメージサイズを小さくするために、マルチステージビルドを使用しましょう。ビルドステージで依存関係をインストールし、実行ステージには必要なファイルだけをコピーします。

### キャッシュを効率的に使う

Dockerfileの命令順序を工夫して、変更が少ない命令（依存関係のインストールなど）を先に配置し、頻繁に変更されるコード部分を後ろに配置することで、キャッシュを効率的に活用できます。

## よくある質問

#### Q1. docker buildとdocker-composeの違いは何ですか？
A. `docker build`は単一のイメージを構築するコマンドです。一方、`docker-compose`は複数のコンテナを定義し、管理するためのツールで、`docker-compose build`でまとめてイメージをビルドできます。

#### Q2. ビルド中にエラーが発生した場合はどうすればよいですか？
A. エラーメッセージを確認し、問題のあるDockerfileの行を修正します。`--no-cache`オプションを使用して完全に新しいビルドを試すこともできます。

#### Q3. イメージサイズを小さくするにはどうすればよいですか？
A. マルチステージビルドの使用、不要なファイルの削除、軽量ベースイメージ（Alpine Linuxなど）の使用、RUN命令の結合などが効果的です。

#### Q4. ビルド時に環境変数を渡すにはどうすればよいですか？
A. `--build-arg`オプションを使用して、Dockerfile内のARG命令で定義された変数に値を渡すことができます。

## 参考資料

https://docs.docker.com/engine/reference/commandline/build/

## Revisions

- 2025/04/30 初版作成