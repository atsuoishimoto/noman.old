# pwd command

Print the current working directory's full pathname.

## Overview

The `pwd` command displays the full absolute path of the current directory you're in. This is useful for confirming your location in the filesystem, especially when navigating between directories or when writing scripts that need to reference the current location.

## Options

### **-L, --logical**

Prints the logical path, which may include symbolic links. This is the default behavior.

```console
$ pwd -L
/home/user/projects
```

### **-P, --physical**

Prints the physical path with all symbolic links resolved to their actual locations.

```console
$ pwd -P
/mnt/data/user/actual_projects
```

## Usage Examples

### Basic usage

```console
$ pwd
/home/user/documents
```

### Comparing logical and physical paths

```console
$ ln -s /var/www/html webroot
$ cd webroot
$ pwd -L
/home/user/webroot
$ pwd -P
/var/www/html
```

## Tips

### Use in Scripts

Include `pwd` in scripts when you need to reference files relative to the script's location:

```bash
#!/bin/bash
CURRENT_DIR=$(pwd)
echo "Working from: $CURRENT_DIR"
```

### Avoid Path Confusion

When working with symbolic links, use `pwd -P` to see the actual physical location, which helps prevent confusion about where files are actually stored.

### Copy Current Path to Clipboard

On macOS, you can copy the current path to clipboard with:
```console
$ pwd | pbcopy
```

On Linux with xclip installed:
```console
$ pwd | xclip -selection clipboard
```

## Frequently Asked Questions

#### Q1. What's the difference between `pwd` and `echo $PWD`?
A. They typically show the same result, but `$PWD` is an environment variable that may not always be updated in certain edge cases, while `pwd` always checks the current directory.

#### Q2. Why does `pwd -P` sometimes show a different path?
A. When you're in a directory accessed through a symbolic link, `-P` shows the actual physical path rather than the path through the symbolic link.

#### Q3. Does `pwd` work the same on all Unix systems?
A. The basic functionality is the same, but some systems might have additional options or slight variations in behavior.

## References

https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html

## Revisions

- 2025/04/30 First revision