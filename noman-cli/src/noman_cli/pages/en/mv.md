# mv command

Move or rename files and directories.

## Overview

The `mv` command moves files or directories from one location to another or renames them. When moving between filesystems, it copies the source file and deletes the original. It's commonly used for organizing files, backing up data, or simply changing filenames.

## Options

### **-f, --force**

Overwrite destination files without prompting for confirmation.

```console
$ mv -f important.txt backup/
```

### **-i, --interactive**

Prompt before overwriting existing files. This is safer than the default behavior.

```console
$ mv -i document.txt ~/Documents/
mv: overwrite '/home/user/Documents/document.txt'? y
```

### **-n, --no-clobber**

Do not overwrite existing files.

```console
$ mv -n *.txt backup/
```

### **-u, --update**

Move only when the source file is newer than the destination file or when the destination file is missing.

```console
$ mv -u new_version.txt ~/Documents/
```

### **-v, --verbose**

Explain what is being done.

```console
$ mv -v file.txt newname.txt
'file.txt' -> 'newname.txt'
```

## Usage Examples

### Renaming a file

```console
$ mv oldname.txt newname.txt
```

### Moving multiple files to a directory

```console
$ mv file1.txt file2.txt file3.txt destination_directory/
```

### Moving and renaming at the same time

```console
$ mv ~/Downloads/report.pdf ~/Documents/quarterly_report_2025.pdf
```

### Moving all files of a specific type

```console
$ mv *.jpg ~/Pictures/
```

## Tips

### Use Wildcards Carefully

When using wildcards with `mv`, first test with `ls` using the same pattern to see which files will be affected.

### Create Target Directories First

Ensure the destination directory exists before moving files. If it doesn't, `mv` will rename your file instead of moving it.

### Preserve Attributes

Use `mv -p` on some systems to preserve file attributes when moving files.

### Backup Before Moving

For important files, consider using `cp` to create a backup before moving, especially when moving between filesystems.

### Moving Hidden Files

Don't forget that `mv .*` will try to move `.` and `..` (current and parent directories), which will fail. Use `mv .[a-zA-Z0-9]*` instead to move only hidden files.

## Frequently Asked Questions

#### Q1. What's the difference between `mv` and `cp`?
A. `mv` moves or renames files, removing them from the source location, while `cp` copies files, leaving the original intact.

#### Q2. How do I move a file without overwriting an existing file?
A. Use `mv -n source destination` to prevent overwriting existing files.

#### Q3. Can I move directories with `mv`?
A. Yes, `mv` can move entire directories along with their contents.

#### Q4. How do I safely move files without losing data?
A. Use `mv -i` to be prompted before overwriting any existing files.

#### Q5. Why does `mv` sometimes take longer between different filesystems?
A. When moving between different filesystems, `mv` must copy the data and then delete the original, which takes longer than simply updating directory entries.

## References

https://www.gnu.org/software/coreutils/manual/html_node/mv-invocation.html

## Revisions

- 2025/05/04 First revision