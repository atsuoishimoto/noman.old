# cp command

Copy files and directories from source to destination.

## Overview

The `cp` command copies files and directories from a source to a destination. It can copy single files, multiple files, or entire directory structures. By default, `cp` will not overwrite existing files unless specified with options, and it preserves the original files while creating duplicates at the target location.

## Options

### **-r, -R, --recursive**

Copy directories recursively, including all subdirectories and their contents.

```console
$ cp -r Documents/ Backup/
```

### **-i, --interactive**

Prompt before overwriting existing files, helping prevent accidental data loss.

```console
$ cp -i report.txt Documents/
cp: overwrite 'Documents/report.txt'? y
```

### **-v, --verbose**

Display the name of each file as it's being copied, providing visual confirmation of the operation.

```console
$ cp -v *.txt Documents/
'notes.txt' -> 'Documents/notes.txt'
'report.txt' -> 'Documents/report.txt'
```

### **-p, --preserve**

Preserve file attributes such as mode, ownership, and timestamps when copying.

```console
$ cp -p important.txt Documents/
```

### **-u, --update**

Copy only when the source file is newer than the destination file or when the destination file doesn't exist.

```console
$ cp -u *.txt Documents/
```

## Usage Examples

### Copying a single file

```console
$ cp source.txt destination.txt
```

### Copying multiple files to a directory

```console
$ cp file1.txt file2.txt file3.txt target_directory/
```

### Copying directories with all contents

```console
$ cp -r source_directory/ destination_directory/
```

### Copying with multiple options

```console
$ cp -rvi Projects/ Backup/
'Projects/index.html' -> 'Backup/Projects/index.html'
'Projects/styles.css' -> 'Backup/Projects/styles.css'
'Projects/images/logo.png' -> 'Backup/Projects/images/logo.png'
```

## Tips

### Trailing Slashes Matter

When copying directories, be aware of trailing slashes. `cp -r dir1 dir2` copies dir1 into dir2, while `cp -r dir1/ dir2/` copies the contents of dir1 into dir2.

### Backup Before Overwriting

Use `cp -b` to create backups of files before overwriting them. This creates a backup with a tilde (~) appended to the filename.

### Force Overwrite

Use `cp -f` to force overwriting destination files without prompting, even if they're write-protected. Use with caution as it can lead to data loss.

### Symbolic Links

By default, `cp` follows symbolic links. Use `cp -P` to preserve symbolic links as links rather than copying the files they point to.

## Frequently Asked Questions

#### Q1. How do I copy a file without overwriting an existing file?
A. Use `cp -n source.txt destination.txt`. The `-n` option prevents overwriting existing files.

#### Q2. How do I copy hidden files?
A. Hidden files (starting with a dot) are copied normally with `cp`. To copy all files including hidden ones, use `cp -r .*` or explicitly name the hidden files.

#### Q3. How do I copy files while preserving all attributes?
A. Use `cp -a source destination`. The `-a` option is equivalent to `-dR --preserve=all`, preserving all file attributes and copying recursively.

#### Q4. How do I copy only specific file types?
A. Use wildcards: `cp *.jpg destination/` copies only JPEG files to the destination directory.

## References

https://www.gnu.org/software/coreutils/manual/html_node/cp-invocation.html

## Revisions

- 2025/04/30 First revision