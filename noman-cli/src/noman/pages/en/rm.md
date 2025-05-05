# rm command

Remove files or directories from the filesystem.

## Overview

The `rm` command deletes files and directories from your filesystem. By default, it removes files but not directories. Once files are deleted with `rm`, they cannot be easily recovered, so use this command with caution.

## Options

### **-f, --force**

Ignore nonexistent files and arguments, never prompt for confirmation

```console
$ rm -f nonexistent_file.txt
$
```

### **-i, --interactive**

Prompt before every removal

```console
$ rm -i important.txt
rm: remove regular file 'important.txt'? y
$
```

### **-r, -R, --recursive**

Remove directories and their contents recursively

```console
$ rm -r project_folder/
$
```

### **-d, --dir**

Remove empty directories

```console
$ rm -d empty_directory/
$
```

### **-v, --verbose**

Explain what is being done

```console
$ rm -v file.txt
removed 'file.txt'
$
```

## Usage Examples

### Removing multiple files

```console
$ rm file1.txt file2.txt file3.txt
$
```

### Removing files with confirmation

```console
$ rm -i *.txt
rm: remove regular file 'document.txt'? y
rm: remove regular file 'notes.txt'? n
$
```

### Removing directories and their contents

```console
$ rm -rf old_project/
$
```

### Removing files with verbose output

```console
$ rm -v *.log
removed 'app.log'
removed 'error.log'
removed 'system.log'
$
```

## Tips:

### Use the -i Flag for Safety

When deleting important files, use `rm -i` to get a confirmation prompt before each deletion. This helps prevent accidental file removal.

### Be Extremely Careful with rm -rf

The combination of `-r` (recursive) and `-f` (force) is powerful and dangerous. Never use `rm -rf /` or `rm -rf /*` as these can destroy your entire system.

### Use Wildcards with Caution

Before using wildcards like `*.txt`, consider running `ls *.txt` first to see which files will be affected.

### Create Aliases for Safety

Consider creating an alias in your shell configuration: `alias rm='rm -i'` to always prompt for confirmation.

## Frequently Asked Questions

#### Q1. Can I recover files deleted with rm?
A. Generally no. Unlike moving files to a "trash" or "recycle bin", `rm` permanently deletes files. Recovery might be possible with specialized tools, but it's not guaranteed.

#### Q2. How do I remove a directory?
A. Use `rm -r directory/` to remove a directory and all its contents. For empty directories, you can also use `rmdir directory/`.

#### Q3. How can I safely delete files?
A. Use `rm -i` for interactive prompts or consider using `trash-cli` utilities that move files to a recoverable trash location instead of deleting them permanently.

#### Q4. What does "Operation not permitted" mean?
A. This usually indicates you don't have sufficient permissions to delete the file. Try using `sudo rm` if you have administrator privileges.

## macOS Precautions

On macOS, the default `rm` command doesn't move files to the Trash. Once deleted, files are permanently removed. Consider using `mv file ~/.Trash/` to move files to the Trash instead, or install tools like `trash` that provide this functionality.

## References

https://www.gnu.org/software/coreutils/manual/html_node/rm-invocation.html

## Revisions

2025/05/04 First revision