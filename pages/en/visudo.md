# visudo command

Edit the sudoers file safely with syntax checking.

## Overview

`visudo` is a command-line utility that provides a safe way to edit the `/etc/sudoers` file, which controls sudo access permissions. It locks the sudoers file to prevent multiple simultaneous edits, performs syntax checking before saving changes, and helps prevent configuration errors that could lock users out of the system.

## Options

### **-c, --check**

Check the sudoers file for syntax errors only, without making any changes.

```console
$ sudo visudo -c
/etc/sudoers: parsed OK
/etc/sudoers.d/custom: parsed OK
```

### **-f, --file=file**

Specify an alternate sudoers file location instead of the default `/etc/sudoers`.

```console
$ sudo visudo -f /etc/sudoers.d/custom
```

### **-q, --quiet**

Enable quiet mode, which suppresses most warning messages.

```console
$ sudo visudo -q -c
```

### **-s, --strict**

Enable strict checking of the sudoers file. Will cause visudo to exit with an error if there are any parse errors.

```console
$ sudo visudo -s -f /etc/sudoers.d/test
>>> /etc/sudoers.d/test: syntax error near line 2 <<<
parse error in /etc/sudoers.d/test near line 2
visudo: fatal error, exiting.
```

## Usage Examples

### Basic Usage

```console
$ sudo visudo
```

This opens the default `/etc/sudoers` file in the editor specified by the EDITOR environment variable.

### Editing a Custom Sudoers File

```console
$ sudo visudo -f /etc/sudoers.d/local
```

This opens a custom sudoers file located in the `/etc/sudoers.d` directory.

### Checking Syntax Without Editing

```console
$ sudo visudo -c
/etc/sudoers: parsed OK
/etc/sudoers.d/custom: parsed OK
```

## Tips

### Set Your Preferred Editor

Before running visudo, you can set your preferred editor by setting the EDITOR or VISUAL environment variable:

```console
$ export EDITOR=nano
$ sudo visudo
```

### Use Includes Instead of Direct Edits

Instead of editing the main sudoers file, create separate files in `/etc/sudoers.d/` for custom configurations. This makes management easier and safer.

```console
$ sudo visudo -f /etc/sudoers.d/myusers
```

### Always Check Syntax Before Exiting

When editing the sudoers file, always use visudo's built-in syntax checking before saving. If you make a syntax error, visudo will warn you and give you a chance to fix it before saving.

## Frequently Asked Questions

#### Q1. What happens if I edit the sudoers file directly without using visudo?
A. Editing `/etc/sudoers` directly with a regular text editor is dangerous. If you introduce syntax errors, you might lose sudo access entirely, potentially locking yourself out of administrative functions.

#### Q2. How do I add a new user to sudoers?
A. Run `sudo visudo` and add a line like `username ALL=(ALL:ALL) ALL` to grant full sudo privileges to a user.

#### Q3. What's the difference between /etc/sudoers and files in /etc/sudoers.d/?
A. The main `/etc/sudoers` file is the primary configuration file, while `/etc/sudoers.d/` is a directory for additional configuration files that are included in the main configuration. Using separate files in this directory is often cleaner and safer.

#### Q4. How do I change the default editor used by visudo?
A. Set the EDITOR or VISUAL environment variable before running visudo: `export EDITOR=nano`.

## References

https://www.sudo.ws/docs/man/1.9.13/visudo.man/

## Revisions

- 2025/05/04 First revision