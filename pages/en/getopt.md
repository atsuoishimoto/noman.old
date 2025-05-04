# getopt command

Parse command-line options in a standardized way.

## Overview

`getopt` is a command-line utility that parses command-line arguments according to a specified format, making it easier to handle options in shell scripts. It helps standardize option processing by rearranging the arguments into a canonical form that is easier for scripts to process.

## Options

### **-a, --alternative**

Enable alternative parsing mode (allows long options to start with a single dash)

```console
$ getopt -a -o a:b -l alpha:,beta -- -alpha foo -b
 -a 'foo' -b --
```

### **-l, --longoptions**

Define the long options to be recognized

```console
$ getopt -l help,version,output: -- --help --output=file.txt
 --help --output 'file.txt' --
```

### **-n, --name**

Set the name used for error messages

```console
$ getopt -n myscript -o a:b -- -x
myscript: invalid option -- 'x'
```

### **-o, --options**

Define the short options to be recognized

```console
$ getopt -o a:bc -- -a value -bc
 -a 'value' -b -c --
```

### **-q, --quiet**

Suppress error messages

```console
$ getopt -q -o a:b -- -x
 --
```

### **-Q, --quiet-output**

Suppress normal output (useful when checking for valid options)

```console
$ getopt -Q -o a:b -- -a value
```

### **-s, --shell**

Set quoting conventions according to the specified shell (bash, sh, csh)

```console
$ getopt -s bash -o a: -- -a "file with spaces"
 -a 'file with spaces' --
```

### **-T, --test**

Test mode - output the parsed options but don't execute

```console
$ getopt -T -o a:b -- -a value -b
 -a 'value' -b --
```

### **-u, --unquoted**

Don't quote the output

```console
$ getopt -u -o a:b -- -a value
 -a value --
```

## Usage Examples

### Basic Option Parsing in a Shell Script

```console
$ cat myscript.sh
#!/bin/bash
OPTS=$(getopt -o a:bc -l alpha:,beta,charlie -- "$@")
eval set -- "$OPTS"
while true; do
  case "$1" in
    -a|--alpha) echo "Alpha option with value: $2"; shift 2 ;;
    -b|--beta) echo "Beta option enabled"; shift ;;
    -c|--charlie) echo "Charlie option enabled"; shift ;;
    --) shift; break ;;
    *) echo "Internal error!"; exit 1 ;;
  esac
done
echo "Remaining arguments: $@"

$ ./myscript.sh -a foo --beta arg1 arg2
Alpha option with value: foo
Beta option enabled
Remaining arguments: arg1 arg2
```

### Handling Options with Spaces in Values

```console
$ getopt -o d: -- -d "my directory"
 -d 'my directory' --
```

### Using Alternative Mode for Single-Dash Long Options

```console
$ getopt -a -o "" -l help,version -- -help -version
 --help --version --
```

## Tips:

### Always Check for Errors

Always check the return code of getopt to ensure options were valid before proceeding with your script.

```console
$ if ! OPTS=$(getopt -o a:b -n "$0" -- "$@"); then exit 1; fi
```

### Use eval set -- to Process the Output

The canonical way to use getopt in scripts is to capture its output and use `eval set --` to replace the script's arguments with the processed ones.

### Prefer Enhanced getopt Over Basic getopt

The enhanced getopt (from util-linux) supports long options and better error handling than the basic version found in some systems. Check which version you have with `getopt -V`.

### Handling Whitespace in Arguments

Always quote variables when passing them to getopt to handle whitespace correctly: `getopt ... -- "$@"` not `getopt ... -- $@`.

## Frequently Asked Questions

#### Q1. What's the difference between getopt and getopts?
A. `getopt` is an external command that supports both short and long options, while `getopts` is a shell builtin that only handles short options but is more portable across different Unix-like systems.

#### Q2. How do I specify an option that requires a value?
A. For short options, add a colon after the option letter in the option string (e.g., `a:` for `-a value`). For long options, add a colon after the option name (e.g., `alpha:` for `--alpha=value`).

#### Q3. How do I handle options with optional arguments?
A. The enhanced getopt supports optional arguments for long options by using two colons (e.g., `alpha::` for `--alpha[=value]`).

#### Q4. Why does my script fail with "getopt: unrecognized option"?
A. You might be using the basic version of getopt which doesn't support long options. Try using only short options or upgrade to the enhanced version.

## References

https://man7.org/linux/man-pages/man1/getopt.1.html

## Revisions

- 2025/05/04 First revision