# script command

Makes a typescript of a terminal session, recording all terminal activity.

## Overview

The `script` command creates a record of everything displayed in your terminal during a session. It captures all input and output, saving it to a file (by default named "typescript"). This is useful for documenting procedures, creating tutorials, or keeping logs of terminal sessions.

## Options

### **-a, --append**

Append the output to the specified file or to typescript, rather than overwriting it.

```console
$ script -a session_log.txt
Script started, output file is session_log.txt
$ ls
Documents Downloads Pictures
$ exit
Script done, output file is session_log.txt
```

### **-f, --flush**

Flush output after each write to ensure real-time recording, useful when monitoring the typescript file while recording.

```console
$ script -f realtime_log.txt
Script started, output file is realtime_log.txt
$ echo "This will be flushed immediately"
This will be flushed immediately
$ exit
Script done, output file is realtime_log.txt
```

### **-q, --quiet**

Runs in quiet mode, suppressing the start and done messages.

```console
$ script -q quiet_log.txt
$ echo "No start message was displayed"
No start message was displayed
$ exit
```

### **-t, --timing[=FILE]**

Output timing data to FILE or to standard error if FILE is not specified. This can be used with scriptreplay to replay the session.

```console
$ script -t timing.log session.log
Script started, output file is session.log
$ echo "This session is being timed"
This session is being timed
$ exit
Script done, output file is session.log
```

### **-c, --command COMMAND**

Run the specified command instead of an interactive shell.

```console
$ script -c "ls -la" command_output.txt
Script started, output file is command_output.txt
total 32
drwxr-xr-x  5 user  staff   160 May  4 10:15 .
drwxr-xr-x  3 user  staff    96 May  4 10:10 ..
-rw-r--r--  1 user  staff  1024 May  4 10:12 file1.txt
-rw-r--r--  1 user  staff  2048 May  4 10:14 file2.txt
Script done, output file is command_output.txt
```

## Usage Examples

### Basic Session Recording

```console
$ script my_session.txt
Script started, output file is my_session.txt
$ ls
Documents Downloads Pictures
$ pwd
/home/user
$ exit
Script done, output file is my_session.txt
```

### Viewing the Recorded Session

```console
$ cat my_session.txt
Script started on Sun May  4 10:20:00 2025
$ ls
Documents Downloads Pictures
$ pwd
/home/user
$ exit

Script done on Sun May  4 10:21:30 2025
```

### Recording and Replaying a Session

```console
$ script --timing=timing.log session.log
Script started, output file is session.log
$ echo "Hello, this is a demo"
Hello, this is a demo
$ ls
Documents Downloads Pictures
$ exit
Script done, output file is session.log

$ scriptreplay timing.log session.log
# The session will be replayed with the original timing
```

## Tips

### Use with scriptreplay

When using the `-t` option to record timing information, you can later replay the session with the `scriptreplay` command, which will show the output at the same pace as it was originally typed.

### Cleaning Up Control Characters

The typescript file may contain control characters that make it difficult to read. You can use tools like `col -b` to clean it up:

```console
$ col -b < my_session.txt > clean_session.txt
```

### Documenting Complex Procedures

Use `script` when documenting complex system administration tasks or software installations to create a complete record that can be referenced later or shared with colleagues.

## Frequently Asked Questions

#### Q1. How do I stop recording a script session?
A. Type `exit` or press Ctrl+D to end the session and stop recording.

#### Q2. Can I record a session without showing the start and end messages?
A. Yes, use the `-q` or `--quiet` option to suppress these messages.

#### Q3. How can I replay a recorded session?
A. If you recorded with timing information using `-t`, you can replay the session using the `scriptreplay` command.

#### Q4. Does script record passwords I type?
A. No, properly designed password prompts don't echo characters to the terminal, so passwords typically won't appear in the typescript file.

#### Q5. Can I append to an existing typescript file?
A. Yes, use the `-a` or `--append` option to add to an existing file rather than overwriting it.

## References

https://man7.org/linux/man-pages/man1/script.1.html

## Revisions

- 2025/05/04 First revision