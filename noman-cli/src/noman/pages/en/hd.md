# hd command

Display file contents in hexadecimal, decimal, octal, or ASCII format.

## Overview

The `hd` command (hexdump) is a utility that displays the contents of files in various formats, primarily hexadecimal. It's useful for examining binary files, debugging data formats, or viewing non-printable characters in text files. The command reads from files or standard input and outputs a formatted representation of the data.

## Options

### **-a, --ascii-dump**

Display ASCII characters alongside the hex dump.

```console
$ echo "Hello" | hd -a
00000000  48 65 6c 6c 6f 0a                                 |Hello.|
00000006
```

### **-c, --canonical**

Display output in canonical hex+ASCII format, showing both hexadecimal values and their ASCII representation.

```console
$ echo "Hello" | hd -c
00000000  48 65 6c 6c 6f 0a                                 |Hello.|
00000006
```

### **-n, --length=N**

Process only the first N bytes of input.

```console
$ echo "Hello World" | hd -n 5
00000000  48 65 6c 6c 6f                                    |Hello|
00000005
```

### **-s, --skip=N**

Skip the first N bytes of input.

```console
$ echo "Hello World" | hd -s 6
00000006  57 6f 72 6c 64 0a                                 |World.|
0000000c
```

### **-v, --no-squeezing**

Display all input data lines, even if they are identical to the previous line.

```console
$ echo -e "AAAA\nAAAA" | hd -v
00000000  41 41 41 41 0a 41 41 41  41 0a                    |AAAA.AAAA.|
0000000a
```

## Usage Examples

### Basic Hexadecimal Dump

```console
$ echo "Hello, World!" | hd
00000000  48 65 6c 6c 6f 2c 20 57  6f 72 6c 64 21 0a        |Hello, World!.|
0000000e
```

### Examining a Binary File

```console
$ hd -n 32 /bin/ls
00000000  cf fa ed fe 07 00 00 01  03 00 00 80 02 00 00 00  |................|
00000010  10 00 00 00 18 07 00 00  85 00 20 00 00 00 00 00  |.......... .....|
00000020
```

### Displaying Different Number Formats

```console
$ echo "ABC" | hd -e '16/1 "%02x " "\n"'
00000000  41 42 43 0a                                       
00000004
```

## Tips

### Examining File Headers

Use `hd -n 16 filename` to quickly examine the first 16 bytes of a file, which often contains format identification information or magic numbers.

### Comparing Binary Files

You can use `hd` with `diff` to compare binary files: `diff <(hd file1) <(hd file2)`.

### Customizing Output Format

The `-e` option allows you to specify custom output formats for more specialized viewing needs.

### Alternative Commands

On some systems, `hexdump` or `xxd` may be available instead of `hd` with similar functionality.

## Frequently Asked Questions

#### Q1. What's the difference between `hd` and `hexdump`?
A. On many systems, `hd` is actually a symbolic link to `hexdump`. They are essentially the same command, with `hd` being a shorter alias.

#### Q2. How can I view only the ASCII representation?
A. Use `hd -c` to see both hex and ASCII, or for ASCII-only, you might need to use a custom format with the `-e` option.

#### Q3. Can `hd` modify files?
A. No, `hd` is only for viewing file contents. It cannot modify files directly.

#### Q4. How do I interpret the output?
A. The leftmost column shows the byte offset in hexadecimal. The middle columns show the hex values of each byte. The rightmost section (after the `|` characters) shows the ASCII representation of those bytes.

## References

https://man7.org/linux/man-pages/man1/hexdump.1.html

## Revisions

- 2025/05/04 First revision