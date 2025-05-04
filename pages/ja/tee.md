# tee コマンド

標準入力から読み取り、標準出力とファイルの両方に同時に書き込みます。

## 概要

`tee` コマンドは標準入力から読み取り、標準出力と1つ以上のファイルに同時に書き込みを行います。これにより、コマンドの出力をターミナルで確認しながら、同時にファイルに保存することができます。パイプラインで中間結果を保存する際によく使用されます。

## オプション

### **-a, --append**

指定されたファイルに追記し、上書きしません

```console
$ echo "追加行" | tee -a output.txt
追加行
```

### **-i, --ignore-interrupts**

割り込み信号（SIGINT）を無視します

```console
$ 長時間実行するコマンド | tee -i output.log
```

### **--help**

ヘルプ情報を表示して終了します

```console
$ tee --help
Usage: tee [OPTION]... [FILE]...
Copy standard input to each FILE, and also to standard output.

  -a, --append              append to the given FILEs, do not overwrite
  -i, --ignore-interrupts   ignore interrupt signals
  -p                        diagnose errors writing to non pipes
      --output-error[=MODE]   set behavior on write error.  See MODE below
      --help     display this help and exit
      --version  output version information and exit

MODE determines behavior with write errors on the outputs:
  'warn'         diagnose errors writing to any output
  'warn-nopipe'  diagnose errors writing to any output not a pipe
  'exit'         exit on error writing to any output
  'exit-nopipe'  exit on error writing to any output not a pipe
The default MODE for the -p option is 'warn-nopipe'.
The default operation when --output-error is not specified, is to
exit immediately on error writing to a pipe, and diagnose errors
writing to non pipe outputs.

GNU coreutils online help: <https://www.gnu.org/software/coreutils/>
Report any translation bugs to <https://translationproject.org/team/>
Full documentation <https://www.gnu.org/software/coreutils/tee>
or available locally via: info '(coreutils) tee invocation'
```

### **--version**

バージョン情報を出力して終了します

```console
$ tee --version
tee (GNU coreutils) 9.0
Copyright (C) 2022 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Mike Parker, Richard M. Stallman, and David MacKenzie.
```

## 使用例

### 基本的な使い方

```console
$ ls -l | tee file_list.txt
total 16
-rw-r--r-- 1 user group 1024 May 4 10:30 document.txt
drwxr-xr-x 2 user group 4096 May 3 15:45 projects
```

### 複数のファイルに書き込む

```console
$ echo "こんにちは、世界！" | tee file1.txt file2.txt file3.txt
こんにちは、世界！
```

### sudoと組み合わせる

```console
$ cat config.txt | sudo tee /etc/app/config.txt > /dev/null
```

### コマンド出力を表示しながら保存する

```console
$ make | tee build.log
[コンパイル出力がここに表示され、build.logにも保存される]
```

## ヒント:

### 保護されたファイルを編集するためにsudoと使用する

特権が必要なファイルを編集する必要がある場合、`tee`を`sudo`と組み合わせてファイルに書き込むことができます：

```console
$ echo "新しい内容" | sudo tee /etc/protected_file.txt
```

### 標準出力を破棄する

ターミナルに出力を表示せず、ファイルにのみ書き込みたい場合は、標準出力を`/dev/null`にリダイレクトします：

```console
$ command | tee output.txt > /dev/null
```

### 標準出力とエラー出力の両方をキャプチャする

標準出力とエラー出力の両方をキャプチャするには：

```console
$ command 2>&1 | tee output.log
```

## よくある質問

#### Q1. `tee`と単純なリダイレクト（`>`）の違いは何ですか？
A. リダイレクト（`>`）は出力をファイルにのみ書き込むのに対し、`tee`はファイルと標準出力の両方に書き込むため、ターミナルで出力を確認しながらファイルに保存できます。

#### Q2. ファイルを上書きせずに追記するにはどうすればよいですか？
A. `-a`オプションを使用します：`command | tee -a file.txt`

#### Q3. 複数のファイルに一度に書き込むことはできますか？
A. はい、すべてのファイルをリストするだけです：`command | tee file1.txt file2.txt file3.txt`

#### Q4. root権限が必要なファイルに`tee`を使って書き込むにはどうすればよいですか？
A. sudoと組み合わせます：`command | sudo tee /path/to/file > /dev/null`

## References

https://www.gnu.org/software/coreutils/manual/html_node/tee-invocation.html

## Revisions

- 2025/05/04 First revision