# env コマンド

現在の環境変数を表示または変更します。

## 概要

`env` コマンドは、現在のシェル環境の環境変数を表示したり、一時的に環境変数を設定してコマンドを実行したりするために使用します。環境変数はシステム全体やプログラムの動作に影響を与える設定値で、プロセスが利用できる情報を保持しています。

## オプション

### **-i, --ignore-environment**

すべての継承された環境変数を無視して、クリーンな環境でコマンドを実行します。

```console
$ env -i python3 -c "import os; print(os.environ)"
{}
```

### **-u, --unset=NAME**

指定した環境変数を削除します。

```console
$ env -u HOME python3 -c "import os; print('HOME' in os.environ)"
False
```

### **--**

それ以降の引数をオプションとして解釈しないようにします。

```console
$ env -- echo $HOME
/home/user
```

## 使用例

### 現在の環境変数をすべて表示する

```console
$ env
SHELL=/bin/bash
USER=username
PATH=/usr/local/bin:/usr/bin:/bin
PWD=/home/username
HOME=/home/username
...
```

### 一時的に環境変数を設定してコマンドを実行する

```console
$ env DEBUG=true python3 app.py
デバッグモードで起動しています
```

### 特定の環境変数だけを表示する

```console
$ env | grep PATH
PATH=/usr/local/bin:/usr/bin:/bin
```

## ヒント:

### 環境変数のソート表示

`env` の出力を `sort` コマンドにパイプすると、アルファベット順に環境変数を表示できます。

```console
$ env | sort
HOME=/home/user
PATH=/usr/local/bin:/usr/bin:/bin
SHELL=/bin/bash
...
```

### 環境変数の一時的な変更

スクリプトやプログラムをテストする際に、環境変数を一時的に変更して実行できます。これはグローバルな環境を変更せずにテストするのに便利です。

```console
$ env NODE_ENV=production node server.js
本番モードでサーバーを起動しています
```

### 環境変数の数を確認する

現在設定されている環境変数の数を確認するには、次のコマンドを使用します。

```console
$ env | wc -l
53
```

## よくある質問

#### Q1. `env` と `export` の違いは何ですか？
A. `env` はコマンドを実行する際に一時的に環境変数を設定しますが、`export` はシェルセッション中に永続的に環境変数を設定します。

#### Q2. 環境変数を永続的に設定するにはどうすればよいですか？
A. `.bashrc`、`.bash_profile`、`.zshrc` などのシェル設定ファイルに `export VAR=value` の形式で追加します。

#### Q3. 特定のプログラムだけに環境変数を設定するにはどうすればよいですか？
A. `env VAR=value command` の形式で実行します。これにより、そのコマンドの実行中だけ環境変数が設定されます。

#### Q4. 環境変数をクリアしてコマンドを実行するにはどうすればよいですか？
A. `env -i command` を使用すると、すべての環境変数をクリアした状態でコマンドを実行できます。

## macOSでの注意点

macOSでは、システム全体の環境変数は `/etc/launchd.conf` や `~/.launchd.conf` で設定できますが、最新のmacOSバージョンではこの方法は推奨されていません。代わりに、`~/.zshrc`（または使用しているシェルの設定ファイル）で環境変数を設定することをお勧めします。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html

## 改訂履歴

- 2025/04/30 初版作成