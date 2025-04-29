# eval

`eval` コマンドは、引数を連結して単一のコマンドとして実行するシェル組み込みコマンドです。変数の間接参照や動的なコマンド生成に特に役立ちます。

## オプション

`eval` コマンド自体には特別なオプションはありません。引数として渡されたコマンドが実行されます。

## 使用例

### 基本的な使用法

```bash
$ eval "echo Hello, World!"
Hello, World!
```

### 変数の間接参照

```bash
$ name="value"
$ ref="name"
$ eval echo \$$ref
value
```

変数 `ref` が指す変数 `name` の値を取得している。

### 動的なコマンド生成

```bash
$ command="ls -la"
$ eval $command
total 32
drwxr-xr-x  5 user  staff   160  4 10 15:30 .
drwxr-xr-x  3 user  staff    96  4  9 14:22 ..
-rw-r--r--  1 user  staff  1024  4 10 15:30 document.txt
drwxr-xr-x  3 user  staff    96  4  9 14:22 projects
```

変数に格納されたコマンドを実行している。

### 複雑な置換を含むコマンド

```bash
$ files="file1.txt file2.txt"
$ eval "ls -l $files"
-rw-r--r--  1 user  staff  100  4 10 15:30 file1.txt
-rw-r--r--  1 user  staff  200  4 10 15:40 file2.txt
```

変数展開を含むコマンドを実行している。

## よくある質問

### Q1. `eval` はどのような時に使うべきですか？
A. 変数の間接参照が必要な場合や、動的に生成されたコマンドを実行する場合に使います。特に、変数に格納された変数名を参照したい時に便利です。

### Q2. `eval` の使用にはどのようなリスクがありますか？
A. ユーザー入力を直接 `eval` に渡すと、コマンドインジェクション攻撃のリスクがあります。信頼できない入力を `eval` で実行しないようにしましょう。

### Q3. `eval` と通常のコマンド実行の違いは何ですか？
A. 通常のコマンド実行では一度だけ変数展開が行われますが、`eval` では二度変数展開が行われます。これにより、動的なコマンド生成や間接参照が可能になります。

## 追加情報

- `eval` は強力ですが、使いすぎると可読性が低下し、デバッグが難しくなることがあります。
- 可能な限り、より安全で明示的な代替手段（配列や関数など）を検討しましょう。
- シェルスクリプトで `eval` を使用する場合は、入力値を適切にエスケープして安全性を確保してください。

## macOSでの注意点

macOSのBashやZshでも `eval` は同様に動作しますが、macOSのデフォルトシェルはZshになっているため、Bashとの微妙な違いがある場合があります。基本的な使い方は同じです。

## 参考情報

https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html#index-eval