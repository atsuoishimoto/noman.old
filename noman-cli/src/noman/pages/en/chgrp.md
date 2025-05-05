# chgrp command

Change the group ownership of files or directories.

## Overview

The `chgrp` command changes the group ownership of files and directories. It allows users with appropriate permissions to modify which group has access to specific files or directories, which is an important aspect of Unix file permission management.

## Options

### **-c, --changes**

Report when a change is made to the group ownership.

```console
$ chgrp -c staff document.txt
changed group of 'document.txt' from 'users' to 'staff'
```

### **-f, --silent, --quiet**

Suppress most error messages.

```console
$ chgrp -f nonexistent_group document.txt
```

### **-v, --verbose**

Output a diagnostic for every file processed.

```console
$ chgrp -v staff *.txt
group of 'document.txt' retained as 'staff'
group of 'notes.txt' changed from 'users' to 'staff'
```

### **-R, --recursive**

Operate on files and directories recursively.

```console
$ chgrp -R developers project_folder/
```

### **-h, --no-dereference**

Affect symbolic links instead of referenced files.

```console
$ chgrp -h staff symlink_file
```

### **--reference=RFILE**

Use RFILE's group rather than specifying a GROUP value.

```console
$ chgrp --reference=template.txt document.txt
```

## Usage Examples

### Changing group ownership of a single file

```console
$ ls -l document.txt
-rw-r--r-- 1 user users 1024 May 4 10:30 document.txt
$ chgrp staff document.txt
$ ls -l document.txt
-rw-r--r-- 1 user staff 1024 May 4 10:30 document.txt
```

### Changing group ownership recursively

```console
$ chgrp -R developers project/
$ ls -l project/
total 8
drwxr-xr-x 2 user developers 4096 May 4 10:35 src/
-rw-r--r-- 1 user developers 2048 May 4 10:32 README.md
```

### Using a reference file for group ownership

```console
$ ls -l template.txt document.txt
-rw-r--r-- 1 user developers 1024 May 4 10:30 template.txt
-rw-r--r-- 1 user users 2048 May 4 10:32 document.txt
$ chgrp --reference=template.txt document.txt
$ ls -l document.txt
-rw-r--r-- 1 user developers 2048 May 4 10:32 document.txt
```

## Tips:

### Check Group Membership First

Before changing a file's group, ensure you are a member of the target group using the `groups` command. You can only change a file's group to one you belong to (unless you're root).

### Use Numeric Group IDs

If you know the group ID number, you can use it instead of the group name:

```console
$ chgrp 1000 document.txt
```

### Combine with chmod

After changing group ownership, you might need to adjust group permissions with `chmod`:

```console
$ chgrp developers project/
$ chmod g+w project/
```

## Frequently Asked Questions

#### Q1. Who can change a file's group?
A. The file owner can change a file's group, but only to a group they are a member of. The root user can change any file's group to any group.

#### Q2. How do I see what groups I belong to?
A. Use the `groups` command to see all groups you belong to.

#### Q3. Can I change both owner and group at once?
A. No, `chgrp` only changes the group. Use `chown` with the syntax `chown user:group file` to change both simultaneously.

#### Q4. Why do I get "Operation not permitted" errors?
A. This usually happens when you're not the file owner, not a member of the target group, or the file has special permissions like the immutable flag set.

## References

https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html

## Revisions

- 2025/05/04 First revision