# pwd command

Print the full pathname of the current working directory.

## Overview

The `pwd` command displays the absolute path of the current directory you're in. This helps you understand your location within the filesystem hierarchy, which is especially useful when navigating between directories or writing scripts that need to reference file locations.

## Options

### **-L, --logical**

Print the logical current working directory, using the environment variable PWD. This follows symbolic links, showing the path as you navigated to it.

```console
$ pwd -L
/home/user/projects
```

### **-P, --physical**

Print the physical current working directory, with all symbolic links resolved. This shows the actual location in the filesystem.

```console
$ ln -s /var/www/html webroot
$ cd webroot
$ pwd -L
/home/user/webroot
$ pwd -P
/var/www/html
```

## Usage Examples

### Basic usage

```console
$ pwd
/home/user/documents
```

### Using pwd in scripts

```console
$ echo "Current directory is $(pwd)"
Current directory is /home/user/documents
```

## Tips

### Use in Shell Scripts

Store the current directory in a variable before changing directories, so you can return later:

```console
$ original_dir=$(pwd)
$ cd /tmp
$ # Do some work...
$ cd "$original_dir"  # Return to where you started
```

### Avoid Trailing Newlines

When using `pwd` in scripts or command substitution, you might want to use `$(pwd)` rather than backticks to avoid potential issues with trailing newlines.

### Resolving Symlink Confusion

If you're working with symbolic links and getting confused about your actual location, use `pwd -P` to see the physical path.

## Frequently Asked Questions

#### Q1. What does "pwd" stand for?
A. "pwd" stands for "print working directory."

#### Q2. What's the difference between -L and -P options?
A. `-L` follows symbolic links and shows the path as you navigated to it, while `-P` resolves all symbolic links and shows the actual physical path.

#### Q3. How can I use pwd in a bash script?
A. You can use `current_dir=$(pwd)` to store the current directory in a variable, or use it directly in commands like `echo "I am in $(pwd)"`.

#### Q4. Does pwd work the same on all Unix/Linux systems?
A. The basic functionality is the same across systems, but some options might vary between different implementations (GNU, BSD, etc.).

## References

https://www.gnu.org/software/coreutils/manual/html_node/pwd-invocation.html

## Revisions

- 2025/05/04 First revision