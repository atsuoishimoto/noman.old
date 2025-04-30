# sed command

Stream editor for filtering and transforming text.

## Overview

`sed` (stream editor) is a powerful utility that parses and transforms text, line by line. It reads input from files or standard input, applies specified operations, and outputs the result. Unlike interactive text editors, `sed` works with a scripted set of editing commands, making it ideal for automated text processing in scripts and pipelines.

## Options

### **-e script**

Adds commands to the set of commands to be executed. Useful when specifying multiple editing commands.

```console
$ echo "Hello World" | sed -e 's/Hello/Hi/' -e 's/World/there/'
Hi there
```

### **-i[suffix]**

Edits files in-place, optionally creating a backup with the specified suffix.

```console
$ sed -i.bak 's/old/new/g' file.txt
```

### **-n**

Suppresses automatic printing of pattern space. Used with commands like `p` to control output.

```console
$ echo -e "Line 1\nLine 2\nLine 3" | sed -n '2p'
Line 2
```

### **-r, -E**

Uses extended regular expressions, which are more powerful and readable.

```console
$ echo "123 abc" | sed -E 's/[0-9]+/NUMBER/'
NUMBER abc
```

## Common Commands

### **s/pattern/replacement/flags**

Substitutes text matching a pattern with replacement text.

```console
$ echo "The quick brown fox" | sed 's/brown/red/'
The quick red fox
```

### **d**

Deletes lines matching the address or pattern.

```console
$ echo -e "Line 1\nLine 2\nLine 3" | sed '2d'
Line 1
Line 3
```

### **p**

Prints lines matching the address or pattern (usually used with -n).

```console
$ echo -e "Line 1\nLine 2\nLine 3" | sed -n '/2/p'
Line 2
```

### **a\, i\, c\**

Appends, inserts, or changes lines.

```console
$ echo "Hello" | sed 'a\World'
Hello
World
```

## Usage Examples

### Basic Substitution

```console
$ echo "The cat sat on the mat" | sed 's/cat/dog/'
The dog sat on the mat
```

### Global Substitution

```console
$ echo "The cat sat on the cat mat" | sed 's/cat/dog/g'
The dog sat on the dog mat
```

### Working with Line Numbers

```console
$ cat file.txt
Line 1
Line 2
Line 3
Line 4
$ sed '2,4d' file.txt
Line 1
```

### Multiple Operations

```console
$ echo "Hello World" | sed -e 's/Hello/Hi/' -e 's/World/Universe/'
Hi Universe
```

## Tips

### Use Delimiters Other Than '/'

When working with paths or URLs that contain slashes, use a different delimiter:

```console
$ echo "/usr/local/bin" | sed 's:/usr:/opt:g'
/opt/local/bin
```

### Create Backup Before Editing

Always use the `-i` option with a suffix to create backups before making in-place edits:

```console
$ sed -i.bak 's/old/new/g' important_file.txt
```

### Use Extended Regular Expressions

The `-E` option makes complex patterns more readable:

```console
$ echo "abc123def" | sed -E 's/[a-z]+([0-9]+)[a-z]+/\1/'
123
```

### Combine Multiple Commands

Use semicolons or the `-e` option to apply multiple transformations:

```console
$ echo "Hello World" | sed 's/Hello/Hi/; s/World/there/'
Hi there
```

## Frequently Asked Questions

#### Q1. How do I replace text in a file permanently?
A. Use the `-i` option: `sed -i 's/old/new/g' file.txt`. Add a suffix like `-i.bak` to create a backup.

#### Q2. How can I delete specific lines from a file?
A. Use the `d` command with line numbers or patterns: `sed '3d' file.txt` deletes line 3, while `sed '/pattern/d' file.txt` deletes lines containing "pattern".

#### Q3. How do I print only certain lines?
A. Use `-n` with the `p` command: `sed -n '2,4p' file.txt` prints only lines 2 through 4.

#### Q4. What's the difference between `sed` and `grep`?
A. `grep` is for searching and filtering text, while `sed` is for editing and transforming text. `sed` can do everything `grep` does and more.

#### Q5. How do I escape special characters in `sed`?
A. Use backslashes to escape special characters: `sed 's/file\.txt/doc\.txt/'` or use different delimiters.

## macOS Considerations

On macOS, the default `sed` is based on BSD rather than GNU. Key differences include:

- The `-i` option requires an extension even if you don't want backups (use `-i ''`)
- Some GNU extensions may not be available
- Consider installing GNU sed via Homebrew (`brew install gnu-sed`) for full compatibility with Linux examples

## References

https://www.gnu.org/software/sed/manual/sed.html

## Revisions

- 2025/04/30 First revision