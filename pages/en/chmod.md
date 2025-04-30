# chmod command

Change file access permissions.

## Overview

The `chmod` command modifies file and directory permissions in Unix-like systems. It allows users to control who can read, write, or execute files by changing the permission bits of files and directories.

## Options

### **-R, --recursive**

Change permissions recursively for directories and their contents

```console
$ chmod -R 755 projects/
```

### **-v, --verbose**

Display a diagnostic message for every file processed

```console
$ chmod -v 644 document.txt
mode of 'document.txt' changed from 0600 (rw-------) to 0644 (rw-r--r--)
```

### **--reference=RFILE**

Use RFILE's permissions instead of specifying a mode value

```console
$ chmod --reference=reference.txt target.txt
```

## Usage Examples

### Using Numeric (Octal) Mode

```console
$ chmod 755 script.sh
$ ls -l script.sh
-rwxr-xr-x  1 user  staff  1024 Apr 30 15:30 script.sh
```

### Using Symbolic Mode

```console
$ chmod u+x script.sh
$ ls -l script.sh
-rwxr--r--  1 user  staff  1024 Apr 30 15:30 script.sh
```

### Changing Multiple Files

```console
$ chmod 644 *.txt
$ ls -l *.txt
-rw-r--r--  1 user  staff  1024 Apr 30 15:30 document1.txt
-rw-r--r--  1 user  staff  2048 Apr 29 10:15 document2.txt
```

## Tips:

### Understanding Permission Numbers

The three digits in numeric mode (like 755) represent permissions for owner, group, and others:
- 4 = read (r)
- 2 = write (w)
- 1 = execute (x)

So 755 means rwx (4+2+1=7) for owner, r-x (4+0+1=5) for group, and r-x (4+0+1=5) for others.

### Common Permission Patterns

- 755 (rwxr-xr-x): Standard for executable files and directories
- 644 (rw-r--r--): Standard for regular files
- 600 (rw-------): Private files only the owner can access

### Symbolic Mode Shortcuts

- `u` (user/owner), `g` (group), `o` (others), `a` (all)
- `+` (add permission), `-` (remove permission), `=` (set exact permission)
- Example: `chmod a+x file` adds execute permission for everyone

## Frequently Asked Questions

#### Q1. What's the difference between numeric and symbolic modes?
A. Numeric mode (like 755) sets all permissions at once using octal numbers. Symbolic mode (like u+x) allows adding, removing, or setting specific permissions without affecting others.

#### Q2. How do I make a file executable?
A. Use `chmod +x filename` or `chmod u+x filename` to make it executable for the owner only.

#### Q3. Why can't I change permissions on certain files?
A. You need to be the file owner or have sudo/root privileges to change permissions.

#### Q4. How do I set permissions recursively for a directory?
A. Use `chmod -R mode directory/` to apply permissions to the directory and all its contents.

## References

https://www.gnu.org/software/coreutils/manual/html_node/chmod-invocation.html

## Revisions

- 2025/04/30 First revision