# apt-file command

Search for files within packages in the APT package management system.

## Overview

`apt-file` is a command-line utility that allows you to search for files in packages available in the APT repositories, even if they are not installed on your system. It's particularly useful for finding which package provides a specific file, or for exploring the contents of packages before installing them.

## Options

### **-l, --list**

List the contents of a specified package.

```console
$ apt-file list firefox
firefox: /etc/firefox/syspref.js
firefox: /etc/xul-ext/ubufox.js
firefox: /usr/bin/firefox
firefox: /usr/lib/firefox/browser/chrome.manifest
firefox: /usr/lib/firefox/browser/chrome/icons/default/default128.png
[...]
```

### **-s, --search**

Search for packages containing a specific file or pattern.

```console
$ apt-file search bin/ls
coreutils: /bin/ls
```

### **-x, --regexp**

Use regular expressions for searching.

```console
$ apt-file -x search '.*bin/python3$'
python3-minimal: /usr/bin/python3
```

### **-a, --architecture**

Specify the architecture to search in.

```console
$ apt-file -a arm64 search bin/ls
coreutils: /bin/ls
```

### **-c, --cache**

Use a specific cache directory.

```console
$ apt-file -c /tmp/apt-file-cache search bin/ls
coreutils: /bin/ls
```

### **-u, --update**

Update the package lists cache.

```console
$ sudo apt-file update
Processing 'main' component lists
Processing 'universe' component lists
Processing 'restricted' component lists
Processing 'multiverse' component lists
```

## Usage Examples

### Finding which package provides a specific command

```console
$ apt-file search bin/grep
grep: /bin/grep
```

### Listing all files in a package

```console
$ apt-file list coreutils | head -5
coreutils: /bin/cat
coreutils: /bin/chgrp
coreutils: /bin/chmod
coreutils: /bin/chown
coreutils: /bin/cp
```

### Searching for a library file

```console
$ apt-file search libssl.so.1.1
libssl1.1: /usr/lib/x86_64-linux-gnu/libssl.so.1.1
```

## Tips

### Update the Cache First

Always run `sudo apt-file update` before using apt-file for the first time or if you haven't used it in a while. This ensures you have the latest package information.

### Narrow Down Results with Grep

When apt-file returns too many results, pipe the output through grep to filter:

```console
$ apt-file search .so | grep ssl
```

### Use with Package Installation

When you encounter a "command not found" error, use apt-file to find which package provides that command:

```console
$ apt-file search bin/missing-command
```

### Combine with Other APT Tools

Use apt-file alongside apt-cache and apt to get comprehensive package information:

```console
$ apt-file search bin/python3
$ apt-cache show python3-minimal
```

## Frequently Asked Questions

#### Q1. How do I install apt-file?
A. Install it using `sudo apt install apt-file`, then update the cache with `sudo apt-file update`.

#### Q2. Why does apt-file search return no results?
A. You may need to update the apt-file cache with `sudo apt-file update`. Also, ensure you're using the correct file path.

#### Q3. Can apt-file search for files in packages not installed on my system?
A. Yes, that's one of its main features. It searches all packages in the configured repositories.

#### Q4. How is apt-file different from dpkg -S?
A. `dpkg -S` only searches for files in installed packages, while `apt-file` searches all available packages in repositories.

#### Q5. How do I search for files with a specific extension?
A. Use the regexp option: `apt-file -x search '\.so$'` to find all .so files.

## References

https://manpages.debian.org/stable/apt-file/apt-file.1.en.html

## Revisions

- 2025/05/04 First revision