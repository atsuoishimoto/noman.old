# file command

Determine file type by examining file contents.

## Overview

The `file` command identifies the type of a file by examining its contents, rather than relying on filename extensions. It can recognize text files, executables, images, archives, and many other formats by analyzing the file's data patterns, headers, and structure.

## Options

### **-b, --brief**

Display the result without the filename prefix

```console
$ file -b document.txt
ASCII text
```

### **-i, --mime**

Display the MIME type of the file

```console
$ file -i document.txt
document.txt: text/plain; charset=us-ascii
```

### **-z, --uncompress**

Try to look inside compressed files

```console
$ file -z archive.tar.gz
archive.tar.gz: gzip compressed data, from Unix, original size modulo 2^32 10240
```

### **-L, --dereference**

Follow symbolic links

```console
$ file -L symlink
symlink: ASCII text
```

## Usage Examples

### Basic file identification

```console
$ file document.txt image.png script.sh
document.txt: ASCII text
image.png: PNG image data, 800 x 600, 8-bit/color RGB, non-interlaced
script.sh: Bourne-Again shell script, ASCII text executable
```

### Checking multiple files at once

```console
$ file *
document.txt:  ASCII text
image.jpg:     JPEG image data, JFIF standard 1.01
program:       ELF 64-bit LSB executable, x86-64
archive.zip:   Zip archive data, at least v2.0 to extract
```

### Examining a binary file

```console
$ file /bin/ls
/bin/ls: ELF 64-bit LSB executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 2.6.32, BuildID[sha1]=123456789abcdef, stripped
```

## Tips

### Use with Directories

When used on a directory, `file` simply identifies it as a directory. To examine files within a directory, combine with `find`:

```console
$ find /path/to/dir -type f -exec file {} \;
```

### Examining Special Files

For device files or sockets, `file` may only report their type without detailed information.

### Magic Database

The `file` command uses a "magic" database to identify file types. If you encounter incorrect identifications, your magic database might need updating.

### Pipe Usage

You can pipe content to `file` using the special `-` argument:

```console
$ cat document.txt | file -
/dev/stdin: ASCII text
```

## Frequently Asked Questions

#### Q1. How does `file` determine a file's type?
A. `file` examines the file's content patterns, headers, and structure using a "magic" database of file signatures, rather than relying on filename extensions.

#### Q2. Can `file` identify the encoding of text files?
A. Yes, using `file -i` will often show the character encoding (charset) of text files.

#### Q3. Why does `file` sometimes misidentify my files?
A. `file` relies on pattern matching which isn't perfect. Some file formats are similar or ambiguous, and the magic database might be outdated for newer formats.

#### Q4. Can `file` identify files without extensions?
A. Yes, since `file` examines the content rather than the filename, it works perfectly well on files without extensions.

## References

https://man7.org/linux/man-pages/man1/file.1.html

## Revisions

- 2025/04/30 First revision