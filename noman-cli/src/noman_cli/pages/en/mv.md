# mv command

Move or rename files and directories.

## Overview

The `mv` command moves files or directories from one location to another, or renames them when the destination is in the same directory. It's one of the core file manipulation commands in Unix-like systems, allowing you to organize your filesystem by relocating files or changing their names.

## Options

### **-i (interactive)**

Prompts for confirmation before overwriting existing files, helping prevent accidental data loss.

```console
$ mv -i file.txt existing-file.txt
mv: overwrite 'existing-file.txt'? y
```

### **-f (force)**

Overrides the interactive mode and removes existing destination files without prompting.

```console
$ mv -f source.txt destination.txt
```

### **-v (verbose)**

Displays what is being done, showing the name of each file as it's moved.

```console
$ mv -v document.txt reports/
'document.txt' -> 'reports/document.txt'
```

### **-n (no-clobber)**

Prevents overwriting existing files, useful when you want to ensure you don't accidentally replace files.

```console
$ mv -n important.txt existing-file.txt
```

## Usage Examples

### Renaming a file

```console
$ mv oldname.txt newname.txt
```

### Moving a file to another directory

```console
$ mv document.txt ~/Documents/
```

### Moving multiple files to a directory

```console
$ mv file1.txt file2.txt file3.txt target_directory/
```

### Moving and renaming at the same time

```console
$ mv ~/Downloads/report.pdf ~/Documents/quarterly-report.pdf
```

## Tips

### Use Tab Completion

Press Tab while typing file paths to auto-complete names, reducing typing errors and saving time.

### Check Before Moving

When moving important files, use `mv -i` to get confirmation prompts or first use `ls` to verify the source and destination.

### Moving Hidden Files

Remember that wildcards like `*` don't match hidden files (those starting with a dot). Use `mv .*` specifically for hidden files or `mv -a *` for all files including hidden ones.

### Create Destination Directories First

The destination directory must exist before using `mv`. If it doesn't, `mv` will treat the destination as a filename instead of a directory.

## Frequently Asked Questions

#### Q1. How do I undo a move operation?
A. There's no direct "undo" command. You need to use `mv` again to move the file back to its original location.

#### Q2. Can I move files between different drives or partitions?
A. Yes, but technically `mv` will copy the file to the new location and then delete the original when moving across filesystems.

#### Q3. How do I rename multiple files at once?
A. Basic `mv` can't rename multiple files with a pattern. For batch renaming, use tools like `rename` or write a simple loop in your shell.

#### Q4. What happens if I move a file to a location where a file with the same name exists?
A. By default, `mv` overwrites the destination file without warning. Use `-i` for confirmation prompts or `-n` to prevent overwriting.

## References

https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html

## Revisions

- 2025/04/30 First revision