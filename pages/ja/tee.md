# tee コマンド

標準入力からデータを読み取り、標準出力とファイルの両方に書き込みます。

## 概要

`tee` コマンドは、入力されたデータを画面（標準出力）に表示すると同時に、指定したファイルにも保存します。パイプラインの途中でデータを「分岐」させるように動作するため、コマンドの出力を確認しながら同時にファイルに保存したい場合に便利です。

## オプション

### **-a, --append**

既存のファイルに追記します（上書きではなく）

```console
$ echo "追加テキスト" | tee -a output.txt
追加テキスト
$ cat output.txt
既存の内容
追加テキスト
```

### **-i, --ignore-interrupts**

割り込み信号（Ctrl+C）を無視します

```console
$ command | tee -i output.txt
```

## 使用例

### 標準出力とファイルに同時に出力する

```console
$ ls -l | tee file_list.txt
total 16
-rw-r--r--  1 user  staff  1024 Apr 10 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 9  14:22 projects
```

### 複数のファイルに同時に書き込む

```console
$ echo "テストデータ" | tee file1.txt file2.txt file3.txt
テストデータ
$ cat file1.txt
テストデータ
```

### 管理者権限が必要なファイルへの書き込み

```console
$ echo "設定内容" | sudo tee /etc/some_config_file
設定内容
```

## ヒント:

### sudo と組み合わせた使い方

`sudo echo "text" > /etc/file` ではリダイレクト（`>`）はシェルによって実行されるため権限エラーになります。代わりに `echo "text" | sudo tee /etc/file` を使うと、管理者権限でファイルに書き込めます。

### 出力を確認しながらログを取る

長時間実行されるコマンドの出力を確認しながらログファイルに保存したい場合に便利です。
```console
$ ./long_running_script.sh | tee log.txt
```

### /dev/null との組み合わせ

標準出力には表示せず、ファイルだけに書き込みたい場合は `/dev/null` にリダイレクトします。
```console
$ command | tee output.txt > /dev/null
```

## よくある質問

#### Q1. `tee` コマンドの名前の由来は何ですか？
A. 配管工事で使われるT字型の分岐管（tee）に由来しています。データの流れを分岐させる様子が似ているためです。

#### Q2. `tee` コマンドと単純なリダイレクト（`>`）の違いは何ですか？
A. リダイレクト（`>`）はコマンドの出力をファイルにのみ保存しますが、`tee` は標準出力にも表示しながらファイルに保存します。

#### Q3. `tee` で複数のファイルに書き込むことはできますか？
A. はい、`tee file1 file2 file3` のように複数のファイル名を指定できます。

#### Q4. `tee` コマンドでバイナリデータを扱えますか？
A. はい、`tee` はテキストだけでなくバイナリデータも処理できます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html

## 改訂履歴

- 2025/04/30 初版作成