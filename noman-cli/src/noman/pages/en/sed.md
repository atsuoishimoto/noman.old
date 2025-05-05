# sed command

Stream editor for filtering and transforming text.

## Overview

`sed` (stream editor) is a powerful utility that parses and transforms text, line by line. It reads input from files or standard input, applies specified editing commands, and outputs the result to standard output. It's commonly used for search and replace operations, text extraction, and other text manipulations in shell scripts and command-line operations.

## Options

### **-e script, --expression=script**

Add commands in the script to the set of commands to be executed.

```console
$ echo "hello world" | sed -e 's/hello/goodbye/' -e 's/world/universe/'
goodbye universe
```

### **-f script-file, --file=script-file**

Add commands from script-file to the set of commands to be executed.

```console
$ cat script.sed
s/hello/goodbye/
s/world/universe/
$ echo "hello world" | sed -f script.sed
goodbye universe
```

### **-i[SUFFIX], --in-place[=SUFFIX]**

Edit files in place (makes backup if SUFFIX supplied).

```console
$ echo "hello world" > file.txt
$ sed -i 's/hello/goodbye/' file.txt
$ cat file.txt
goodbye world
```

### **-n, --quiet, --silent**

Suppress automatic printing of pattern space.

```console
$ echo -e "line 1\nline 2\nline 3" | sed -n '2p'
line 2
```

### **-r, --regexp-extended**

Use extended regular expressions in the script.

```console
$ echo "hello 123 world" | sed -r 's/[0-9]+/NUMBER/'
hello NUMBER world
```

## Usage Examples

### Basic Substitution

```console
$ echo "The quick brown fox" | sed 's/brown/red/'
The quick red fox
```

### Global Substitution

```console
$ echo "one two one three one" | sed 's/one/ONE/g'
ONE two ONE three ONE
```

### Print Specific Lines

```console
$ cat file.txt
Line 1
Line 2
Line 3
Line 4
$ sed -n '2,3p' file.txt
Line 2
Line 3
```

### Delete Lines

```console
$ cat file.txt
Line 1
Line 2
Line 3
Line 4
$ sed '2,3d' file.txt
Line 1
Line 4
```

### Multiple Editing Commands

```console
$ echo "hello world" | sed 's/hello/hi/; s/world/there/'
hi there
```

## Tips

### Use Delimiters Other Than '/'

When your pattern or replacement contains slashes, use a different delimiter to avoid escaping:

```console
$ echo "/usr/local/bin" | sed 's:/usr:~:'
~/local/bin
```

### Backup Files When Editing In-place

Always create backups when using `-i` for in-place editing:

```console
$ sed -i.bak 's/old/new/g' file.txt
```

### Address Ranges

Use line numbers, patterns, or ranges to target specific lines:
- `1,5` - lines 1 through 5
- `/start/,/end/` - lines from pattern "start" to pattern "end"
- `5,+2` - line 5 and the next 2 lines

### Append, Insert, and Change Lines

```console
$ echo -e "line 1\nline 2\nline 3" | sed '2a\new line after 2'
line 1
line 2
new line after 2
line 3
```

## Frequently Asked Questions

#### Q1. How do I replace text in a file permanently?
A. Use the `-i` option: `sed -i 's/old/new/g' filename`. Add a suffix like `-i.bak` to create a backup.

#### Q2. How can I print only lines matching a pattern?
A. Use `-n` with the `p` command: `sed -n '/pattern/p' filename`.

#### Q3. What's the difference between 's/pattern/replacement/' and 's/pattern/replacement/g'?
A. Without the `g` flag, only the first occurrence on each line is replaced. With `g`, all occurrences are replaced.

#### Q4. How do I delete lines matching a pattern?
A. Use the `d` command: `sed '/pattern/d' filename`.

#### Q5. How can I use variables in sed commands?
A. Use double quotes and escape special characters: `sed "s/$var/replacement/g" filename`.

## References

https://www.gnu.org/software/sed/manual/sed.html

## Revisions

- 2025/05/04 First revision