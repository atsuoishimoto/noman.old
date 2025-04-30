# until コマンド

指定した条件が真になるまでコマンドを繰り返し実行するシェルの制御構造です。

## 概要

`until` は、条件が偽（終了ステータスが0以外）である間、コマンドブロックを繰り返し実行します。条件が真（終了ステータス0）になると、ループを終了します。これは `while` の逆の動作をするもので、条件が満たされるまで処理を続けたい場合に便利です。

## 構文

### **基本構文**

```bash
until 条件コマンド
do
  実行コマンド
done
```

条件コマンドが偽（終了ステータスが0以外）である限り、実行コマンドが繰り返し実行されます。

## 使用例

### 基本的な使い方

```console
$ count=1
$ until [ $count -gt 5 ]
> do
>   echo "カウント: $count"
>   count=$((count + 1))
> done
カウント: 1
カウント: 2
カウント: 3
カウント: 4
カウント: 5
```

この例では、変数 `count` が5より大きくなるまでループが続きます。

### ファイルが存在するまで待機する

```console
$ until [ -f /tmp/signal_file ]
> do
>   echo "ファイルを待っています..."
>   sleep 5
> done
> echo "ファイルが見つかりました！"
ファイルを待っています...
ファイルを待っています...
ファイルが見つかりました！
```

この例では、`/tmp/signal_file` が作成されるまで5秒ごとにメッセージを表示します。

### プロセスが終了するまで待機する

```console
$ process_id=1234
$ until ! ps -p $process_id > /dev/null
> do
>   echo "プロセス $process_id はまだ実行中です"
>   sleep 10
> done
> echo "プロセスが終了しました"
プロセス 1234 はまだ実行中です
プロセス 1234 はまだ実行中です
プロセスが終了しました
```

この例では、指定したプロセスIDのプロセスが終了するまで待機します。

## ヒント:

### while との違いを理解する

`until` は `while` の逆の動作をします。`while` は条件が真の間ループし、`until` は条件が偽の間ループします。

```console
# while の例
$ count=1
$ while [ $count -le 3 ]
> do
>   echo "while: $count"
>   count=$((count + 1))
> done
while: 1
while: 2
while: 3

# 同等の until の例
$ count=1
$ until [ $count -gt 3 ]
> do
>   echo "until: $count"
>   count=$((count + 1))
> done
until: 1
until: 2
until: 3
```

### 無限ループに注意

条件が決して真にならない場合、無限ループになる可能性があります。必ず終了条件を確認してください。

### 複数の条件を組み合わせる

複数の条件を組み合わせるには、論理演算子（`&&` や `||`）を使用します。

```console
$ count=1
$ until [ $count -gt 5 ] || [ -f /tmp/stop_file ]
> do
>   echo "カウント: $count"
>   count=$((count + 1))
>   sleep 1
> done
```

この例では、カウントが5を超えるか、`/tmp/stop_file` が存在するとループが終了します。

## よくある質問

#### Q1. `until` と `while` の違いは何ですか？
A. `until` は条件が偽の間ループを続け、条件が真になると終了します。一方、`while` は条件が真の間ループを続け、条件が偽になると終了します。

#### Q2. `until` ループを途中で抜けるにはどうすればいいですか？
A. `break` コマンドを使用すると、条件に関係なくループを抜けることができます。

#### Q3. `until` ループの現在の繰り返しをスキップするにはどうすればいいですか？
A. `continue` コマンドを使用すると、現在の繰り返しの残りの部分をスキップして次の繰り返しに進みます。

#### Q4. `until` はすべてのシェルで使用できますか？
A. `until` は POSIX 準拠のシェル（bash, zsh, sh など）で使用できますが、すべてのシェルで利用可能とは限りません。

## 参考資料

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## 改訂履歴

- 2025/04/30 初版作成