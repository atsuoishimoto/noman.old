# yes コマンド

文字列を中断されるまで繰り返し出力します。

## 概要

`yes` コマンドは、デフォルトでは「y」という文字列を改行付きで、終了されるまで連続して出力します。主に確認を求めるコマンドプロンプトに自動的に応答するために使用され、スクリプトが手動介入なしで実行できるようにします。

## オプション

### **-V, --version**

バージョン情報を表示して終了します。

```console
$ yes --version
yes (GNU coreutils) 9.0
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by David MacKenzie.
```

### **--help**

ヘルプ情報を表示して終了します。

```console
$ yes --help
Usage: yes [STRING]...
  or:  yes OPTION
Repeatedly output a line with all specified STRING(s), or 'y'.

      --help     display this help and exit
      --version  output version information and exit
```

## 使用例

### デフォルトの動作（「y」を出力）

```console
$ yes
y
y
y
y
[Ctrl+Cで中断されるまで続く]
```

### カスタム文字列の出力

```console
$ yes "同意します"
同意します
同意します
同意します
[Ctrl+Cで中断されるまで続く]
```

### スクリプトでのプロンプトへの自動応答

```console
$ yes | rm -i *.txt
rm: remove regular file 'file1.txt'? rm: remove regular file 'file2.txt'?
```

### コマンドに複数の入力を提供

```console
$ yes n y | rm -i file1.txt file2.txt
rm: remove regular file 'file1.txt'? rm: remove regular file 'file2.txt'?
```

## ヒント:

### コマンドの停止

`yes` は Ctrl+C で停止するまで無限に実行されることを常に覚えておきましょう。終了し忘れると、システムリソースを不必要に消費する可能性があります。

### 出力の制限

出力回数を制限したい場合は、`yes` を `head` にパイプすることができます：

```console
$ yes | head -n 5
y
y
y
y
y
```

### パフォーマンステスト

`yes` コマンドは、最大速度で出力を生成するため、簡単なパフォーマンステストやシステムに負荷をかけるために使用できます。

### 破壊的なコマンドでの注意

`rm -rf` のような破壊的なコマンドで `yes` を使用する際は注意が必要である。期待通りの動作をするか、まず安全なコマンドでテストしてから使用すること。

## よくある質問

#### Q1. `yes` コマンドの目的は何ですか？
A. 主な目的は、スクリプト内の対話式プロンプトに自動的に応答することで、通常は確認の質問に「y」で答えます。

#### Q2. `yes` コマンドを停止するにはどうすればよいですか？
A. Ctrl+C を押してコマンドを終了します。

#### Q3. `yes` に「y」以外の文字列を出力させることはできますか？
A. はい、引数として希望の文字列を指定するだけです：`yes "カスタムテキスト"`

#### Q4. `yes` が文字列を出力する回数を制限する方法はありますか？
A. コマンド自体にはこのオプションはありませんが、`head` に `-n` オプションを付けてパイプすることができます：`yes | head -n 10`

#### Q5. `yes` はシステムリソースを多く消費しますか？
A. 可能な限り高速に出力を生成するため、かなりのCPUリソースを消費する可能性があります。必要がなくなったら必ず終了してください。

## 参考文献

https://www.gnu.org/software/coreutils/manual/html_node/yes-invocation.html

## 改訂履歴

- 2025/05/04 初版作成