# eval コマンド

引数からコマンドを構築して実行します。

## 概要

`eval` コマンドは、引数をシェルコマンドとして評価・実行します。引数を単一の文字列に結合し、その文字列を現在のシェル環境でコマンドとして実行します。これは、動的にコマンドを構築したり、変数に格納されたコマンドを実行したりする場合に特に便利です。

## オプション

`eval` コマンド自体には特定のオプションはありません。単に引数を受け取り、それらをシェルコマンドとして実行するだけです。提供されるオプションはすべて、評価されるコマンドに渡されます。

## 使用例

### 基本的な使い方

```console
$ eval "echo Hello, World!"
Hello, World!
```

### 変数を使ったコマンド

```console
$ command="ls -la"
$ eval $command
total 32
drwxr-xr-x  5 user  staff   160 May  4 10:23 .
drwxr-xr-x  3 user  staff    96 May  4 10:20 ..
-rw-r--r--  1 user  staff  1024 May  4 10:22 file1.txt
-rw-r--r--  1 user  staff  2048 May  4 10:23 file2.txt
drwxr-xr-x  2 user  staff    64 May  4 10:21 directory
```

### 動的なコマンド構築

```console
$ file="document.txt"
$ action="cat"
$ eval "$action $file"
This is the content of document.txt
```

### 複数の引数を持つコマンド

```console
$ options="-l -a"
$ directory="/tmp"
$ eval "ls $options $directory"
total 16
drwxrwxrwt  5 root  wheel   160 May  4 10:30 .
drwxr-xr-x 20 root  wheel   640 May  4 09:15 ..
-rw-r--r--  1 user  wheel  1024 May  4 10:25 temp1.txt
drwxr-xr-x  2 user  wheel    64 May  4 10:28 tempdir
```

## ヒント:

### 引用符を慎重に使用する

`eval` で変数を使用する場合は、単語分割や予期しない動作を防ぐために、常に変数を引用符で囲みましょう：

```console
$ filename="my file.txt"
$ eval "echo $filename"    # 不適切: "my"と"file.txt"として解釈される
my file.txt
$ eval "echo \"$filename\""  # 適切: スペースが保持される
my file.txt
```

### セキュリティ上の考慮事項

ユーザー入力や信頼できないデータと一緒に `eval` を使用する場合は、コマンドインジェクションの脆弱性につながる可能性があるため、非常に注意が必要です。より単純な代替手段がある場合は、`eval` の使用を避けましょう。

### evalコマンドのデバッグ

`eval` が実際に実行せずにどのようなコマンドを実行するかを確認するには、まず `echo` を使用します：

```console
$ cmd="ls -la /tmp"
$ echo "$cmd"
ls -la /tmp
$ eval "$cmd"
[ls -la /tmpの出力]
```

## よくある質問

#### Q1. `eval` はいつ使うべきですか？
A. コマンドを動的に構築して実行する必要がある場合、特にコマンド構造が変数に格納されているか、実行時に生成される場合に `eval` を使用します。

#### Q2. なぜ `eval` は危険と考えられているのですか？
A. `eval` は引数をシェルコマンドとして実行するため、それらの引数に信頼できない入力が含まれている場合、セキュリティ脆弱性につながる可能性があります。これにより、コマンドインジェクション攻撃が可能になる恐れがあります。

#### Q3. `eval` の代替手段はありますか？
A. はい、ユースケースによります。単純な変数展開の場合、パラメータ置換で十分なことが多いです。より複雑なケースでは、関数、配列、コマンド置換の使用を検討してください。

#### Q4. `eval` はエラーをどのように処理しますか？
A. `eval` は実行された最後のコマンドの終了ステータスを返します。コマンド文字列が構文的に正しくない場合、ゼロ以外の終了ステータスを返します。

## 参考文献

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/eval.html

## 改訂履歴

- 2025/05/04 初版作成