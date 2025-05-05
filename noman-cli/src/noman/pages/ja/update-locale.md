# update-locale コマンド

システム全体のロケール設定を `/etc/default/locale` ファイルを更新することで設定します。

## 概要

`update-locale` コマンドは、Debian系Linuxディストリビューションでシステム全体のロケール設定を変更するために使用されます。このコマンドは `/etc/default/locale` ファイルを更新し、システムやアプリケーションで使用される言語、文字エンコーディング、地域フォーマットの設定を定義する環境変数を設定します。

## オプション

### **--reset**

`/etc/default/locale` ファイルを削除することですべてのロケール変数をリセットします

```console
$ sudo update-locale --reset
```

### **VARIABLE=value**

特定のロケール変数を指定した値に設定します

```console
$ sudo update-locale LANG=ja_JP.UTF-8
```

### **--locale-file=FILE**

デフォルトの `/etc/default/locale` の代わりに別のロケールファイルを指定します

```console
$ sudo update-locale --locale-file=/path/to/custom/locale
```

## 使用例

### システム言語を日本語に設定する

```console
$ sudo update-locale LANG=ja_JP.UTF-8
```

### 複数のロケール変数を一度に設定する

```console
$ sudo update-locale LANG=ja_JP.UTF-8 LC_TIME=ja_JP.UTF-8 LC_PAPER=ja_JP.UTF-8
```

### 特定のロケール変数を削除する

```console
$ sudo update-locale LC_PAPER=
```

## ヒント:

### 現在のロケール設定を確認する

変更を行う前に、`locale` コマンドで現在のロケール設定を確認し、何を変更するのかを理解しておくとよいでしょう。

```console
$ locale
LANG=ja_JP.UTF-8
LC_CTYPE="ja_JP.UTF-8"
LC_NUMERIC="ja_JP.UTF-8"
...
```

### 必要なロケールを先に生成する

使用したいロケールがシステムで生成されていることを確認してください。`locale -a` で利用可能なロケールを一覧表示し、不足しているロケールは `sudo locale-gen <locale>` で生成できます。

### システム再起動が必要な場合がある

ロケール設定の変更は、すべてのアプリケーションに完全に反映されるためにシステムの再起動、または少なくともログアウト/ログインが必要な場合があります。

## よくある質問

#### Q1. LANGとLC_ALLの違いは何ですか？
A. `LANG` は特定の `LC_*` 変数が設定されていない場合のすべてのカテゴリのデフォルトロケールです。`LC_ALL` は `LANG` を含む他のすべてのロケール変数よりも優先されます。

#### Q2. システムを英語インターフェースで使用しながら、ローカルフォーマットを使うにはどうすればよいですか？
A. `LANG` を希望する英語ロケール（例：`en_US.UTF-8`）に設定し、`LC_TIME` や `LC_MONETARY` などの特定の `LC_*` 変数をローカルフォーマットに設定します。

#### Q3. 一部のアプリケーションが私のロケール設定を無視するのはなぜですか？
A. 一部のアプリケーションはシステムロケールを上書きする独自の言語設定を持っているか、設定したロケールをサポートしていない可能性があります。

#### Q4. すべてのロケール設定を完全にリセットするにはどうすればよいですか？
A. `sudo update-locale --reset` を使用して、システム設定ファイルからすべてのロケール設定を削除できます。

## 参考資料

https://manpages.debian.org/bullseye/locales/update-locale.8.en.html

## 改訂履歴

- 2025/05/04 初回改訂