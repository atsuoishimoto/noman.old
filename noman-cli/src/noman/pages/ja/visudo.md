# visudo コマンド

sudoers ファイルを構文チェック付きで安全に編集します。

## 概要

`visudo` は `/etc/sudoers` ファイルを安全に編集するためのコマンドラインユーティリティです。sudoers ファイルは sudo アクセス権限を制御します。visudo は同時編集を防ぐためにファイルをロックし、変更を保存する前に構文チェックを行い、ユーザーがシステムからロックアウトされる可能性のある設定エラーを防止します。

## オプション

### **-c, --check**

sudoers ファイルの構文エラーのみをチェックし、変更は行いません。

```console
$ sudo visudo -c
/etc/sudoers: parsed OK
/etc/sudoers.d/custom: parsed OK
```

### **-f, --file=file**

デフォルトの `/etc/sudoers` の代わりに、別の sudoers ファイルの場所を指定します。

```console
$ sudo visudo -f /etc/sudoers.d/custom
```

### **-q, --quiet**

静かモードを有効にし、ほとんどの警告メッセージを抑制します。

```console
$ sudo visudo -q -c
```

### **-s, --strict**

sudoers ファイルの厳格なチェックを有効にします。構文解析エラーがある場合、visudo はエラーで終了します。

```console
$ sudo visudo -s -f /etc/sudoers.d/test
>>> /etc/sudoers.d/test: syntax error near line 2 <<<
parse error in /etc/sudoers.d/test near line 2
visudo: fatal error, exiting.
```

## 使用例

### 基本的な使用法

```console
$ sudo visudo
```

これにより、EDITOR 環境変数で指定されたエディタでデフォルトの `/etc/sudoers` ファイルが開きます。

### カスタム Sudoers ファイルの編集

```console
$ sudo visudo -f /etc/sudoers.d/local
```

これにより、`/etc/sudoers.d` ディレクトリにあるカスタム sudoers ファイルが開きます。

### 編集せずに構文をチェック

```console
$ sudo visudo -c
/etc/sudoers: parsed OK
/etc/sudoers.d/custom: parsed OK
```

## ヒント:

### 好みのエディタを設定する

visudo を実行する前に、EDITOR または VISUAL 環境変数を設定して好みのエディタを指定できます：

```console
$ export EDITOR=nano
$ sudo visudo
```

### 直接編集ではなくインクルードを使用する

メインの sudoers ファイルを編集する代わりに、カスタム設定用に `/etc/sudoers.d/` に別ファイルを作成しましょう。これにより管理が容易かつ安全になります。

```console
$ sudo visudo -f /etc/sudoers.d/myusers
```

### 終了前に必ず構文チェックを行う

sudoers ファイルを編集する際は、保存前に必ず visudo の組み込み構文チェックを使用してください。構文エラーがある場合、visudo は警告を表示し、保存前に修正する機会を与えてくれます。

## よくある質問

#### Q1. visudo を使わずに直接 sudoers ファイルを編集するとどうなりますか？
A. `/etc/sudoers` を通常のテキストエディタで直接編集することは危険です。構文エラーを導入すると、sudo アクセスが完全に失われ、管理機能からロックアウトされる可能性があります。

#### Q2. 新しいユーザーを sudoers に追加するにはどうすればよいですか？
A. `sudo visudo` を実行し、`username ALL=(ALL:ALL) ALL` のような行を追加することで、ユーザーに完全な sudo 権限を付与できます。

#### Q3. /etc/sudoers と /etc/sudoers.d/ 内のファイルの違いは何ですか？
A. メインの `/etc/sudoers` ファイルは主要な設定ファイルであり、`/etc/sudoers.d/` はメイン設定に含まれる追加設定ファイル用のディレクトリです。このディレクトリに別ファイルを使用する方が、より整理された安全な方法です。

#### Q4. visudo が使用するデフォルトエディタを変更するにはどうすればよいですか？
A. visudo を実行する前に EDITOR または VISUAL 環境変数を設定します：`export EDITOR=nano`

## 参考資料

https://www.sudo.ws/docs/man/1.9.13/visudo.man/

## 改訂履歴

- 2025/05/04 初回改訂