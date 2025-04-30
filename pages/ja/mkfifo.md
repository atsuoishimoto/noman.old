# mkfifo コマンド

名前付きパイプ（FIFO特殊ファイル）を作成します。

## 概要

`mkfifo`コマンドは、プロセス間通信に使用される名前付きパイプ（FIFO: First-In-First-Out）を作成します。通常のファイルとは異なり、FIFOは一時的なデータストリームを提供し、あるプロセスが書き込んだデータを別のプロセスが読み取ることができます。これにより、関連のないプロセス間でデータを安全に転送できます。

## オプション

### **-m, --mode=MODE**

作成するFIFOのパーミッションを設定します（デフォルトは0666）。

```console
$ mkfifo -m 0644 myfifo
$ ls -l myfifo
prw-r--r--  1 user  staff  0 Apr 30 10:00 myfifo
```

### **-p, --parents**

必要に応じて親ディレクトリを作成します。

```console
$ mkfifo -p path/to/new/myfifo
$ ls -l path/to/new/myfifo
prw-r--r--  1 user  staff  0 Apr 30 10:01 path/to/new/myfifo
```

### **-Z, --context=CTX**

SELinuxセキュリティコンテキストを設定します（SELinux対応システムのみ）。

```console
$ mkfifo -Z user_u:object_r:user_tmp_t:s0 myfifo
```

## 使用例

### 基本的な名前付きパイプの作成

```console
$ mkfifo myfifo
$ ls -l myfifo
prw-r--r--  1 user  staff  0 Apr 30 10:02 myfifo
```

### 名前付きパイプを使ったプロセス間通信

ターミナル1で：
```console
$ mkfifo myfifo
$ cat > myfifo
Hello, this is a test message.
```

ターミナル2で（同時に実行）：
```console
$ cat < myfifo
Hello, this is a test message.
```

### コマンド出力のリダイレクト

```console
$ mkfifo myfifo
$ ls -l > myfifo &
$ grep "txt" < myfifo
document.txt
notes.txt
```

## ヒント:

### FIFOは一度だけ使用可能

名前付きパイプからデータが読み取られると、そのデータは消費されます。複数のプロセスで同じデータを読み取りたい場合は、`tee`コマンドを使用するか、データを再送信する必要があります。

### ブロッキング動作に注意

読み取り側がない状態で書き込みを行うと、書き込み側のプロセスはブロックされます（逆も同様）。これはデッドロックの原因になる可能性があるため、使用時には注意が必要です。

### 永続的なストレージではない

FIFOはデータの一時的な転送のみを目的としており、ファイルシステム上に存在しますが、データを永続的に保存するものではありません。

## よくある質問

#### Q1. 名前付きパイプと通常のパイプ（|）の違いは何ですか？
A. 通常のパイプ（|）は一時的で、コマンドライン上でのみ使用できますが、名前付きパイプはファイルシステム上に存在し、関連のないプロセス間でも通信できます。

#### Q2. 名前付きパイプはいつ削除されますか？
A. 名前付きパイプはファイルシステム上の通常のファイルと同様に扱われるため、明示的に削除（`rm`コマンドなど）するまで存在し続けます。ただし、システムの再起動後もデータは保持されません。

#### Q3. 名前付きパイプの最大サイズはどれくらいですか？
A. 名前付きパイプのバッファサイズはOSによって異なりますが、通常は数KBです（Linuxでは通常64KBまで）。バッファが一杯になると、書き込み側はブロックされます。

#### Q4. 複数のプロセスが同時に名前付きパイプに書き込むことはできますか？
A. はい、可能です。ただし、小さなデータチャンクが交互に書き込まれる可能性があるため、アプリケーションによっては問題が生じる場合があります。

## macOSでの注意点

macOSでは基本的にLinuxと同様に`mkfifo`が動作しますが、SELinux関連のオプション（-Z）はサポートされていません。また、macOSのパイプバッファサイズはLinuxとは異なる場合があります。

## 参考文献

https://www.gnu.org/software/coreutils/manual/html_node/mkfifo-invocation.html

## 改訂履歴

- 2025/04/30 初版作成