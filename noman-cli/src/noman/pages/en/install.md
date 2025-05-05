# install command

Copy files and set attributes.

## Overview

The `install` command copies files to specified destinations while setting their permissions and ownership. It's commonly used in scripts and makefiles to install programs, scripts, and configuration files to their proper locations in the system.

## Options

### **-d, --directory**

Create directories (and their parents if needed) instead of copying files.

```console
$ install -d /tmp/new_directory
$ ls -ld /tmp/new_directory
drwxr-xr-x 2 user user 4096 May 4 10:15 /tmp/new_directory
```

### **-m, --mode=MODE**

Set the permission mode (as in chmod) for the destination file or directory.

```console
$ install -m 755 script.sh /usr/local/bin/
$ ls -l /usr/local/bin/script.sh
-rwxr-xr-x 1 root root 256 May 4 10:20 /usr/local/bin/script.sh
```

### **-o, --owner=OWNER**

Set the owner for the destination files (requires superuser privileges).

```console
$ sudo install -o nobody script.sh /usr/local/bin/
$ ls -l /usr/local/bin/script.sh
-rwxr-xr-x 1 nobody root 256 May 4 10:25 /usr/local/bin/script.sh
```

### **-g, --group=GROUP**

Set the group for the destination files (requires superuser privileges).

```console
$ sudo install -g staff script.sh /usr/local/bin/
$ ls -l /usr/local/bin/script.sh
-rwxr-xr-x 1 root staff 256 May 4 10:30 /usr/local/bin/script.sh
```

### **-s, --strip**

Strip symbol tables from executables.

```console
$ install -s myprogram /usr/local/bin/
```

### **-v, --verbose**

Print the name of each file before copying it.

```console
$ install -v script.sh /usr/local/bin/
'script.sh' -> '/usr/local/bin/script.sh'
```

## Usage Examples

### Installing a script with specific permissions

```console
$ sudo install -m 755 -o root -g root myscript.sh /usr/local/bin/
$ ls -l /usr/local/bin/myscript.sh
-rwxr-xr-x 1 root root 512 May 4 10:35 /usr/local/bin/myscript.sh
```

### Creating multiple directories at once

```console
$ install -d -m 750 /tmp/project/{bin,lib,doc}
$ ls -ld /tmp/project/bin /tmp/project/lib /tmp/project/doc
drwxr-x--- 2 user user 4096 May 4 10:40 /tmp/project/bin
drwxr-x--- 2 user user 4096 May 4 10:40 /tmp/project/doc
drwxr-x--- 2 user user 4096 May 4 10:40 /tmp/project/lib
```

### Installing multiple files to a directory

```console
$ install -m 644 config.json settings.ini /etc/myapp/
$ ls -l /etc/myapp/
-rw-r--r-- 1 root root 1024 May 4 10:45 config.json
-rw-r--r-- 1 root root 512 May 4 10:45 settings.ini
```

## Tips:

### Use in Makefiles

The `install` command is commonly used in Makefiles for software installation. It's preferred over `cp` because it handles permissions and ownership in one step.

### Creating Directory Trees

When using `-d`, parent directories are created automatically if they don't exist, similar to `mkdir -p`.

### Default Permissions

If no mode is specified with `-m`, the default is typically 755 (rwxr-xr-x) for executables and 644 (rw-r--r--) for non-executables.

### Backup Option

Use `-b` or `--backup` to create backups of existing destination files before overwriting them.

## Frequently Asked Questions

#### Q1. What's the difference between `install` and `cp`?
A. While `cp` simply copies files, `install` copies files and sets permissions, ownership, and other attributes in a single command. It's designed specifically for installing files in a system.

#### Q2. Can I use `install` to create directories?
A. Yes, use `install -d` to create directories with specific permissions, similar to `mkdir -p` but with more control over permissions.

#### Q3. Do I need root privileges to use `install`?
A. You only need root privileges when installing to system directories or when changing ownership with `-o` or `-g` options.

#### Q4. Can `install` preserve file attributes?
A. Unlike `cp -p`, `install` is designed to set specific attributes rather than preserve existing ones. Use `cp -p` if you want to preserve the original file's attributes.

## References

https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html

## Revisions

- 2025/05/04 First revision