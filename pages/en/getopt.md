# getopt command

Parse command-line options in shell scripts.

## Overview

`getopt` is a command-line utility that helps parse command-line arguments in shell scripts. It standardizes option handling by allowing scripts to easily process both short options (like `-a`) and long options (like `--all`), with or without arguments.

## Options

### **-o, --options**

Specifies the short options to be recognized. Each character in the string represents a valid option. A colon after an option means it requires an argument, and two colons mean the argument is optional.

```console
$ getopt -o a:bc -- -a value -b -c
 -a 'value' -b -c --
```

### **-l, --longoptions**

Specifies the long options to be recognized. Options are comma-separated, and a colon after an option means it requires an argument.

```console
$ getopt -o a:bc -l alpha:,beta,gamma -- --alpha=value --beta
 --alpha 'value' --beta --
```

### **-n, --name**

Sets the name used in error messages. Useful for making error messages more user-friendly.

```console
$ getopt -n "myscript" -o a:bc -- -d
myscript: invalid option -- 'd'
```

### **-q, --quiet**

Suppresses error messages. The script must check the exit status to detect errors.

```console
$ getopt -q -o a:bc -- -d
```

### **-u, --unquoted**

Disables quoting of output, which can be useful in some contexts but may cause problems with arguments containing spaces.

```console
$ getopt -u -o a: -- -a "hello world"
 -a hello world --
```

## Usage Examples

### Basic Option Parsing in a Shell Script

```console
$ cat myscript.sh
#!/bin/bash
OPTS=$(getopt -o ab:c:: -l alpha,beta:,gamma:: -n 'myscript' -- "$@")
eval set -- "$OPTS"

while true; do
  case "$1" in
    -a | --alpha) echo "Option alpha"; shift ;;
    -b | --beta) echo "Option beta with value $2"; shift 2 ;;
    -c | --gamma) 
      case "$2" in
        "") echo "Option gamma with no value"; shift 2 ;;
        *) echo "Option gamma with value $2"; shift 2 ;;
      esac ;;
    --) shift; break ;;
    *) echo "Internal error!"; exit 1 ;;
  esac
done

echo "Remaining arguments: $@"
```

### Handling Required Arguments

```console
$ cat required-args.sh
#!/bin/bash
OPTS=$(getopt -o f:o: -l file:,output: -n 'required-args' -- "$@")
if [ $? -ne 0 ]; then exit 1; fi
eval set -- "$OPTS"

FILE=""
OUTPUT=""

while true; do
  case "$1" in
    -f | --file) FILE="$2"; shift 2 ;;
    -o | --output) OUTPUT="$2"; shift 2 ;;
    --) shift; break ;;
    *) echo "Internal error!"; exit 1 ;;
  esac
done

if [ -z "$FILE" ]; then
  echo "Error: --file option is required"
  exit 1
fi

echo "Processing file: $FILE"
echo "Output: ${OUTPUT:-standard output}"
```

## Tips

### Use Enhanced getopt

The enhanced version of getopt (found on most Linux systems) supports long options and better error handling. The traditional version (found on some Unix systems) is more limited.

### Always Check Return Status

Always check the return status of getopt to handle invalid options gracefully:

```bash
OPTS=$(getopt -o ab:c -n 'myscript' -- "$@")
if [ $? -ne 0 ]; then
  echo "Failed to parse options"
  exit 1
fi
```

### Properly Quote Variables

When using eval with getopt output, always quote the variables to handle spaces and special characters correctly:

```bash
eval set -- "$OPTS"
```

### Use -- to Separate Options from Arguments

Always include `--` in your getopt command to properly separate options from non-option arguments.

## Frequently Asked Questions

#### Q1. What's the difference between getopt and getopts?
A. `getopt` is an external command that supports both short and long options, while `getopts` is a shell builtin that only supports short options but is more portable.

#### Q2. How do I handle options with optional arguments?
A. Use double colons for short options (`a::`) and double colons for long options (`alpha::`). The argument must be attached to the option with an equals sign for long options.

#### Q3. Why does my getopt not support long options?
A. You might be using the traditional version of getopt. Check if your system has an enhanced version or consider using the getopts builtin instead.

#### Q4. How do I handle non-option arguments?
A. After processing all options with getopt, the remaining arguments will be available as positional parameters after the `--` separator.

## References

https://www.gnu.org/software/libc/manual/html_node/Getopt.html

## Revisions

- 2025/04/30 First revision