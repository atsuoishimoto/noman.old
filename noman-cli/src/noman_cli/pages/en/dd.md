# dd command

Convert and copy files with block-level operations.

## Overview

`dd` is a command-line utility that copies data between files or devices at a low level, allowing you to specify exact block sizes and counts. It's commonly used for creating disk images, backing up partitions, converting data formats, and performing precise I/O operations where standard file copying tools might not be suitable.

## Options

### **if=FILE**

Specifies the input file to read from (input file)

```console
$ dd if=/dev/sda
```

### **of=FILE**

Specifies the output file to write to (output file)

```console
$ dd of=/dev/sdb
```

### **bs=BYTES**

Sets both input and output block size to BYTES at once

```console
$ dd if=/dev/zero of=testfile bs=1M count=10
10+0 records in
10+0 records out
10485760 bytes (10 MB, 10 MiB) transferred in 0.008832 s, 1.2 GB/s
```

### **count=N**

Copies only N input blocks

```console
$ dd if=/dev/urandom of=random.data bs=1M count=5
5+0 records in
5+0 records out
5242880 bytes (5.2 MB, 5.0 MiB) transferred in 0.043109 s, 122 MB/s
```

### **status=LEVEL**

Controls the information displayed during copying:
- `none`: displays nothing
- `noxfer`: suppresses the final transfer statistics
- `progress`: shows periodic transfer statistics

```console
$ dd if=/dev/zero of=testfile bs=1G count=1 status=progress
536870912 bytes (537 MB, 512 MiB) copied, 0.5 s, 1.1 GB/s
1+0 records in
1+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) transferred in 0.969301 s, 1.1 GB/s
```

## Usage Examples

### Creating a disk image

```console
$ dd if=/dev/sda of=disk.img bs=4M
1024+0 records in
1024+0 records out
4294967296 bytes (4.3 GB, 4.0 GiB) transferred in 45.3 s, 94.8 MB/s
```

### Writing an ISO to a USB drive

```console
$ dd if=ubuntu.iso of=/dev/sdb bs=4M status=progress
1485881344 bytes (1.5 GB, 1.4 GiB) copied, 82 s, 18.1 MB/s
354+1 records in
354+1 records out
1485881344 bytes (1.5 GB, 1.4 GiB) transferred in 82.467 s, 18.0 MB/s
```

### Creating a file of zeros

```console
$ dd if=/dev/zero of=zeros.bin bs=1M count=100
100+0 records in
100+0 records out
104857600 bytes (105 MB, 100 MiB) transferred in 0.082674 s, 1.3 GB/s
```

## Tips

### Use Status=progress for Long Operations

For operations that take a long time, use `status=progress` to see real-time progress instead of waiting blindly.

### Be Extremely Careful with Device Names

Double-check device names (like `/dev/sda`) before executing `dd` commands. Using the wrong device can overwrite important data permanently.

### Use Appropriate Block Sizes

Larger block sizes (like `bs=4M` or `bs=8M`) can significantly improve performance for large transfers, but very large values may cause memory issues.

### Sync After Writing to Devices

After writing to physical devices, run the `sync` command to ensure all data is flushed from cache to the device.

### Use conv Options for Format Conversion

The `conv=` option can perform conversions like `ascii`, `ebcdic`, or `swab` (byte swapping) during the copy operation.

## Frequently Asked Questions

#### Q1. What does "dd" stand for?
A. While often jokingly called "disk destroyer" due to its power to overwrite disks, the name doesn't officially stand for anything specific. It likely comes from IBM JCL's DD (Data Definition) statement.

#### Q2. How can I monitor the progress of a dd operation?
A. Use `status=progress` for newer versions of dd. For older versions, you can send the USR1 signal to the dd process: `kill -USR1 $(pgrep dd)`.

#### Q3. How do I make a bootable USB drive with dd?
A. Use `dd if=image.iso of=/dev/sdX bs=4M status=progress`, where sdX is your USB drive. Make sure to identify the correct device name.

#### Q4. Is dd dangerous to use?
A. Yes, it can be dangerous if used incorrectly. It performs low-level operations and can overwrite entire disks without confirmation. Always double-check device names.

## References

https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html

## Revisions

- 2025/04/30 First revision