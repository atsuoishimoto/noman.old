# tar command

Manipulate tape archives by creating, extracting, or listing the contents of archive files.

## Overview

The `tar` command creates, maintains, and extracts files from archive files known as tarballs. It's commonly used for bundling files together for backup, distribution, or compression. The name "tar" stands for "tape archive," reflecting its original purpose for tape backups, though it's now primarily used with regular files.

## Options

### **-c, --create**

Create a new archive

```console
$ tar -c -f archive.tar file1.txt file2.txt
```

### **-x, --extract**

Extract files from an archive

```console
$ tar -x -f archive.tar
```

### **-t, --list**

List the contents of an archive

```console
$ tar -t -f archive.tar
file1.txt
file2.txt
```

### **-f, --file=ARCHIVE**

Specify the archive file name (required for most operations)

```console
$ tar -cf archive.tar directory/
```

### **-v, --verbose**

Verbosely list files processed

```console
$ tar -cvf archive.tar directory/
directory/
directory/file1.txt
directory/file2.txt
directory/subdirectory/
directory/subdirectory/file3.txt
```

### **-z, --gzip**

Filter the archive through gzip (create/extract .tar.gz files)

```console
$ tar -czf archive.tar.gz directory/
```

### **-j, --bzip2**

Filter the archive through bzip2 (create/extract .tar.bz2 files)

```console
$ tar -cjf archive.tar.bz2 directory/
```

### **-C, --directory=DIR**

Change to directory DIR before performing operations

```console
$ tar -xf archive.tar -C /tmp/extract/
```

## Usage Examples

### Creating a compressed archive of a directory

```console
$ tar -czf backup.tar.gz /home/user/documents
```

### Extracting a compressed archive

```console
$ tar -xzf backup.tar.gz
```

### Viewing the contents of a compressed archive without extracting

```console
$ tar -tzf backup.tar.gz
home/user/documents/
home/user/documents/file1.txt
home/user/documents/file2.txt
home/user/documents/projects/
home/user/documents/projects/notes.md
```

### Extracting specific files from an archive

```console
$ tar -xf archive.tar file1.txt file2.txt
```

### Adding files to an existing archive

```console
$ tar -rf archive.tar newfile.txt
```

## Tips

### Preserve File Permissions

By default, `tar` preserves file permissions, ownership, and timestamps. This is useful for backups but may cause issues when extracting as a non-root user. Use `--no-same-owner` when extracting if you want to avoid permission problems.

### Extract to a Different Directory

Always use the `-C` option when you want to extract to a specific directory. This prevents files from being extracted to your current directory.

### Use Progress Indicators

For large archives, add `--checkpoint=1000 --checkpoint-action=dot` to show progress during creation or extraction.

### Exclude Files or Directories

Use `--exclude=PATTERN` to exclude files or directories matching a pattern:

```console
$ tar -czf backup.tar.gz --exclude="*.log" --exclude="temp/" /home/user/documents
```

## Frequently Asked Questions

#### Q1. What's the difference between .tar, .tar.gz, and .tar.bz2?
A. `.tar` is an uncompressed archive, `.tar.gz` (or `.tgz`) is compressed with gzip (faster, less compression), and `.tar.bz2` is compressed with bzip2 (slower, better compression).

#### Q2. How do I extract a single file from a tar archive?
A. Use `tar -xf archive.tar path/to/specific/file` to extract just that file.

#### Q3. How can I see what's in a tar file without extracting it?
A. Use `tar -tf archive.tar` to list contents without extraction.

#### Q4. How do I create a tar archive that preserves file permissions?
A. `tar` preserves permissions by default. Use `tar -cpf archive.tar directory/` where `-p` explicitly preserves permissions.

#### Q5. How do I handle "Removing leading '/' from member names" warnings?
A. This is normal behavior when archiving absolute paths. `tar` removes leading slashes for security reasons. Use relative paths when possible.

## References

https://www.gnu.org/software/tar/manual/tar.html

## Revisions

- 2025/05/04 First revision