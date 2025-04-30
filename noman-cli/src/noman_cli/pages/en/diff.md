# diff command

Compare files line by line.

## Overview

The `diff` command identifies differences between two files or directories. It analyzes the content line by line and outputs the changes needed to transform the first file into the second. This tool is essential for comparing versions of text files, checking changes in code, and creating patches.

## Options

### **-u (unified)**

Shows differences in a unified format with context, making changes easier to understand.

```console
$ diff -u file1.txt file2.txt
--- file1.txt	2025-04-30 10:00:00.000000000 -0700
+++ file2.txt	2025-04-30 10:30:00.000000000 -0700
@@ -1,3 +1,4 @@
 This is a test file.
-It has some content.
+It has some modified content.
 The end of the file.
+A new line added.
```

### **-i (ignore case)**

Ignores differences in case when comparing files.

```console
$ diff -i uppercase.txt lowercase.txt
[No output if files differ only in case]
```

### **-w (ignore whitespace)**

Ignores all whitespace differences between files.

```console
$ diff -w spaced.txt tabbed.txt
[No output if files differ only in whitespace]
```

### **-r (recursive)**

Recursively compares directories and their contents.

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

### **-q (brief)**

Reports only whether files differ, not the details of differences.

```console
$ diff -q file1.txt file2.txt
Files file1.txt and file2.txt differ
```

## Usage Examples

### Comparing two text files

```console
$ diff file1.txt file2.txt
2c2
< It has some content.
---
> It has some modified content.
3a4
> A new line added.
```

### Creating a patch file

```console
$ diff -u original.c modified.c > changes.patch
$ patch original.c < changes.patch
patching file original.c
```

### Comparing directories with detailed output

```console
$ diff -r -u project_v1 project_v2
Only in project_v2: new_feature.py
diff -r -u project_v1/main.py project_v2/main.py
--- project_v1/main.py	2025-04-29 15:00:00.000000000 -0700
+++ project_v2/main.py	2025-04-30 09:30:00.000000000 -0700
@@ -10,6 +10,7 @@
 def main():
     initialize()
     process_data()
+    new_function()
     cleanup()
 
 if __name__ == "__main__":
```

## Tips

### Understanding diff output

The standard diff output format uses line numbers and commands:
- `a` (add): Lines in the second file not in the first
- `c` (change): Lines that are different between files
- `d` (delete): Lines in the first file not in the second

### Colored diff output

Use `diff --color` (on systems that support it) to see differences highlighted in color, making them easier to spot.

### Side-by-side comparison

Use `diff -y` or `diff --side-by-side` to display differences in a two-column format, which can be easier to read for some comparisons.

### Ignoring specific patterns

Use `diff -I 'pattern'` to ignore lines that match a specific pattern, useful for ignoring version numbers or timestamps.

## Frequently Asked Questions

#### Q1. How do I compare binary files?
A. Use `diff -a` to treat binary files as text, but for true binary comparison, consider using `cmp` instead.

#### Q2. How can I see just the different lines without the special symbols?
A. Use `diff -u` for unified format, which is more readable, or consider using enhanced tools like `colordiff` or `git diff`.

#### Q3. How do I ignore specific types of files when comparing directories?
A. You can't directly with `diff`, but you can use it with `find` or consider using `rsync --dry-run` for more filtering options.

#### Q4. What's the difference between `diff` and `cmp`?
A. `diff` compares files line by line and shows detailed differences, while `cmp` compares byte by byte and stops at the first difference.

## References

https://www.gnu.org/software/diffutils/manual/html_node/diff.html

## Revisions

- 2025/04/30 First revision