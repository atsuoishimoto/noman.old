# xargs コマンド

標準入力から引数を受け取り、コマンドを実行します。

## 概要

`xargs` は標準入力からアイテムを読み取り、それらを引数として使用してコマンド（デフォルトでは `/bin/echo`）を実行するコマンドラインユーティリティです。標準入力のアイテムは空白または改行で区切られます。これは他のコマンドの出力を処理し、複数のファイルやデータストリームに対して操作を適用する場合に特に便利です。

## オプション

### **-0, --null**

入力アイテムが空白ではなくヌル文字で終了するものとして扱います。入力に空白や改行が含まれる可能性がある場合に便利です。

```console
$ find . -name "*.txt" -print0 | xargs -0 grep "example"
./file1.txt:example text here
./path with spaces/file2.txt:another example
```

### **-I, --replace[=REPLACE]**

初期引数内の REPLACE（デフォルトは {}）の出現を標準入力から読み取った名前で置き換えます。

```console
$ echo "file1.txt file2.txt" | xargs -I {} cp {} backup/
```

### **-n, --max-args=MAX-ARGS**

コマンドラインごとに最大 MAX-ARGS 個の引数を使用します。

```console
$ echo "1 2 3 4" | xargs -n 2 echo
1 2
3 4
```

### **-P, --max-procs=MAX-PROCS**

最大 MAX-PROCS 個のプロセスを同時に実行します。

```console
$ find . -name "*.jpg" | xargs -P 4 -I {} convert {} {}.png
```

### **-t, --verbose**

実行前にコマンドを表示します。

```console
$ echo "file1.txt file2.txt" | xargs -t rm
rm file1.txt file2.txt
```

### **-p, --interactive**

各コマンドを実行する前にユーザーに確認を求めます。

```console
$ echo "file1.txt file2.txt" | xargs -p rm
rm file1.txt file2.txt ?...
```

## 使用例

### 名前に空白を含むファイルの処理

```console
$ find . -name "*.txt" -print0 | xargs -0 grep "pattern"
./document.txt:pattern found here
./notes with spaces.txt:another pattern example
```

### ファイルのバッチ処理

```console
$ find . -name "*.jpg" | xargs -P 4 -I {} convert {} {}.png
```

### ファイルにリストされたファイルの削除

```console
$ cat files_to_delete.txt | xargs rm
```

### 各入力に対して複数のコマンドを実行

```console
$ echo "file1 file2" | xargs -I {} sh -c 'echo {}; wc -l {}'
file1
      42 file1
file2
      18 file2
```

## ヒント:

### find -print0 と xargs -0 を組み合わせる

空白、改行、その他の特殊文字を含むファイル名を扱う場合は、常に `find -print0` と `xargs -0` をペアで使用して、適切に処理されるようにしましょう。

### コマンドインジェクションを防ぐ

ユーザー提供の入力を xargs で使用する場合は注意が必要です。コマンドインジェクションの脆弱性を避けるために、プレースホルダーを使用した `-I` オプションを使用しましょう。

### -t オプションでコマンドをプレビュー

特に `rm` のような破壊的な操作を行う場合は、`-t` オプションを使用して実行前にどのようなコマンドが実行されるかを確認しましょう。

### 並列処理の制御

CPU負荷の高いタスクの場合、`-P` オプションにCPUコア数を指定することで、システムに負荷をかけすぎずにパフォーマンスを最適化できます。

## よくある質問

#### Q1. パイプでコマンドに送る方法と xargs を使用する方法の違いは何ですか？
A. パイプ（`|`）は、あるコマンドの出力を別のコマンドの入力として送りますが、`xargs` は入力をコマンドの引数に変換します。多くのコマンドはファイル名として標準入力からの入力を受け付けないため、そのような場合に xargs が必要になります。

#### Q2. 空白を含むファイル名を xargs で処理するにはどうすればよいですか？
A. `find -print0` と `xargs -0` を使用して、空白、改行、その他の特殊文字を含むファイル名を適切に処理できます。

#### Q3. 各入力に対して複数のコマンドを実行することはできますか？
A. はい、`-I` オプションと `sh -c` を使用して複数のコマンドを実行できます：`xargs -I {} sh -c 'command1 {}; command2 {}'`

#### Q4. コマンドごとの引数の数を制限するにはどうすればよいですか？
A. `-n` オプションの後に最大引数数を指定します：`xargs -n 5 command`

## 参考資料

https://www.gnu.org/software/findutils/manual/html_node/find_html/xargs-options.html

## 改訂履歴

- 2025/05/04 初回改訂