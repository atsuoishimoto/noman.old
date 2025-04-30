# script command

Make a typescript of a terminal session, capturing all input and output.

## Overview

The `script` command creates a record of everything that happens in your terminal session, saving both your commands and their outputs to a file. This is useful for documenting procedures, creating tutorials, or keeping logs of terminal activities.

## Options

### **-a, --append**

Append the output to the file instead of overwriting it.

```console
$ script -a session_log.txt
Script started, file is session_log.txt
$ echo "This will be appended to existing content"
This will be appended to existing content
$ exit
Script done, file is session_log.txt
```

### **-f, --flush**

Flush output after each write to ensure real-time recording, useful when monitoring the typescript file while recording.

```console
$ script -f realtime_log.txt
Script started, file is realtime_log.txt
$ echo "This output is flushed immediately"
This output is flushed immediately
$ exit
Script done, file is realtime_log.txt
```

### **-q, --quiet**

Run in quiet mode, suppressing the start and end messages.

```console
$ script -q quiet_log.txt
$ echo "Recording silently"
Recording silently
$ exit
```

### **-t, --timing=FILE**

Record timing data to FILE, allowing for playback with the `scriptreplay` command.

```console
$ script -t timing.log typescript.txt
Script started, file is typescript.txt
$ echo "This session can be replayed later"
This session can be replayed later
$ exit
Script done, file is typescript.txt
```

## Usage Examples

### Basic Usage

```console
$ script my_session.txt
Script started, file is my_session.txt
$ ls
Documents  Downloads  Pictures
$ echo "Hello, world!"
Hello, world!
$ exit
Script done, file is my_session.txt
```

### Replaying a Recorded Session

When used with timing data, you can replay the session:

```console
$ script -t timing.log typescript.txt
Script started, file is typescript.txt
$ echo "Commands for demonstration"
Commands for demonstration
$ ls -la
[output of ls -la command]
$ exit
Script done, file is typescript.txt

$ scriptreplay timing.log typescript.txt
[The session replays with original timing]
```

## Tips

### Automatic Session Documentation

Use `script` at the beginning of important system administration tasks to automatically document what you did, which can be invaluable for troubleshooting or creating documentation later.

### Sharing Terminal Sessions

When teaching others command line operations, record your session with `script` and share the typescript file so they can see exactly what commands you ran and their outputs.

### Cleaning Up Control Characters

The output file may contain terminal control characters. Use `cat -A` to view them or tools like `col -b` to remove them:

```console
$ col -b < typescript.txt > clean_typescript.txt
```

## Frequently Asked Questions

#### Q1. How do I stop recording a script session?
A. Type `exit` or press Ctrl+D to end the recording session.

#### Q2. Can I record a session without saving commands I type?
A. No, `script` records everything in the terminal, including both input and output.

#### Q3. How can I replay a recorded session?
A. If you recorded with the `-t` option, use the `scriptreplay` command with the timing and typescript files.

#### Q4. Does script record passwords I type?
A. Yes, `script` records everything visible in the terminal. However, most password prompts don't display the characters you type, so passwords typically won't appear in the typescript file.

## macOS Considerations

On macOS, the `script` command has slightly different options than the Linux version. The `-t` timing option works differently, and some options like `--flush` may not be available. Use `man script` on macOS to see the specific options available.

## References

https://man7.org/linux/man-pages/man1/script.1.html

## Revisions

- 2025/04/30 First revision