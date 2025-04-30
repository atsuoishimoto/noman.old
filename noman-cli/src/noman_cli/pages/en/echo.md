# echo command

Display a line of text or variables to the standard output.

## Overview

The `echo` command prints text or variable values to the terminal. It's commonly used in shell scripts to display messages, show variable contents, or generate output that can be piped to other commands.

## Options

### **-n**

Suppresses the trailing newline that `echo` normally adds to output.

```console
$ echo -n "Hello"
Hello$
```

### **-e**

Enables interpretation of backslash escape sequences like `\n` for newline and `\t` for tab.

```console
$ echo -e "Hello\nWorld"
Hello
World
```

### **--help**

Displays help information about the echo command.

```console
$ echo --help
Usage: echo [SHORT-OPTION]... [STRING]...
  or:  echo LONG-OPTION
Echo the STRING(s) to standard output.

  -n             do not output the trailing newline
  -e             enable interpretation of backslash escapes
  -E             disable interpretation of backslash escapes (default)
      --help     display this help and exit
      --version  output version information and exit
```

## Usage Examples

### Displaying text

```console
$ echo Hello World
Hello World
```

### Displaying variable contents

```console
$ name="John"
$ echo "My name is $name"
My name is John
```

### Using escape sequences

```console
$ echo -e "Tab:\t1\t2\t3\nNewline"
Tab:	1	2	3
Newline
```

### Redirecting output to a file

```console
$ echo "This is a test" > test.txt
$ cat test.txt
This is a test
```

## Tips

### Quoting Differences

Single quotes (`'`) prevent variable expansion and escape sequence interpretation, while double quotes (`"`) allow them.

```console
$ name="John"
$ echo "Hello $name"
Hello John
$ echo 'Hello $name'
Hello $name
```

### Combining with Command Substitution

Use `echo` with command substitution to display command results:

```console
$ echo "Today's date is $(date)"
Today's date is Wed Apr 30 10:15:23 PDT 2025
```

### Multiline Output

Create multiline output with escape sequences:

```console
$ echo -e "Line 1\nLine 2\nLine 3"
Line 1
Line 2
Line 3
```

## Frequently Asked Questions

#### Q1. What's the difference between echo and printf?
A. `echo` is simpler but less powerful than `printf`. `printf` offers more formatting options and better control over output formatting.

#### Q2. How do I echo without a newline?
A. Use the `-n` option: `echo -n "text"`.

#### Q3. How can I display special characters like tabs or newlines?
A. Use the `-e` option with escape sequences: `echo -e "Tab:\t Newline:\n"`.

#### Q4. Why doesn't echo -e work in some shells?
A. Some shell implementations (like some versions of `sh`) don't support the `-e` option. In those cases, use `printf` instead.

## References

https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html

## Revisions

- 2025/04/30 First revision