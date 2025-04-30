# until command

Execute a command repeatedly until a condition is met.

## Overview

The `until` command is a shell construct that runs a command block repeatedly until a specified condition becomes true. It's essentially the opposite of a `while` loop - it continues execution as long as the test condition evaluates to false.

## Options

The `until` command doesn't have traditional command-line options as it's a shell construct rather than a standalone program.

## Usage Examples

### Basic Usage

```console
$ until [ $counter -ge 5 ]; do
>   echo "Counter: $counter"
>   ((counter++))
> done
Counter: 0
Counter: 1
Counter: 2
Counter: 3
Counter: 4
```

### Waiting for a File to Exist

```console
$ until [ -f /tmp/signal_file ]; do
>   echo "Waiting for signal file to appear..."
>   sleep 5
> done
> echo "Signal file found!"
Waiting for signal file to appear...
Waiting for signal file to appear...
Signal file found!
```

### Retrying a Command Until Success

```console
$ until ping -c 1 example.com > /dev/null; do
>   echo "Network not available, waiting..."
>   sleep 10
> done
> echo "Network is up!"
Network not available, waiting...
Network is up!
```

## Tips:

### Use Break to Exit Early

You can use the `break` statement to exit an `until` loop early if a certain condition is met:

```console
$ until [ -f /tmp/complete ]; do
>   if [ -f /tmp/abort ]; then
>     echo "Abort file found, exiting..."
>     break
>   fi
>   echo "Working..."
>   sleep 5
> done
```

### Combine with Timeout

For operations that might hang indefinitely, combine `until` with a timeout mechanism:

```console
$ timeout=60
$ start_time=$(date +%s)
$ until [ -f /tmp/ready ] || [ $(($(date +%s) - start_time)) -gt $timeout ]; do
>   echo "Waiting..."
>   sleep 5
> done
```

### Use Continue to Skip Iterations

The `continue` statement can be used to skip to the next iteration of the loop:

```console
$ counter=0
$ until [ $counter -ge 5 ]; do
>   ((counter++))
>   if [ $((counter % 2)) -eq 0 ]; then
>     continue
>   fi
>   echo "Odd number: $counter"
> done
Odd number: 1
Odd number: 3
Odd number: 5
```

## Frequently Asked Questions

#### Q1. What's the difference between `until` and `while`?
A. `until` executes a command block as long as the test condition is false, whereas `while` executes as long as the condition is true. `until [ condition ]` is equivalent to `while ! [ condition ]`.

#### Q2. Can I use multiple conditions in an `until` loop?
A. Yes, you can combine multiple conditions using logical operators like `&&` (AND) and `||` (OR) within the test brackets.

#### Q3. How do I prevent an infinite `until` loop?
A. Ensure that the condition will eventually become true, or include a `break` statement with a secondary exit condition. Always make sure the condition is properly updated within the loop.

#### Q4. Does `until` work in all shells?
A. `until` is available in most modern shells including bash, zsh, and ksh, but it might not be available in more minimal shells like dash or ash.

## References

https://www.gnu.org/software/bash/manual/html_node/Looping-Constructs.html

## Revisions

- 2025/04/30 First revision