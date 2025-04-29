# strace コマンド
プロセスのシステムコールとシグナルをトレースするツール。

## 概要
`strace`はLinuxシステムで実行中のプログラムが行うシステムコール（OSへの要求）とシグナルを監視・記録するコマンドです。プログラムのデバッグやパフォーマンス分析に役立ち、プログラムがどのファイルにアクセスしているか、どのネットワーク接続を確立しているかなどを確認できます。

## オプション
### **-f**
子プロセスも含めてトレースします。`fork()`や`clone()`で生成された子プロセスも追跡できます。

```console
$ strace -f ls
execve("/bin/ls", ["ls"], 0x7ffc7c9d5b40 /* 24 vars */) = 0
brk(NULL)                               = 0x55a3e2a1b000
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
...
[pid 12345] openat(AT_FDCWD, ".", O_RDONLY|O_NONBLOCK|O_CLOEXEC|O_DIRECTORY) = 3
...
```

### **-o ファイル名**
出力を指定したファイルに保存します。

```console
$ strace -o trace.log ls
$ cat trace.log
execve("/bin/ls", ["ls"], 0x7ffd8a1d3b40 /* 24 vars */) = 0
brk(NULL)                               = 0x55c8e4c0c000
...
```

### **-p PID**
実行中のプロセスをPIDを指定してトレースします。

```console
$ strace -p 1234
strace: Process 1234 attached
read(3, "data\n", 4096)                 = 5
write(1, "data\n", 5)                   = 5
...
```

### **-e expr**
トレースするシステムコールやシグナルを指定します。

```console
$ strace -e open,read ls
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
read(3, "\237\235\0\0\4\0\0\0\24\0\0\0\3\0\0\0GNU\0\2\0\0\300\4\0\0\0\3\0\0\0"..., 4096) = 4096
...
```

### **-c**
各システムコールの統計情報を表示します。

```console
$ strace -c ls
file1  file2  file3

% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0        11           read
  0.00    0.000000           0         9           write
...
------ ----------- ----------- --------- --------- ----------------
100.00    0.000123                   106         1 total
```

## 使用例
### 基本的なプログラムのトレース
```console
$ strace ls
execve("/bin/ls", ["ls"], 0x7ffc7c9d5b40 /* 24 vars */) = 0
brk(NULL)                               = 0x55a3e2a1b000
...
write(1, "file1  file2  file3\n", 20)   = 20
close(1)                                = 0
exit_group(0)                           = ?
+++ exited with 0 +++
```

### ファイルアクセスのみをトレース
```console
$ strace -e trace=file ls
execve("/bin/ls", ["ls"], 0x7ffd8a1d3b40 /* 24 vars */) = 0
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
...
+++ exited with 0 +++
```

### ネットワーク関連のシステムコールのみをトレース
```console
$ strace -e trace=network curl example.com
socket(AF_INET, SOCK_STREAM, IPPROTO_TCP) = 3
connect(3, {sa_family=AF_INET, sin_port=htons(80), sin_addr=inet_addr("93.184.216.34")}, 16) = 0
...
```

## ヒント:
### 出力が多すぎる場合
`-o`オプションでファイルに出力し、あとでgrepなどで必要な情報を抽出すると効率的です。

### パフォーマンス分析
`-c`オプションを使うと、どのシステムコールが頻繁に呼ばれているか、どれが時間を消費しているかが分かります。

### デバッグのコツ
ファイルが見つからないエラーを調査する場合は、`-e open`でファイルオープン操作だけを追跡すると効果的です。

### 権限の問題
多くのシステムコールをトレースするには管理者権限（root）が必要な場合があります。

## よくある質問
#### Q1. straceを使うとプログラムの実行速度は遅くなりますか？
A. はい、straceはプログラムの実行を大幅に遅くします。本番環境での使用は避け、デバッグ目的でのみ使用することをお勧めします。

#### Q2. MacOSでstraceは使えますか？
A. MacOSではstraceの代わりに`dtruss`や`dtrace`を使用します。ただし、System Integrity Protection (SIP)が有効な場合は制限があります。

#### Q3. 特定のシステムコールだけをトレースするにはどうすればいいですか？
A. `-e trace=システムコール名`を使用します。例えば、`strace -e trace=open,read,write ls`とすると、open、read、writeのシステムコールだけをトレースします。

#### Q4. straceの出力を読みやすくするには？
A. `-v`（詳細表示）や`-s 文字数`（表示する文字列の長さを指定）オプションを使うと読みやすくなります。

## 参考情報
https://man7.org/linux/man-pages/man1/strace.1.html

## 注意事項（macOS）
macOSではstraceは直接サポートされていません。代わりに`dtruss`コマンド（sudoが必要）や`instruments`アプリケーションを使用してください。

## Revisions
- 2025/04/29 初版作成