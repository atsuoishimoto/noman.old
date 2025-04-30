# gzip command

Compress or expand files using the gzip algorithm.

## Overview

`gzip` is a compression utility that reduces the size of files using Lempel-Ziv coding (LZ77). It replaces the original file with a compressed version having a `.gz` extension, preserving the original file's ownership, permissions, and timestamp. It's commonly used to save disk space and reduce file transfer times.

## Options

### **-d, --decompress**

Decompress files (same as using `gunzip`)

```console
$ gzip -d file.gz
```

### **-c, --stdout**

Write output to standard output and keep original files

```console
$ gzip -c file.txt > file.txt.gz
```

### **-k, --keep**

Keep (don't delete) input files during compression or decompression

```console
$ gzip -k file.txt
```

### **-r, --recursive**

Recursively compress files in directories

```console
$ gzip -r directory/
```

### **-[1-9], --fast, --best**

Set compression level (1=fastest/least, 9=slowest/best)

```console
$ gzip -9 file.txt
```

## Usage Examples

### Basic Compression

```console
$ ls -l
-rw-r--r--  1 user  staff  10240 Apr 30 10:00 largefile.txt

$ gzip largefile.txt

$ ls -l
-rw-r--r--  1 user  staff  2048 Apr 30 10:00 largefile.txt.gz
```

### Compressing Multiple Files

```console
$ gzip file1.txt file2.txt file3.txt

$ ls
file1.txt.gz  file2.txt.gz  file3.txt.gz
```

### Viewing Compressed Files Without Decompressing

```console
$ gzip -c file.txt > file.txt.gz
$ zcat file.txt.gz
[contents of file displayed without decompressing]
```

### Comparing Compression Levels

```console
$ cp largefile.txt test1.txt
$ cp largefile.txt test9.txt

$ time gzip -1 test1.txt
real    0m0.032s

$ time gzip -9 test9.txt
real    0m0.187s

$ ls -l test*.gz
-rw-r--r--  1 user  staff  2300 Apr 30 10:00 test1.txt.gz
-rw-r--r--  1 user  staff  2048 Apr 30 10:00 test9.txt.gz
```

## Tips

### Check Compression Ratio

Use `gzip -l` on compressed files to see statistics about the compression ratio:

```console
$ gzip -l file.gz
         compressed        uncompressed  ratio uncompressed_name
                2048              10240  80.0% file
```

### Combine with tar

For compressing multiple files or directories while preserving structure, combine with `tar`:

```console
$ tar -czf archive.tar.gz directory/
```

### Use zcat, zless for Viewing

Instead of decompressing files to view them, use `zcat`, `zless`, or `zmore` to view compressed content directly.

### Preserve Original Files

Always use `-k` option when you want to keep the original files, especially for important data.

## Frequently Asked Questions

#### Q1. How do I decompress a .gz file?
A. Use `gzip -d filename.gz` or `gunzip filename.gz`.

#### Q2. Can gzip compress directories?
A. Not directly. Use `gzip -r` to compress all files in a directory individually, or use `tar` with `gzip` (`tar -czf`) to compress entire directories.

#### Q3. What's the difference between gzip, bzip2, and xz?
A. They use different compression algorithms. Generally, gzip is fastest but has lower compression ratios, bzip2 is in the middle, and xz offers the best compression but is slowest.

#### Q4. How do I compress without losing the original file?
A. Use `gzip -k filename` to keep the original file.

#### Q5. How can I see what's in a .gz file without decompressing it?
A. Use `zcat`, `zless`, or `zmore` to view the contents without decompression.

## References

https://www.gnu.org/software/gzip/manual/gzip.html

## Revisions

- 2025/04/30 First revision