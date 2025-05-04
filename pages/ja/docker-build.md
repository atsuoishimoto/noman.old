# docker build コマンド

Dockerfileからイメージをビルドします。

## 概要

`docker build`コマンドは、DockerfileとコンテキストからDockerイメージをビルドします。コンテキストとは、指定されたPATHまたはURLにある一連のファイルのことです。ビルドプロセスはコンテキスト内のどのファイルも参照できます。Dockerfileには、Dockerが新しいイメージを作成するための指示が含まれています。

## オプション

### **-t, --tag**

ビルドしたイメージに名前とオプションでタグを「名前:タグ」形式で付けます。

```console
$ docker build -t myapp:1.0 .
[+] Building 10.5s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 215B                                       0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/node:14                 1.2s
 => [1/5] FROM docker.io/library/node:14@sha256:123abc...                  0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 32.5kB                                        0.0s
 => [2/5] WORKDIR /app                                                     0.3s
 => [3/5] COPY package*.json ./                                            0.1s
 => [4/5] RUN npm install                                                  7.5s
 => [5/5] COPY . .                                                         0.1s
 => exporting to image                                                     1.1s
 => => exporting layers                                                    1.1s
 => => writing image sha256:def456...                                      0.0s
 => => naming to docker.io/library/myapp:1.0                               0.0s
```

### **-f, --file**

Dockerfileの名前を指定します（デフォルトは「PATH/Dockerfile」）。

```console
$ docker build -f Dockerfile.prod -t myapp:prod .
[+] Building 12.3s (10/10) FINISHED
 => [internal] load build definition from Dockerfile.prod                  0.1s
 => => transferring dockerfile: 256B                                       0.0s
...
```

### **--no-cache**

イメージのビルド時にキャッシュを使用しません。

```console
$ docker build --no-cache -t myapp .
[+] Building 25.7s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
...
```

### **--build-arg**

Dockerfile内でARG命令を使用して定義されたビルド時変数を設定します。

```console
$ docker build --build-arg NODE_ENV=production -t myapp .
[+] Building 11.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
...
```

### **--target**

マルチステージビルドを使用する際にビルドするターゲットステージを設定します。

```console
$ docker build --target development -t myapp:dev .
[+] Building 8.3s (8/8) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
 => [internal] load .dockerignore                                          0.0s
 => [internal] load metadata for docker.io/library/node:14                 1.2s
 => [development 1/4] FROM docker.io/library/node:14@sha256:123abc...      0.0s
...
```

## 使用例

### タグ付きでイメージをビルドする

```console
$ docker build -t myapp:latest .
[+] Building 15.2s (10/10) FINISHED
...
```

### 複数のタグでビルドする

```console
$ docker build -t myapp:latest -t myapp:1.0 -t registry.example.com/myapp:latest .
[+] Building 14.8s (10/10) FINISHED
...
```

### 特定のコンテキストからビルドする

```console
$ docker build -t myapp https://github.com/user/repo.git#main
[+] Building 22.5s (10/10) FINISHED
...
```

### 特定のDockerfileとターゲットステージでビルドする

```console
$ docker build -f Dockerfile.multistage --target production -t myapp:prod .
[+] Building 18.7s (12/12) FINISHED
...
```

## ヒント:

### .dockerignoreファイルを使用する

`.dockerignore`ファイルを作成して、ビルドコンテキストからファイルやディレクトリを除外しましょう。これにより、不要なファイルがDockerデーモンに送信されるのを防ぎ、ビルド時間とサイズを削減できます。

### ビルドキャッシュを活用する

Dockerは中間レイヤーをキャッシュします。キャッシュの使用を最大化するために、Dockerfileのコマンドを変更頻度の低いものから高いものへと順序付けましょう。例えば、アプリケーションコードをコピーする前に依存関係をインストールします。

### マルチステージビルドを活用する

マルチステージビルドでは、Dockerfile内で複数のFROM文を使用できます。これはビルドステージから必要なアーティファクトのみをコピーすることで、より小さな本番イメージを作成するのに役立ちます。

### レイヤー数を最小限に抑える

関連するコマンドを単一のRUN命令内で`&&`を使って結合することで、レイヤー数を減らし、より小さなイメージを作成できます。

## よくある質問

#### Q1. `docker build`と`docker image build`の違いは何ですか？
A. 両者は同じコマンドです。`docker image build`はDockerのコマンド再構成で導入されたより明示的な形式ですが、`docker build`も引き続きサポートされており、より一般的に使用されています。

#### Q2. キャッシュを使用せずにイメージをビルドするにはどうすればよいですか？
A. `--no-cache`オプションを使用します：`docker build --no-cache -t myapp .`

#### Q3. ビルドプロセスに環境変数を渡すにはどうすればよいですか？
A. `--build-arg`オプションを使用します：`docker build --build-arg VAR_NAME=value -t myapp .`

#### Q4. マルチステージDockerfileで特定のステージをビルドするにはどうすればよいですか？
A. `--target`オプションを使用します：`docker build --target stage_name -t myapp .`

#### Q5. Gitリポジトリからビルドできますか？
A. はい、ビルドコンテキストとしてGitリポジトリのURLを指定できます：`docker build -t myapp https://github.com/user/repo.git`

## 参考資料

https://docs.docker.com/engine/reference/commandline/build/

## 改訂履歴

- 2025/05/04 初回改訂