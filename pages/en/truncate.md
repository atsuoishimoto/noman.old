# truncate command

Shrink or extend the size of a file to a specified size.

## Overview

The `truncate` command modifies a file's size by either shrinking it or extending it to a specified length. It can create new empty files of a specific size or adjust existing files without having to rewrite their entire contents, making it faster than other methods for resizing files.

## Options

### **-s, --size=SIZE**

Set or adjust the file size to SIZE bytes

```console
$ truncate -s 100 myfile.txt
```

### **-c, --no-create**

Do not create files that don't exist

```console
$ truncate -c -s 50 nonexistent.txt
truncate: cannot open 'nonexistent.txt' for writing: No such file or directory
```

### **-r, --reference=RFILE**

Base size on RFILE's size

```console
$ truncate -r reference.txt myfile.txt
```

## Usage Examples

### Creating a new empty file of specific size

```console
$ truncate -s 1M newfile.dat
$ ls -lh newfile.dat
-rw-r--r-- 1 user group 1.0M Apr 30 10:15 newfile.dat
```

### Shrinking an existing file

```console
$ echo "This is a test file with some content" > testfile.txt
$ ls -l testfile.txt
-rw-r--r-- 1 user group 38 Apr 30 10:16 testfile.txt
$ truncate -s 10 testfile.txt
$ ls -l testfile.txt
-rw-r--r-- 1 user group 10 Apr 30 10:16 testfile.txt
$ cat testfile.txt
This is a 
```

### Using relative sizes

```console
$ truncate -s 100 myfile.txt
$ truncate -s +50 myfile.txt  # Add 50 bytes
$ truncate -s -30 myfile.txt  # Remove 30 bytes
```

## Tips

### Use Size Suffixes for Readability

You can use suffixes like K (kilobytes), M (megabytes), G (gigabytes) to specify sizes more easily:

```console
$ truncate -s 10K myfile.txt  # Creates a 10 kilobyte file
```

### Data Loss Warning

Be careful when shrinking files as `truncate` permanently removes data beyond the specified size without confirmation.

### Zero-filling vs. Sparse Files

When extending files, `truncate` creates sparse files (files with "holes") rather than filling them with zeros, which saves disk space but might behave differently than expected with some applications.

## Frequently Asked Questions

#### Q1. What's the difference between truncate and dd for creating files?
A. `truncate` is much faster for creating empty files as it only modifies file metadata, while `dd` actually writes data to the disk.

#### Q2. Can truncate recover data after shrinking a file?
A. No, once a file is truncated, the removed data is permanently lost and cannot be recovered.

#### Q3. How do I create a file with actual data instead of a sparse file?
A. Use `dd` with `if=/dev/zero` instead of `truncate` if you need a file filled with zeros rather than a sparse file.

#### Q4. What happens if I truncate a file to a larger size?
A. The file size increases, but the new space is not filled with any data (creating a sparse file). Reading from this extended area will return zeros.

## References

https://www.gnu.org/software/coreutils/manual/html_node/truncate-invocation.html

## Revisions

- 2025/04/30 First revision