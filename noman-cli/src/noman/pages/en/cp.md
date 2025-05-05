# cp command

Copy files and directories from source to destination.

## Overview

The `cp` command copies files and directories. It can copy a single file to another file, multiple files to a directory, or entire directories with their contents. By default, `cp` will not overwrite existing files unless the `-f` option is used, and it won't copy directories recursively unless the `-R` or `-r` option is specified.

## Options

### **-a, --archive**

Archive mode that preserves all file attributes and recursively copies directories. Equivalent to `-dR --preserve=all`.

```console
$ cp -a documents/ backup/
```

### **-r, -R, --recursive**

Copy directories recursively, including all subdirectories and their contents.

```console
$ cp -r projects/ backup/
```

### **-i, --interactive**

Prompt before overwriting existing files, allowing you to decide for each file.

```console
$ cp -i report.txt backup/
cp: overwrite 'backup/report.txt'? y
```

### **-f, --force**

Force the copy by removing the destination file if it cannot be opened for writing.

```console
$ cp -f important.txt backup/
```

### **-v, --verbose**

Display the name of each file before copying it, showing what's being processed.

```console
$ cp -v *.txt documents/
'report.txt' -> 'documents/report.txt'
'notes.txt' -> 'documents/notes.txt'
```

### **-p, --preserve**

Preserve file attributes like mode, ownership, and timestamps.

```console
$ cp -p config.ini backup/
```

### **-u, --update**

Copy only when the source file is newer than the destination file or when the destination file doesn't exist.

```console
$ cp -u *.txt backup/
```

## Usage Examples

### Copying a Single File

```console
$ cp report.txt backup/report.txt
```

### Copying Multiple Files to a Directory

```console
$ cp file1.txt file2.txt file3.txt destination/
```

### Recursive Copy with Verbose Output

```console
$ cp -rv projects/ backup/
'projects/main.c' -> 'backup/projects/main.c'
'projects/lib/utils.c' -> 'backup/projects/lib/utils.c'
'projects/lib/utils.h' -> 'backup/projects/lib/utils.h'
```

### Copying with Preservation of Attributes

```console
$ cp -ap documents/ archive/
```

## Tips

### Use Trailing Slashes Carefully

When copying directories, a trailing slash on the source means "copy the contents of this directory" rather than the directory itself:
- `cp -r dir1 dir2` creates dir2/dir1 if dir2 exists
- `cp -r dir1/ dir2` copies contents of dir1 into dir2

### Backup Before Overwriting

Use the `--backup` option to create backups of files before overwriting them:

```console
$ cp --backup=numbered important.txt destination/
```

### Symbolic Links Handling

By default, `cp` follows symbolic links. Use `-P` or `--no-dereference` to copy the links themselves instead of what they point to.

## Frequently Asked Questions

#### Q1. How do I copy a file without overwriting an existing file?
A. Use `cp -n source destination` which prevents overwriting existing files.

#### Q2. How do I copy hidden files?
A. Hidden files (starting with a dot) are copied normally. To copy all files including hidden ones, use patterns like `cp -r .* * destination/` or explicitly name the hidden files.

#### Q3. How do I copy only the directory structure without the files?
A. There's no direct option in `cp`. You might need to use `find` with `mkdir` or `rsync --include='*/' --exclude='*'`.

#### Q4. How do I copy files while preserving permissions?
A. Use `cp -p` to preserve mode, ownership, and timestamps, or `cp -a` to preserve all attributes.

## References

https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html

## Revisions

- 2025/05/04 First revision