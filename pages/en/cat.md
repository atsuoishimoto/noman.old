# cat command

Display the contents of files or concatenate files.

## Overview

The `cat` command reads files and outputs their contents to the standard output. It's commonly used to display file contents, combine multiple files, or create new files. The name "cat" comes from "concatenate," which is its original purpose.

## Options

### **-n, --number**

Numbers all output lines, starting with 1.

```console
$ cat -n file.txt
     1  This is the first line.
     2  This is the second line.
     3  This is the third line.
```

### **-b, --number-nonblank**

Numbers only non-empty lines, starting with 1.

```console
$ cat -b file.txt
     1  This is the first line.
     2  This is the second line.

     3  This is the fourth line.
```

### **-s, --squeeze-blank**

Suppresses repeated empty output lines, showing only one blank line instead of multiple consecutive ones.

```console
$ cat -s file_with_blanks.txt
This is text.

This has only one blank line between paragraphs instead of multiple.
```

### **-A, --show-all**

Shows all non-printing characters (equivalent to -vET).

```console
$ cat -A file.txt
This is a line with a tab^I and a newline$
```

## Usage Examples

### Displaying file contents

```console
$ cat document.txt
This is the content of document.txt.
It has multiple lines.
```

### Concatenating multiple files

```console
$ cat file1.txt file2.txt
Contents of file1.txt
Contents of file2.txt
```

### Creating a new file with content

```console
$ cat > newfile.txt
Type your content here.
Press Ctrl+D when finished.
```

### Appending to an existing file

```console
$ cat >> existing.txt
This text will be added to the end of the file.
Press Ctrl+D when finished.
```

## Tips

### Use Less for Large Files

For large files, pipe `cat` to `less` to view content page by page: `cat largefile.txt | less` or simply use `less largefile.txt`.

### Combine with Grep

Pipe `cat` to `grep` to search for specific patterns: `cat file.txt | grep "search term"`.

### Avoid Unnecessary Use

Avoid using `cat` when unnecessary. For example, instead of `cat file.txt | grep pattern`, use `grep pattern file.txt` directly.

### Create Files with Heredocs

Create files with multi-line content using heredocs:
```console
$ cat > file.txt << EOF
Line 1
Line 2
EOF
```

## Frequently Asked Questions

#### Q1. What does "cat" stand for?
A. "Cat" stands for "concatenate," which reflects its primary function of joining files together.

#### Q2. How do I view file contents without line numbers?
A. Simply use `cat filename` without any options.

#### Q3. How can I see non-printable characters in a file?
A. Use `cat -A filename` or `cat -v filename` to display non-printable characters.

#### Q4. Can cat create empty files?
A. Yes, use `cat > filename` and immediately press Ctrl+D to create an empty file.

#### Q5. How do I append the contents of one file to another?
A. Use `cat file1 >> file2` to append the contents of file1 to file2.

## References

https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html

## Revisions

- 2025/04/30 First revision