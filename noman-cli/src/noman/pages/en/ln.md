# ln command

Create links between files.

## Overview

The `ln` command creates links to files or directories. It can create hard links (the default) or symbolic links (with the `-s` option). Hard links point directly to the file's data on disk, while symbolic links are special files that point to another file or directory by name.

## Options

### **-s, --symbolic**

Create a symbolic link instead of a hard link.

```console
$ ln -s target_file link_name
$ ls -l link_name
lrwxrwxrwx 1 user user 10 May 4 10:00 link_name -> target_file
```

### **-f, --force**

Remove existing destination files.

```console
$ ln -sf target_file existing_link
```

### **-n, --no-dereference**

Treat destination that is a symbolic link to a directory as if it were a normal file.

```console
$ ln -sfn new_target existing_link
```

### **-v, --verbose**

Print the name of each linked file.

```console
$ ln -sv target_file link_name
'link_name' -> 'target_file'
```

### **-r, --relative**

Create symbolic links relative to link location.

```console
$ ln -sr ../dir1/file1 link_name
```

## Usage Examples

### Creating a hard link

```console
$ echo "Original content" > original.txt
$ ln original.txt hardlink.txt
$ ls -l *txt
-rw-r--r-- 2 user user 16 May 4 10:00 hardlink.txt
-rw-r--r-- 2 user user 16 May 4 10:00 original.txt
```

### Creating a symbolic link to a file

```console
$ ln -s /path/to/file.txt symlink.txt
$ ls -l symlink.txt
lrwxrwxrwx 1 user user 15 May 4 10:00 symlink.txt -> /path/to/file.txt
```

### Creating a symbolic link to a directory

```console
$ ln -s /usr/local/bin bin_link
$ ls -l bin_link
lrwxrwxrwx 1 user user 14 May 4 10:00 bin_link -> /usr/local/bin
```

### Creating a relative symbolic link

```console
$ mkdir -p dir1/subdir
$ touch dir1/file.txt
$ ln -sr dir1/file.txt dir1/subdir/link.txt
$ ls -l dir1/subdir/link.txt
lrwxrwxrwx 1 user user 9 May 4 10:00 dir1/subdir/link.txt -> ../file.txt
```

## Tips

### Hard Links vs. Symbolic Links

- Hard links share the same inode as the original file, meaning they reference the same physical data on disk. Changes to either file affect both.
- Hard links cannot span filesystems and cannot link to directories.
- Symbolic links are separate files that point to another file by name and can span filesystems.
- If the original file of a symbolic link is deleted, the link becomes "broken" and points to nothing.

### Updating Existing Symbolic Links

Use `-sfn` together to safely update existing symbolic links:
```console
$ ln -sfn new_target existing_link
```

### Checking for Broken Symbolic Links

Find broken symbolic links in the current directory:
```console
$ find . -type l -exec test ! -e {} \; -print
```

## Frequently Asked Questions

#### Q1. What's the difference between hard links and symbolic links?
A. Hard links directly reference a file's inode (data on disk) and can't span filesystems or link to directories. Symbolic links are pointer files that reference another file by path and can link across filesystems and to directories.

#### Q2. How do I update an existing symbolic link?
A. Use `ln -sf new_target existing_link` to force the creation of a new link, replacing the existing one.

#### Q3. Can I create a hard link to a directory?
A. No, hard links to directories are not allowed in most Unix/Linux systems to prevent filesystem loops.

#### Q4. How can I tell if a file is a symbolic link?
A. Use `ls -l filename` - symbolic links will show an "l" at the beginning of the permissions and display the target with an arrow (->).

## macOS Considerations

On macOS, the `ln` command works similarly to Linux, but there are some differences:
- The `-r` (relative) option may not be available in older macOS versions.
- For compatibility across systems, use the full `-symbolic` option instead of just `-s` if you encounter issues.

## References

https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html

## Revisions

- 2025/05/04 First revision