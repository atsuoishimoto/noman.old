# docker run コマンド

新しいコンテナを作成し、指定されたイメージから起動するコマンドです。

## 概要

`docker run` コマンドは、新しいコンテナを作成し、指定されたイメージから起動します。このコマンドは、イメージのダウンロード（必要な場合）、コンテナの作成、起動、そして指定されたコマンドの実行までを一度に行います。開発環境の構築、アプリケーションのテスト、本番環境へのデプロイなど、Dockerを使用する際の基本的なコマンドです。

## オプション

### **-i, --interactive**

コンテナの標準入力を開いたままにします。通常は `-t` オプションと組み合わせて使用します。

```console
$ docker run -i ubuntu
# 標準入力が開いたままになる
```

### **-t, --tty**

疑似TTY（ターミナル）を割り当てます。対話型シェルを使用する場合に便利です。

```console
$ docker run -it ubuntu bash
root@f8d9c7b6a5:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

### **--rm**

コンテナ終了時に自動的に削除します。一時的な作業やテストに便利です。

```console
$ docker run --rm alpine echo "Hello, World!"
Hello, World!
# コンテナは実行後に自動的に削除される
```

## 使用例

### 対話型シェルの起動

```console
$ docker run -it ubuntu bash
root@f8d9c7b6a5:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

このコマンドはUbuntuコンテナを対話モードで起動し、bashシェルを実行している。

### バックグラウンドでのWebサーバー起動

```console
$ docker run -d -p 8080:80 --name my-web-server nginx
b8a5f8d9c9e8f7d6e5c4b3a2
```

このコマンドはnginxコンテナをバックグラウンドで起動し、ホストの8080ポートをコンテナの80ポートにマッピングしている。

### 一時的なコンテナでのコマンド実行

```console
$ docker run --rm alpine ls -la
total 64
drwxr-xr-x    1 root     root          4096 Apr 30 12:34 .
drwxr-xr-x    1 root     root          4096 Apr 30 12:34 ..
-rwxr-xr-x    1 root     root             0 Apr 30 12:34 .dockerenv
drwxr-xr-x    2 root     root          4096 Mar 23 00:00 bin
drwxr-xr-x    5 root     root           340 Apr 30 12:34 dev
...
```

このコマンドはAlpineコンテナを起動してls -laコマンドを実行し、終了後にコンテナを削除している。

## ヒント:

### コンテナの名前付け

`--name` オプションを使用して、コンテナに分かりやすい名前を付けると、後で参照しやすくなります。

```console
$ docker run --name my-app-container nginx
```

### 環境変数の設定

`-e` または `--env` オプションを使用して、コンテナ内で使用する環境変数を設定できます。

```console
$ docker run -e DB_HOST=localhost -e DB_PORT=5432 my-app
```

### ボリュームマウントの活用

開発中は `-v` オプションを使ってソースコードをマウントすると、コンテナを再ビルドせずに変更を反映できます。

```console
$ docker run -v $(pwd):/app my-dev-image
```

## よくある質問

#### Q1. `-i` と `-t` オプションの違いは何ですか？
A. `-i`（interactive）はコンテナの標準入力を開いたままにし、`-t`（tty）は疑似ターミナルを割り当てます。通常は `-it` として一緒に使用し、対話型シェルを実現します。

#### Q2. コンテナを一時的に使用するにはどうすればよいですか？
A. `--rm` オプションを使用すると、コンテナが停止した後に自動的に削除されます。一時的な作業やテストに便利です。

#### Q3. コンテナ内で実行されるデフォルトのコマンドを上書きするにはどうすればよいですか？
A. `docker run` コマンドの最後にコマンドを指定することで、イメージのデフォルトコマンドを上書きできます。例：`docker run ubuntu echo "Hello"`

#### Q4. macOSでボリュームマウントが遅い場合はどうすればよいですか？
A. macOSでは、特に大量のファイルを扱う場合、ボリュームマウントのパフォーマンスが低下することがあります。Docker Desktop for Macの設定で、ファイル共有の最適化オプションを確認するか、Docker Volumeを使用することを検討してください。

## 参考文献

https://docs.docker.com/engine/reference/commandline/run/

## 改訂履歴

- 2025/04/30 -i, -t, --rmオプションの詳細説明を追加し、使用例を更新
- 2025/04/30 初版作成