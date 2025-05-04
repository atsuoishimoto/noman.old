# gunzip command

Decompress files compressed with gzip.

## Overview

`gunzip` is a utility that decompresses files previously compressed with the `gzip` program. It restores the original file, removing the compressed version by default. It works with files having extensions like `.gz`, `.z`, `.taz`, `.tgz`, or `.tz`.

## Options

### **-c, --stdout, --to-stdout**

Write output to standard output and keep original files unchanged.

```console
$ gunzip -c archive.gz > extracted_file
```

### **-f, --force**

Force decompression even if the file has multiple links or the corresponding file already exists.

```console
$ gunzip -f already_exists.gz
```

### **-k, --keep**

Keep (don't delete) input files during decompression.

```console
$ gunzip -k archive.gz
$ ls
archive  archive.gz
```

### **-l, --list**

List the contents of the compressed file without decompressing.

```console
$ gunzip -l archive.gz
         compressed        uncompressed  ratio uncompressed_name
                547                 1213  54.9% archive
```

### **-q, --quiet**

Suppress all warnings.

```console
$ gunzip -q archive.gz
```

### **-r, --recursive**

Recursively decompress files in directories.

```console
$ gunzip -r directory_with_gz_files/
```

### **-t, --test**

Test the compressed file integrity without decompressing.

```console
$ gunzip -t archive.gz
```

### **-v, --verbose**

Display the name and percentage reduction for each file decompressed.

```console
$ gunzip -v archive.gz
archive.gz:	 54.9% -- replaced with archive
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

### Decompressing While Preserving Original

```console
$ gunzip -k important_backup.gz
$ ls
important_backup important_backup.gz
```

### Testing Archive Integrity

```console
$ gunzip -tv archive.gz
archive.gz: OK
```

## Tips:

### Use with tar Files

For `.tar.gz` or `.tgz` files, you can use `gunzip` followed by `tar`:

```console
$ gunzip archive.tar.gz
$ tar xf archive.tar
```

Or more efficiently, use `tar` with the `z` option directly:

```console
$ tar xzf archive.tar.gz
```

### Pipe Directly to Other Commands

Use `-c` to decompress and pipe to another command without creating intermediate files:

```console
$ gunzip -c logs.gz | grep "error"
```

### Handling Multiple Compression Formats

If you're unsure about the compression format, consider using `zcat` which works with multiple formats:

```console
$ zcat file.gz > uncompressed_file
```

## Frequently Asked Questions

#### Q1. What's the difference between `gunzip` and `gzip -d`?
A. They are functionally equivalent. `gunzip` is essentially a symbolic link to `gzip -d`.

#### Q2. How do I decompress a file without removing the original compressed file?
A. Use the `-k` or `--keep` option: `gunzip -k file.gz`

#### Q3. Can `gunzip` handle multiple compression formats?
A. No, `gunzip` is specifically for gzip-compressed files. For other formats, use tools like `bunzip2` (for bzip2) or `unxz` (for xz).

#### Q4. How can I see what's in a gzipped file without decompressing it?
A. Use `gunzip -l file.gz` to list information about the compressed file.

#### Q5. How do I decompress a file to a different name?
A. Use the `-c` option and redirect output: `gunzip -c file.gz > newname`

## References

https://www.gnu.org/software/gzip/manual/gzip.html

## Revisions

- 2025/05/04 First revision