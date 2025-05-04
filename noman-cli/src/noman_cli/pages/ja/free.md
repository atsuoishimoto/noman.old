# free コマンド

システム内の空きメモリと使用中メモリの量を表示します。

## 概要

`free`コマンドは、物理RAMとスワップスペースの両方について、システムのメモリ使用状況（合計、使用中、利用可能なメモリ）に関する情報を提供します。メモリリソースを素早く確認し、潜在的なメモリ制約を特定するための簡単な方法です。

## オプション

### **-b, --bytes**

メモリ量をバイト単位で表示します。

```console
$ free -b
               total        used        free      shared  buff/cache   available
Mem:     8273514496  3145728000  1073741824   536870912  4053844992  4594966528
Swap:    2147483648   268435456  1879048192
```

### **-k, --kilo**

メモリ量をキロバイト単位で表示します（デフォルト）。

```console
$ free -k
               total        used        free      shared  buff/cache   available
Mem:        8080580     3072000     1048576      524288     3959808     4487272
Swap:       2097152      262144     1835008
```

### **-m, --mega**

メモリ量をメガバイト単位で表示します。

```console
$ free -m
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792
```

### **-g, --giga**

メモリ量をギガバイト単位で表示します。

```console
$ free -g
               total        used        free      shared  buff/cache   available
Mem:              7           2           1           0           3           4
Swap:             2           0           1
```

### **-h, --human**

すべての出力フィールドを自動的に最短の3桁単位にスケーリングし、単位を表示します。

```console
$ free -h
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.0Gi       1.0Gi       512Mi       3.7Gi       4.2Gi
Swap:          2.0Gi       256Mi       1.7Gi
```

### **-s, --seconds N**

N秒間隔で結果を継続的に表示します。

```console
$ free -s 2
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792

               total        used        free      shared  buff/cache   available
Mem:           7890        3010        1014         512        3866        4372
Swap:          2048         256        1792
```

### **-c, --count N**

結果をN回表示した後、終了します。-sオプションと一緒に使用する必要があります。

```console
$ free -c 3 -s 1
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792

               total        used        free      shared  buff/cache   available
Mem:           7890        3010        1014         512        3866        4372
Swap:          2048         256        1792

               total        used        free      shared  buff/cache   available
Mem:           7890        3020        1004         512        3866        4362
Swap:          2048         256        1792
```

### **-t, --total**

列の合計を示す行を表示します。

```console
$ free -t
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792
Total:         9938        3256        2816
```

### **-w, --wide**

ワイドモードに切り替えます。ワイドモードでは80文字より長い行が生成されます。

```console
$ free -w
               total        used        free      shared     buffers       cache   available
Mem:           7890        3000        1024         512         366        3500        4382
Swap:          2048         256        1792
```

## 使用例

### 基本的なメモリ情報

```console
$ free
               total        used        free      shared  buff/cache   available
Mem:           7890        3000        1024         512        3866        4382
Swap:          2048         256        1792
```

### 人間が読みやすい形式でのメモリ情報と合計

```console
$ free -ht
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.0Gi       1.0Gi       512Mi       3.7Gi       4.2Gi
Swap:          2.0Gi       256Mi       1.7Gi
Total:         9.7Gi       3.2Gi       2.7Gi
```

### 5秒間隔での継続的なモニタリング

```console
$ free -h -s 5
               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.0Gi       1.0Gi       512Mi       3.7Gi       4.2Gi
Swap:          2.0Gi       256Mi       1.7Gi

               total        used        free      shared  buff/cache   available
Mem:           7.7Gi       3.1Gi       900Mi       512Mi       3.7Gi       4.1Gi
Swap:          2.0Gi       256Mi       1.7Gi
```

## ヒント:

### 出力列の理解

- **total**: インストールされた総メモリ
- **used**: 現在使用中のメモリ
- **free**: 未使用のメモリ
- **shared**: 複数のプロセスで共有されているメモリ
- **buff/cache**: カーネルバッファとページキャッシュで使用されているメモリ
- **available**: スワップなしで新しいアプリケーションに利用可能なメモリの推定値

### 利用可能なメモリに注目する

「available」列は「free」列よりも重要です。これには、必要に応じてバッファやキャッシュから再利用できるメモリが含まれているためです。

### 時間経過によるメモリのモニタリング

`free -s`を使用して時間経過によるメモリ使用状況をモニタリングすると、メモリリークや使用パターンを特定するのに役立ちます。

### 他のコマンドと組み合わせる

`free`の出力を他のコマンドにパイプして特定の情報を取得できます：
```console
$ free -m | grep Mem
Mem:           7890        3000        1024         512        3866        4382
```

## よくある質問

#### Q1. 「free」と「available」メモリの違いは何ですか？
A. 「free」メモリは完全に未使用のメモリであるのに対し、「available」にはスワップなしで新しいアプリケーションのためにバッファやキャッシュから再利用できるメモリが含まれています。

#### Q2. なぜ「free」メモリが少ないのですか？
A. Linuxはパフォーマンス向上のために利用可能なメモリをディスクキャッシュに使用します。アプリケーションが使用できるメモリの指標としては「available」列を見るのがより適切です。

#### Q3. システムのメモリ不足をどうやって確認できますか？
A. 「available」列をモニタリングしてください。それが常に低く、スワップ使用量が高い場合、システムはメモリ圧迫状態にある可能性があります。

#### Q4. 「buff/cache」列は何を表していますか？
A. カーネルバッファとディスクキャッシュに使用されているメモリを示しています。このメモリは、アプリケーションが必要とする場合に再利用できることが多いです。

#### Q5. メモリ使用状況を継続的にモニタリングするにはどうすればよいですか？
A. `free -s N`を使用します。Nは更新間隔の秒数です。

## 参考資料

https://www.man7.org/linux/man-pages/man1/free.1.html

## 改訂履歴

- 2025/05/04 初回改訂