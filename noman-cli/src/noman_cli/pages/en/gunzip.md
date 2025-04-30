# gunzip command

Decompress files compressed with gzip.

## Overview

`gunzip` is a utility that expands files compressed with the gzip compression algorithm. It essentially reverses what the `gzip` command does, restoring compressed files to their original state. When you run `gunzip` on a file with a `.gz` extension, it decompresses the file and removes the extension.

## Options

### **-c, --stdout**

Output decompressed content to standard output instead of creating a new file.

```console
$ gunzip -c archive.gz
This is the content of the decompressed file.
```

### **-f, --force**

Force decompression even when the output file already exists or when the compressed file has multiple links.

```console
$ gunzip -f already_exists.gz
```

### **-k, --keep**

Keep (don't delete) the input files during decompression.

```console
$ gunzip -k important_archive.gz
$ ls
important_archive  important_archive.gz
```

### **-l, --list**

List information about the compressed file without decompressing it.

```console
$ gunzip -l archive.gz
         compressed        uncompressed  ratio uncompressed_name
                547                 1024  46.5% archive
```

### **-r, --recursive**

Recursively decompress files in directories.

```console
$ gunzip -r compressed_folder/
```

## Usage Examples

### Basic Decompression

```console
$ gunzip archive.gz
$ ls
archive
```

### Decompressing Multiple Files

```console
$ gunzip file1.gz file2.gz file3.gz
$ ls
file1 file2 file3
```

### Viewing Compressed Content Without Decompressing

```console
$ gunzip -c logfile.gz | head -10
[First 10 lines of the decompressed content]
```

### Decompressing to a Different Name

```console
$ gunzip < archive.gz > new_name
$ ls
archive.gz new_name
```

## Tips

### Use zcat Instead of gunzip -c

The `zcat` command is equivalent to `gunzip -c` and may be more intuitive when you want to view compressed content without decompressing the file.

### Preserve Original Compressed Files

When you need to keep the compressed version while accessing the contents, use the `-k` option or redirect the output with `-c`.

### Handle Multiple Compression Formats

For files compressed multiple times with different algorithms (like `.tar.gz`), you'll need to use the appropriate tools in sequence (e.g., `gunzip` followed by `tar xf`).

### Check Available Disk Space

Decompressed files can be significantly larger than their compressed versions. Check that you have enough disk space before decompressing large files.

## Frequently Asked Questions

#### Q1. What's the difference between gunzip and gzip -d?
A. They are functionally equivalent. `gzip -d` and `gunzip` both decompress gzip files.

#### Q2. Can gunzip handle .zip files?
A. No, `gunzip` only works with files compressed using the gzip algorithm (typically .gz files). For .zip files, use the `unzip` command.

#### Q3. How do I decompress a file without losing the original compressed version?
A. Use `gunzip -k filename.gz` or `gunzip -c filename.gz > newfilename`.

#### Q4. How can I see what's in a .gz file without decompressing it?
A. Use `gunzip -l filename.gz` to see metadata or `zcat filename.gz | less` to view the contents.

## References

https://www.gnu.org/software/gzip/manual/gzip.html

## Revisions

- 2025/04/30 First revision