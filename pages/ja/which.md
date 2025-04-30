# which コマンド

指定したコマンドの実行ファイルのパスを表示します。

## 概要

`which` コマンドは、シェルが実行するコマンドの完全なパスを特定するために使用されます。コマンド名を引数として与えると、環境変数 `PATH` に設定されているディレクトリを検索し、最初に見つかった実行可能ファイルのパスを表示します。これにより、どのバージョンのコマンドが実行されるかを確認できます。

## オプション

### **-a (--all)**

指定したコマンド名に一致するすべての実行可能ファイルを表示します。デフォルトでは最初に見つかったものだけを表示します。

```console
$ which -a python
/usr/bin/python
/usr/local/bin/python
```

### **-s (--silent)**

出力を表示せず、終了ステータスのみを返します。コマンドが見つかった場合は 0、見つからなかった場合は 1 を返します。

```console
$ which -s ls
$ echo $?
0
```

## 使用例

### 基本的な使い方

```console
$ which ls
/bin/ls
```

### 複数のコマンドを一度に検索

```console
$ which ls grep find
/bin/ls
/usr/bin/grep
/usr/bin/find
```

### 存在しないコマンドを検索

```console
$ which nonexistentcommand
which: no nonexistentcommand in (/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin)
```

## ヒント:

### エイリアスの確認

`which` はエイリアスを解決しません。エイリアスの実体を確認するには `type` コマンドを使用するとよいでしょう。

```console
$ alias ll='ls -l'
$ which ll
which: no ll in (/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin)
$ type ll
ll is aliased to 'ls -l'
```

### スクリプトの場所を確認

自作スクリプトがどこにインストールされているか確認するのに便利です。

```console
$ which my_script
/usr/local/bin/my_script
```

### PATH の優先順位を理解する

同じ名前のコマンドが複数存在する場合、`which` は `PATH` 環境変数の順序に従って最初に見つかったものを表示します。これにより、どのバージョンが実行されるかを確認できます。

## よくある質問

#### Q1. `which` と `whereis` の違いは何ですか？
A. `which` はコマンドの実行ファイルのパスのみを表示しますが、`whereis` はバイナリ、ソース、マニュアルページの場所も検索します。

#### Q2. `which` がコマンドを見つけられない場合はどうなりますか？
A. コマンドが見つからない場合、エラーメッセージを表示し、終了ステータス 1 を返します。

#### Q3. `which` はシェルの組み込みコマンドを検出できますか？
A. いいえ、`which` はシェルの組み込みコマンド（例：`cd`、`echo`）を検出できません。これらは実行ファイルではなくシェル自体の一部であるためです。

#### Q4. `which` と `type` の違いは何ですか？
A. `which` はコマンドの実行ファイルのパスのみを表示しますが、`type` はコマンドの種類（エイリアス、関数、組み込みコマンド、実行ファイル）も識別できます。

## macOS での注意点

macOSの `which` コマンドは GNU バージョンと若干動作が異なります。特に、macOS では `-a` オプションがサポートされていない場合があります。代わりに、すべてのパスを表示するには `whereis` コマンドを使用するか、Homebrew などでGNU版の coreutils をインストールして `gwhich` を使用することを検討してください。

## 参考資料

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/which.html

## 改訂履歴

- 2025/04/30 初版作成