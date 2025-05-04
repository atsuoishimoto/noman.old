# shift command

Shifts positional parameters in a shell script, removing the first parameter and moving all others down by one position.

## Overview

The `shift` command is a shell built-in that adjusts the positional parameters ($1, $2, etc.) in shell scripts. By default, it removes the first parameter ($1) and shifts all remaining parameters down by one position (making $2 become $1, $3 become $2, and so on). It's commonly used in scripts to process command-line arguments sequentially.

## Options

### **-n N** (Bash only)

Shifts the positional parameters N positions instead of just one.

```console
$ set -- a b c d e
$ echo $1 $2 $3
a b c
$ shift 2
$ echo $1 $2 $3
c d e
```

Note: The `shift` command has very few options, as its primary purpose is straightforward.

## Usage Examples

### Basic Usage in a Script

```console
$ cat shift_example.sh
#!/bin/bash
echo "Total arguments: $#"
echo "First argument: $1"
shift
echo "After shift, first argument: $1"
echo "Total arguments after shift: $#"

$ ./shift_example.sh apple banana cherry
Total arguments: 3
First argument: apple
After shift, first argument: banana
Total arguments after shift: 2
```

### Processing All Arguments in a Loop

```console
$ cat process_args.sh
#!/bin/bash
while [ $# -gt 0 ]; do
    echo "Processing: $1"
    shift
done

$ ./process_args.sh one two three
Processing: one
Processing: two
Processing: three
```

### Using shift with a Number (Bash)

```console
$ cat shift_multiple.sh
#!/bin/bash
echo "Original arguments: $@"
echo "Count: $#"
shift 2
echo "After shift 2: $@"
echo "Count: $#"

$ ./shift_multiple.sh a b c d e
Original arguments: a b c d e
Count: 5
After shift 2: c d e
Count: 3
```

## Tips

### Check Remaining Arguments

Always check if there are enough arguments left before shifting, especially when using `shift n`. If you try to shift more positions than there are arguments, some shells will produce an error.

```console
$ cat safe_shift.sh
#!/bin/bash
if [ $# -ge 2 ]; then
    shift 2
else
    echo "Not enough arguments to shift 2 positions"
fi
```

### Combine with getopts

When processing both options and arguments, use `getopts` for the options first, then use `shift` to process the remaining arguments.

### Remember $0 is Unchanged

The `shift` command only affects positional parameters ($1, $2, etc.). The script name ($0) remains unchanged.

## Frequently Asked Questions

#### Q1. What happens if I use shift when there are no arguments left?
A. In most shells, using `shift` when no arguments remain will not cause an error, but using `shift n` when fewer than n arguments remain may cause an error depending on the shell.

#### Q2. Does shift affect the $@ and $* variables?
A. Yes, both $@ and $* are updated to reflect the new set of positional parameters after the shift.

#### Q3. Can I use shift in interactive shell sessions?
A. Yes, but it's primarily useful in scripts. In an interactive session, you can use `set -- arg1 arg2` to set positional parameters first.

#### Q4. How do I know how many arguments are left after shifting?
A. Use the $# variable, which always contains the current number of positional parameters.

## References

The `shift` command is a shell built-in, documented in the Bash manual:
https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html#index-shift

## Revisions

- 2025/05/04 First revision