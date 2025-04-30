# visudo command

Edit the sudoers file safely with syntax checking.

## Overview

`visudo` is a command-line utility that provides a safe way to edit the sudoers configuration file, which controls sudo access permissions. It locks the sudoers file during editing, performs syntax checking before saving changes, and prevents multiple simultaneous edits that could corrupt the file.

## Options

### **-c**

Check the sudoers file for syntax errors without making any changes.

```console
$ sudo visudo -c
/etc/sudoers: parsed OK
/etc/sudoers.d/custom: parsed OK
```

### **-f [file]**

Specify an alternate sudoers file location to edit instead of the default.

```console
$ sudo visudo -f /etc/sudoers.d/custom
```

### **-s**

Enable strict checking of the sudoers file. Warnings are treated as errors.

```console
$ sudo visudo -s
>>> /etc/sudoers: syntax error near line 28 <<<
What now?
```

### **-q**

Enable quiet mode that will not print error messages.

```console
$ sudo visudo -q -c
```

## Usage Examples

### Basic Usage

```console
$ sudo visudo
```

This opens the default sudoers file in the system's default editor. After making changes, save and exit to have visudo check the syntax.

### Creating a New Configuration File

```console
$ sudo visudo -f /etc/sudoers.d/developers
```

This creates or edits a file in the sudoers.d directory, which is commonly used for custom sudo configurations.

### Checking Multiple Files

```console
$ sudo visudo -c
/etc/sudoers: parsed OK
/etc/sudoers.d/custom: parsed OK
/etc/sudoers.d/developers: parsed OK
```

## Tips

### Use EDITOR Environment Variable

Set your preferred editor before running visudo:

```console
$ EDITOR=nano sudo visudo
```

### Create User-Specific Rules in Separate Files

Instead of editing the main sudoers file, create separate files in `/etc/sudoers.d/` for different users or groups. This makes management easier and safer.

### Always Use visudo, Never Edit Directly

Never edit `/etc/sudoers` with a regular text editor. If you introduce syntax errors, you might lock yourself out of sudo access, which can be difficult to recover from.

### Common Sudoers Syntax

Basic syntax for giving a user full sudo access:
```
username ALL=(ALL) ALL
```

For passwordless sudo:
```
username ALL=(ALL) NOPASSWD: ALL
```

## Frequently Asked Questions

#### Q1. What happens if I save a sudoers file with syntax errors?
A. visudo will alert you to the error and give you options to re-edit the file, write it to a different location, or abandon your changes. This prevents you from corrupting the sudoers file.

#### Q2. How do I change the default editor used by visudo?
A. Set the EDITOR or VISUAL environment variable before running visudo: `EDITOR=nano sudo visudo`

#### Q3. Can I use visudo to edit files other than the main sudoers file?
A. Yes, use the `-f` option to specify an alternate file: `sudo visudo -f /etc/sudoers.d/myconfig`

#### Q4. What's the difference between /etc/sudoers and files in /etc/sudoers.d/?
A. The main `/etc/sudoers` file is the primary configuration file, while `/etc/sudoers.d/` is a directory for additional configuration files that are included in the main configuration. Using separate files in this directory helps organize sudo rules.

## References

https://www.sudo.ws/docs/man/visudo.man/

## Revisions

- 2025/04/30 First revision