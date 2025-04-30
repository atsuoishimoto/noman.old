# uname コマンド

システムの情報を表示するコマンドです。

## 概要

`uname` コマンドはシステムの基本情報（カーネル名、ホスト名、オペレーティングシステム、プロセッサアーキテクチャなど）を表示します。オプションなしで実行すると、カーネル名のみを表示します。システム管理やスクリプト内での環境判定に役立ちます。

## オプション

### **-a (--all)**

すべてのシステム情報を表示します。

```console
$ uname -a
Darwin MacBook-Pro.local 21.6.0 Darwin Kernel Version 21.6.0: Mon Aug 22 20:19:52 PDT 2022; root:xnu-8020.140.49~2/RELEASE_ARM64_T6000 arm64
```

### **-s (--kernel-name)**

カーネル名を表示します（デフォルトの動作）。

```console
$ uname -s
Darwin
```

### **-n (--nodename)**

ネットワークノード名（ホスト名）を表示します。

```console
$ uname -n
MacBook-Pro.local
```

### **-r (--kernel-release)**

カーネルリリース番号を表示します。

```console
$ uname -r
21.6.0
```

### **-v (--kernel-version)**

カーネルのバージョン情報を表示します。

```console
$ uname -v
Darwin Kernel Version 21.6.0: Mon Aug 22 20:19:52 PDT 2022; root:xnu-8020.140.49~2/RELEASE_ARM64_T6000
```

### **-m (--machine)**

ハードウェアのマシンタイプ（アーキテクチャ）を表示します。

```console
$ uname -m
arm64
```

### **-p (--processor)**

プロセッサタイプを表示します（多くのシステムでは「unknown」と表示されることがあります）。

```console
$ uname -p
arm
```

### **-o (--operating-system)**

オペレーティングシステム名を表示します。

```console
$ uname -o
Darwin
```

## 使用例

### 複数の情報を組み合わせて表示

```console
$ uname -sr
Darwin 21.6.0
```

### スクリプト内での使用例

```console
$ os_type=$(uname -s)
$ if [ "$os_type" = "Darwin" ]; then
>   echo "macOSで実行中です"
> else
>   echo "macOS以外のシステムで実行中です"
> fi
macOSで実行中です
```

## ヒント:

### シェルスクリプトでの条件分岐

`uname` の出力を使って、異なるOSに応じた処理を行うことができます。例えば：

```bash
if [ "$(uname)" = "Darwin" ]; then
  # macOS固有の処理
elif [ "$(uname)" = "Linux" ]; then
  # Linux固有の処理
fi
```

### アーキテクチャの確認

Apple Silicon（M1/M2）とIntelプロセッサの区別が必要な場合は `uname -m` を使用します。arm64ならApple Silicon、x86_64ならIntelです。

### システム情報の取得

`uname -a` は、サポートを求める際やバグレポートを提出する際に、システム情報を簡潔に伝えるのに役立ちます。

## よくある質問

#### Q1. `uname` と `sw_vers`（macOS）の違いは何ですか？
A. `uname` はカーネルレベルの情報を表示しますが、`sw_vers` はmacOSのバージョン情報（例：macOS 13.0 Ventura）を表示します。

#### Q2. Linuxディストリビューション名を取得できますか？
A. `uname` だけではディストリビューション名（Ubuntu、Fedoraなど）は取得できません。代わりに `/etc/os-release` ファイルを確認するか、`lsb_release -a` コマンドを使用してください。

#### Q3. macOSでプロセッサの詳細情報を取得するには？
A. `sysctl -n machdep.cpu.brand_string` コマンドを使用すると、より詳細なプロセッサ情報を取得できます。

## 参考情報

https://www.gnu.org/software/coreutils/manual/html_node/uname-invocation.html

## macOSでの注意点

macOSでは、`uname -o` オプションがサポートされていない場合があります。また、macOSの正確なバージョン情報を取得するには、`sw_vers` コマンドを使用することをお勧めします。

## 改訂履歴

- 2025/04/30 初版作成