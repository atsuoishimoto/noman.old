# od command

Display file contents in various formats, including octal, decimal, hexadecimal, and ASCII.

## Overview

The `od` (octal dump) command displays the content of files in different formats. Originally designed to show data in octal format, modern versions support multiple output formats including hexadecimal, decimal, ASCII, and more. It's particularly useful for examining binary files, viewing non-printable characters, or analyzing file content byte by byte.

## Options

### **-t TYPE**

Specify the output format type. Common types include:
- `x`: hexadecimal
- `d`: decimal
- `o`: octal (default)
- `c`: ASCII characters and backslash escapes
- `a`: named characters

```console
$ echo "Hello" | od -t x1
0000000    48  65  6c  6c  6f  0a
0000006
```

### **-A FORMAT**

Specify the address radix for displaying file offsets:
- `d`: decimal (default)
- `o`: octal
- `x`: hexadecimal
- `n`: none (no addresses)

```console
$ echo "Hello" | od -A x -t c
000000    H   e   l   l   o  \n
000006
```

### **-N BYTES**

Limit output to the first BYTES bytes of input

```console
$ echo "Hello World" | od -N 5 -t c
0000000    H   e   l   l   o
0000005
```

### **-j BYTES**

Skip BYTES bytes from the beginning of input

```console
$ echo "Hello World" | od -j 6 -t c
0000006    W   o   r   l   d  \n
0000014
```

## Usage Examples

### Viewing file content in hexadecimal format

```console
$ echo "ABC123" > sample.txt
$ od -t x1 sample.txt
0000000    41  42  43  31  32  33  0a
0000007
```

### Multiple format display

```console
$ echo "Hello" | od -t x1z -t c
0000000    48  65  6c  6c  6f  0a                              >Hello.
           H   e   l   l   o  \n
0000006
```

### Examining binary file

```console
$ od -t x1 -N 16 /bin/ls
0000000    cf  fa  ed  fe  07  00  00  01  03  00  00  00  02  00  00  00
0000020
```

## Tips

### Combine Format Types

Use multiple `-t` options to display the same data in different formats simultaneously, making it easier to interpret binary data.

### Examining Non-Printable Characters

Use `-t c` to see ASCII representation of data, which helps identify control characters and other non-printable bytes.

### Byte Grouping

Append a number to the format type (like `-t x2` or `-t d4`) to group bytes together, which is useful for viewing 16-bit or 32-bit values.

### Analyzing File Structure

Use `-j` with `-N` to examine specific sections of a file, which is helpful when analyzing file headers or specific data structures.

## Frequently Asked Questions

#### Q1. What does "od" stand for?
A. "od" stands for "octal dump," reflecting its original purpose of displaying file contents in octal format.

#### Q2. How do I view a file in hexadecimal format?
A. Use `od -t x1 filename` to display the file in hexadecimal format, with each byte shown individually.

#### Q3. How can I display both hex and ASCII representations together?
A. Use `od -t x1 -t c filename` or the shorthand `od -t xc filename` to show both formats.

#### Q4. How do I skip the address column in the output?
A. Use `od -A n` to suppress the address column in the output.

#### Q5. How can I limit the output to a specific number of bytes?
A. Use `od -N bytes filename` to limit output to the specified number of bytes.

## References

https://www.gnu.org/software/coreutils/manual/html_node/od-invocation.html

## Revisions

- 2025/04/30 First revision