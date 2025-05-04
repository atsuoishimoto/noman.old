# until command

Execute a command repeatedly until a condition is met.

## Overview

The `until` command is a shell construct that runs a set of commands in a loop until a specified condition becomes true. Unlike the `while` loop which continues as long as a condition is true, `until` continues as long as a condition is false. It's useful for waiting for a specific event or repeating tasks until a certain state is achieved.

## Options

The `until` command doesn't have traditional command-line options as it's a shell built-in construct rather than a standalone program. Instead, it follows a specific syntax:

```bash
until test-command
do
  commands
done
```

Where:
- `test-command` is evaluated before each iteration
- `commands` are executed as long as `test-command` returns a non-zero exit status (false)
- The loop terminates when `test-command` returns a zero exit status (true)

## Usage Examples

### Basic Usage

```console
$ count=1
$ until [ $count -gt 5 ]
> do
>   echo "Count is $count"
>   ((count++))
> done
Count is 1
Count is 2
Count is 3
Count is 4
Count is 5
```

### Waiting for a File to Exist

```console
$ until [ -f /tmp/ready.txt ]
> do
>   echo "Waiting for file to appear..."
>   sleep 5
> done
> echo "File exists, continuing!"
Waiting for file to appear...
Waiting for file to appear...
File exists, continuing!
```

### Retrying a Command Until Success

```console
$ until ping -c 1 example.com > /dev/null
> do
>   echo "Server not responding, retrying in 5 seconds..."
>   sleep 5
> done
> echo "Server is up!"
Server not responding, retrying in 5 seconds...
Server is up!
```

## Tips:

### Use Break to Exit Early

You can use the `break` statement to exit an `until` loop early if a certain condition is met:

```bash
until [ condition1 ]
do
  if [ condition2 ]; then
    break
  fi
  commands
done
```

### Combine with Sleep for Polling

When waiting for a condition to become true, combine `until` with `sleep` to avoid excessive CPU usage:

```bash
until command_to_check
do
  sleep 5  # Wait 5 seconds between checks
done
```

### Infinite Loops with Caution

Be careful when creating loops that might never terminate. Consider adding a timeout or maximum iteration count:

```bash
count=0
max_tries=100
until [ condition ] || [ $count -ge $max_tries ]
do
  commands
  ((count++))
done
```

## Frequently Asked Questions

#### Q1. What's the difference between `until` and `while`?
A. `until` continues executing commands as long as the test condition is false, whereas `while` continues as long as the condition is true. In other words, `until [ condition ]` is equivalent to `while ! [ condition ]`.

#### Q2. Can I use multiple conditions with `until`?
A. Yes, you can combine multiple conditions using logical operators like `&&` (AND) and `||` (OR) within the test command.

#### Q3. How do I debug an `until` loop that isn't working as expected?
A. Add `set -x` before the loop to enable shell debugging, which will show each command as it's executed. Use `set +x` after the loop to turn debugging off.

#### Q4. Can I use `until` in all shells?
A. `until` is available in most modern shells including bash, zsh, and ksh, but might not be available in more minimal shells like dash or ash.

## References

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## Revisions

- 2025/05/04 First revision