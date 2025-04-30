# apt command

Package management tool for Debian-based Linux distributions like Ubuntu.

## Overview

`apt` (Advanced Package Tool) is a command-line utility for installing, updating, removing, and managing software packages on Debian-based Linux distributions. It simplifies package management by handling dependencies automatically and providing a user-friendly interface compared to lower-level tools like `dpkg`.

## Options

### **apt update**

Updates the package lists from repositories

```console
$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
```

### **apt install**

Installs new packages

```console
$ sudo apt install firefox
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  firefox-locale-en
Suggested packages:
  fonts-lyx
The following NEW packages will be installed:
  firefox firefox-locale-en
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 74.3 MB of archives.
After this operation, 239 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

### **apt remove**

Removes packages but keeps configuration files

```console
$ sudo apt remove firefox
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  firefox firefox-locale-en
0 upgraded, 0 newly installed, 2 to remove and 0 not upgraded.
After this operation, 239 MB disk space will be freed.
Do you want to continue? [Y/n] y
```

### **apt purge**

Completely removes packages including configuration files

```console
$ sudo apt purge firefox
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  firefox* firefox-locale-en*
0 upgraded, 0 newly installed, 2 to remove and 0 not upgraded.
After this operation, 239 MB disk space will be freed.
Do you want to continue? [Y/n] y
```

### **apt upgrade**

Upgrades all installed packages to their latest versions

```console
$ sudo apt upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  firefox libc6 python3-apt
3 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 85.6 MB of archives.
After this operation, 2,048 B of additional disk space will be used.
Do you want to continue? [Y/n] y
```

### **apt search**

Searches for packages by name or description

```console
$ apt search text editor
Sorting... Done
Full Text Search... Done
gedit/jammy,now 41.0-1 amd64 [installed]
  GNU text editor for the GNOME desktop environment

nano/jammy,now 6.2-1 amd64 [installed]
  small, friendly text editor inspired by Pico

vim/jammy 2:8.2.3995-1ubuntu2 amd64
  Vi IMproved - enhanced vi editor
```

### **apt list**

Lists packages based on package names

```console
$ apt list --installed | grep firefox
firefox/jammy-updates,jammy-security,now 112.0+build2-0ubuntu0.22.04.1 amd64 [installed]
firefox-locale-en/jammy-updates,jammy-security,now 112.0+build2-0ubuntu0.22.04.1 amd64 [installed,automatic]
```

## Usage Examples

### Updating and upgrading the system

```console
$ sudo apt update && sudo apt upgrade -y
[update output]
[upgrade output]
```

### Installing multiple packages at once

```console
$ sudo apt install git vim curl
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  [list of dependencies]
Do you want to continue? [Y/n] y
```

### Removing unused dependencies

```console
$ sudo apt autoremove
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  libllvm13 linux-headers-5.15.0-60 linux-headers-5.15.0-60-generic
0 upgraded, 0 newly installed, 3 to remove and 0 not upgraded.
After this operation, 122 MB disk space will be freed.
Do you want to continue? [Y/n] y
```

## Tips:

### Use apt instead of apt-get

`apt` provides a more user-friendly interface with progress bars and color output compared to the older `apt-get` command.

### Check package information before installing

Use `apt show package-name` to view detailed information about a package before installing it.

### Fix broken packages

If you encounter issues with broken packages, try running `sudo apt --fix-broken install` to resolve dependency problems.

### Clean up package cache

Run `sudo apt clean` periodically to free up disk space by removing downloaded package files from the local cache.

### Simulate installations

Use the `-s` or `--simulate` option with any apt command to see what would happen without actually making changes to your system.

## Frequently Asked Questions

#### Q1. What's the difference between apt and apt-get?
A. `apt` is a newer, more user-friendly command that combines the most commonly used features of `apt-get` and `apt-cache` with improved output formatting and progress information.

#### Q2. How do I install a specific version of a package?
A. Use `sudo apt install package=version`. For example: `sudo apt install nginx=1.18.0-0ubuntu1`.

#### Q3. How can I see what packages are available for upgrade?
A. Run `apt list --upgradable` to see a list of packages that can be upgraded.

#### Q4. How do I fix "Unable to lock the administration directory" errors?
A. This usually means another package manager is running. Wait for it to finish or check for stuck processes with `ps aux | grep apt` and terminate them if necessary.

#### Q5. How do I add a new repository?
A. Use `sudo add-apt-repository ppa:repository-name` for PPAs or edit the `/etc/apt/sources.list` file, then run `sudo apt update`.

## References

https://manpages.ubuntu.com/manpages/jammy/man8/apt.8.html

## Revisions

- 2025/04/30 First revision