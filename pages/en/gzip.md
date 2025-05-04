# gzip command

Compress or expand files using the Lempel-Ziv coding (LZ77).

## Overview

`gzip` reduces the size of files using Lempel-Ziv compression. By default, it replaces the original file with a compressed version having the `.gz` extension, preserving the original file's ownership, permissions, and timestamps. It's commonly used to compress single files or as part of pipeline operations to compress data streams.

## Options

### **-d, --decompress, --uncompress**

Decompress files instead of compressing them.

```console
$ gzip -d file.gz
```

### **-c, --stdout, --to-stdout**

Write output to standard output and keep original files unchanged.

```console
$ gzip -c file.txt > file.txt.gz
```

### **-f, --force**

Force compression or decompression even if the file has multiple links or the corresponding file already exists.

```console
$ gzip -f already_compressed.gz
```

### **-k, --keep**

Keep (don't delete) input files during compression or decompression.

```console
$ gzip -k important_file.txt
```

### **-l, --list**

List the compressed size, uncompressed size, ratio, and filename for each compressed file.

```console
$ gzip -l *.gz
         compressed        uncompressed  ratio uncompressed_name
                 220                 631  65.1% file1.txt
                 143                 341  58.1% file2.txt
```

### **-r, --recursive**

Recursively compress files in directories.

```console
$ gzip -r directory/
```

### **-v, --verbose**

Display the name and percentage reduction for each file compressed or decompressed.

```console
$ gzip -v file.txt
file.txt:       63.4% -- replaced with file.txt.gz
```

### **-[1-9], --fast, --best**

Regulate the speed of compression using the specified digit, where -1 (or --fast) indicates the fastest compression method (less compression) and -9 (or --best) indicates the slowest (best compression). The default compression level is -6.

```console
$ gzip -9 large_file.txt
```

## Usage Examples

### Basic Compression

```console
$ gzip document.txt
$ ls
document.txt.gz
```

### Compressing Multiple Files

```console
$ gzip file1.txt file2.txt file3.txt
$ ls
file1.txt.gz file2.txt.gz file3.txt.gz
```

### Compressing While Keeping Originals

```console
$ gzip -k important_data.txt
$ ls
important_data.txt important_data.txt.gz
```

### Viewing Compressed Files Without Decompressing

```console
$ gzip -c file.txt > file.txt.gz
$ zcat file.txt.gz
[contents of file.txt displayed]
```

### Compressing Standard Input

```console
$ cat file.txt | gzip > file.txt.gz
```

## Tips

### Use With tar for Directory Compression

While `gzip` compresses single files, combine it with `tar` to compress entire directories:

```console
$ tar -czf archive.tar.gz directory/
```

### Check Compression Ratio

Use the `-l` option to check how well files have been compressed before deciding whether to keep them:

```console
$ gzip -l *.gz
```

### Pipe Through gzip in Scripts

For temporary compression in scripts or data processing, use pipes:

```console
$ cat large_file | gzip | ssh remote_server "gunzip > large_file"
```

### Optimal Compression Level

For most files, the default compression level (-6) offers a good balance between speed and compression ratio. Use -9 only when file size is critical and processing time isn't a concern.

## Frequently Asked Questions

#### Q1. How do I decompress a .gz file?
A. Use `gzip -d filename.gz` or the equivalent command `gunzip filename.gz`.

#### Q2. Can gzip compress directories?
A. No, `gzip` only compresses individual files. To compress directories, first use `tar` to create an archive, then compress it with `gzip` (or use `tar` with the `-z` option).

#### Q3. How do I view the contents of a .gz file without decompressing it?
A. Use `zcat`, `zless`, or `zmore` commands, which are specifically designed for viewing compressed files.

#### Q4. Does gzip delete the original file after compression?
A. Yes, by default `gzip` replaces the original file with the compressed version. Use the `-k` option to keep the original.

#### Q5. How can I compare compression levels?
A. Use `gzip -[1-9] -c file > file.gz` with different numbers and then check the resulting file sizes with `ls -l`.

## References

https://www.gnu.org/software/gzip/manual/gzip.html

## Revisions

- 2025/05/04 First revision