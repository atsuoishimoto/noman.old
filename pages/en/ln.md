# ln command

Create links between files.

## Overview

The `ln` command creates links between files. It can create hard links (the default) or symbolic links (with the `-s` option). Hard links point directly to the file's data on disk, while symbolic links are special files that point to another file path.

## Options

### **-s, --symbolic**

Create a symbolic link instead of a hard link.

```console
$ ln -s target_file link_name
$ ls -l link_name
lrwxrwxrwx 1 user group 10 Apr 30 10:00 link_name -> target_file
```

### **-f, --force**

Remove existing destination files.

```console
$ ln -sf target_file existing_link
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
$ ln -sr ../dir1/file dir2/link
$ ls -l dir2/link
lrwxrwxrwx 1 user group 12 Apr 30 10:00 dir2/link -> ../dir1/file
```

## Usage Examples

### Creating a hard link

```console
$ echo "Hello" > original.txt
$ ln original.txt hard_link.txt
$ ls -l *txt
-rw-r--r-- 2 user group 6 Apr 30 10:00 hard_link.txt
-rw-r--r-- 2 user group 6 Apr 30 10:00 original.txt
```

### Creating a symbolic link to a directory

```console
$ ln -s /path/to/directory link_to_dir
$ ls -l link_to_dir
lrwxrwxrwx 1 user group 16 Apr 30 10:00 link_to_dir -> /path/to/directory
```

### Creating multiple links at once

```console
$ ln -s file1 file2 file3 directory/
$ ls -l directory/
lrwxrwxrwx 1 user group 5 Apr 30 10:00 directory/file1 -> file1
lrwxrwxrwx 1 user group 5 Apr 30 10:00 directory/file2 -> file2
lrwxrwxrwx 1 user group 5 Apr 30 10:00 directory/file3 -> file3
```

## Tips

### Understanding Hard vs. Symbolic Links

Hard links share the same inode (data location on disk) as the original file. Deleting the original file won't affect hard links. Symbolic links are just pointers to file paths and will break if the original file is moved or deleted.

### Relative vs. Absolute Paths

When creating symbolic links, consider using relative paths (`-r` option) if the linked files might be moved together. Use absolute paths when the link needs to work regardless of where it's accessed from.

### Checking Link Status

Use `ls -l` to see what a symbolic link points to. The number after permissions in a file listing shows how many hard links a file has.

### Broken Links

Symbolic links that point to non-existent files are called "broken links." Use `find -L . -type l -print` to locate broken links in a directory.

## Frequently Asked Questions

#### Q1. What's the difference between hard and symbolic links?
A. Hard links directly reference a file's data on disk and can't cross filesystems. Symbolic links are pointer files that contain the path to another file and can point to files on different filesystems.

#### Q2. Can I create a hard link to a directory?
A. No, most Unix systems don't allow hard links to directories to prevent filesystem loops.

#### Q3. What happens if I delete a file that has hard links?
A. The file's data remains available through the hard links until all links are deleted.

#### Q4. How do I know if a file has hard links?
A. Use `ls -l` and look at the number after the permissions. If it's greater than 1, the file has hard links.

#### Q5. Why do my symbolic links break when I move files?
A. Symbolic links point to file paths. If you move the target file without updating the link, the link will break. Consider using relative paths with the `-r` option.

## References

https://www.gnu.org/software/coreutils/manual/html_node/ln-invocation.html

## Revisions

- 2025/04/30 First revision