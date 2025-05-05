# uname コマンド

システムのオペレーティングシステムに関する情報を表示します。

## 概要

`uname` コマンドは、コンピュータで実行されているオペレーティングシステムに関するシステム情報を表示します。カーネル名、ネットワークホスト名、カーネルリリース、カーネルバージョン、マシンハードウェア、プロセッサタイプ、オペレーティングシステムなどの詳細を表示できます。

## オプション

### **-a, --all**

カーネル名、ネットワークホスト名、カーネルリリース、カーネルバージョン、マシンハードウェア、プロセッサタイプ、オペレーティングシステムの順にすべての情報を表示します。

```console
$ uname -a
Linux hostname 5.15.0-91-generic #101-Ubuntu SMP Tue Apr 16 14:15:57 UTC 2024 x86_64 x86_64 GNU/Linux
```

### **-s, --kernel-name**

カーネル名を表示します。オプションが指定されていない場合のデフォルトです。

```console
$ uname -s
Linux
```

### **-n, --nodename**

ネットワークノードのホスト名を表示します。

```console
$ uname -n
hostname
```

### **-r, --kernel-release**

カーネルリリースを表示します。

```console
$ uname -r
5.15.0-91-generic
```

### **-v, --kernel-version**

カーネルバージョンを表示します。

```console
$ uname -v
#101-Ubuntu SMP Tue Apr 16 14:15:57 UTC 2024
```

### **-m, --machine**

マシンハードウェア名を表示します。

```console
$ uname -m
x86_64
```

### **-p, --processor**

プロセッサタイプを表示します（判断できない場合は「unknown」と表示されます）。

```console
$ uname -p
x86_64
```

### **-o, --operating-system**

オペレーティングシステムを表示します。

```console
$ uname -o
GNU/Linux
```

## 使用例

### 互換性のためにカーネルバージョンを確認する

```console
$ uname -r
5.15.0-91-generic
```

### システムの完全な情報を取得する

```console
$ uname -a
Linux hostname 5.15.0-91-generic #101-Ubuntu SMP Tue Apr 16 14:15:57 UTC 2024 x86_64 x86_64 GNU/Linux
```

### ソフトウェアインストール用にアーキテクチャを確認する

```console
$ uname -m
x86_64
```

## ヒント:

### 他のコマンドと組み合わせる

`uname` を `lsb_release` などの他のコマンドと組み合わせて、より詳細なディストリビューション情報を取得できます：

```console
$ uname -r && lsb_release -a
5.15.0-91-generic
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.3 LTS
Release:        22.04
Codename:       jammy
```

### スクリプトでの使用

`uname` コマンドは、システム固有の操作を実行する前にオペレーティングシステムやアーキテクチャを判断するシェルスクリプトで特に役立ちます。

### macOSに関する考慮事項

macOSでは、`uname -s` は「Linux」ではなく「Darwin」を返し、`-o` などの一部のオプションは利用できないか、動作が異なる場合があります。

## よくある質問

#### Q1. 実行中のLinuxカーネルバージョンを確認するにはどうすればよいですか？
A. `uname -r` を使用してカーネルリリースバージョンを表示します。

#### Q2. システムが32ビットか64ビットかを確認するにはどうすればよいですか？
A. `uname -m` を使用してマシンハードウェア名を表示します。「x86_64」は64ビットシステムを示し、「i686」または「i386」は32ビットシステムを示します。

#### Q3. `uname -r` と `uname -v` の違いは何ですか？
A. `uname -r` はカーネルリリース（「5.15.0-91-generic」など）を表示し、`uname -v` はカーネルバージョンを表示します。これには通常、ビルド情報（「#101-Ubuntu SMP Tue Apr 16 14:15:57 UTC 2024」など）が含まれます。

#### Q4. なぜ `uname -p` が時々「unknown」を返すのですか？
A. 一部のシステムではプロセッサタイプを判断できない場合があり、その場合は「unknown」が返されます。

## 参考資料

https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html

## 改訂履歴

2025/05/04 初版作成