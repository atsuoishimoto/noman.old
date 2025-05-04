# dmesg コマンド

カーネルメッセージバッファを表示または制御します。

## 概要

`dmesg`コマンドは、システムリングバッファからカーネルメッセージを表示します。このバッファにはハードウェア、デバイスドライバ、システム初期化に関する情報が含まれています。ハードウェアの問題のトラブルシューティング、起動メッセージの確認、カーネルイベントの監視に特に役立ちます。

## オプション

### **-c, --clear**

内容を表示した後にリングバッファをクリアします。

```console
$ sudo dmesg -c
[    0.000000] Linux version 5.15.0-76-generic (buildd@lcy02-amd64-017) (gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #83-Ubuntu SMP
[...]
```

### **-H, --human**

色付き、相対的なタイムスタンプ、適切な改行を含む人間が読みやすい出力を有効にします。

```console
$ dmesg -H
[May 4 09:15] Linux version 5.15.0-76-generic (buildd@lcy02-amd64-017) (gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #83-Ubuntu SMP
[...]
```

### **-l, --level**

指定された優先度レベル（カンマ区切りリスト）に出力を制限します。

```console
$ dmesg -l err,warn
[    5.123456] ACPI BIOS Error (bug): Could not resolve symbol [\_SB.PCI0.GFX0.DD1F], AE_NOT_FOUND
[    7.654321] WARNING: CPU: 2 PID: 123 at drivers/gpu/drm/i915/intel_runtime_pm.c:655
```

### **-f, --facility**

指定されたファシリティ（カンマ区切りリスト）に出力を制限します。

```console
$ dmesg -f kern,daemon
[    0.123456] kernel: Memory: 16123456K/16777216K available
[    1.234567] systemd[1]: Detected virtualization kvm.
```

### **-t, --notime**

タイムスタンプを表示しません。

```console
$ dmesg -t
Linux version 5.15.0-76-generic (buildd@lcy02-amd64-017) (gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #83-Ubuntu SMP
[...]
```

### **-w, --follow**

新しいメッセージを待機します（`tail -f`と同様）。

```console
$ dmesg -w
[    0.000000] Linux version 5.15.0-76-generic
[...]
[  123.456789] usb 1-2: new high-speed USB device number 3 using xhci_hcd
```

## 使用例

### USBに関連するメッセージのフィルタリング

```console
$ dmesg | grep -i usb
[    2.123456] usb 1-1: new high-speed USB device number 2 using xhci_hcd
[    2.234567] usb 1-1: New USB device found, idVendor=8087, idProduct=0024, bcdDevice= 0.01
[    2.345678] usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
```

### ハードウェアエラーの確認

```console
$ dmesg --level=err
[    5.123456] ACPI BIOS Error (bug): Could not resolve symbol [\_SB.PCI0.GFX0.DD1F], AE_NOT_FOUND
[   10.234567] EXT4-fs error (device sda1): ext4_lookup:1809: inode #2: comm systemd-journal: deleted inode referenced: 12345
```

### リアルタイムでのカーネルメッセージの監視

```console
$ sudo dmesg --follow --human
[May 4 09:20] Linux version 5.15.0-76-generic
[...]
[+0.005678] Booting paravirtualized kernel on bare hardware
[+1.234567] usb 1-2: new high-speed USB device number 3 using xhci_hcd
```

## ヒント:

### 読みやすさを向上させるために人間が読みやすい形式を使用する

`-H`または`--human`オプションを使用すると、相対的なタイムスタンプ、色付き、適切なフォーマットで出力が読みやすくなります。

### 対象を絞ったトラブルシューティングのためにgrepと組み合わせる

特定のハードウェアのトラブルシューティングを行う場合は、`dmesg`の出力を「usb」、「wifi」、「error」などの関連キーワードで`grep`にパイプすると効果的です。

### 読み取り後にバッファをクリアする

`sudo dmesg -c`を使用して、読み取り後にバッファをクリアします。これは、特定のアクションの後に表示される新しいメッセージのみを監視したい場合に役立ちます。

### 後で分析するために起動メッセージを保存する

起動後、`dmesg > boot_log.txt`でカーネルメッセージを保存しておくと、後で分析や比較ができます。

## よくある質問

#### Q1. 「dmesg: read kernel buffer failed: Operation not permitted」というエラーが出るのはなぜですか？
A. 多くのシステムでは、カーネルバッファにアクセスするには root 権限が必要です。代わりに `sudo dmesg` を使用してください。

#### Q2. 最近のメッセージだけを見るにはどうすればいいですか？
A. `dmesg | tail` を使用して最新のメッセージを表示するか、`dmesg -T` を使用して人間が読みやすいタイムスタンプを表示し、時間でフィルタリングします。

#### Q3. dmesg 出力のタイムスタンプをどう解釈すればいいですか？
A. デフォルトでは、タイムスタンプは起動からの秒数を示します。人間が読みやすいタイムスタンプには `-T` または `--ctime` を、相対的なタイムスタンプには `-H` を使用してください。

#### Q4. tail -f のように dmesg を継続的に監視できますか？
A. はい、`dmesg -w` または `dmesg --follow` を使用して、新しいカーネルメッセージを継続的に監視できます。

## macOSに関する注意点

macOSでは、`dmesg`コマンドのオプションはLinuxよりも少なくなっています。`--human`や`--follow`などのオプションはサポートされていません。macOSでより詳細なシステムログを取得するには、代わりに`log`コマンドの使用を検討してください。例えば、`log show --predicate 'eventMessage contains "kernel"'`などです。

## 参考資料

https://man7.org/linux/man-pages/man1/dmesg.1.html

## 改訂履歴

2025/05/04 初版作成