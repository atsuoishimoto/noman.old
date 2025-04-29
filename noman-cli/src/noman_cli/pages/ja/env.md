# env

環境変数を表示したり、指定した環境変数の下でコマンドを実行したりするためのコマンドです。

## オプション

### **-i, --ignore-environment**

すべての継承された環境変数を無視して、空の環境でコマンドを実行します。

```bash
$ env -i bash -c 'echo $PATH'

```

上記の例では、空の環境で新しいbashシェルを起動し、PATHが設定されていないことを確認しています。

### **-u, --unset=NAME**

指定した環境変数を削除してからコマンドを実行します。

```bash
$ env -u HOME echo $HOME

```

この例では、HOME環境変数を削除してからechoコマンドを実行しています。

### **NAME=VALUE**

指定した環境変数を設定してからコマンドを実行します。

```bash
$ env LANG=ja_JP.UTF-8 date
2023年 4月 10日 月曜日 15:30:45 JST
```

この例では、LANG環境変数を日本語に設定してからdateコマンドを実行しています。

## 使用例

### 現在の環境変数をすべて表示

```bash
$ env
TERM=xterm-256color
SHELL=/bin/bash
USER=username
PATH=/usr/local/bin:/usr/bin:/bin
PWD=/home/username
HOME=/home/username
...
```

### 特定の環境変数を設定してコマンドを実行

```bash
$ env HTTP_PROXY=http://proxy.example.com:8080 curl example.com
<!doctype html>
<html>
...
</html>
```

### 環境変数を追加・変更してコマンドを実行

```bash
$ env PATH=$PATH:/opt/custom/bin DEBUG=true python script.py
デバッグモードで実行中...
```

## よくある質問

### Q1. envコマンドとprintenvコマンドの違いは何ですか？
A. `env`は環境変数の表示だけでなく、環境変数を設定してコマンドを実行する機能も持っています。一方、`printenv`は環境変数の表示のみを行います。

### Q2. 特定の環境変数だけを表示するにはどうすればいいですか？
A. `env | grep 変数名` を使用します。例えば、`env | grep PATH` とすると、PATH関連の環境変数だけが表示されます。

### Q3. 一時的に環境変数を変更するにはどうすればいいですか？
A. `env 変数名=値 コマンド` の形式で実行します。これにより、現在のシェルの環境変数は変更されず、指定したコマンドの実行時のみ環境変数が変更されます。

## 追加情報

- `env`コマンドは、異なる環境設定でプログラムをテストする際に非常に便利です。
- スクリプトの先頭に `#!/usr/bin/env プログラム名` と記述することで、環境に依存しないシバン（shebang）行を作成できます。
- macOSでは、`env`コマンドはBSD由来のバージョンが使用されており、GNU版と若干オプションが異なる場合があります。

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/env-invocation.html