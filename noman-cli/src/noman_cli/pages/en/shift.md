# shift command

Shifts positional parameters in a shell script, removing the first parameter and moving all others down by one position.

## Overview

The `shift` command is used in shell scripts to manipulate positional parameters. It removes the first parameter (`$1`) and shifts all remaining parameters down by one position, so `$2` becomes `$1`, `$3` becomes `$2`, and so on. This is particularly useful when processing command-line arguments in a loop.

## Options

### **shift n**

Shifts parameters by 'n' positions instead of just one. If 'n' is not specified, it defaults to 1.

```console
$ shift 2  # Shifts parameters by 2 positions
```

## Usage Examples

### Basic Usage in a Script

```console
$ cat shift_example.sh
#!/bin/bash
echo "Initial parameters: $1 $2 $3"
shift
echo "After shift: $1 $2 $3"

$ ./shift_example.sh apple banana cherry
Initial parameters: apple banana cherry
After shift: banana cherry
```

### Processing Arguments in a Loop

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

### Using shift with a Number

```console
$ cat shift_multiple.sh
#!/bin/bash
echo "Initial parameters: $1 $2 $3 $4"
shift 2
echo "After shift 2: $1 $2 $3 $4"

$ ./shift_multiple.sh a b c d
Initial parameters: a b c d
After shift 2: c d
```

## Tips:

### Check Parameter Count Before Shifting

Always check that you have enough parameters before shifting, especially when using `shift n`. Use `$#` to get the current number of parameters.

```console
$ cat safe_shift.sh
#!/bin/bash
if [ $# -ge 2 ]; then
    shift 2
else
    echo "Not enough parameters to shift by 2"
fi
```

### Use with getopts

`shift` is commonly used after processing options with `getopts` to handle the remaining non-option arguments.

### Preserve Original Arguments

If you need to access the original arguments later, save them to variables or an array before shifting.

## Frequently Asked Questions

#### Q1. What happens if I shift more positions than there are parameters?
A. In Bash, this is not an error, but all parameters will be removed. In some other shells, it might produce an error.

#### Q2. Does shift affect the $0 parameter (script name)?
A. No, `shift` only affects positional parameters starting from `$1`. The `$0` parameter (which contains the script name) remains unchanged.

#### Q3. How can I tell how many parameters are left after shifting?
A. Use the `$#` special variable, which contains the number of positional parameters.

#### Q4. Can I "unshift" parameters (add them back)?
A. No, once parameters are shifted, they cannot be directly "unshifted". If you need to preserve them, save them to variables before shifting.

## References

https://www.gnu.org/software/bash/manual/html_node/Bourne-Shell-Builtins.html#index-shift

## Revisions

- 2025/04/30 First revision