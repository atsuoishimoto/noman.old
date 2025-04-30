# chgrp command

Change the group ownership of files or directories.

## Overview

The `chgrp` command changes the group ownership of files and directories. It allows system administrators and users to reassign which group has access to specific files, which is useful for managing file permissions and access control in multi-user environments.

## Options

### **-R, --recursive**

Change group ownership recursively, affecting all files and directories within the specified directory

```console
$ chgrp -R developers project/
```

### **-v, --verbose**

Display a diagnostic message for every file processed

```console
$ chgrp -v staff report.txt
changed group of 'report.txt' from 'users' to 'staff'
```

### **-c, --changes**

Like verbose, but only report when a change is made

```console
$ chgrp -c staff *.txt
changed group of 'document.txt' from 'users' to 'staff'
```

### **-h, --no-dereference**

Affect symbolic links instead of referenced files

```console
$ chgrp -h developers symlink
```

## Usage Examples

### Basic usage

```console
$ chgrp accounting financial.xlsx
$ ls -l financial.xlsx
-rw-r--r--  1 john  accounting  2048 Apr 28 10:15 financial.xlsx
```

### Changing group for multiple files

```console
$ chgrp developers *.py
$ ls -l
-rw-r--r--  1 alice  developers  1024 Apr 29 14:30 app.py
-rw-r--r--  1 alice  developers   512 Apr 29 14:32 utils.py
```

### Recursive and verbose change

```console
$ chgrp -Rv webteam website/
changed group of 'website/index.html' from 'alice' to 'webteam'
changed group of 'website/css/style.css' from 'alice' to 'webteam'
changed group of 'website/js/script.js' from 'alice' to 'webteam'
```

## Tips

### Check Available Groups

Before changing group ownership, use the `groups` command to see which groups you belong to, or check `/etc/group` to see all system groups.

### Permissions Required

You must be the owner of the file or have superuser (root) privileges to change a file's group. Additionally, you can only assign a file to a group that you are a member of (unless you're root).

### Use with chmod

Often used together with `chmod` to set both group ownership and permissions. For example: `chgrp developers project/ && chmod g+w project/` changes the group and gives that group write permissions.

### Reference File's Group

Use the `--reference=RFILE` option to set the same group as another file: `chgrp --reference=template.txt newfile.txt`

## Frequently Asked Questions

#### Q1. What's the difference between chgrp and chown?
A. `chgrp` only changes the group ownership of a file, while `chown` can change both the user and group ownership. `chown user:group file` is equivalent to running both `chown user file` and `chgrp group file`.

#### Q2. How do I see which group a file currently belongs to?
A. Use `ls -l filename` to see detailed file information including group ownership.

#### Q3. Can I use group ID numbers instead of group names?
A. Yes, you can use either the group name or its numeric GID: `chgrp 1001 file.txt`

#### Q4. How do I change group ownership of a symbolic link?
A. Use the `-h` option: `chgrp -h newgroup symlink`

## References

https://www.gnu.org/software/coreutils/manual/html_node/chgrp-invocation.html

## Revisions

- 2025/04/30 First revision