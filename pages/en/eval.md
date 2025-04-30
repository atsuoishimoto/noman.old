# eval command

Construct and execute commands from arguments, allowing dynamic command creation.

## Overview

The `eval` command takes its arguments, joins them into a single string, and executes that string as a shell command. It's useful for creating commands dynamically, executing commands stored in variables, or performing multiple levels of variable expansion.

## Options

`eval` doesn't have specific options of its own. It simply takes the arguments provided to it, concatenates them, and executes the resulting string as a shell command.

## Usage Examples

### Basic Variable Expansion

```console
$ variable="ls -l"
$ eval $variable
total 16
-rw-r--r--  1 user  staff  1024 Apr 29 15:30 document.txt
drwxr-xr-x  3 user  staff   96  Apr 28 14:22 projects
```

### Dynamic Command Construction

```console
$ command="find"
$ path="."
$ options="-name '*.txt'"
$ eval $command $path $options
./document.txt
./projects/notes.txt
./readme.txt
```

### Double Variable Expansion

```console
$ var1="var2"
$ var2="Hello, World!"
$ eval echo \$$var1
Hello, World!
```

### Creating and Using Aliases Dynamically

```console
$ alias_name="ll"
$ alias_value="ls -la"
$ eval alias $alias_name=\"$alias_value\"
$ ll
total 24
drwxr-xr-x  5 user  staff   160 Apr 30 10:15 .
drwxr-xr-x  3 user  staff    96 Apr 25 09:30 ..
-rw-r--r--  1 user  staff  1024 Apr 29 15:30 document.txt
drwxr-xr-x  3 user  staff    96 Apr 28 14:22 projects
-rw-r--r--  1 user  staff   256 Apr 27 11:45 readme.txt
```

## Tips

### Use Quotes Carefully

Always quote your variables when using them with `eval` to prevent word splitting and unexpected behavior:

```console
$ filename="my file.txt"
$ eval echo \"$filename\"
my file.txt
```

### Security Considerations

Be cautious with `eval` when processing user input, as it can execute arbitrary commands. Avoid using it with untrusted input to prevent command injection attacks.

### Debugging Complex Eval Commands

To debug complex `eval` commands without executing them, use `echo` first:

```console
$ echo eval $command $path $options
eval find . -name '*.txt'
```

## Frequently Asked Questions

#### Q1. When should I use `eval`?
A. Use `eval` when you need to construct commands dynamically, perform double variable expansion, or execute commands stored in variables.

#### Q2. What's the difference between `eval` and simply executing a command?
A. `eval` performs an additional round of variable expansion and word splitting before executing the command, allowing for more dynamic command construction.

#### Q3. Is `eval` dangerous to use?
A. It can be if used with untrusted input, as it will execute any command it's given. Always validate and sanitize input before using it with `eval`.

#### Q4. How can I safely use variables with `eval`?
A. Always quote your variables to prevent word splitting and unexpected behavior: `eval "$command"` rather than `eval $command`.

## References

https://pubs.opengroup.org/onlinepubs/9699919799/utilities/eval.html

## Revisions

- 2025/04/30 First revision