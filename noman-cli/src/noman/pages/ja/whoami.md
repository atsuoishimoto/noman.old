# whoami コマンド

現在の実効ユーザー名を表示します。

## 概要

`whoami`コマンドは、現在の実効ユーザーIDに関連付けられたユーザー名を出力します。このシンプルなユーティリティは、現在のセッションでどのユーザーアカウントが使用されているかを識別するのに役立ちます。特にスクリプト内での使用、ユーザー間の切り替え時、またはパーミッションの問題をトラブルシューティングする際に便利です。

## オプション

`whoami`コマンドは単一の明確な機能を実行するため、オプションはほとんどありません。

### **--help**

ヘルプ情報を表示して終了します。

```console
$ whoami --help
Usage: whoami [OPTION]...
Print the user name associated with the current effective user ID.
Same as id -un.

      --help     display this help and exit
      --version  output version information and exit

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report whoami translation bugs to <https://translationproject.org/team/>
```

### **--version**

バージョン情報を表示して終了します。

```console
$ whoami --version
whoami (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Richard Mlynarik.
```

## 使用例

### 基本的な使い方

単に`whoami`と入力すると、現在の実効ユーザー名が表示されます：

```console
$ whoami
alice
```

### スクリプト内での使用

このコマンドは、シェルスクリプト内で現在のユーザーを確認するためによく使用されます：

```console
$ if [ "$(whoami)" != "root" ]; then
>   echo "このスクリプトはroot権限で実行する必要があります"
>   exit 1
> fi
このスクリプトはroot権限で実行する必要があります
```

### ユーザー切り替え後

`su`や`sudo`を使用してユーザーを変更した後、`whoami`は新しい実効ユーザーを表示します：

```console
$ whoami
alice
$ sudo -s
# whoami
root
```

## ヒント:

### 実効ユーザーIDと実ユーザーIDの違いを理解する

`whoami`は実効ユーザーIDを表示しますが、これは`sudo`などのコマンドを使用する場合、実ユーザーIDとは異なる場合があります。両方のIDを確認するには、代わりに`id`コマンドを使用してください。

### 代替コマンド

`id -un`コマンドは`whoami`と同じ情報を提供し、すべてのUNIX系システムで利用可能なため、スクリプトではより移植性の高い代替手段となります。

### セキュリティに関する考慮事項

セキュリティに敏感なスクリプトを作成する場合、`whoami`は実効ユーザーのみを表示し、必ずしもプロセスを最初に起動したユーザーを表示するわけではないことを覚えておいてください。

## よくある質問

#### Q1. `whoami`と`who am i`の違いは何ですか？
A. `whoami`は現在のプロセスの実効ユーザー名を表示しますが、`who am i`（または`who -m`）は元のログイン名、端末、およびログイン時間を表示します。

#### Q2. `whoami`でroot権限で実行しているかどうかを確認できますか？
A. はい。`whoami`が「root」を返す場合、root権限で実行していることになります。

#### Q3. `whoami`はすべてのUnix/Linuxシステムで同じように動作しますか？
A. はい、基本的な機能はUnix系システム間で一貫していますが、一部のシステムでは出力形式が若干異なる場合があります。

#### Q4. なぜ`id`の代わりに`whoami`を使用するのですか？
A. `whoami`はよりシンプルで、ユーザー名のみを提供します。一方、`id`はユーザーID、グループID、およびグループメンバーシップを含むより包括的な情報を提供します。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/whoami-invocation.html

## 改訂履歴

- 2025/05/04 初版作成