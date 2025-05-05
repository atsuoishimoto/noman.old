# unlink command

Remove a single file from the filesystem.

## Overview

The `unlink` command is used to delete a single file by removing its link from the filesystem. It's a simpler alternative to `rm` when you only need to delete one file. Unlike `rm`, `unlink` cannot remove multiple files or directories and has fewer options.

## Options

### **-h, --help**

Display help information and exit.

```console
$ unlink --help
Usage: unlink FILE
  or:  unlink OPTION
Call the unlink function to remove the specified FILE.

      --help     display this help and exit
      --version  output version information and exit
```

### **--version**

Output version information and exit.

```console
$ unlink --version
unlink (GNU coreutils) 8.32
Copyright (C) 2020 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by Michael Stone.
```

## Usage Examples

### Removing a file

```console
$ touch temp_file.txt
$ ls
temp_file.txt
$ unlink temp_file.txt
$ ls
$
```

### Attempting to remove a directory (will fail)

```console
$ mkdir test_dir
$ unlink test_dir
unlink: cannot unlink 'test_dir': Is a directory
```

## Tips

### Use `rm` for Multiple Files

If you need to delete multiple files, use `rm` instead of `unlink`. The `unlink` command can only remove one file at a time.

### Symbolic Links

When using `unlink` on a symbolic link, it removes the link itself, not the file it points to.

### No Recovery

Files deleted with `unlink` are not sent to a trash or recycle bin. They are permanently deleted and can only be recovered from backups.

### No Confirmation

Unlike `rm`, which can prompt for confirmation with the `-i` option, `unlink` provides no confirmation prompt before deleting a file.

## Frequently Asked Questions

#### Q1. What's the difference between `unlink` and `rm`?
A. `unlink` can only remove a single file and has minimal options, while `rm` can remove multiple files, directories (with `-r`), and has many additional options.

#### Q2. Can `unlink` remove directories?
A. No, `unlink` cannot remove directories. Use `rmdir` for empty directories or `rm -r` for directories with contents.

#### Q3. Does `unlink` move files to trash?
A. No, `unlink` permanently deletes files. They cannot be recovered from a trash or recycle bin.

#### Q4. What happens if I try to unlink a file that doesn't exist?
A. `unlink` will return an error message stating that the file doesn't exist.

## References

https://www.gnu.org/software/coreutils/manual/html_node/unlink-invocation.html

## Revisions

- 2025/05/04 First revision