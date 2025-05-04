# rmdir command

Remove empty directories from the filesystem.

## Overview

The `rmdir` command removes empty directories from the filesystem. It will only delete directories that contain no files or subdirectories. For removing directories with content, you would need to use the `rm` command with specific options.

## Options

### **-p, --parents**

Remove directory and its ancestors. For example, `rmdir -p a/b/c` is similar to `rmdir a/b/c a/b a`.

```console
$ mkdir -p test/nested/dir
$ rmdir -p test/nested/dir
$ ls test
ls: cannot access 'test': No such file or directory
```

### **-v, --verbose**

Output a diagnostic message for every directory processed.

```console
$ mkdir empty1 empty2
$ rmdir -v empty1 empty2
rmdir: removing directory, 'empty1'
rmdir: removing directory, 'empty2'
```

### **--ignore-fail-on-non-empty**

Ignore failures that occur solely because a directory is non-empty.

```console
$ mkdir nonempty
$ touch nonempty/file
$ rmdir --ignore-fail-on-non-empty nonempty
$ ls
nonempty
```

## Usage Examples

### Removing a single empty directory

```console
$ mkdir emptydir
$ rmdir emptydir
$ ls
[emptydir no longer appears in the listing]
```

### Removing multiple empty directories at once

```console
$ mkdir dir1 dir2 dir3
$ rmdir dir1 dir2 dir3
$ ls
[none of the directories appear in the listing]
```

### Attempting to remove a non-empty directory

```console
$ mkdir nonempty
$ touch nonempty/file
$ rmdir nonempty
rmdir: failed to remove 'nonempty': Directory not empty
```

## Tips:

### Check if a Directory is Empty First

Before using `rmdir`, you can check if a directory is empty with `ls -A directory_name`. If nothing is listed, the directory is empty.

### Use with find Command

Combine with `find` to remove multiple empty directories: `find /path -type d -empty -exec rmdir {} \;`

### Removing Directory Trees

For removing entire directory trees (including non-empty directories), use `rm -r` instead of `rmdir`. Be careful as this will delete all contents without prompting.

## Frequently Asked Questions

#### Q1. Why does rmdir fail with "Directory not empty"?
A. `rmdir` only removes empty directories. If the directory contains any files or subdirectories, use `rm -r directory_name` instead.

#### Q2. How is rmdir different from rm -d?
A. They are functionally equivalent for empty directories. Both commands can only remove empty directories.

#### Q3. Can rmdir remove multiple directories at once?
A. Yes, you can specify multiple directories: `rmdir dir1 dir2 dir3`.

#### Q4. How do I remove nested empty directories?
A. Use the `-p` option: `rmdir -p parent/child/grandchild` will remove all three directories if they're empty.

## References

https://www.gnu.org/software/coreutils/manual/html_node/rmdir-invocation.html

## Revisions

- 2025/05/04 First revision