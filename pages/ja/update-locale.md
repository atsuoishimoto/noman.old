# update-locale コマンド

システムのロケール設定を表示または変更するコマンド。

## 概要

`update-locale`は、Linuxシステム（特にDebian系ディストリビューション）でシステム全体のロケール設定を管理するためのコマンドです。ロケールとは、言語、日付形式、数値形式などの地域固有の設定のことで、このコマンドを使用することで、これらの設定を簡単に変更できます。

## オプション

### **--help**

ヘルプメッセージを表示します。

```console
$ update-locale --help
Usage: update-locale [OPTIONS] [VARIABLE=VALUE ...]
Options:
  --help                   このヘルプを表示する
  --reset                  すべてのロケール変数をリセットする
  --no-checks              変数の値をチェックしない
```

### **--reset**

すべてのロケール設定をリセットします。

```console
$ sudo update-locale --reset
```

### **VARIABLE=VALUE**

特定のロケール変数を設定します。

```console
$ sudo update-locale LANG=ja_JP.UTF-8
```

## 使用例

### 現在のロケール設定を表示する

```console
$ update-locale
LANG=en_US.UTF-8
LANGUAGE=en_US:en
LC_CTYPE="en_US.UTF-8"
LC_NUMERIC="en_US.UTF-8"
LC_TIME="en_US.UTF-8"
LC_COLLATE="en_US.UTF-8"
LC_MONETARY="en_US.UTF-8"
LC_MESSAGES="en_US.UTF-8"
LC_PAPER="en_US.UTF-8"
LC_NAME="en_US.UTF-8"
LC_ADDRESS="en_US.UTF-8"
LC_TELEPHONE="en_US.UTF-8"
LC_MEASUREMENT="en_US.UTF-8"
LC_IDENTIFICATION="en_US.UTF-8"
```

### システム全体の言語を日本語に変更する

```console
$ sudo update-locale LANG=ja_JP.UTF-8
```

### 複数のロケール設定を一度に変更する

```console
$ sudo update-locale LANG=ja_JP.UTF-8 LC_TIME=ja_JP.UTF-8 LC_MESSAGES=en_US.UTF-8
```

## ヒント:

### 変更の反映

ロケール設定を変更した後は、変更を反映させるためにログアウトして再ログインするか、システムを再起動する必要があります。

### 利用可能なロケールの確認

設定する前に、システムで利用可能なロケールを確認するには以下のコマンドを使用します：

```console
$ locale -a
C
C.UTF-8
en_US.utf8
ja_JP.utf8
...
```

### 部分的なロケール設定

すべてのロケール設定を同じ値にする必要はありません。例えば、インターフェースは英語（`LANG=en_US.UTF-8`）で、日付形式は日本式（`LC_TIME=ja_JP.UTF-8`）というように設定できます。

## よくある質問

#### Q1. update-localeとlocaleコマンドの違いは何ですか？
A. `locale`コマンドは現在のロケール設定を表示するだけですが、`update-locale`はシステム全体のロケール設定を変更できます。

#### Q2. 変更したロケール設定はどこに保存されますか？
A. 通常は`/etc/default/locale`ファイルに保存されます。

#### Q3. 特定のユーザーだけのロケールを変更するにはどうすればいいですか？
A. `update-locale`はシステム全体の設定を変更します。特定のユーザーだけのロケールを変更するには、そのユーザーの`.bashrc`や`.profile`などの設定ファイルに`export LANG=ja_JP.UTF-8`のような行を追加します。

#### Q4. 設定したロケールが反映されない場合はどうすればいいですか？
A. 該当するロケールがシステムにインストールされているか確認してください。必要に応じて`sudo apt-get install language-pack-ja`などでロケールパッケージをインストールします。

## 参考資料

https://manpages.debian.org/buster/locales/update-locale.8.en.html

## 改訂履歴

- 2025/04/30 初版作成