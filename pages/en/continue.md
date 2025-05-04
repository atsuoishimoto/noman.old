# continue command

Resume a suspended job by bringing it to the foreground or sending it to the background.

## Overview

The `continue` command is a shell built-in that resumes the execution of a job that has been suspended (typically with Ctrl+Z). It allows you to bring a suspended process back to either the foreground (where it can interact with the terminal) or the background (where it runs without requiring terminal input).

## Options

### **fg** - Foreground

Brings a suspended job to the foreground, allowing it to continue execution and interact with the terminal.

```console
$ fg [job_spec]
```

### **bg** - Background

Continues a suspended job in the background, allowing it to run without occupying the terminal.

```console
$ bg [job_spec]
```

## Usage Examples

### Resuming the most recently suspended job in the foreground

```console
$ fg
[1]+ Running     vim document.txt
```

### Resuming a specific job in the foreground

```console
$ fg %2
[2]+ Running     nano notes.txt
```

### Continuing a suspended job in the background

```console
$ bg
[1]+ Running     find / -name "*.log" &
```

### Continuing a specific job in the background

```console
$ bg %3
[3]+ Running     tar -czf archive.tar.gz directory/ &
```

## Tips:

### View All Jobs

Before using `continue` commands, you can view all suspended and background jobs with the `jobs` command to identify which job you want to resume.

```console
$ jobs
[1]  Stopped    vim document.txt
[2]- Running    find / -name "*.log" &
[3]+ Stopped    nano notes.txt
```

### Job Specification

You can specify jobs by:
- `%n` - job number (e.g., `%1`)
- `%+` or `%%` - current job (most recently suspended)
- `%-` - previous job

### Suspend Running Process

To suspend a running foreground process, press Ctrl+Z. This allows you to use `fg` or `bg` to resume it later.

## Frequently Asked Questions

#### Q1. What's the difference between `fg` and `bg`?
A. `fg` brings a job to the foreground where it can interact with the terminal, while `bg` runs the job in the background without requiring terminal interaction.

#### Q2. How do I know which jobs are available to continue?
A. Use the `jobs` command to list all suspended and background jobs.

#### Q3. Can I continue a job that's already running in the background?
A. No, `continue` commands are for suspended jobs. A job already running in the background is already continuing execution.

#### Q4. What happens if I don't specify a job number?
A. Without a job specification, `fg` and `bg` operate on the current job (marked with `+` in the `jobs` output).

## References

These commands are shell built-ins, documented in the Bash manual:
https://www.gnu.org/software/bash/manual/html_node/Job-Control-Builtins.html

## Revisions

- 2025/05/04 First revision