# od command

Display file contents in various formats, primarily octal, hexadecimal, or other numeric representations.

## Overview

The `od` (octal dump) command displays the content of files in various formats. While originally designed to show file contents in octal format, modern versions support multiple output formats including hexadecimal, decimal, ASCII, and more. It's particularly useful for examining binary files, viewing non-printable characters, or analyzing file structures.

## Options

### **-t, --format=TYPE**

Specify the output format type. Common format types include:
- `a` - named characters
- `c` - ASCII characters or backslash escapes
- `d` - signed decimal
- `o` - octal (default)
- `x` - hexadecimal
- `f` - floating point

```console
$ echo "Hello" | od -t c
0000000   H   e   l   l   o  \n
0000006
```

### **-A, --address-radix=RADIX**

Select the radix for displaying file offsets. Options include:
- `d` - decimal (default)
- `o` - octal
- `x` - hexadecimal
- `n` - none (no addresses)

```console
$ echo "Hello" | od -A x -t c
000000   H   e   l   l   o  \n
000006
```

### **-j, --skip-bytes=BYTES**

Skip BYTES input bytes before reading data.

```console
$ echo "Hello World" | od -t c -j 6
0000006   W   o   r   l   d  \n
0000014
```

### **-N, --read-bytes=BYTES**

Limit dump to BYTES input bytes.

```console
$ echo "Hello World" | od -t c -N 5
0000000   H   e   l   l   o
0000005
```

### **-v, --output-duplicates**

Do not use * (asterisk) to mark line suppression.

```console
$ echo "AAAAA" | od -t c -v
0000000   A   A   A   A   A  \n
0000006
```

### **-w, --width=BYTES**

Output BYTES bytes per output line.

```console
$ echo "Hello World" | od -t c -w3
0000000   H   e   l
0000003   l   o      
0000006   W   o   r
0000011   l   d  \n
0000014
```

## Usage Examples

### Viewing file in hexadecimal format

```console
$ echo "Hello" | od -t x1
0000000 48 65 6c 6c 6f 0a
0000006
```

### Viewing file in multiple formats simultaneously

```console
$ echo "ABC" | od -t x1z -t c
0000000 41 42 43 0a                                >ABC.<
0000004   A   B   C  \n
0000004
```

### Examining binary file structure

```console
$ od -t x1 -N 16 /bin/ls
0000000 cf fa ed fe 07 00 00 01 03 00 00 80 02 00 00 00
0000020
```

### Viewing file with custom address format and byte width

```console
$ echo "Hello World" | od -A x -t c -w4
000000   H   e   l   l
000004   o       W   o
000008   r   l   d  \n
00000c
```

## Tips:

### Combine Format Types for Better Analysis

Use multiple `-t` options to display the same data in different formats simultaneously, making it easier to interpret binary data.

### Use with Pipes for Quick Data Inspection

Pipe command output directly to `od` for quick inspection of binary or special character data without creating temporary files.

### Customize Address Display for Readability

Use `-A` to change how addresses are displayed. For example, `-A n` removes addresses completely when you only care about the content.

### Examine Specific Portions of Large Files

Combine `-j` (skip) and `-N` (limit) to examine specific sections of large files without loading the entire file.

## Frequently Asked Questions

#### Q1. What does "od" stand for?
A. "od" stands for "octal dump," reflecting its original purpose of displaying file contents in octal format.

#### Q2. How do I view a file in hexadecimal format?
A. Use `od -t x1` to view the file in hexadecimal format with one byte per hexadecimal number.

#### Q3. How can I view both hexadecimal and ASCII representations?
A. Use `od -t x1 -t c` to display both hexadecimal and character representations side by side.

#### Q4. How do I examine just a portion of a large file?
A. Use `od -j OFFSET -N LENGTH` to examine a specific section, where OFFSET is the starting byte position and LENGTH is how many bytes to read.

#### Q5. Why do I see asterisks (*) in the output?
A. Asterisks indicate repeated lines that have been suppressed. Use the `-v` option to show all lines without suppression.

## References

https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html

## Revisions

- 2025/05/04 First revision