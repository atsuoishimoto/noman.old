# truncate command

Shrink or extend the size of a file to a specified size.

## Overview

The `truncate` command modifies a file's size by either shrinking it or extending it to a specified length. It can create new files if they don't exist, and can set multiple files to the same size in a single command. This is useful for quickly creating files of specific sizes or truncating log files.

## Options

### **-s, --size=SIZE**

Set or adjust the file size to SIZE bytes

```console
$ truncate -s 100 myfile.txt
$ ls -l myfile.txt
-rw-r--r-- 1 user group 100 May 4 10:15 myfile.txt
```

### **-c, --no-create**

Do not create files that do not exist

```console
$ truncate -c -s 50 nonexistent.txt
truncate: cannot open 'nonexistent.txt' for writing: No such file or directory
```

### **-o, --io-blocks**

Treat SIZE as number of IO blocks instead of bytes

```console
$ truncate -o -s 2 blockfile.dat
```

### **-r, --reference=RFILE**

Base size on RFILE's size

```console
$ truncate -r reference.txt target.txt
```

## Usage Examples

### Creating a new empty file of specific size

```console
$ truncate -s 1M largefile.bin
$ ls -lh largefile.bin
-rw-r--r-- 1 user group 1.0M May 4 10:20 largefile.bin
```

### Shrinking an existing file

```console
$ echo "This is a test file with some content" > testfile.txt
$ truncate -s 10 testfile.txt
$ cat testfile.txt
This is a 
```

### Using relative sizes

```console
$ truncate -s 100 myfile.txt    # Set to exactly 100 bytes
$ truncate -s +50 myfile.txt    # Add 50 bytes (now 150 bytes)
$ truncate -s -30 myfile.txt    # Remove 30 bytes (now 120 bytes)
$ truncate -s %64 myfile.txt    # Round size down to multiple of 64 (96 bytes)
```

## Tips

### Zero-filling vs Truncation

When extending a file, `truncate` doesn't fill the new space with zeros or any other data - it simply extends the file size. This creates a "sparse file" where the extended portion doesn't actually use disk space until written to.

### Quick Log Rotation

You can use `truncate -s 0` to quickly empty a log file without deleting it, which preserves file permissions and ownership:

```console
$ truncate -s 0 /path/to/logfile.log
```

### Creating Test Files

Create test files of specific sizes for testing disk space or file transfer operations:

```console
$ truncate -s 10M test10mb.bin
$ truncate -s 1G test1gb.bin
```

## Frequently Asked Questions

#### Q1. What's the difference between `truncate` and `touch`?
A. While `touch` updates timestamps and can create empty files, `truncate` can create files of specific sizes or modify existing file sizes.

#### Q2. Does `truncate` actually allocate disk space?
A. When extending files, `truncate` creates sparse files that don't immediately consume the full disk space until data is written to them.

#### Q3. Can I use `truncate` to append data to a file?
A. No, `truncate` only changes file size without adding content. To append data, use redirection (`>>`) or tools like `echo` or `cat`.

#### Q4. How do I completely empty a file without deleting it?
A. Use `truncate -s 0 filename` to reduce the file size to zero while preserving the file itself.

## References

https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html

## Revisions

- 2025/05/04 First revision