# apt command

Package management utility for Debian-based Linux distributions like Ubuntu.

## Overview

`apt` (Advanced Package Tool) is a command-line utility for installing, updating, removing, and managing software packages on Debian-based Linux distributions. It simplifies package management by handling dependencies automatically and providing a user-friendly interface compared to lower-level tools like `dpkg`.

## Options

### **-y, --yes, --assume-yes**

Automatically answer "yes" to prompts, allowing for non-interactive use

```console
$ sudo apt install firefox -y
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
firefox is already the newest version (115.0+build2-0ubuntu0.22.04.1).
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
```

### **-q, --quiet**

Produces output suitable for logging, omitting progress indicators

```console
$ sudo apt update -q
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Fetched 110 kB in 1s (110 kB/s)
Reading package lists...
Building dependency tree...
Reading state information...
All packages are up to date.
```

### **--no-install-recommends**

Skip installation of recommended packages, installing only required dependencies

```console
$ sudo apt install gimp --no-install-recommends
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be installed:
  gimp gimp-data libbabl-0.1-0 libgegl-0.4-0 [...]
```

### **-s, --simulate, --just-print, --dry-run, --recon, --no-act**

Simulate actions but don't actually change the system

```console
$ sudo apt remove firefox -s
NOTE: This is only a simulation!
      apt needs root privileges for real execution.
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  firefox
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
Remv firefox [115.0+build2-0ubuntu0.22.04.1]
```

## Usage Examples

### Installing a package

```console
$ sudo apt install vlc
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following additional packages will be installed:
  libvlc-bin libvlc5 libvlccore9 vlc-bin vlc-data vlc-plugin-base
Suggested packages:
  vlc-plugin-access-extra vlc-plugin-video-output vlc-plugin-video-splitter
  vlc-plugin-visualization
The following NEW packages will be installed:
  libvlc-bin libvlc5 libvlccore9 vlc vlc-bin vlc-data vlc-plugin-base
0 upgraded, 7 newly installed, 0 to remove and 0 not upgraded.
Need to get 7,192 kB of archives.
After this operation, 32.8 MB of additional disk space will be used.
Do you want to continue? [Y/n] y
```

### Updating package lists

```console
$ sudo apt update
Hit:1 http://archive.ubuntu.com/ubuntu jammy InRelease
Get:2 http://security.ubuntu.com/ubuntu jammy-security InRelease [110 kB]
Get:3 http://archive.ubuntu.com/ubuntu jammy-updates InRelease [119 kB]
Fetched 229 kB in 2s (114 kB/s)
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
All packages are up to date.
```

### Upgrading installed packages

```console
$ sudo apt upgrade
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Calculating upgrade... Done
The following packages will be upgraded:
  firefox libnss3 python3-software-properties software-properties-common
4 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
Need to get 75.8 MB of archives.
After this operation, 1,024 B of additional disk space will be used.
Do you want to continue? [Y/n] y
```

### Removing a package

```console
$ sudo apt remove gimp
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
The following packages will be REMOVED:
  gimp
0 upgraded, 0 newly installed, 1 to remove and 0 not upgraded.
After this operation, 20.5 MB disk space will be freed.
Do you want to continue? [Y/n] y
```

### Searching for packages

```console
$ apt search text-editor
Sorting... Done
Full Text Search... Done
gedit/jammy,now 41.0-3 amd64 [installed]
  GNU text editor for the GNOME desktop environment

mousepad/jammy 0.5.8-1 amd64
  simple Xfce oriented text editor

nano/jammy,now 6.2-1 amd64 [installed]
  small, friendly text editor inspired by Pico
```

## Tips

### Use apt instead of apt-get

`apt` provides a more user-friendly interface with progress bars and colored output compared to the older `apt-get` command, while offering the most commonly used functionality.

### Clean up unused packages

Run `sudo apt autoremove` periodically to remove packages that were automatically installed as dependencies but are no longer needed.

### Fix broken packages

If you encounter package installation issues, try `sudo apt --fix-broken install` to resolve dependency problems.

### Check available disk space

Before large installations or upgrades, check available disk space with `df -h`. Package operations can fail if you run out of space.

### Use apt-mark to protect packages

Use `sudo apt-mark hold package_name` to prevent a package from being automatically upgraded, removed, or installed.

## Frequently Asked Questions

#### Q1. What's the difference between apt and apt-get?
A. `apt` is a newer, more user-friendly command that combines the most commonly used features of `apt-get` and `apt-cache` with improved output formatting and progress information.

#### Q2. How do I completely remove a package including configuration files?
A. Use `sudo apt purge package_name` instead of `remove`. To also remove dependencies that are no longer needed, add `autoremove`: `sudo apt purge package_name && sudo apt autoremove`.

#### Q3. How can I install a specific version of a package?
A. Use `sudo apt install package_name=version`. For example: `sudo apt install nginx=1.18.0-0ubuntu1`.

#### Q4. How do I fix "Unable to lock the administration directory" errors?
A. This usually means another package manager is running. Wait for it to finish or check for stuck processes with `ps aux | grep apt` and kill them if necessary. You might also need to remove lock files with `sudo rm /var/lib/apt/lists/lock /var/cache/apt/archives/lock /var/lib/dpkg/lock*`.

#### Q5. How do I update a single package?
A. Use `sudo apt install --only-upgrade package_name`.

## References

https://manpages.ubuntu.com/manpages/jammy/man8/apt.8.html

## Revisions

- 2025/05/04 First revision