# echo command

Display a line of text or variables to standard output.

## Overview

The `echo` command prints text or variable values to the terminal. It's commonly used in shell scripts to display messages, show variable contents, or generate output that can be piped to other commands. Echo is one of the most fundamental Unix commands for text output.

## Options

### **-n**

Suppresses the trailing newline that echo normally adds to output.

```console
$ echo -n "Hello"
Hello$
```

### **-e**

Enables interpretation of backslash escape sequences.

```console
$ echo -e "Hello\nWorld"
Hello
World
```

### **--help**

Display help information and exit.

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

### Displaying variable values

```console
$ name="John"
$ echo "My name is $name"
My name is John
```

### Using escape sequences with -e

```console
$ echo -e "Tab:\t| Newline:\n| Backslash:\\"
Tab:	| Newline:
| Backslash:\
```

### Suppressing newline with -n

```console
$ echo -n "Enter your name: "
Enter your name: $
```

### Redirecting output to a file

```console
$ echo "This is a test" > test.txt
$ cat test.txt
This is a test
```

## Tips

### Quoting Matters

Single quotes (`'`) prevent variable expansion and escape sequence interpretation, while double quotes (`"`) allow them:

```console
$ name="John"
$ echo "Hello $name"
Hello John
$ echo 'Hello $name'
Hello $name
```

### Combining with Command Substitution

Use echo with command substitution to format command output:

```console
$ echo "Current date: $(date)"
Current date: Tue May 4 10:15:30 EDT 2025
```

### Escape Sequences with -e

Common escape sequences include:
- `\n` - newline
- `\t` - tab
- `\b` - backspace
- `\\` - backslash
- `\a` - alert (bell)

## Frequently Asked Questions

#### Q1. What's the difference between echo and printf?
A. `echo` is simpler but less powerful than `printf`. While `echo` is good for basic output, `printf` offers more formatting control similar to C's printf function.

#### Q2. How do I echo without a newline?
A. Use the `-n` option: `echo -n "text"`.

#### Q3. How can I display special characters like tabs or newlines?
A. Use the `-e` option with escape sequences: `echo -e "Line1\nLine2\tTabbed"`.

#### Q4. Why doesn't echo -e work in some shells?
A. Some shell implementations (like some versions of dash) don't support the `-e` option by default. In those cases, use `printf` instead.

## References

https://www.gnu.org/software/coreutils/manual/html_node/echo-invocation.html

## Revisions

- 2025/05/04 First revision