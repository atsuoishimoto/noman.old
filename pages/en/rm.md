# rm command

Remove files or directories from the filesystem.

## Overview

The `rm` command permanently deletes files and directories from your system. Once files are removed with this command, they cannot be easily recovered (unlike moving files to a trash/recycle bin in graphical interfaces). The command can delete individual files, multiple files, or entire directories with their contents.

## Options

### **-f, --force**

Force removal without prompting for confirmation, even for write-protected files.

```console
$ rm -f important.txt
```

### **-i, --interactive**

Prompt before every removal, requiring confirmation.

```console
$ rm -i document.txt
rm: remove regular file 'document.txt'? y
```

### **-r, -R, --recursive**

Remove directories and their contents recursively.

```console
$ rm -r projects/
```

### **-v, --verbose**

Explain what is being done, showing each file as it's removed.

```console
$ rm -v *.log
removed 'error.log'
removed 'access.log'
```

## Usage Examples

### Removing multiple files

```console
$ rm file1.txt file2.txt file3.txt
```

### Removing directories with confirmation

```console
$ rm -ri old_project/
rm: descend into directory 'old_project/'? y
rm: remove regular file 'old_project/readme.txt'? y
rm: remove directory 'old_project/'? y
```

### Forcefully removing a directory and all its contents

```console
$ rm -rf temp_folder/
```

## Tips:

### Use with Caution

The `rm` command permanently deletes files without moving them to a trash folder. Always double-check what you're deleting, especially when using wildcards or the `-r` option.

### Prevent Accidental Deletions

Consider creating an alias in your shell configuration: `alias rm='rm -i'` to always prompt for confirmation before deleting files.

### Safe Deletion Practice

When deleting multiple files with wildcards, first use `ls` with the same pattern to preview which files will be deleted:

```console
$ ls *.tmp
$ rm *.tmp
```

### Avoid Dangerous Commands

Never run `rm -rf /` or `rm -rf /*` as these can destroy your entire system.

## Frequently Asked Questions

#### Q1. Can I recover files deleted with `rm`?
A. Generally no. Unlike graphical interfaces, `rm` doesn't move files to a trash folder. Recovery requires specialized tools and isn't guaranteed.

#### Q2. How do I safely delete a directory with all its contents?
A. Use `rm -r directory/`. For added safety, use `rm -ri directory/` to confirm each deletion.

#### Q3. What's the difference between `rm -f` and regular `rm`?
A. `rm -f` forces deletion without prompting, even for write-protected files, while regular `rm` will ask for confirmation in some cases.

#### Q4. How can I see what files I'm about to delete?
A. Use `ls` with the same pattern first, or add the `-v` option to `rm` to see each file as it's deleted.

## macOS Considerations

On macOS, you can use `rm -P` to overwrite files before deletion for more secure removal. However, on SSDs with TRIM enabled (most modern Macs), this may not provide additional security.

## References

https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html

## Revisions

- 2025/04/30 First revision