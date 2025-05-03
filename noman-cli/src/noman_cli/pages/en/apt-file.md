# apt-file command

Search for files within packages in Debian-based Linux distributions, even if the package is not installed.

## Overview

`apt-file` is a command-line utility that allows you to search for files in packages available in Debian-based Linux distributions (like Ubuntu). It's particularly useful when you need to find which package provides a specific file, or to list all files contained in a package without installing it.

## Options

### **-l, --list**

List the contents of a package

```console
$ apt-file list firefox
firefox: /etc/apparmor.d/usr.bin.firefox
firefox: /etc/firefox/syspref.js
firefox: /usr/bin/firefox
firefox: /usr/lib/firefox/browser/chrome.manifest
firefox: /usr/lib/firefox/browser/features/formautofill@mozilla.org.xpi
[more output...]
```

### **-s, --search**

Search for packages containing a specific file

```console
$ apt-file search /usr/bin/python3
python3-minimal: /usr/bin/python3
python3.10-minimal: /usr/bin/python3.10
python3.11-minimal: /usr/bin/python3.11
```

### **-u, --update**

Update the package database

```console
$ sudo apt-file update
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
[more output...]
Processing apt file indexes... Done
```

### **-x, --regexp**

Search using regular expressions

```console
$ apt-file search -x '.*bin/gcc$'
gcc-11: /usr/bin/gcc
gcc-12: /usr/bin/gcc
gcc-9: /usr/bin/gcc
```

## Usage Examples

### Finding which package provides a specific command

```console
$ apt-file search /usr/bin/curl
curl: /usr/bin/curl
```

### Listing all files in a package before installing it

```console
$ apt-file list htop
htop: /usr/bin/htop
htop: /usr/share/applications/htop.desktop
htop: /usr/share/doc/htop/AUTHORS
htop: /usr/share/doc/htop/NEWS.gz
htop: /usr/share/doc/htop/README
[more output...]
```

### Finding a library file needed by an application

```console
$ apt-file search libncurses.so.6
libncurses6:amd64: /lib/x86_64-linux-gnu/libncurses.so.6
libncurses6:amd64: /lib/x86_64-linux-gnu/libncurses.so.6.2
libncurses6:i386: /lib/i386-linux-gnu/libncurses.so.6
libncurses6:i386: /lib/i386-linux-gnu/libncurses.so.6.2
```

## Tips

### Update the Database Regularly

The apt-file database needs to be updated regularly to ensure you have the latest package information. Run `sudo apt-file update` periodically, especially after changing repositories.

### Install Missing Dependencies

When you encounter "command not found" or missing library errors, use apt-file to find which package provides the missing file, then install it with `apt install`.

### Combine with Grep for Better Filtering

For complex searches, pipe the output to grep: `apt-file search bin | grep python` to find Python-related binaries.

### Initial Setup

When first installing apt-file, you must run `sudo apt-file update` before you can use it to search for files.

## Frequently Asked Questions

#### Q1. What's the difference between `apt-file` and `dpkg -S`?
A. `dpkg -S` only searches within installed packages, while `apt-file` searches all available packages, even those not installed.

#### Q2. Do I need to run apt-file as root?
A. You only need root privileges for the `apt-file update` command. Searches can be performed as a regular user.

#### Q3. How do I install apt-file?
A. Install it with `sudo apt install apt-file`, then run `sudo apt-file update` to initialize the database.

#### Q4. Why is apt-file search not finding my file?
A. Make sure you've run `sudo apt-file update` recently. Also, try using the full path to the file or use the `-x` option with a regular expression.

## References

https://manpages.debian.org/bullseye/apt-file/apt-file.1.en.html

## Revisions

- 2025/04/30 First revision