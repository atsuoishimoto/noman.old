# sleep コマンド

指定した時間だけ実行を一時停止します。

## 概要

`sleep` コマンドは、スクリプトやコマンドラインの実行を指定した時間だけ一時停止させます。シェルスクリプト内でコマンド間に遅延を導入したり、リソースが利用可能になるのを待ったり、時間指定の操作を作成したりするのによく使用されます。

## オプション

### **-s, --suffix=SUFFIX**

時間の単位を指定します（s は秒、m は分、h は時間、d は日）。

```console
$ sleep 5s
[5秒間一時停止する]
```

### **--help**

ヘルプ情報を表示して終了します。

```console
$ sleep --help
Usage: sleep NUMBER[SUFFIX]...
  or:  sleep OPTION
Pause for NUMBER seconds.  SUFFIX may be 's' for seconds (the default),
'm' for minutes, 'h' for hours or 'd' for days.  NUMBER may be an
arbitrary floating point number.  Given two or more arguments, pause for
the sum of their values.

      --help     display this help and exit
      --version  output version information and exit
```

### **--version**

バージョン情報を出力して終了します。

```console
$ sleep --version
sleep (GNU coreutils) 9.0
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Jim Meyering and Paul Eggert.
```

## 使用例

### 基本的な使い方

```console
$ sleep 5
[5秒間一時停止する]
```

### 異なる時間単位の使用

```console
$ sleep 1m
[1分間一時停止する]

$ sleep 2h
[2時間一時停止する]

$ sleep 1d
[1日間一時停止する]
```

### 小数値の使用

```console
$ sleep 0.5
[0.5秒間一時停止する]
```

### 複数の値の組み合わせ

```console
$ sleep 1m 30s
[1分30秒間一時停止する]
```

### スクリプト内での使用

```console
$ echo "タスクを開始します..."
タスクを開始します...
$ sleep 2
$ echo "2秒後にタスクが完了しました"
2秒後にタスクが完了しました
```

## ヒント:

### スリープコマンドの中断

実行中のsleepコマンドはCtrl+Cで中断できます。

### バックグラウンドでのスリープ

`&`を使ってsleepをバックグラウンドで実行すると、ターミナルを引き続き使用できます：
```console
$ sleep 60 &
[1] 12345
```

### 他のコマンドとの組み合わせ

sleepを他のコマンドと組み合わせて、時間指定の操作を作成できます：
```console
$ (sleep 5; echo "5秒後のメッセージ") &
```

### ループ内での使用

sleepはループ内で過度のリソース使用を防ぐのに役立ちます：
```console
$ for i in {1..5}; do echo "繰り返し $i"; sleep 1; done
繰り返し 1
繰り返し 2
繰り返し 3
繰り返し 4
繰り返し 5
```

## よくある質問

#### Q1. 単位を指定しない場合はどうなりますか？
A. 単位が指定されていない場合、sleepはデフォルトで秒を単位として使用します。

#### Q2. sleepで小数値を使用できますか？
A. はい、`0.5`のような小数値を使用して0.5秒などの時間を指定できます。

#### Q3. スクリプトを特定の時間待機させるにはどうすればよいですか？
A. 適切な時間値でsleepを使用します。例えば、`sleep 10m`で10分間待機します。

#### Q4. 異なる時間単位を組み合わせることはできますか？
A. はい、複数の引数を提供すると、それらが合計されます。例えば、`sleep 1h 30m`で1.5時間待機します。

#### Q5. sleepはシステムリソースを多く消費しますか？
A. いいえ、sleepは非常に軽量で、待機中のCPUリソース使用は最小限です。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/sleep-invocation.html

## 改訂履歴

- 2025/05/04 初回改訂