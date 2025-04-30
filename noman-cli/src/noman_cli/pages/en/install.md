# install command

Copy files to their destination, setting permission modes and owner/group.

## Overview

The `install` command copies files to specified destinations while also setting their permissions, owner, and group. Unlike a simple copy operation, `install` ensures the target files have the correct attributes, making it particularly useful for software installation scripts and system administration tasks.

## Options

### **-m, --mode=MODE**

Set the permission mode (as in chmod) for the destination file or directory.

```console
$ install -m 755 script.sh /usr/local/bin/
```

### **-o, --owner=OWNER**

Set the ownership of the destination files (superuser only).

```console
$ sudo install -o root script.sh /usr/local/bin/
```

### **-g, --group=GROUP**

Set the group ownership of the destination files (superuser only).

```console
$ sudo install -g wheel script.sh /usr/local/bin/
```

### **-d, --directory**

Create directories instead of copying files. Creates all components of the specified directories.

```console
$ install -d -m 755 /path/to/new/directory
```

### **-v, --verbose**

Print the name of each file or directory being processed.

```console
$ install -v script.sh /usr/local/bin/
'script.sh' -> '/usr/local/bin/script.sh'
```

## Usage Examples

### Installing an executable with proper permissions

```console
$ sudo install -m 755 -o root -g wheel myscript.sh /usr/local/bin/
```

### Creating multiple directories with specific permissions

```console
$ install -d -m 750 ~/projects/app/{bin,lib,doc}
```

### Copying configuration files with restricted permissions

```console
$ sudo install -m 600 -o root config.conf /etc/myapp/
```

### Installing multiple files to a directory

```console
$ install -m 644 *.txt /usr/share/doc/myapp/
```

## Tips:

### Use for System Files Installation

`install` is preferable to `cp` when deploying system files because it handles permissions and ownership in a single command, reducing the chance of security issues from improperly configured files.

### Create Parent Directories Automatically

When using `-d`, all parent directories are created if they don't exist, similar to `mkdir -p`.

### Backup Existing Files

Use the `-b` or `--backup` option to create backups of existing destination files before overwriting them.

### Preserve File Attributes

Use `-p` or `--preserve-timestamps` to preserve the original files' access and modification times in the copies.

## Frequently Asked Questions

#### Q1. What's the difference between `install` and `cp`?
A. `install` combines copying with setting permissions and ownership in one command, while `cp` primarily copies files and requires separate `chmod` and `chown` commands to modify attributes.

#### Q2. Can `install` create directories like `mkdir`?
A. Yes, with the `-d` option, `install` can create directories and set their permissions in one step.

#### Q3. Do I need sudo to use `install`?
A. You only need sudo when installing to system directories or when changing ownership to users other than yourself.

#### Q4. Can `install` preserve file timestamps?
A. Yes, use the `-p` option to preserve the original file's timestamps.

## References

https://www.gnu.org/software/coreutils/manual/html_node/install-invocation.html

## Revisions

- 2025/04/30 First revision