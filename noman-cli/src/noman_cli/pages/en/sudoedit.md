# sudoedit command

Edit files securely as a superuser while using your own user's editor configuration.

## Overview

`sudoedit` (also accessible as `sudo -e`) allows you to edit files that require elevated privileges while using your own editor preferences and configuration. It works by creating a temporary copy of the target file, letting you edit that copy with your regular user permissions, and then copying the changes back to the original file with superuser privileges.

## Options

### **-u username**

Specify which user's identity to assume when editing the file

```console
$ sudoedit -u root /etc/hosts
```

### **-H**

Set the HOME environment variable to the target user's home directory

```console
$ sudoedit -H /etc/ssh/sshd_config
```

### **-C directory**

Change to the specified directory before editing

```console
$ sudoedit -C /etc /ssh/sshd_config
```

## Usage Examples

### Basic file editing

```console
$ sudoedit /etc/ssh/sshd_config
[Your default editor opens with the file contents]
```

### Using sudo -e (equivalent to sudoedit)

```console
$ sudo -e /etc/hosts
[Your default editor opens with the file contents]
```

### Editing multiple files

```console
$ sudoedit /etc/hosts /etc/resolv.conf
[Your default editor opens with each file in sequence]
```

## Tips:

### Setting Your Preferred Editor

`sudoedit` uses the EDITOR or VISUAL environment variables to determine which editor to launch. Set these in your shell configuration:

```console
$ echo 'export EDITOR=nano' >> ~/.bashrc
```

### Security Benefits

Unlike running your editor directly with sudo (e.g., `sudo vim file`), `sudoedit` prevents editor plugins or configurations from running with elevated privileges, reducing security risks.

### Temporary File Location

The temporary copy is created in the same directory as the original file. If you don't have write permissions to that directory, use the TMPDIR environment variable to specify an alternative location.

## Frequently Asked Questions

#### Q1. What's the difference between `sudoedit` and `sudo vim`?
A. `sudoedit` creates a temporary copy that you edit with your normal user privileges, then copies it back with sudo privileges. `sudo vim` runs the entire editor with elevated privileges, which can be a security risk if your editor has plugins or runs external commands.

#### Q2. How do I specify which editor to use?
A. Set the EDITOR or VISUAL environment variable in your shell configuration file (e.g., `~/.bashrc`).

#### Q3. Can I use `sudoedit` to edit multiple files at once?
A. Yes, simply list multiple files as arguments: `sudoedit file1 file2 file3`.

#### Q4. Why does `sudoedit` sometimes fail with "sudoedit: unable to stat file: No such file or directory"?
A. This typically happens when the directory containing the file doesn't exist or when you don't have permission to access the directory structure leading to the file.

## References

https://www.sudo.ws/docs/man/sudoedit.man/

## Revisions

- 2025/04/30 First revision