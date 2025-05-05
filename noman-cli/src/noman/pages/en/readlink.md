# readlink command

Print the resolved symbolic links or canonical file names.

## Overview

The `readlink` command displays the target of a symbolic link or the canonical path of a file. It resolves symbolic links in a path, showing where they actually point to. This is useful for determining the actual location of files in a filesystem with many symbolic links.

## Options

### **-f, --canonicalize**

Canonicalize by following every symlink in every component of the given path recursively

```console
$ ln -s /etc/hosts mylink
$ readlink -f mylink
/etc/hosts
```

### **-e, --canonicalize-existing**

Canonicalize by following every symlink in every component of the given path recursively, all components must exist

```console
$ readlink -e mylink
/etc/hosts
$ readlink -e nonexistent
# No output, as the file doesn't exist
```

### **-m, --canonicalize-missing**

Canonicalize by following every symlink in every component of the given path recursively, without requirements on components existence

```console
$ readlink -m /nonexistent/path/file.txt
/nonexistent/path/file.txt
```

### **-n, --no-newline**

Do not output the trailing delimiter (newline)

```console
$ readlink -n mylink && echo " (this continues on same line)"
/etc/hosts (this continues on same line)
```

### **-z, --zero**

End each output line with NUL, not newline

```console
$ readlink -z mylink | hexdump -C
00000000  2f 65 74 63 2f 68 6f 73  74 73 00                 |/etc/hosts.|
0000000b
```

### **-v, --verbose**

Report errors (not implemented on all systems)

```console
$ readlink -v nonexistent
readlink: nonexistent: No such file or directory
```

## Usage Examples

### Basic usage to read a symbolic link

```console
$ ln -s /usr/bin/python3 python
$ readlink python
/usr/bin/python3
```

### Finding the canonical path of a file with multiple symlinks

```console
$ ln -s /etc/passwd passwd_link
$ ln -s passwd_link passwd_link2
$ readlink -f passwd_link2
/etc/passwd
```

### Working with relative paths

```console
$ mkdir -p dir1/dir2
$ ln -s dir1/dir2 mydir
$ readlink -f mydir
/home/user/dir1/dir2
```

## Tips:

### Distinguish Between Direct and Full Resolution

Use plain `readlink` to see only the immediate target of a symlink, or use `readlink -f` to follow chains of symlinks to the final destination.

### Check if a Path is a Symlink

If `readlink` returns nothing and exits with a non-zero status, the path is not a symlink. This can be used in scripts to test if a file is a symlink.

### Combine with Other Commands

Pipe the output of `readlink` to other commands when you need to operate on the actual file rather than the symlink.

## Frequently Asked Questions

#### Q1. What's the difference between `readlink` and `realpath`?
A. While both resolve symlinks, `realpath` always provides the absolute path, whereas basic `readlink` only shows the immediate target of a symlink. `readlink -f` is similar to `realpath`.

#### Q2. Why does `readlink` without options sometimes return nothing?
A. Without options, `readlink` only works on symbolic links. If you try to use it on a regular file or directory, it will return nothing and exit with an error code.

#### Q3. How can I use `readlink` in a shell script safely?
A. Use `readlink -f "$path"` to get the canonical path, which handles spaces and special characters correctly when properly quoted.

#### Q4. What happens if a symlink points to a non-existent file?
A. Basic `readlink` will still show the target path, even if it doesn't exist. `readlink -e` will fail, while `readlink -f` and `readlink -m` will resolve as much as possible.

## References

https://www.gnu.org/software/coreutils/manual/html_node/readlink-invocation.html

## Revisions

- 2025/05/04 First revision