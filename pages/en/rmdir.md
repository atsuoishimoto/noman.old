# rmdir command

Remove empty directories from the filesystem.

## Overview

The `rmdir` command removes empty directories from the filesystem. It's specifically designed to delete directory entries that don't contain any files or subdirectories. If a directory contains any content, `rmdir` will refuse to delete it.

## Options

### **-p, --parents**

Remove directory and its ancestors. For example, `rmdir -p a/b/c` is similar to `rmdir a/b/c a/b a`.

```console
$ mkdir -p test/nested/dir
$ rmdir -p test/nested/dir
$ ls test
ls: test: No such file or directory
```

### **-v, --verbose**

Output a diagnostic message for every directory processed.

```console
$ mkdir -p example/folder
$ rmdir -v example/folder
rmdir: removing directory, 'example/folder'
```

### **--ignore-fail-on-non-empty**

Ignore failures that occur when a directory is not empty.

```console
$ mkdir test
$ touch test/file.txt
$ rmdir --ignore-fail-on-non-empty test
$ ls
test
```

## Usage Examples

### Removing a single empty directory

```console
$ mkdir empty_dir
$ rmdir empty_dir
$ ls
[empty_dir no longer appears in the listing]
```

### Removing multiple empty directories at once

```console
$ mkdir dir1 dir2 dir3
$ rmdir dir1 dir2 dir3
$ ls
[none of the directories appear in the listing]
```

### Removing nested empty directories with parents option

```console
$ mkdir -p parent/child/grandchild
$ rmdir -p parent/child/grandchild
$ ls
[parent directory and all subdirectories are removed]
```

## Tips:

### Use `rm -r` for Non-Empty Directories

If you need to remove directories that contain files, use `rm -r` instead of `rmdir`. Be careful with this command as it will recursively delete all contents.

### Combine with `mkdir -p`

`mkdir -p` creates parent directories as needed, and `rmdir -p` removes them in the reverse order. These commands complement each other well for temporary directory structures.

### Check Before Removing

Use `ls` to verify directory contents before using `rmdir` to avoid error messages about non-empty directories.

## Frequently Asked Questions

#### Q1. Why does `rmdir` fail with "Directory not empty"?
A. `rmdir` only removes empty directories. If the directory contains any files or subdirectories, use `rm -r` instead.

#### Q2. How is `rmdir` different from `rm -d`?
A. They're functionally equivalent for empty directories. Both commands remove empty directories but refuse to remove non-empty ones.

#### Q3. Can I use wildcards with `rmdir`?
A. Yes, you can use wildcards like `rmdir dir*` to remove multiple directories matching a pattern, but each must be empty.

#### Q4. How do I remove a directory and all its parent directories if they become empty?
A. Use `rmdir -p path/to/directory` to remove the directory and its parent directories if they become empty.

## References

https://www.gnu.org/software/coreutils/manual/html_node/rmdir-invocation.html

## Revisions

- 2025/04/30 First revision