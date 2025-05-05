# cat command

Display the contents of files or concatenate files.

## Overview

The `cat` command reads files and outputs their contents to standard output. It's commonly used to display file contents, combine multiple files, or create new files. The name "cat" comes from "concatenate," reflecting its ability to join files together.

## Options

### **-n, --number**

Number all output lines, starting at 1.

```console
$ cat -n file.txt
     1  This is the first line
     2  This is the second line
     3  This is the third line
```

### **-b, --number-nonblank**

Number only non-empty output lines, starting at 1.

```console
$ cat -b file.txt
     1  This is the first line
     2  This is the second line

     3  This is the fourth line
```

### **-s, --squeeze-blank**

Suppress repeated empty output lines, showing only one blank line instead of multiple consecutive ones.

```console
$ cat -s file_with_blanks.txt
This is text.

This has only one blank line between paragraphs instead of multiple.
```

### **-A, --show-all**

Show all control characters and non-printing characters.

```console
$ cat -A file.txt
This is a line with a tab^I and a newline$
```

### **-E, --show-ends**

Display $ at the end of each line.

```console
$ cat -E file.txt
This is the first line$
This is the second line$
```

### **-T, --show-tabs**

Display TAB characters as ^I.

```console
$ cat -T file.txt
This is a line with a    ^Itab character.
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

### Creating a new file using redirection

```console
$ cat > newfile.txt
This is a new file.
I'm typing the contents directly.
[Ctrl+D to end input]
```

### Appending to an existing file

```console
$ cat >> existing.txt
This text will be added to the end of the file.
[Ctrl+D to end input]
```

## Tips

### View Files Without Modification

Unlike text editors, `cat` displays files exactly as they are, without any modifications. This makes it ideal for quickly checking file contents.

### Use Pipes for Processing

Combine `cat` with other commands using pipes: `cat file.txt | grep "search term"` to filter content.

### Avoid Using `cat` Unnecessarily

For large files, use `less` or `more` instead of `cat` to view contents page by page, as `cat` will dump the entire file to your terminal.

### Create Files with Heredocs

For creating files with multiple lines, use heredocs:
```console
$ cat << EOF > file.txt
Line 1
Line 2
EOF
```

## Frequently Asked Questions

#### Q1. What is the difference between `cat` and `less`?
A. `cat` displays the entire file at once, while `less` shows the file one screen at a time, allowing you to scroll through it.

#### Q2. How can I display line numbers with `cat`?
A. Use `cat -n filename` to display line numbers for all lines, or `cat -b filename` to number only non-blank lines.

#### Q3. Can `cat` display binary files?
A. Yes, but it's not recommended as it can produce unprintable characters that might affect your terminal. Use specialized tools like `hexdump` or `xxd` for binary files.

#### Q4. How do I combine multiple files with `cat`?
A. Simply list all files as arguments: `cat file1.txt file2.txt file3.txt`.

## References

https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html

## Revisions

- 2025/05/04 First revision