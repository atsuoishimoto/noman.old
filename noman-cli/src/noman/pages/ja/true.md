# true コマンド

常に成功の終了ステータス（0）を返します。

## 概要

`true` コマンドは何も実行せず、単に成功の終了ステータス（0）を返すだけのシンプルなユーティリティです。シェルスクリプト、条件文、ループなどで、常に成功するコマンドが必要な場合によく使用されます。

## オプション

`true` コマンドは、成功ステータスで終了することが唯一の目的であるため、機能的なオプションはありません。

### **--help**

ヘルプ情報を表示して終了します。

```console
$ true --help
Usage: true [ignored command line arguments]
  or:  true OPTION
Exit with a status code indicating success.

      --help     display this help and exit
      --version  output version information and exit

NOTE: your shell may have its own version of true, which usually supersedes
the version described here.  Please refer to your shell's documentation
for details about the options it supports.
```

### **--version**

バージョン情報を出力して終了します。

```console
$ true --version
true (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Jim Meyering.
```

## 使用例

### 条件文での使用

```console
$ if true; then echo "これは常に実行されます"; fi
これは常に実行されます
```

### ループでの使用

```console
$ while true; do echo "Ctrl+Cで終了"; sleep 1; done
Ctrl+Cで終了
Ctrl+Cで終了
Ctrl+Cで終了
^C
```

### プレースホルダーとして

```console
$ true || echo "これは決して実行されません"
$
```

## ヒント:

### 無限ループの作成

`while true; do [コマンド]; done` は、Ctrl+Cで手動終了するか、ループ内のbreak文で終了させる必要がある無限ループを作成します。

### エラーの抑制

`command || true` を使用すると、コマンドが失敗してもスクリプトが継続されます。これは `true` コマンドが常に成功を返すためです。

### 空の関数

シェルスクリプトでは、存在する必要があるが何もする必要がない関数の本体として `true` を使用できます：
```bash
empty_function() { true; }
```

## よくある質問

#### Q1. `true` と `:` の違いは何ですか？
A. ほとんどのシェルでは、`:` (コロン) も `true` と同様に成功 (0) を返すビルトインコマンドです。コロンはシェルのビルトインであり、外部コマンドを実行する必要がないため、スクリプトではよく使用されます。

#### Q2. `true` を使って空のファイルを作成できますか？
A. いいえ、代わりに `touch ファイル名` を使用してください。`true > ファイル名` で空のファイルを作成できますが、コマンドの本来の用途ではありません。

#### Q3. `true` で無限ループを作成するにはどうすればよいですか？
A. `while true; do コマンド; done` を使用します。ループから抜け出す方法を含めないと永遠に実行され続けることに注意してください。

#### Q4. `true` の終了ステータスは何ですか？
A. 終了ステータスは常に0で、成功を示します。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/true-invocation.html

## 改訂履歴

- 2025/05/04 初版作成