# diff3 command

Compare three files line by line and show differences.

## Overview

`diff3` is a utility that compares three files and identifies the differences between them. It's particularly useful when merging changes from multiple versions of a file, such as in version control systems. The command shows which lines are unique to each file and which are common across files.

## Options

### **-A, --show-all**

Output all changes, bracketing conflicts between files.

```console
$ diff3 -A file1 file2 file3
<<<<<<< file1
This is in file1
||||||| file2
This is in file2
======= 
This is in file3
>>>>>>> file3
```

### **-e, --ed**

Create an ed script that incorporates all changes from file1 to file3 into file2.

```console
$ diff3 -e file1 file2 file3
w
q
```

### **-m, --merge**

Output the merged file directly instead of an ed script.

```console
$ diff3 -m file1 file2 file3
Common text
<<<<<<< file1
Text from file1
||||||| file2
Text from file2
=======
Text from file3
>>>>>>> file3
More common text
```

### **-T, --initial-tab**

Make tabs line up by prefixing a tab to output lines.

```console
$ diff3 -T file1 file2 file3
	====1
	line from file1
	====2
	line from file2
	====3
	line from file3
```

### **-x, --overlap-only**

Show only overlapping changes.

```console
$ diff3 -x file1 file2 file3
====
1:1c
line in file1
2:1c
line in file2
3:1c
line in file3
```

## Usage Examples

### Basic Comparison

```console
$ diff3 file1 file2 file3
====
1:1c
This is file1
2:1c
This is file2
3:1c
This is file3
```

### Creating a Merged File

```console
$ diff3 -m file1 file2 file3 > merged_file
$ cat merged_file
Common text
<<<<<<< file1
Text from file1
||||||| file2
Text from file2
=======
Text from file3
>>>>>>> file3
More common text
```

### Resolving Conflicts Automatically

```console
$ diff3 --merge --easy-only file1 file2 file3 > merged_file
```

## Tips

### Understanding the Output Format

In standard output, `diff3` uses `====` to mark the beginning of a difference block, followed by line numbers and change types. For example, `1:1c` means line 1 in file1 is changed.

### Merging Files Effectively

When using `-m` (merge), conflicts are marked with `<<<<<<<`, `|||||||`, `=======`, and `>>>>>>>`. You'll need to manually edit these sections to resolve conflicts.

### Automating Conflict Resolution

Use `--easy-only` with `--merge` to automatically incorporate non-conflicting changes, leaving only true conflicts for manual resolution.

### Working with Version Control

`diff3` is often used behind the scenes in version control systems like Git when resolving merge conflicts between branches.

## Frequently Asked Questions

#### Q1. What's the difference between `diff` and `diff3`?
A. `diff` compares two files, while `diff3` compares three files, making it useful for merging changes from multiple sources.

#### Q2. How do I interpret the output of `diff3`?
A. The output shows line numbers and content from each file. Lines marked with `====` indicate differences, followed by line numbers and content from each file.

#### Q3. Can `diff3` automatically resolve conflicts?
A. Partially. Using `--merge --easy-only` will automatically resolve non-conflicting changes, but you'll still need to manually resolve true conflicts.

#### Q4. How do I save the merged output to a file?
A. Use redirection: `diff3 -m file1 file2 file3 > merged_file`

## References

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-diff3.html

## Revisions

- 2025/05/04 First revision