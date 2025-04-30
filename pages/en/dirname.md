# dirname command

Extract the directory portion from a pathname.

## Overview

The `dirname` command removes the last component from a pathname, leaving only the directory path. It's useful in scripts when you need to determine the parent directory of a file or path.

## Options

### **--zero, -z**

Output is terminated with a null character (NUL) instead of a newline.

```console
$ dirname -z /usr/bin/file
/usr/bin$
```

### **--help**

Display help information and exit.

```console
$ dirname --help
Usage: dirname [OPTION] NAME...
Output each NAME with its last non-slash component and trailing slashes
removed; if NAME contains no /'s, output '.' (meaning the current directory).

  -z, --zero     end each output line with NUL, not newline
      --help     display this help and exit
      --version  output version information and exit

Examples:
  dirname /usr/bin/          -> "/usr"
  dirname dir1/str dir2/str  -> "dir1" followed by "dir2"
  dirname stdio.h            -> "."
```

### **--version**

Display version information and exit.

```console
$ dirname --version
dirname (GNU coreutils) 9.0
Copyright (C) 2021 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>.
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by David MacKenzie.
```

## Usage Examples

### Basic Usage

```console
$ dirname /usr/bin/bash
/usr/bin
```

### Multiple Arguments

```console
$ dirname /usr/bin/bash /etc/passwd /home/user/file.txt
/usr/bin
/etc
/home/user
```

### Current Directory

```console
$ dirname file.txt
.
```

### Using in Shell Scripts

```console
$ script_dir=$(dirname "$0")
$ echo "This script is located in: $script_dir"
This script is located in: .
```

## Tips

### Use with Absolute Paths

Always use absolute paths with `dirname` when possible to avoid confusion, especially in scripts that might run from different working directories.

### Combine with `basename`

`dirname` pairs well with the `basename` command. While `dirname` extracts the directory portion, `basename` extracts the filename portion.

### Path Normalization

`dirname` doesn't normalize paths. For example, `dirname a/b/..` returns `a/b` rather than `a`.

## Frequently Asked Questions

#### Q1. What's the difference between `dirname` and `pwd`?
A. `dirname` extracts the directory portion from a given path, while `pwd` prints the current working directory.

#### Q2. How do I get the directory of a script that's running?
A. Use `script_dir=$(dirname "$0")` where `$0` is the path to the script being executed.

#### Q3. Does `dirname` follow symbolic links?
A. No, `dirname` simply manipulates the string path and doesn't interact with the filesystem.

#### Q4. What does `dirname` return for a path without directories?
A. It returns `.` (the current directory) for paths without any directory components.

## References

https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html

## Revisions

- 2025/04/30 First revision