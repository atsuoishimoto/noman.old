# diff command

Compare files line by line.

## Overview

The `diff` command compares two files or directories and displays the differences between them. It's commonly used to see what changes have been made to files, create patch files, or compare configurations. The output shows which lines need to be changed to make the files identical.

## Options

### **-u, --unified**

Output differences in the unified format, showing context around the differences. This is the most readable and commonly used format.

```console
$ diff -u file1.txt file2.txt
--- file1.txt	2025-05-04 10:00:00.000000000 -0400
+++ file2.txt	2025-05-04 10:30:00.000000000 -0400
@@ -1,3 +1,4 @@
 This is a test file.
-It has some content.
+It has some modified content.
 The end of the file.
+A new line was added.
```

### **-i, --ignore-case**

Ignore case differences when comparing files.

```console
$ diff -i uppercase.txt lowercase.txt
[No output if files differ only in case]
```

### **-b, --ignore-space-change**

Ignore changes in the amount of white space.

```console
$ diff -b spaced.txt compact.txt
[No output if files differ only in spacing]
```

### **-w, --ignore-all-space**

Ignore all white space when comparing lines.

```console
$ diff -w file1.txt file2.txt
[No output if files differ only in whitespace]
```

### **-r, --recursive**

Recursively compare any subdirectories found.

```console
$ diff -r dir1 dir2
Only in dir1: unique_file1.txt
Only in dir2: unique_file2.txt
diff -r dir1/common.txt dir2/common.txt
1c1
< Original content
---
> Modified content
```

### **-q, --brief**

Report only whether files differ, not the details of the differences.

```console
$ diff -q file1.txt file2.txt
Files file1.txt and file2.txt differ
```

## Usage Examples

### Basic File Comparison

```console
$ diff file1.txt file2.txt
2c2
< It has some content.
---
> It has some modified content.
3a4
> A new line was added.
```

### Creating a Patch File

```console
$ diff -u original.txt modified.txt > changes.patch
$ patch original.txt < changes.patch
patching file original.txt
```

### Comparing Directories

```console
$ diff -r project_v1 project_v2
Only in project_v2: new_feature.py
diff -r project_v1/main.py project_v2/main.py
10c10,12
< print("Hello World")
---
> print("Hello World!")
> print("Version 2.0")
> print("Copyright 2025")
```

### Side-by-Side Comparison

```console
$ diff -y file1.txt file2.txt
This is a test file.                 This is a test file.
It has some content.               | It has some modified content.
The end of the file.                 The end of the file.
                                   > A new line was added.
```

## Tips

### Use Color for Better Readability

Many systems have `colordiff` installed, which adds color highlighting to diff output:

```console
$ colordiff -u file1.txt file2.txt
```

### Context Control

Control the amount of context shown with `-U NUM` or `--unified=NUM`:

```console
$ diff -U1 file1.txt file2.txt
```

### Ignore Version Control Files

When comparing directories, use `--exclude=PATTERN` to ignore certain files:

```console
$ diff -r --exclude=".git" dir1 dir2
```

### Use with Version Control

While version control systems have their own diff tools, you can use external diff:

```console
$ git diff --no-index --external-diff=diff -u file1.txt file2.txt
```

## Frequently Asked Questions

#### Q1. What do the symbols in diff output mean?
A. In normal output: `a` means add, `d` means delete, `c` means change. Lines with `<` are from the first file, `>` are from the second file, and `---` separates the changes.

#### Q2. How can I make diff output more readable?
A. Use the unified format (`-u`) or side-by-side format (`-y`). For colored output, use `colordiff` if available.

#### Q3. How do I create a patch file that can be applied later?
A. Use `diff -u original_file modified_file > patch_file.patch` and then apply it with `patch original_file < patch_file.patch`.

#### Q4. Can diff compare binary files?
A. By default, diff works with text files. For binary files, consider using `cmp` or specialized tools like `xxdiff` or `hexdump` combined with diff.

## References

https://www.gnu.org/software/diffutils/manual/html_node/diff.html

## Revisions

- 2025/05/04 First revision