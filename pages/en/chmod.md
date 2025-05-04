# chmod command

Change file mode bits (permissions) of files and directories.

## Overview

The `chmod` command modifies the access permissions of files and directories in Unix-like operating systems. It controls who can read, write, or execute files by changing the file mode bits. This command is essential for managing file security and access control.

## Options

### **-R, --recursive**

Change permissions recursively, affecting all files and subdirectories within the specified directories.

```console
$ chmod -R 755 projects/
```

### **-v, --verbose**

Display a diagnostic message for every file processed, showing the changes being made.

```console
$ chmod -v 644 document.txt
mode of 'document.txt' changed from 0600 (rw-------) to 0644 (rw-r--r--)
```

### **-c, --changes**

Like verbose, but only report when a change is actually made.

```console
$ chmod -c 644 document.txt
mode of 'document.txt' changed from 0600 (rw-------) to 0644 (rw-r--r--)
```

### **-f, --silent, --quiet**

Suppress most error messages.

```console
$ chmod -f 644 nonexistent.txt
```

## Usage Examples

### Using Numeric (Octal) Mode

```console
$ chmod 755 script.sh
$ ls -l script.sh
-rwxr-xr-x 1 user group 1024 May 4 10:00 script.sh
```

### Using Symbolic Mode

```console
$ chmod u+x script.sh
$ ls -l script.sh
-rwxr--r-- 1 user group 1024 May 4 10:00 script.sh
```

### Changing Permissions Recursively

```console
$ chmod -R go-w documents/
$ ls -l documents/
total 8
-rw-r--r-- 1 user group 1024 May 4 10:00 file1.txt
-rw-r--r-- 1 user group 2048 May 4 10:00 file2.txt
drwxr-xr-x 2 user group 4096 May 4 10:00 subfolder
```

## Tips:

### Understanding Permission Notation

- Numeric (octal) mode: 
  - First digit: owner permissions (4=read, 2=write, 1=execute)
  - Second digit: group permissions
  - Third digit: others permissions
  - Example: 755 = rwxr-xr-x (owner can read/write/execute, group and others can read/execute)

- Symbolic mode:
  - u: user/owner, g: group, o: others, a: all
  - +: add permission, -: remove permission, =: set exact permission
  - r: read, w: write, x: execute
  - Example: u+x (add execute permission for owner)

### Common Permission Patterns

- 755 (rwxr-xr-x): Standard for directories and executable scripts
- 644 (rw-r--r--): Standard for regular files
- 600 (rw-------): Private files (only owner can read/write)
- 777 (rwxrwxrwx): Full access for everyone (use with caution)

### Check Before You Change

Always verify the current permissions with `ls -l` before making changes, especially when using recursive options.

## Frequently Asked Questions

#### Q1. How do I make a file executable?
A. Use `chmod +x filename` or `chmod u+x filename` to make it executable for the owner only.

#### Q2. What's the difference between symbolic and numeric modes?
A. Symbolic mode (like u+x) is more intuitive and allows for relative changes. Numeric mode (like 755) sets absolute permissions and is more concise.

#### Q3. How do I give read and write permissions to a file's owner only?
A. Use `chmod 600 filename` or `chmod u=rw,go= filename`.

#### Q4. Can chmod change ownership of a file?
A. No, chmod only changes permissions. Use `chown` to change file ownership.

#### Q5. How do I fix "Permission denied" errors?
A. Either change the file permissions with `chmod` or run the command with elevated privileges using `sudo`.

## References

https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html

## Revisions

- 2025/05/04 First revision