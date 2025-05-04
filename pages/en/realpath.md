# realpath command

Print the resolved absolute file path.

## Overview

The `realpath` command resolves a pathname to its absolute path, following all symbolic links. It's useful for determining the actual location of files, especially when working with symbolic links or relative paths.

## Options

### **-e, --canonicalize-existing**

All components of the path must exist

```console
$ realpath -e /etc/hosts
/etc/hosts

$ realpath -e /nonexistent/file
realpath: /nonexistent/file: No such file or directory
```

### **-m, --canonicalize-missing**

No path components need to exist or be a directory

```console
$ realpath -m /nonexistent/file
/nonexistent/file
```

### **-L, --logical**

Resolve '..' components before symlinks (default behavior)

```console
$ ln -s /usr/bin bin_link
$ realpath -L bin_link/../share
/usr/share
```

### **-P, --physical**

Resolve symlinks as encountered, then resolve '..' components

```console
$ ln -s /usr/bin bin_link
$ realpath -P bin_link/../share
/share
```

### **-q, --quiet**

Suppress error messages

```console
$ realpath -q /nonexistent/file
$ echo $?
1
```

### **-s, --strip, --no-symlinks**

Don't expand symlinks

```console
$ ln -s /usr/bin bin_link
$ realpath -s bin_link
/home/user/bin_link
```

### **-z, --zero**

End each output line with NUL, not newline

```console
$ realpath -z /etc/hosts | hexdump -C
00000000  2f 65 74 63 2f 68 6f 73  74 73 00                 |/etc/hosts.|
0000000b
```

## Usage Examples

### Resolving a relative path

```console
$ cd /usr/local
$ realpath bin/../share
/usr/local/share
```

### Working with symbolic links

```console
$ ln -s /var/log logs
$ realpath logs
/var/log
```

### Using in scripts to get absolute paths

```console
$ cat myscript.sh
#!/bin/bash
SCRIPT_DIR=$(realpath $(dirname "$0"))
echo "Script is located in: $SCRIPT_DIR"
```

## Tips

### Use in Shell Scripts

When writing shell scripts, use `realpath` to get the absolute path of the script directory with `SCRIPT_DIR=$(realpath $(dirname "$0"))`. This ensures your script works correctly regardless of where it's called from.

### Combine with Other Commands

Pair `realpath` with commands like `find` or `xargs` to process files with their absolute paths: `find . -type f | xargs realpath`.

### Handling Errors

Use the `-q` option when you want to suppress error messages, and check the exit status instead. This is useful in scripts where you want to handle errors gracefully.

## Frequently Asked Questions

#### Q1. What's the difference between `realpath` and `readlink -f`?
A. Both commands resolve symbolic links and return absolute paths, but `realpath` offers more options for controlling how paths are resolved. `readlink -f` is more commonly available on older systems.

#### Q2. How do I use `realpath` to check if a file exists?
A. Use `realpath -e` which will return an error if the file doesn't exist.

#### Q3. Can `realpath` handle spaces in filenames?
A. Yes, but when using it in scripts, make sure to quote the arguments: `realpath "$filename"`.

#### Q4. What's the difference between `-L` and `-P` options?
A. `-L` (logical) resolves '..' components before symlinks, while `-P` (physical) resolves symlinks first, then resolves '..' components. The default is `-L`.

## References

https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html

## Revisions

- 2025/05/04 First revision