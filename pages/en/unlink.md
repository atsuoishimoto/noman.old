# unlink command

Remove a single file from the filesystem.

## Overview

The `unlink` command removes a single file from the filesystem by deleting its directory entry and potentially freeing disk space. It's a simpler alternative to `rm` when you only need to delete one file at a time.

## Options

`unlink` is a simple command with minimal options, as its primary purpose is to remove a single file.

### **--help**

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

Display version information and exit.

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
unlink: test_dir: is a directory
```

## Tips

### Use `rm` for Multiple Files

`unlink` can only remove one file at a time. For removing multiple files, use the `rm` command instead.

### Cannot Remove Directories

Unlike `rm -r`, `unlink` cannot remove directories. It's designed specifically for single file removal.

### Symbolic Links

When using `unlink` on a symbolic link, only the link itself is removed, not the file it points to.

### No Confirmation Prompt

`unlink` doesn't ask for confirmation before deleting a file, so be careful when using it on important files.

## Frequently Asked Questions

#### Q1. What's the difference between `unlink` and `rm`?
A. `unlink` can only remove a single file and has no options for recursive deletion or handling multiple files, while `rm` is more versatile with options for multiple files, directories, and interactive prompts.

#### Q2. Can I recover a file after using `unlink`?
A. Generally no. Once a file is unlinked, it's removed from the filesystem. Recovery might be possible with specialized tools, but it's not guaranteed.

#### Q3. Does `unlink` work on directories?
A. No, `unlink` cannot remove directories. Use `rmdir` for empty directories or `rm -r` for directories with contents.

#### Q4. Is there any way to make `unlink` ask for confirmation?
A. No, `unlink` doesn't have a built-in confirmation option. If you need confirmation before deletion, use `rm -i` instead.

## References

https://www.gnu.org/software/coreutils/manual/html_node/unlink-invocation.html

## Revisions

- 2025/04/30 First revision