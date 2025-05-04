# docker-compose コマンド

複数のDockerコンテナを定義して実行するためのツールです。

## 概要

Docker Composeは、複数のDockerコンテナで構成されるアプリケーションを定義・実行するためのツールです。YAMLファイルを使用してサービス、ネットワーク、ボリュームを設定し、単一のコマンドですべてのサービスを起動できます。アプリケーションの一部として連携する複数のコンテナを管理するプロセスを簡素化します。

## オプション

### **-f, --file FILE**

別のComposeファイルを指定します（デフォルト: docker-compose.yml）

```console
$ docker-compose -f custom-compose.yml up
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_db_1  ... done
```

### **-p, --project-name NAME**

別のプロジェクト名を指定します（デフォルト: ディレクトリ名）

```console
$ docker-compose -p myproject up
Creating network "myproject_default" with the default driver
Creating myproject_web_1 ... done
Creating myproject_db_1  ... done
```

### **--verbose**

より詳細な出力を表示します

```console
$ docker-compose --verbose up
compose.config.config.find: Using configuration files: ./docker-compose.yml
docker.auth.find_config_file: Trying paths: ['/home/user/.docker/config.json', '/home/user/.dockercfg']
docker.auth.find_config_file: Found file at path: /home/user/.docker/config.json
...
```

### **--log-level LEVEL**

ログレベルを設定します（DEBUG, INFO, WARNING, ERROR, CRITICAL）

```console
$ docker-compose --log-level INFO up
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_db_1  ... done
```

## 一般的なコマンド

### **up**

コンテナを作成して起動します

```console
$ docker-compose up -d
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_db_1  ... done
```

### **down**

コンテナ、ネットワーク、イメージ、ボリュームを停止して削除します

```console
$ docker-compose down
Stopping myapp_web_1 ... done
Stopping myapp_db_1  ... done
Removing myapp_web_1 ... done
Removing myapp_db_1  ... done
Removing network myapp_default
```

### **ps**

コンテナを一覧表示します

```console
$ docker-compose ps
    Name                  Command               State           Ports
-----------------------------------------------------------------------------
myapp_db_1    docker-entrypoint.sh mysqld      Up      3306/tcp, 33060/tcp
myapp_web_1   docker-php-entrypoint php-fpm    Up      9000/tcp
```

### **logs**

コンテナからの出力を表示します

```console
$ docker-compose logs
Attaching to myapp_web_1, myapp_db_1
db_1   | 2025-05-04T10:15:30.123456Z 0 [Note] mysqld: ready for connections.
web_1  | [04-May-2025 10:15:32] NOTICE: fpm is running, pid 1
```

### **exec**

実行中のコンテナでコマンドを実行します

```console
$ docker-compose exec web php -v
PHP 8.2.0 (cli) (built: Dec 6 2024) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.2.0, Copyright (c) Zend Technologies
```

### **build**

サービスをビルドまたは再ビルドします

```console
$ docker-compose build
Building web
Step 1/10 : FROM php:8.2-fpm
 ---> 123456789abc
Step 2/10 : WORKDIR /var/www/html
 ---> Using cache
 ---> abcdef123456
...
Successfully built 987654321fed
Successfully tagged myapp_web:latest
```

## 使用例

### データベース付きの基本的なWebアプリケーション

```console
$ cat docker-compose.yml
version: '3'
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: myapp

$ docker-compose up -d
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_db_1  ... done
```

### サービスのスケーリング

```console
$ docker-compose up -d --scale web=3
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_web_2 ... done
Creating myapp_web_3 ... done
Creating myapp_db_1  ... done
```

## ヒント:

### 環境変数を使用する

パスワードなどの機密情報は、docker-compose.ymlファイルにハードコーディングするのではなく、`.env`ファイルに保存しましょう。

```console
$ cat .env
DB_PASSWORD=secretpassword

$ cat docker-compose.yml
version: '3'
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
```

### プロファイルを使用して選択的にサービスを起動する

プロファイルを使用すると、必要なサービスのみを起動できます。

```console
$ cat docker-compose.yml
version: '3.9'
services:
  app:
    image: myapp
  db:
    image: mysql
  test:
    image: myapp-test
    profiles:
      - testing

$ docker-compose --profile testing up
```

### Docker Compose オーバーライドファイルを使用する

メインのComposeファイルを変更せずに設定を上書きするには、`docker-compose.override.yml`ファイルを作成します。

```console
$ cat docker-compose.yml
version: '3'
services:
  web:
    image: nginx

$ cat docker-compose.override.yml
version: '3'
services:
  web:
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
```

## よくある質問

#### Q1. `docker-compose up`と`docker-compose up -d`の違いは何ですか？
A. `docker-compose up`はコンテナを起動し、その出力をターミナルに表示します。`-d`フラグ（デタッチドモード）を使用すると、コンテナをバックグラウンドで実行します。

#### Q2. 他のサービスに影響を与えずに単一のサービスを更新するにはどうすればよいですか？
A. `docker-compose up -d --no-deps --build service_name`を使用すると、依存サービスを再起動せずに特定のサービスを再ビルドして更新できます。

#### Q3. 特定のサービスのログを表示するにはどうすればよいですか？
A. `docker-compose logs service_name`を使用して特定のサービスのログを表示できます。リアルタイムでログを追跡するには`-f`を追加します。

#### Q4. Docker Composeを本番環境で使用できますか？
A. Docker Composeは本番環境でも使用できますが、追加のオーケストレーション機能があるDocker SwarmやKubernetesが本番デプロイメントには好まれることが多いです。

#### Q5. 未使用のボリュームをクリーンアップするにはどうすればよいですか？
A. `docker-compose down -v`を使用すると、Composeファイルで定義されたコンテナ、ネットワーク、ボリュームを削除できます。

## 参考資料

https://docs.docker.com/compose/reference/

## 改訂履歴

2025/05/04 初版作成