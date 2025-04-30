# diff3 command

Compare three files line by line and show differences between them.

## Overview

`diff3` is a text comparison utility that analyzes three files and identifies the differences between them. It's particularly useful for comparing an original file with two different modified versions, making it valuable for resolving merge conflicts in version control systems or for comparing different revisions of a document.

## Options

### **-A, --show-all**

Output all changes, including conflicts, in a unified format that's easier to read

```console
$ diff3 -A file1 file2 file3
<<<<<<< file1
This is in file1
||||||| file2
This is in file2
======= file3
This is in file3
>>>>>>> file3
```

### **-m, --merge**

Produce output in a merge format suitable for further editing

```console
$ diff3 -m file1 file2 file3
<<<<<<< file1
Content from file1
||||||| file2
Content from file2
======= file3
Content from file3
>>>>>>> file3
```

### **-e, --ed**

Create an ed script that can be used to incorporate changes from file1 to file3 into file2

```console
$ diff3 -e file1 file2 file3
w
q
```

### **-x, --overlap-only**

Show only the overlapping changes (conflicts)

```console
$ diff3 -x file1 file2 file3
====
1:1c
This is file1
2:1c
This is file2
3:1c
This is file3
====
```

## Usage Examples

### Basic Comparison

```console
$ diff3 original.txt yours.txt theirs.txt
====
1:1c
This is the original file
2:1c
This is your modified version
3:1c
This is their modified version
====
```

### Creating a Merged File

```console
$ diff3 -m original.txt yours.txt theirs.txt > merged.txt
$ cat merged.txt
<<<<<<< original.txt
This is the original file
||||||| yours.txt
This is your modified version
======= theirs.txt
This is their modified version
>>>>>>> theirs.txt
```

## Tips

### Understanding the Output Format

The default output format shows line numbers and content from each file. The numbers before the colon indicate which file (1, 2, or 3) the content comes from, and the letter after the colon indicates the type of change (a for add, c for change, d for delete).

### Using diff3 for Version Control

When resolving merge conflicts in Git or other version control systems, understanding diff3 output can help you better interpret what changes were made by different parties.

### Automating Merges

Use the `-m` option to create a merged file that you can then edit manually to resolve conflicts. This is often more efficient than trying to merge files by hand.

## Frequently Asked Questions

#### Q1. What's the difference between diff and diff3?
A. `diff` compares two files, while `diff3` compares three files, making it useful for comparing an original file with two different modified versions.

#### Q2. How do I interpret the output of diff3?
A. The output shows sections where the files differ, with line numbers and content from each file. The numbers (1:, 2:, 3:) indicate which file the content comes from.

#### Q3. Can diff3 automatically resolve conflicts?
A. No, diff3 can identify conflicts but cannot automatically resolve them. It can produce a merged file with conflict markers that you must resolve manually.

#### Q4. How do I save the output to a file?
A. Use output redirection: `diff3 file1 file2 file3 > output.txt` or use the `-m` option to create a merged file.

## References

https://www.gnu.org/software/diffutils/manual/html_node/Invoking-diff3.html

## Revisions

- 2025/04/30 First revision