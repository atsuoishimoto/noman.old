# readlink command

Print the resolved symbolic links or canonical file names.

## Overview

The `readlink` command displays the target of a symbolic link or the canonical path of a file. It's useful for determining where a symbolic link points to or for getting the absolute path of a file with all symbolic links resolved.

## Options

### **-f, --canonicalize**

Canonicalize by following every symlink in every component of the given path recursively

```console
$ ln -s /usr/bin bin_link
$ readlink -f bin_link
/usr/bin
```

### **-e, --canonicalize-existing**

Canonicalize by following every symlink in every component of the given path recursively, all components must exist

```console
$ readlink -e bin_link
/usr/bin
$ readlink -e nonexistent_link
[no output, returns error]
```

### **-n, --no-newline**

Do not output the trailing newline

```console
$ readlink -n bin_link
/usr/bin$ echo " (this continues on same line)"
 (this continues on same line)
```

### **-v, --verbose**

Report errors

```console
$ readlink -v nonexistent_link
readlink: nonexistent_link: No such file or directory
```

## Usage Examples

### Basic usage to show where a symlink points

```console
$ ln -s /etc/hosts hosts_link
$ readlink hosts_link
/etc/hosts
```

### Getting the absolute path with all symlinks resolved

```console
$ cd /usr/local/bin
$ readlink -f python
/usr/bin/python3.9
```

### Checking if a path is a symlink

```console
$ readlink regular_file
[no output]
$ echo $?
1
```

## Tips

### Distinguish Between Symlinks and Regular Files

If `readlink` returns no output and an exit status of 1, the file is not a symbolic link. This can be used in scripts to determine if a file is a symlink.

### Use in Scripts

When writing shell scripts, `readlink -f` is useful for getting the absolute path of a script regardless of where it's called from:

```bash
SCRIPT_DIR=$(dirname $(readlink -f "$0"))
```

### Combine with Other Commands

Combine `readlink` with other commands to operate on the target of a symlink:
```bash
cat $(readlink symlink_to_file)
```

## Frequently Asked Questions

#### Q1. What's the difference between `readlink` and `realpath`?
A. Both commands can resolve symbolic links, but `realpath` always prints the absolute path while `readlink` without options only shows the immediate target of a symlink. With the `-f` option, `readlink` behaves similarly to `realpath`.

#### Q2. How do I get the absolute path of a file?
A. Use `readlink -f filename` to get the absolute path with all symbolic links resolved.

#### Q3. Why does `readlink` return nothing for a regular file?
A. `readlink` only shows information for symbolic links. For regular files without the `-f` option, it returns nothing and an exit status of 1.

#### Q4. How can I use `readlink` in a script to find the script's location?
A. Use `SCRIPT_DIR=$(dirname $(readlink -f "$0"))` to get the directory containing the script.

## References

https://www.gnu.org/software/coreutils/manual/html_node/readlink-invocation.html

## Revisions

- 2025/04/30 First revision