# dmesg コマンド

カーネルのリングバッファからシステムメッセージを表示します。

## 概要

`dmesg`（display message）コマンドは、Linuxカーネルが起動時や実行中に生成するメッセージを表示します。これらのメッセージには、ハードウェアの検出、ドライバの読み込み、エラー、警告などの重要な情報が含まれています。システム管理者やトラブルシューティングを行うユーザーにとって非常に役立つツールです。

## オプション

### **-H, --human**

人間が読みやすい形式で出力を表示します。タイムスタンプの相対表示や色分けなどが含まれます。

```console
$ dmesg -H
[Apr30 10:15] Linux version 5.10.0-8-amd64 (debian-kernel@lists.debian.org)
[  +0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.10.0-8-amd64 root=UUID=...
[  +0.000073] KERNEL supported cpus:
[  +0.000002]   Intel GenuineIntel
[  +0.000001]   AMD AuthenticAMD
```

### **-c, --clear**

メッセージを表示した後、カーネルのリングバッファをクリアします。

```console
$ dmesg -c
[    0.000000] Linux version 5.10.0-8-amd64 (debian-kernel@lists.debian.org)
[    0.000073] Command line: BOOT_IMAGE=/boot/vmlinuz-5.10.0-8-amd64 root=UUID=...
...
# バッファがクリアされるため、再度実行すると何も表示されない
$ dmesg
```

### **-l, --level**

指定したレベルのメッセージのみを表示します。レベルには emerg, alert, crit, err, warn, notice, info, debug があります。

```console
$ dmesg --level=err,warn
[    1.234567] WARNING: CPU: 0 PID: 42 at drivers/usb/core/urb.c:377
[    2.345678] usb 1-1: device descriptor read/64, error -110
```

### **-f, --facility**

指定した機能（facility）のメッセージのみを表示します。

```console
$ dmesg -f kern
[    0.000000] Linux version 5.10.0-8-amd64 (debian-kernel@lists.debian.org)
[    0.000073] Command line: BOOT_IMAGE=/boot/vmlinuz-5.10.0-8-amd64 root=UUID=...
```

### **-T, --ctime**

タイムスタンプを人間が読める形式で表示します。

```console
$ dmesg -T
[Wed Apr 30 10:15:30 2025] Linux version 5.10.0-8-amd64 (debian-kernel@lists.debian.org)
[Wed Apr 30 10:15:30 2025] Command line: BOOT_IMAGE=/boot/vmlinuz-5.10.0-8-amd64 root=UUID=...
```

## 使用例

### 特定のキーワードでフィルタリング

```console
$ dmesg | grep USB
[    2.123456] usb 1-1: new high-speed USB device number 2 using ehci-pci
[    2.234567] usb 1-1: New USB device found, idVendor=0781, idProduct=5567
```

### 最新のメッセージを監視

```console
$ dmesg -w
[    0.000000] Linux version 5.10.0-8-amd64 (debian-kernel@lists.debian.org)
...
# 新しいメッセージが発生すると自動的に表示される
[   15.678901] usb 2-1: new high-speed USB device number 3 using xhci_hcd
```

### エラーメッセージの確認

```console
$ dmesg --level=err
[    3.456789] EXT4-fs (sda1): re-mounted. Opts: errors=remount-ro
[    5.678901] nouveau 0000:01:00.0: DRM: failed to create kernel channel, -22
```

## ヒント:

### 起動時の問題を診断する

システムの起動に問題がある場合、`dmesg`を使用して起動プロセス中に発生したエラーや警告を確認できます。特に「error」や「fail」などのキーワードで検索すると効果的です。

```console
$ dmesg | grep -i error
```

### ハードウェアの問題を特定する

新しいハードウェアを接続した後に問題が発生した場合、`dmesg`を使用して認識状況やエラーメッセージを確認できます。

### ログの保存

重要なシステムメッセージを保存したい場合は、出力をファイルにリダイレクトします。

```console
$ dmesg > dmesg_log.txt
```

## よくある質問

#### Q1. dmesgの出力が多すぎる場合、どうすれば必要な情報だけを見つけられますか？
A. `grep`コマンドと組み合わせて特定のキーワードでフィルタリングするか、`--level`オプションを使用して特定の重要度のメッセージだけを表示できます。

#### Q2. dmesgの出力にタイムスタンプが数字で表示されますが、これは何を意味していますか？
A. デフォルトでは、タイムスタンプはシステム起動からの経過秒数を表示します。人間が読みやすい形式で表示するには、`-T`または`-H`オプションを使用してください。

#### Q3. rootユーザーでないとdmesgが使えないのはなぜですか？
A. 最近のLinuxディストリビューションでは、セキュリティ上の理由からrootユーザーまたはsudo権限を持つユーザーのみがdmesgを使用できるように制限されています。

#### Q4. dmesgの出力をリアルタイムで監視するにはどうすればよいですか？
A. `dmesg -w`または`dmesg --follow`を使用すると、新しいメッセージが発生するたびに表示されます。

## macOSでの注意点

macOSでは`dmesg`コマンドの動作がLinuxとは異なります。macOSでは`syslog`システムを使用しており、システムログを表示するには代わりに以下のコマンドを使用することをお勧めします：

```console
$ sudo log show --predicate 'eventMessage contains "kernel"' --last 10m
```

または、より古いバージョンのmacOSでは：

```console
$ sudo syslog -k Sender kernel
```

## 参考資料

https://man7.org/linux/man-pages/man1/dmesg.1.html

## 改訂履歴

- 2025/04/30 初版作成