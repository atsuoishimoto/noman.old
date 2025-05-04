# cmp command

Compare two files byte by byte.

## Overview

The `cmp` command compares two files of any type and reports the position of the first difference found. Unlike `diff`, which shows all differences between text files, `cmp` simply identifies the first byte or line where files differ, making it useful for quick binary file comparisons.

## Options

### **-b, --print-bytes**

Print differing bytes as octal values

```console
$ cmp -b file1.txt file2.txt
file1.txt file2.txt differ: byte 5, line 1 is 141 a 142 b
```

### **-i, --ignore-initial=SKIP**

Skip the first SKIP bytes of input

```console
$ cmp -i 10 file1.txt file2.txt
file1.txt file2.txt differ: byte 11, line 2
```

### **-l, --verbose**

Output byte numbers and differing byte values for all differences

```console
$ cmp -l file1.txt file2.txt
5 141 142
10 156 157
15 163 164
```

### **-n, --bytes=LIMIT**

Compare at most LIMIT bytes

```console
$ cmp -n 20 file1.txt file2.txt
file1.txt file2.txt differ: byte 5, line 1
```

### **-s, --quiet, --silent**

Suppress all normal output (only return exit status)

```console
$ cmp -s file1.txt file2.txt
$ echo $?
1
```

## Usage Examples

### Basic Comparison

```console
$ cmp file1.txt file2.txt
file1.txt file2.txt differ: byte 5, line 1
```

### Comparing Binary Files

```console
$ cmp image1.jpg image2.jpg
image1.jpg image2.jpg differ: byte 1024, line 8
```

### Silent Mode with Exit Status in Scripts

```console
$ cmp -s file1.txt file2.txt && echo "Files are identical" || echo "Files differ"
Files differ
```

## Tips

### Understanding Exit Status

The `cmp` command returns exit status 0 if files are identical, 1 if files differ, and 2 if an error occurred. This makes it perfect for shell scripts where you need to check file equality.

### Comparing Portions of Files

Use `-i` and `-n` together to compare specific sections of files, which is useful when comparing large files where you only care about certain regions.

### Binary vs Text Comparisons

While `diff` is better for text files, `cmp` works well for both text and binary files. Use `cmp -l` for detailed binary comparisons when you need to see all differences.

## Frequently Asked Questions

#### Q1. What's the difference between `cmp` and `diff`?
A. `cmp` reports only the first byte where files differ, while `diff` shows all differences and is optimized for text files. `cmp` works equally well with binary files.

#### Q2. How can I check if two files are identical in a script?
A. Use `cmp -s file1 file2` and check the exit status with `$?`. A status of 0 means the files are identical.

#### Q3. Can `cmp` compare directories?
A. No, `cmp` only compares files. For directory comparisons, use `diff -r` instead.

#### Q4. How do I see all differences between binary files?
A. Use `cmp -l file1 file2` to see all byte positions and values where the files differ.

## References

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html

## Revisions

- 2025/05/04 First revision