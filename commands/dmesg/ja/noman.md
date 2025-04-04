# dmesgコマンド概要

`dmesg`はカーネルのリングバッファからシステムメッセージを表示するコマンドです。起動時のハードウェア検出やエラーメッセージなど、システムの診断情報を確認するのに役立ちます。

## 主なオプション

- **`-H`, `--human`**: 人間が読みやすい形式で出力します（タイムスタンプの整形、色付けなど）
  - 例: `dmesg -H`

- **`-c`, `--clear`**: メッセージを表示した後、バッファをクリアします
  - 例: `dmesg -c`

- **`-f`, `--facility=LIST`**: 指定した種類（facility）のメッセージのみを表示します（例：kern, user, daemon）
  - 例: `dmesg -f kern`

- **`-l`, `--level=LIST`**: 指定したレベルのメッセージのみを表示します（例：err, warn, info）
  - 例: `dmesg -l err,warn`

- **`-T`, `--ctime`**: 人間が読みやすい時刻形式で表示します
  - 例: `dmesg -T`

- **`-w`, `--follow`**: 新しいメッセージを待ち続けます（`tail -f`のような動作）
  - 例: `dmesg -w`

- **`-k`, `--kernel`**: カーネルメッセージを表示します（デフォルト）
  - 例: `dmesg -k`

## 使用例

```bash
# 基本的な使用法（すべてのカーネルメッセージを表示）
dmesg
# 出力例
[    0.000000] Linux version 5.4.0-42-generic (buildd@lgw01-amd64-060) (gcc version 9.3.0 (Ubuntu 9.3.0-10ubuntu2)) #46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020
[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-42-generic root=UUID=1234abcd-1234-1234-1234-1234abcd ro quiet splash
...
```

```bash
# 人間が読みやすい形式で表示
dmesg -H
# 出力例
[Jul15 10:58] Linux version 5.4.0-42-generic (buildd@lgw01-amd64-060) (gcc version 9.3.0 (Ubuntu 9.3.0-10ubuntu2)) #46-Ubuntu SMP Fri Jul 10 00:24:02 UTC 2020
[  +0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-42-generic root=UUID=1234abcd-1234-1234-1234-1234abcd ro quiet splash
...
```

```bash
# エラーと警告のみを表示
dmesg -l err,warn
# 出力例
[12345.678901] usb 1-2: device descriptor read/64, error -110
[12346.789012] sd 0:0:0:0: [sda] Assuming drive cache: write through
```

```bash
# 新しいメッセージをリアルタイムで監視
dmesg -w
# 出力例（新しいメッセージが発生するたびに表示されます）
[12347.890123] usb 2-1: new high-speed USB device number 3 using ehci-pci
[12348.901234] usb 2-1: New USB device found, idVendor=abcd, idProduct=1234, bcdDevice=1.00
```

## 追加情報

- システムの問題を診断する際に、`dmesg | grep -i error`のようにgrepと組み合わせて特定のメッセージを検索すると効果的です。
- 最新のメッセージだけを見たい場合は、`dmesg | tail`を使用すると便利です。
- Linuxディストリビューションによっては、`/var/log/dmesg`にログが保存されていることもあります。
- 一般ユーザーでは一部のメッセージが表示されないことがあります。重要な診断を行う場合は`sudo dmesg`を使用してください。