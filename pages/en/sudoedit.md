# sudoedit command

Edit files securely as a privileged user while maintaining file ownership and permissions.

## Overview

`sudoedit` (also available as `sudo -e`) allows users to edit files that require elevated privileges while using their own editor preferences and preserving the file's original ownership and permissions. Unlike direct editing with `sudo vim`, `sudoedit` creates a temporary copy of the file that you edit with your preferred editor, then copies the changes back to the original file when you're done.

## Options

### **-u username/ID** / **--user=username/ID**

Edit the file as the specified user rather than root

```console
$ sudoedit -u www-data /var/www/html/index.html
```

### **-H** / **--set-home**

Sets the HOME environment variable to the target user's home directory

```console
$ sudoedit -H /etc/ssh/sshd_config
```

### **-C num** / **--close-from=num**

Closes all file descriptors greater than or equal to num before executing a command

```console
$ sudoedit -C 3 /etc/hosts
```

### **-E** / **--preserve-env**

Preserves the user's environment variables when editing

```console
$ sudoedit -E /etc/nginx/nginx.conf
```

## Usage Examples

### Basic file editing

```console
$ sudoedit /etc/ssh/sshd_config
[Your default editor opens with the file]
```

### Using sudo -e (equivalent to sudoedit)

```console
$ sudo -e /etc/fstab
[Your default editor opens with the file]
```

### Editing multiple files at once

```console
$ sudoedit /etc/hosts /etc/hostname
[Your default editor opens with the first file, then the second]
```

## Tips

### Setting Your Preferred Editor

`sudoedit` uses the SUDO_EDITOR, VISUAL, or EDITOR environment variables (in that order) to determine which editor to use. Set one of these in your shell configuration:

```console
$ echo 'export EDITOR=vim' >> ~/.bashrc
```

### Checking Differences Before Saving

When editing critical system files, you can use the diff command to verify your changes before they're applied:

```console
$ diff /etc/ssh/sshd_config /tmp/sshd_config.tmp
```

### Security Advantage

Using `sudoedit` is more secure than `sudo vim` because it minimizes the time spent with elevated privileges and prevents editor plugins from potentially executing malicious code with root privileges.

## Frequently Asked Questions

#### Q1. What's the difference between `sudoedit` and `sudo vim`?
A. `sudoedit` creates a temporary copy of the file that you edit with your normal privileges, then copies it back with sudo privileges. This is more secure than running the entire editor as root with `sudo vim`.

#### Q2. How do I specify which editor to use with `sudoedit`?
A. Set the SUDO_EDITOR, VISUAL, or EDITOR environment variable in your shell configuration file (e.g., ~/.bashrc).

#### Q3. Can I edit multiple files at once with `sudoedit`?
A. Yes, simply list all the files you want to edit as arguments: `sudoedit file1 file2 file3`.

#### Q4. Why does `sudoedit` sometimes fail with "sudoedit: no writable temporary directory found"?
A. This occurs when `sudoedit` cannot find a temporary directory with appropriate permissions. Try setting the TMPDIR environment variable to a directory you can write to.

## macOS Considerations

On macOS, `sudoedit` works similarly to Linux, but the default editor might be different. macOS typically uses nano as the default editor. To change this, set your EDITOR environment variable in your ~/.zshrc or ~/.bash_profile file.

## References

https://www.sudo.ws/docs/man/sudoedit.man/

## Revisions

- 2025/05/04 First revision