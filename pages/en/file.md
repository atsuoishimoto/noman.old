# file command

Determine file type by examining file contents.

## Overview

The `file` command examines each file argument to classify its type. It performs a series of tests to determine if the file is text, executable, data, or another format. Unlike many commands that rely on file extensions, `file` looks at the actual content of files to identify their types.

## Options

### **-b, --brief**

Display the result without the filename prefix.

```console
$ file -b document.txt
ASCII text
```

### **-i, --mime**

Display MIME type strings instead of traditional descriptions.

```console
$ file -i document.txt
document.txt: text/plain; charset=us-ascii
```

### **-z, --uncompress**

Try to look inside compressed files.

```console
$ file -z archive.gz
archive.gz: ASCII text (gzip compressed data, was "notes.txt", last modified: Wed Apr 28 15:30:45 2021, from Unix)
```

### **-L, --dereference**

Follow symbolic links.

```console
$ file -L symlink
symlink: ASCII text
```

### **-s, --special-files**

Read block or character special files.

```console
$ file -s /dev/sda1
/dev/sda1: Linux rev 1.0 ext4 filesystem data (extents) (large files)
```

## Usage Examples

### Basic file identification

```console
$ file document.txt image.png script.sh
document.txt: ASCII text
image.png:    PNG image data, 1920 x 1080, 8-bit/color RGB, non-interlaced
script.sh:    Bourne-Again shell script, ASCII text executable
```

### Examining multiple files

```console
$ file *
document.txt:  ASCII text
image.png:     PNG image data, 1920 x 1080, 8-bit/color RGB, non-interlaced
script.sh:     Bourne-Again shell script, ASCII text executable
archive.tar:   POSIX tar archive (GNU)
binary:        ELF 64-bit LSB executable, x86-64
```

### Examining a directory

```console
$ file projects/
projects/: directory
```

## Tips

### Use with Pipes

You can pipe output from other commands to `file` using the special `-` argument to read from stdin:

```console
$ cat unknown_file | file -
/dev/stdin: ASCII text
```

### Recursive File Type Identification

Combine with `find` to identify file types recursively:

```console
$ find . -type f -exec file {} \;
```

### Identifying Executables

The `file` command can help determine if a binary is 32-bit or 64-bit, and what architecture it's compiled for:

```console
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32
```

## Frequently Asked Questions

#### Q1. How does the `file` command determine file types?
A. `file` uses "magic" tests - examining the first few bytes of a file and comparing them against known patterns in a database (usually located at `/usr/share/file/magic`).

#### Q2. Can `file` identify all file types?
A. While `file` can identify many common file types, it may not recognize specialized or proprietary formats. It provides its best guess based on file content.

#### Q3. Why does `file` sometimes report text files as having specific encodings?
A. `file` analyzes character patterns to detect text encodings like UTF-8, ASCII, or other character sets.

#### Q4. How can I get just the MIME type without the filename?
A. Use `file -b -i filename` to get only the MIME type without the filename prefix.

## macOS Considerations

On macOS, the `file` command works similarly to Linux versions but may have slightly different output formats or detection capabilities. The magic database location is typically at `/usr/share/file/magic` or `/etc/magic`.

## References

https://man7.org/linux/man-pages/man1/file.1.html

## Revisions

- 2025/05/04 First revision