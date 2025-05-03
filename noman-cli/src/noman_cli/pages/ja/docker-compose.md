# docker-compose コマンド

複数のコンテナを定義し、実行するためのツール。

## 概要

Docker Composeは、複数のDockerコンテナを定義し、一度に起動・管理するためのツールです。YAMLファイル（通常は`docker-compose.yml`）にアプリケーションの構成を記述し、単一のコマンドでアプリケーション全体の環境を構築・実行できます。開発環境、テスト環境、CI/CDパイプラインなどで広く使用されています。

## オプション

### **up**

コンテナを作成して起動します。

```console
$ docker-compose up
Creating network "myapp_default" with the default driver
Creating myapp_db_1    ... done
Creating myapp_web_1   ... done
Attaching to myapp_db_1, myapp_web_1
db_1   | 2025-04-30 12:34:56.789 UTC [1] LOG:  database system is ready to accept connections
web_1  | * Serving Flask app "app" (lazy loading)
```

### **down**

コンテナを停止して削除します。

```console
$ docker-compose down
Stopping myapp_web_1 ... done
Stopping myapp_db_1  ... done
Removing myapp_web_1 ... done
Removing myapp_db_1  ... done
Removing network myapp_default
```

### **ps**

実行中のコンテナを表示します。

```console
$ docker-compose ps
    Name                  Command               State           Ports
-----------------------------------------------------------------------------
myapp_db_1    docker-entrypoint.sh postgres    Up      5432/tcp
myapp_web_1   python app.py                    Up      0.0.0.0:5000->5000/tcp
```

### **logs**

コンテナのログを表示します。

```console
$ docker-compose logs
Attaching to myapp_db_1, myapp_web_1
db_1   | 2025-04-30 12:34:56.789 UTC [1] LOG:  database system is ready to accept connections
web_1  | * Serving Flask app "app" (lazy loading)
web_1  | * Environment: production
```

### **build**

サービスのイメージをビルドまたは再ビルドします。

```console
$ docker-compose build
Building web
Step 1/7 : FROM python:3.9-alpine
 ---> a1234567890b
Step 2/7 : WORKDIR /app
 ---> Using cache
 ---> c1234567890d
...
Successfully built f1234567890e
Successfully tagged myapp_web:latest
```

## 使用例

### 基本的な起動とバックグラウンド実行

```console
$ docker-compose up -d
Creating network "myapp_default" with the default driver
Creating myapp_db_1    ... done
Creating myapp_web_1   ... done
```

### 特定のサービスのみ起動

```console
$ docker-compose up -d db
Creating myapp_db_1 ... done
```

### コンテナ内でコマンドを実行

```console
$ docker-compose exec web python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
```

### スケーリング（複数のコンテナを起動）

```console
$ docker-compose up -d --scale web=3
Creating myapp_db_1    ... done
Creating myapp_web_1   ... done
Creating myapp_web_2   ... done
Creating myapp_web_3   ... done
```

## ヒント:

### 環境変数の利用

`.env`ファイルを作成すると、docker-composeが自動的に読み込みます。これにより、機密情報をバージョン管理から除外できます。

```console
$ cat .env
DB_PASSWORD=secret
$ docker-compose up -d
```

### 複数の設定ファイルを使用する

基本設定と環境固有の設定を分けることができます。

```console
$ docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

### ボリュームを使ったデータ永続化

データベースなどのデータを永続化するには、ボリュームを使用します。

```yaml
volumes:
  db-data:

services:
  db:
    image: postgres
    volumes:
      - db-data:/var/lib/postgresql/data
```

## よくある質問

#### Q1. docker-composeとdockerの違いは何ですか？
A. dockerは単一のコンテナを管理するためのコマンドであるのに対し、docker-composeは複数のコンテナからなるアプリケーション全体を定義・管理するためのツールです。

#### Q2. docker-compose.ymlファイルの基本構造は？
A. サービス（コンテナ）、ネットワーク、ボリュームの3つの主要セクションで構成されています。最低限、servicesセクションが必要です。

#### Q3. 本番環境でもdocker-composeを使うべきですか？
A. 小規模な本番環境では使用できますが、大規模な環境ではKubernetesなどのオーケストレーションツールの使用が推奨されます。

#### Q4. コンテナ間の通信はどのように行いますか？
A. サービス名をホスト名として使用できます。例えば、`web`サービスから`db`サービスに接続する場合、ホスト名として`db`を指定します。

## macOSでの注意点

macOSでは、Docker Desktopをインストールすると、docker-composeコマンドも一緒にインストールされます。ただし、ファイル共有のパフォーマンスが低下する場合があるため、頻繁にファイルを変更する開発環境では、ボリュームマウントの代わりにDocker volumesの使用を検討してください。

## 参考

https://docs.docker.com/compose/

## Revisions

- 2025/04/30 First revision