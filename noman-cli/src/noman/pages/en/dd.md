# dd command

Convert and copy files with block-level operations.

## Overview

`dd` is a command-line utility for copying and converting data. Unlike standard copy commands, it allows precise control over block sizes, byte order, and data transformations. It's commonly used for creating disk images, backing up partitions, converting file formats, and performing low-level data operations.

## Options

### **-if=FILE, --input=FILE**

Specifies the input file to read from (default is standard input)

```console
$ dd if=/dev/sda
```

### **-of=FILE, --output=FILE**

Specifies the output file to write to (default is standard output)

```console
$ dd if=/dev/sda of=/dev/sdb
```

### **-bs=BYTES, --block-size=BYTES**

Sets both input and output block sizes to BYTES

```console
$ dd if=/dev/zero of=testfile bs=1M count=10
10+0 records in
10+0 records out
10485760 bytes (10 MB, 10 MiB) copied, 0.0119631 s, 876 MB/s
```

### **-count=N, --count=N**

Copies only N input blocks

```console
$ dd if=/dev/urandom of=random.dat bs=1M count=5
5+0 records in
5+0 records out
5242880 bytes (5.2 MB, 5.0 MiB) copied, 0.0452266 s, 116 MB/s
```

### **-status=LEVEL, --status=LEVEL**

Controls the level of information displayed (none, noxfer, progress)

```console
$ dd if=/dev/zero of=testfile bs=1M count=100 status=progress
51380224 bytes (51 MB, 49 MiB) copied, 0.0519088 s, 990 MB/s
100+0 records in
100+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 0.105822 s, 991 MB/s
```

### **-conv=CONVS, --conv=CONVS**

Converts the file as per the comma-separated symbol list

```console
$ dd if=input.txt of=output.txt conv=ucase
```

## Usage Examples

### Creating a disk image

```console
$ dd if=/dev/sda of=disk.img bs=4M status=progress
8589934592 bytes (8.6 GB, 8.0 GiB) copied, 126 s, 68.2 MB/s
2048+0 records in
2048+0 records out
8589934592 bytes (8.6 GB, 8.0 GiB) copied, 126.453 s, 67.9 MB/s
```

### Creating a bootable USB drive

```console
$ sudo dd if=ubuntu.iso of=/dev/sdb bs=4M status=progress conv=fsync
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 35.6279 s, 30.1 MB/s
256+0 records in
256+0 records out
1073741824 bytes (1.1 GB, 1.0 GiB) copied, 35.6423 s, 30.1 MB/s
```

### Creating a file of zeros

```console
$ dd if=/dev/zero of=zeros.bin bs=1M count=100
100+0 records in
100+0 records out
104857600 bytes (105 MB, 100 MiB) copied, 0.101822 s, 1.0 GB/s
```

## Tips

### Use Status Progress for Long Operations

For operations that take a long time, use `status=progress` to see real-time information about the copy process.

### Be Careful with Block Devices

When working with block devices like `/dev/sda`, double-check your command before executing. A mistake can overwrite important data.

### Optimize Performance with Block Size

Larger block sizes (like `bs=4M` or `bs=8M`) often improve performance for large transfers, but very large values may not always be better.

### Use fsync for USB Drives

When writing to USB drives, add `conv=fsync` to ensure all data is written to the device before dd completes.

### Backup the MBR

To backup just the Master Boot Record: `sudo dd if=/dev/sda of=mbr.bin bs=512 count=1`

## Frequently Asked Questions

#### Q1. How do I clone an entire hard drive?
A. Use `dd if=/dev/source_drive of=/dev/destination_drive bs=4M status=progress`. Make sure the destination drive is at least as large as the source.

#### Q2. Why is dd called "disk destroyer"?
A. This nickname comes from its potential to cause data loss if used incorrectly. Always double-check device names before executing dd commands.

#### Q3. How can I make dd faster?
A. Increase the block size (bs) parameter to values like 4M or 8M, and avoid unnecessary conversions.

#### Q4. How do I create a file of a specific size?
A. Use `dd if=/dev/zero of=filename bs=1M count=X` where X is the desired size in megabytes.

#### Q5. How do I monitor dd progress?
A. Use `status=progress` option in newer versions. For older versions, you can send the USR1 signal to the dd process: `kill -USR1 $(pgrep dd)`.

## References

https://www.gnu.org/software/coreutils/manual/html_node/dd-invocation.html

## Revisions

- 2025/05/04 First revision