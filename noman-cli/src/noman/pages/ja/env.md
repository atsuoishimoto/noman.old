# env コマンド

現在の環境変数を表示したり、変更された環境で指定したコマンドを実行したりします。

## 概要

`env` コマンドは、すべての環境変数を表示したり、変更された環境でプログラムを実行したりすることができます。環境変数は、システム上でプロセスの実行に影響を与える名前と値のペアです。このコマンドは、現在の環境を確認したり、一時的に環境変数を変更して単一のコマンドを実行したり、コマンドを実行する前に環境をクリアしたりする場合に便利です。

## オプション

### **-i, --ignore-environment**

空の環境から開始し、継承された環境変数を無視します。

```console
$ env -i bash -c 'echo $HOME'

```

### **-u, --unset=NAME**

指定した NAME 変数を環境から削除します。

```console
$ env -u HOME bash -c 'echo $HOME'

```

### **-0, --null**

各出力行を改行ではなくヌル文字で終了します。

```console
$ env -0 | tr '\0' '\n' | head -3
TERM=xterm-256color
SHELL=/bin/bash
USER=username
```

### **--help**

ヘルプ情報を表示して終了します。

```console
$ env --help
Usage: env [OPTION]... [-] [NAME=VALUE]... [COMMAND [ARG]...]
Set each NAME to VALUE in the environment and run COMMAND.
...
```

### **--version**

バージョン情報を表示して終了します。

```console
$ env --version
env (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
...
```

## 使用例

### すべての環境変数を表示する

```console
$ env
SHELL=/bin/bash
USER=username
HOME=/home/username
PATH=/usr/local/bin:/usr/bin:/bin
PWD=/home/username
LANG=en_US.UTF-8
...
```

### 変更された環境でコマンドを実行する

```console
$ env DEBUG=true NODE_ENV=development node app.js
```

### 環境をクリアしてからコマンドを実行する

```console
$ env -i PATH=/bin:/usr/bin HOME=/tmp bash -c 'echo $HOME'
/tmp
```

### 複数の環境変数を設定してコマンドを実行する

```console
$ env LANG=ja_JP.UTF-8 TZ=Asia/Tokyo date
2025年 5月 4日 日曜日 12:00:00 JST
```

## ヒント:

### 特定の環境変数を表示する

`env | grep PATTERN` を使用して、特定の環境変数をフィルタリングして見つけることができます：

```console
$ env | grep PATH
PATH=/usr/local/bin:/usr/bin:/bin
MANPATH=/usr/local/man:/usr/local/share/man:/usr/share/man
```

### 一時的な環境変更

`env` コマンドは、現在のシェルセッションではなく、実行されるコマンドの環境のみを変更します。永続的な変更を行うには、シェルの設定ファイルを変更する必要があります。

### 環境の問題のデバッグ

アプリケーションの問題をトラブルシューティングする際は、`env` を使用して特定の環境変数でアプリケーションを実行し、設定の問題を特定するのに役立ちます。

### セキュリティに関する考慮事項

スクリプトで `env -i` を使用する場合は注意が必要です。PATHなどの重要な環境変数が削除されます。このオプションを使用する場合は、常に必要最小限の変数を指定してください。

## よくある質問

#### Q1. `env` と `export` の違いは何ですか？
A. `env` は環境変数を表示したり、変更された環境変数でコマンドを実行したりしますが、変更はそのコマンドにのみ影響します。`export` は変数を現在のシェルのすべての子プロセスで利用できるようにします。

#### Q2. 環境変数を永続的に設定するにはどうすればよいですか？
A. `env` は一時的にのみ変数を設定します。永続的な変更を行うには、シェルの設定ファイル（~/.bashrcや~/.zshrcなど）にexportコマンドを追加してください。

#### Q3. `env` を使用して複数の変数を一度に削除できますか？
A. はい、複数の `-u` オプションを使用できます：`env -u VAR1 -u VAR2 command`

#### Q4. コマンドを実行する前にすべての環境変数をクリアするにはどうすればよいですか？
A. `env -i command` を使用して空の環境から開始し、必要な変数のみを追加してください。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html

## 改訂履歴

- 2025/05/04 初版作成