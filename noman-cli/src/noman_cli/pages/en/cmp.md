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
$ cmp -i 10 file1.bin file2.bin
file1.bin file2.bin differ: byte 11, line 1
```

### **-l, --verbose**

Output all differences, not just the first one

```console
$ cmp -l file1.txt file2.txt
5 141 142
8 164 167
12 141 142
```

### **-s, --silent, --quiet**

Output nothing, only return exit status (0 for identical, 1 for different)

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
image1.jpg image2.jpg differ: byte 1024, line 3
```

### Using cmp in Scripts

```console
$ if cmp -s file1.txt file2.txt; then
>   echo "Files are identical"
> else
>   echo "Files are different"
> fi
Files are different
```

## Tips

### Use Silent Mode for Scripts

The `-s` option makes `cmp` output nothing, but sets an exit status (0 for identical, 1 for different). This is perfect for shell scripts where you only need to know if files match.

### Compare Specific Portions of Files

Use the `-i` option to skip the beginning of files, which is useful when comparing files with identical headers but potentially different content.

### Combine with Other Commands

Pipe the output of other commands to `cmp` using process substitution to compare their results:
```console
$ cmp <(command1) <(command2)
```

### Binary vs Text Files

Remember that `cmp` treats all files as binary by default. For text file comparisons with more context, `diff` might be more appropriate.

## Frequently Asked Questions

#### Q1. What's the difference between `cmp` and `diff`?
A. `cmp` reports only the first byte where files differ and is suitable for binary files, while `diff` shows all differences and is designed for text files.

#### Q2. How can I check if two files are identical?
A. Use `cmp -s file1 file2` and check the exit status with `echo $?`. A status of 0 means identical files.

#### Q3. Can `cmp` compare directories?
A. No, `cmp` only compares files. For directory comparisons, use `diff -r` instead.

#### Q4. How do I interpret the output of `cmp -l`?
A. It shows three columns: byte position, octal value in first file, and octal value in second file for each differing byte.

## References

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html

## Revisions

- 2025/04/30 First revision