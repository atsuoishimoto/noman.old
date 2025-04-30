# whoami コマンド

現在のユーザー名を表示します。

## 概要

`whoami` コマンドは、現在のシェルセッションで実行しているユーザーの名前（ユーザーID）を表示します。システム管理やスクリプト作成時に、現在どのユーザーとして操作しているかを確認するのに役立ちます。

## オプション

`whoami` コマンドは基本的にオプションなしで使用されることが多いですが、いくつかの一般的なオプションがあります。

### **--help**

ヘルプメッセージを表示します。

```console
$ whoami --help
使用法: whoami [オプション]...
現在の実効ユーザーIDに関連付けられたユーザー名を表示する

      --help     このヘルプを表示して終了
      --version  バージョン情報を表示して終了
```

### **--version**

バージョン情報を表示します。

```console
$ whoami --version
whoami (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
ライセンス GPLv3+: GNU GPL バージョン 3 以降 <https://gnu.org/licenses/gpl.html>.
これはフリーソフトウェアです: 自由に変更および配布できます.
法律の許す限り、　無保証　です.
```

## 使用例

### 基本的な使用法

```console
$ whoami
username
```

上記の例では、現在ログインしているユーザー名（この場合は「username」）が表示されています。

### スクリプト内での使用例

```console
$ echo "現在のユーザー: $(whoami)"
現在のユーザー: username
```

### sudo と組み合わせた使用例

```console
$ whoami
username
$ sudo whoami
root
```

通常のユーザーと、sudo（管理者権限）を使用した場合のユーザーの違いを確認できます。

## ヒント:

### ユーザー切り替え確認

`su` や `sudo` コマンドでユーザーを切り替えた後、正しく切り替わったかを確認するために使用できます。

### スクリプト内での条件分岐

シェルスクリプト内で現在のユーザーに基づいて処理を分岐させる際に役立ちます。

```bash
if [ "$(whoami)" = "root" ]; then
    echo "管理者として実行中です"
else
    echo "一般ユーザーとして実行中です"
fi
```

### 関連コマンド

`id` コマンドを使うと、ユーザー名だけでなくユーザーIDやグループ情報も表示できます。

## よくある質問

#### Q1. `whoami` と `who am i` の違いは何ですか？
A. `whoami` は現在の実効ユーザーを表示しますが、`who am i`（または `who -m`）はログイン時のユーザー情報を表示します。`su` などでユーザーを切り替えた場合に違いが出ます。

#### Q2. `whoami` と `id` の違いは何ですか？
A. `whoami` はユーザー名のみを表示しますが、`id` コマンドはユーザーID、グループIDなどより詳細な情報を表示します。

#### Q3. スクリプト内で `whoami` の出力を変数に格納するにはどうすればよいですか？
A. `USER=$(whoami)` のように変数に代入できます。その後、`$USER` で参照できます。

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/whoami-invocation.html

## 改訂履歴

- 2025/04/30 初版作成