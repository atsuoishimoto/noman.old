# dmesg command

Display or control the kernel message buffer.

## Overview

The `dmesg` command displays kernel messages from the system ring buffer, which contains information about hardware, device drivers, and system initialization. It's particularly useful for troubleshooting hardware issues, checking boot messages, and monitoring kernel events.

## Options

### **-c, --clear**

Clear the ring buffer after printing its contents.

```console
$ sudo dmesg -c
[    0.000000] Linux version 5.15.0-76-generic (buildd@lcy02-amd64-017) (gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #83-Ubuntu SMP
[...]
```

### **-H, --human**

Enable human-readable output with colors, relative timestamps, and appropriate line breaks.

```console
$ dmesg -H
[May 4 09:15] Linux version 5.15.0-76-generic (buildd@lcy02-amd64-017) (gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #83-Ubuntu SMP
[...]
```

### **-l, --level**

Restrict output to the specified priority levels (comma-separated list).

```console
$ dmesg -l err,warn
[    5.123456] ACPI BIOS Error (bug): Could not resolve symbol [\_SB.PCI0.GFX0.DD1F], AE_NOT_FOUND
[    7.654321] WARNING: CPU: 2 PID: 123 at drivers/gpu/drm/i915/intel_runtime_pm.c:655
```

### **-f, --facility**

Restrict output to the specified facilities (comma-separated list).

```console
$ dmesg -f kern,daemon
[    0.123456] kernel: Memory: 16123456K/16777216K available
[    1.234567] systemd[1]: Detected virtualization kvm.
```

### **-t, --notime**

Don't print timestamps.

```console
$ dmesg -t
Linux version 5.15.0-76-generic (buildd@lcy02-amd64-017) (gcc (Ubuntu 11.3.0-1ubuntu1~22.04) 11.3.0, GNU ld (GNU Binutils for Ubuntu) 2.38) #83-Ubuntu SMP
[...]
```

### **-w, --follow**

Wait for new messages (similar to `tail -f`).

```console
$ dmesg -w
[    0.000000] Linux version 5.15.0-76-generic
[...]
[  123.456789] usb 1-2: new high-speed USB device number 3 using xhci_hcd
```

## Usage Examples

### Filtering for USB-related messages

```console
$ dmesg | grep -i usb
[    2.123456] usb 1-1: new high-speed USB device number 2 using xhci_hcd
[    2.234567] usb 1-1: New USB device found, idVendor=8087, idProduct=0024, bcdDevice= 0.01
[    2.345678] usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
```

### Checking for hardware errors

```console
$ dmesg --level=err
[    5.123456] ACPI BIOS Error (bug): Could not resolve symbol [\_SB.PCI0.GFX0.DD1F], AE_NOT_FOUND
[   10.234567] EXT4-fs error (device sda1): ext4_lookup:1809: inode #2: comm systemd-journal: deleted inode referenced: 12345
```

### Monitoring kernel messages in real-time

```console
$ sudo dmesg --follow --human
[May 4 09:20] Linux version 5.15.0-76-generic
[...]
[+0.005678] Booting paravirtualized kernel on bare hardware
[+1.234567] usb 1-2: new high-speed USB device number 3 using xhci_hcd
```

## Tips

### Use Human-Readable Format for Better Readability

The `-H` or `--human` option makes output much easier to read with relative timestamps, colors, and proper formatting.

### Combine with grep for Targeted Troubleshooting

When troubleshooting specific hardware, pipe `dmesg` output to `grep` with relevant keywords like "usb", "wifi", or "error".

### Clear the Buffer After Reading

Use `sudo dmesg -c` to clear the buffer after reading it. This can help when you want to monitor only new messages that appear after a specific action.

### Save Boot Messages for Later Analysis

After booting, save the kernel messages with `dmesg > boot_log.txt` for later analysis or comparison.

## Frequently Asked Questions

#### Q1. Why do I get "dmesg: read kernel buffer failed: Operation not permitted"?
A. On many systems, you need root privileges to access the kernel buffer. Use `sudo dmesg` instead.

#### Q2. How can I see only recent messages?
A. Use `dmesg | tail` to see the most recent messages, or use `dmesg -T` to show human-readable timestamps and filter by time.

#### Q3. How do I interpret the timestamps in dmesg output?
A. By default, timestamps show seconds since boot. Use `-T` or `--ctime` for human-readable timestamps, or `-H` for relative timestamps.

#### Q4. Can I monitor dmesg continuously like tail -f?
A. Yes, use `dmesg -w` or `dmesg --follow` to continuously monitor new kernel messages.

## macOS Considerations

On macOS, the `dmesg` command has fewer options than on Linux. It doesn't support options like `--human` or `--follow`. For more detailed system logs on macOS, consider using the `log` command instead, e.g., `log show --predicate 'eventMessage contains "kernel"'`.

## References

https://man7.org/linux/man-pages/man1/dmesg.1.html

## Revisions

2025/05/04 First revision