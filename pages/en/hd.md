# hd command

Display file contents in hexadecimal, decimal, octal, or ASCII format.

## Overview

The `hd` command (hexdump) displays the contents of files in various formats, primarily hexadecimal. It's useful for examining binary files, debugging data formats, or viewing non-printable characters in text files. The command reads from files or standard input and outputs a formatted representation of the data.

## Options

### **-n LENGTH**

Limit the output to the first LENGTH bytes of input

```console
$ echo "Hello" | hd -n 3
00000000  48 65 6c                                          |Hel|
```

### **-s OFFSET**

Skip OFFSET bytes from the beginning of input

```console
$ echo "Hello World" | hd -s 6
00000006  57 6f 72 6c 64 0a                                 |World.|
```

### **-v**

Display all input data (suppress the * line that indicates duplicate content)

```console
$ echo "AAAAAAAA" | hd -v
00000000  41 41 41 41 41 41 41 41  0a                       |AAAAAAAA.|
```

### **-c BYTES**

Format output with BYTES number of octets per line

```console
$ echo "Hello World" | hd -c 4
00000000  48 65 6c 6c                                       |Hell|
00000004  6f 20 57 6f                                       |o Wo|
00000008  72 6c 64 0a                                       |rld.|
```

## Usage Examples

### Basic hexdump of a file

```console
$ hd sample.txt
00000000  48 65 6c 6c 6f 20 57 6f  72 6c 64 0a 54 68 69 73  |Hello World.This|
00000010  20 69 73 20 61 20 74 65  73 74 2e 0a              | is a test..|
0000001c
```

### Examining binary data

```console
$ hd /bin/ls | head -3
00000000  cf fa ed fe 07 00 00 01  03 00 00 80 02 00 00 00  |................|
00000010  10 00 00 00 18 07 00 00  85 00 20 00 00 00 00 00  |.......... .....|
00000020  19 00 00 00 48 00 00 00  5f 5f 50 41 47 45 5a 45  |....H...__PAGEZE|
```

### Piping data to hd

```console
$ echo -n "Binary data" | hd
00000000  42 69 6e 61 72 79 20 64  61 74 61                 |Binary data|
0000000b
```

## Tips

### Comparing Binary Files

Use `hd` with `diff` to compare binary files: `diff <(hd file1) <(hd file2)` to see exactly where and how files differ.

### Examining File Headers

Use `hd -n 32 filename` to examine just the first 32 bytes of a file, which often contains header information that identifies the file type.

### Customizing Output Format

Combine options like `-c` and `-v` to create a more readable format when examining complex binary structures.

### Alternative Commands

On some systems, `hexdump` or `xxd` commands may be available as alternatives with similar functionality.

## Frequently Asked Questions

#### Q1. What's the difference between `hd` and `hexdump`?
A. On many systems, `hd` is actually a symbolic link to `hexdump` or provides similar functionality with a shorter name. The specific behavior may vary slightly between systems.

#### Q2. How can I convert hexadecimal output back to binary?
A. `hd` is primarily for displaying data, not converting it back. For the reverse operation, consider using tools like `xxd -r` or dedicated hex editors.

#### Q3. Can I use `hd` to edit binary files?
A. No, `hd` is only for viewing file contents. To edit binary files, use a hex editor like `hexedit` or `bvi`.

#### Q4. How do I interpret the output format?
A. The left column shows byte offsets in hexadecimal, the middle columns show the hexadecimal values of each byte, and the right column shows the ASCII representation (with dots for non-printable characters).

## macOS Considerations

On macOS, `hd` is typically available as part of the base system. However, its behavior and available options may differ slightly from other Unix-like systems. If you need more advanced hexdump functionality, consider installing GNU hexdump via Homebrew with `brew install hexdump`.

## References

https://www.freebsd.org/cgi/man.cgi?query=hexdump

## Revisions

- 2025/04/30 First revision