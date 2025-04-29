# dmesgコマンド
カーネルのリングバッファからシステムメッセージを表示します。

## 概要
dmesgコマンドは、Linuxカーネルのリングバッファに記録されたシステムメッセージを表示します。起動時のハードウェア検出、デバイスドライバの読み込み、エラーメッセージなど、システムの診断情報を確認するのに役立ちます。システム管理者やトラブルシューティングを行うユーザーにとって重要なツールです。

## オプション
### **-H, --human**
人間が読みやすい形式で出力します（タイムスタンプの整形、色付けなど）
```console
$ dmesg -H
[4月29 10:58] Linux version 5.15.0-91-generic (buildd@lcy02-amd64-017) (gcc version 11.4.0) #101-Ubuntu SMP Tue Apr 20 14:30:22 UTC 2023
[  +0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-91-generic root=UUID=1234abcd-1234-1234-1234-1234abcd ro quiet splash
```

### **-c, --clear**
メッセージを表示した後、バッファをクリアします
```console
$ dmesg -c
[12345.678901] usb 1-2: new high-speed USB device number 3 using xhci_hcd
[12345.789012] usb 1-2: New USB device found, idVendor=abcd, idProduct=1234
```

### **-l, --level=LIST**
指定したレベル（err, warn, info など）のメッセージのみを表示します
```console
$ dmesg -l err,warn
[12345.678901] usb 1-2: device descriptor read/64, error -110
[12346.789012] sd 0:0:0:0: [sda] Assuming drive cache: write through
```

### **-T, --ctime**
人間が読みやすい時刻形式で表示します
```console
$ dmesg -T
[水 4月 29 10:58:23 2025] Linux version 5.15.0-91-generic (buildd@lcy02-amd64-017) (gcc version 11.4.0)
[水 4月 29 10:58:23 2025] Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-91-generic root=UUID=1234abcd-1234-1234-1234-1234abcd ro quiet splash
```

### **-w, --follow**
新しいメッセージを待ち続けます（`tail -f`のような動作）
```console
$ dmesg -w
[12347.890123] usb 2-1: new high-speed USB device number 3 using ehci-pci
[12348.901234] usb 2-1: New USB device found, idVendor=abcd, idProduct=1234, bcdDevice=1.00
# 新しいメッセージが発生するたびに表示される
```

## 使用例
### 基本的な使用法
```console
$ dmesg
[    0.000000] Linux version 5.15.0-91-generic (buildd@lcy02-amd64-017) (gcc version 11.4.0) #101-Ubuntu SMP Tue Apr 20 14:30:22 UTC 2023
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.15.0-91-generic root=UUID=1234abcd-1234-1234-1234-1234abcd ro quiet splash
# 以下、多数のメッセージが表示される
```

### 特定のキーワードでフィルタリング
```console
$ dmesg | grep -i usb
[    2.123456] usb 1-1: new high-speed USB device number 2 using xhci_hcd
[    2.234567] usb 1-1: New USB device found, idVendor=8087, idProduct=0024
# USBに関連するメッセージのみが表示される
```

### 最新のメッセージのみを表示
```console
$ dmesg | tail -n 10
[12345.678901] wlan0: associated
[12345.789012] IPv6: ADDRCONF(NETDEV_CHANGE): wlan0: link becomes ready
# 最新の10行のメッセージが表示される
```

## ヒント:
### 管理者権限の使用
一般ユーザーでは一部のメッセージが表示されないことがあります。重要な診断を行う場合は`sudo dmesg`を使用してください。

### ログファイルの確認
多くのLinuxディストリビューションでは、起動時のdmesgの出力が`/var/log/dmesg`または`/var/log/boot.log`に保存されています。過去の起動情報を確認したい場合はこれらのファイルを参照してください。

### 効果的なトラブルシューティング
ハードウェアの問題を診断する際は、デバイスを接続した直後に`dmesg | tail`を実行すると、そのデバイスに関連する最新のメッセージを確認できます。

### タイムスタンプの解釈
デフォルトのタイムスタンプは起動からの秒数です。`-T`または`-H`オプションを使用すると、より読みやすい時刻形式で表示されます。

## よくある質問
#### Q1. dmesgの出力が多すぎる場合、どうすれば必要な情報だけを見つけられますか？
A. `dmesg | grep キーワード`を使用して特定のキーワードでフィルタリングしたり、`dmesg -l err,warn`でエラーと警告のみを表示したりすることができます。

#### Q2. dmesgの出力をファイルに保存するにはどうすればよいですか？
A. `dmesg > ファイル名.txt`を実行すると、出力をファイルに保存できます。

#### Q3. dmesgのバッファサイズはどのくらいですか？
A. デフォルトでは数百KBですが、`/proc/sys/kernel/printk`の設定によって変わります。古いメッセージは新しいメッセージによって上書きされます。

#### Q4. macOSでdmesgは使えますか？
A. macOSにもdmesgコマンドはありますが、Linuxとは異なる動作をします。macOSでは`log show --predicate 'eventMessage contains "kernel"'`コマンドを使用することでカーネルログを確認できます。

## 参考
https://man7.org/linux/man-pages/man1/dmesg.1.html

## 改訂
- 2025/04/29 macOSでの使用に関する情報を追加。よくある質問セクションを拡充。
- 2025/04/29 初版作成。