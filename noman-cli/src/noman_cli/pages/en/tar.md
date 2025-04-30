# tar command

Archive files and directories into a single file, with optional compression.

## Overview

The `tar` command creates, extracts, and manipulates archive files. It can combine multiple files and directories into a single file (tarball) while preserving file permissions, ownership, and directory structures. It also supports various compression methods like gzip, bzip2, and xz to reduce archive size.

## Options

### **-c (create)**

Create a new archive

```console
$ tar -cf archive.tar file1 file2 directory/
```

### **-x (extract)**

Extract files from an archive

```console
$ tar -xf archive.tar
```

### **-t (list)**

List the contents of an archive without extracting

```console
$ tar -tf archive.tar
file1
file2
directory/
directory/file3
```

### **-v (verbose)**

Display detailed progress information

```console
$ tar -cvf archive.tar file1 file2
file1
file2
```

### **-f (file)**

Specify the archive filename (must be used with other operations)

```console
$ tar -cf archive.tar file1 file2
```

### **-z (gzip)**

Compress the archive using gzip

```console
$ tar -czf archive.tar.gz directory/
```

### **-j (bzip2)**

Compress the archive using bzip2 (better compression but slower)

```console
$ tar -cjf archive.tar.bz2 directory/
```

### **-J (xz)**

Compress the archive using xz (best compression but slowest)

```console
$ tar -cJf archive.tar.xz directory/
```

## Usage Examples

### Creating a compressed archive of a directory

```console
$ tar -czf backup.tar.gz ~/Documents
```

### Extracting a compressed archive

```console
$ tar -xzf backup.tar.gz
```

### Extracting specific files from an archive

```console
$ tar -xf archive.tar file1 directory/file3
```

### Viewing the contents of a compressed archive

```console
$ tar -tzf backup.tar.gz
Documents/
Documents/report.pdf
Documents/notes.txt
Documents/images/
Documents/images/photo1.jpg
```

## Tips

### Preserve File Permissions

The `-p` option preserves file permissions, ownership, and timestamps when extracting. This is useful for system backups:
```console
$ tar -xpf backup.tar
```

### Extract to a Different Directory

Use the `-C` option to extract files to a specific directory:
```console
$ tar -xf archive.tar -C /path/to/extract
```

### Exclude Files or Directories

Use `--exclude` to skip specific files or patterns:
```console
$ tar -czf backup.tar.gz ~/Documents --exclude="*.log" --exclude="tmp"
```

### Add Files to an Existing Archive

Use the `-r` option to append files to an existing archive (doesn't work with compressed archives):
```console
$ tar -rf archive.tar newfile.txt
```

## Frequently Asked Questions

#### Q1. How do I know which compression option to use?
A. Use `-z` (gzip) for a good balance of speed and compression, `-j` (bzip2) for better compression at the cost of speed, or `-J` (xz) for maximum compression when speed isn't critical.

#### Q2. How can I see what's in a tar archive without extracting it?
A. Use `tar -tf archive.tar` to list contents, or add the `-v` flag (`tar -tvf archive.tar`) for more detailed information.

#### Q3. How do I extract a single file from a tar archive?
A. Use `tar -xf archive.tar path/to/file` specifying the exact path of the file as it appears in the archive.

#### Q4. Why doesn't tar show a progress bar?
A. By default, tar doesn't show progress. Use the `--progress` option or pipe through `pv` if installed: `pv archive.tar | tar -xf -`

## References

https://www.gnu.org/software/tar/manual/

## Revisions

- 2025/04/30 First revision