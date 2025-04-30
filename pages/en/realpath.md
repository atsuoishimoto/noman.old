# realpath command

Print the resolved absolute file path.

## Overview

The `realpath` command resolves a file path to its absolute, canonical form, following all symbolic links and removing any redundant components like `.` and `..`. It's useful for scripts that need to work with absolute paths or when you need to determine where a symbolic link actually points.

## Options

### **-s, --strip, --no-symlinks**

Don't expand symbolic links; instead show the absolute path to the symlink itself.

```console
$ ln -s /etc/hosts mylink
$ realpath mylink
/etc/hosts
$ realpath -s mylink
/home/user/mylink
```

### **-e, --canonicalize-existing**

All components of the path must exist.

```console
$ realpath -e /etc/hosts
/etc/hosts
$ realpath -e /nonexistent
realpath: /nonexistent: No such file or directory
```

### **-m, --canonicalize-missing**

No path components need to exist or be a directory.

```console
$ realpath -m /nonexistent/file.txt
/nonexistent/file.txt
```

### **-q, --quiet**

Suppress error messages.

```console
$ realpath -q /nonexistent
$ echo $?
1
```

### **-z, --zero**

End each output line with NUL, not newline (useful for parsing in scripts).

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

### Finding where a symbolic link points

```console
$ ln -s /var/log/syslog logfile
$ realpath logfile
/var/log/syslog
```

### Using in shell scripts

```console
$ SCRIPT_DIR=$(realpath $(dirname "$0"))
$ echo "This script is located in: $SCRIPT_DIR"
This script is located in: /home/user/scripts
```

## Tips

### Use in Scripts for Reliable Paths

When writing shell scripts, use `realpath` to get the absolute path of the script directory with `SCRIPT_DIR=$(realpath $(dirname "$0"))`. This ensures your script works correctly regardless of where it's called from.

### Combine with Other Commands

Pair `realpath` with commands like `find` or `xargs` to process files with their absolute paths: `find . -type f | xargs realpath`.

### Check if Two Paths Reference the Same File

Use `realpath` to determine if two different paths actually point to the same file: `[ "$(realpath path1)" = "$(realpath path2)" ]`.

## Frequently Asked Questions

#### Q1. What's the difference between `realpath` and `readlink -f`?
A. They're similar, but `realpath` is part of GNU coreutils and has more options. `readlink -f` is more commonly available on different Unix systems.

#### Q2. How do I use `realpath` to get the directory of a script?
A. Use `realpath $(dirname "$0")` in your script to get its directory.

#### Q3. Can `realpath` handle paths with spaces?
A. Yes, but make sure to quote the paths: `realpath "path with spaces"`.

#### Q4. What happens if I use `realpath` on a non-existent path?
A. By default, it will return an error. Use `-m` option to get the canonical path even if it doesn't exist.

## References

https://www.gnu.org/software/coreutils/manual/html_node/realpath-invocation.html

## Revisions

- 2025/04/30 First revision