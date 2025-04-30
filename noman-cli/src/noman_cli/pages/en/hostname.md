# hostname command

Display or set the system's host name.

## Overview

The `hostname` command displays or sets the name of the current host system. This name identifies your computer on a network and is used by various network services. On most systems, the hostname is configured during installation but can be changed later.

## Options

### **-s, --short**

Display the short hostname (the portion before the first dot) without the domain name.

```console
$ hostname -s
macbook
```

### **-f, --fqdn, --long**

Display the Fully Qualified Domain Name (FQDN), which includes both the hostname and domain.

```console
$ hostname -f
macbook.local
```

### **-i, --ip-address**

Display the IP address(es) of the host.

```console
$ hostname -i
192.168.1.5
```

### **-d, --domain**

Display the domain name the host belongs to.

```console
$ hostname -d
local
```

## Usage Examples

### Displaying the current hostname

```console
$ hostname
macbook.local
```

### Setting a new hostname (requires root privileges)

```console
$ sudo hostname new-hostname
$ hostname
new-hostname
```

## Tips

### Permanent Hostname Changes

The `hostname` command only changes the hostname temporarily until the next reboot. For permanent changes:
- On Linux: Edit files like `/etc/hostname` or use system tools like `hostnamectl`
- On macOS: Use System Preferences > Sharing > Computer Name

### Network Configuration

Changing your hostname might require updating other network configuration files like `/etc/hosts` to ensure proper name resolution.

### Hostname Conventions

Choose hostnames that are unique on your network and follow DNS naming rules: use only letters, numbers, and hyphens, and don't start with a number.

## Frequently Asked Questions

#### Q1. What's the difference between hostname and computer name?
A. They're generally the same thing, though some operating systems distinguish between a "pretty" computer name (with spaces and special characters) and a network hostname (which follows stricter naming rules).

#### Q2. Why does my hostname show ".local" at the end?
A. The ".local" suffix is commonly used in local networks, especially on macOS systems using Bonjour/mDNS for local network discovery.

#### Q3. How can I make hostname changes permanent?
A. The method varies by operating system. On Linux, edit `/etc/hostname` or use `hostnamectl set-hostname`. On macOS, use System Preferences > Sharing.

#### Q4. Can I set my hostname to anything?
A. While technically possible, it's best to follow DNS naming conventions: use only letters, numbers, and hyphens, don't start with a number, and keep it under 63 characters.

## macOS Specifics

On macOS, the hostname command works similarly to Linux, but permanent hostname changes should be made through System Preferences > Sharing > Computer Name. macOS also maintains separate settings for the "Computer Name" (user-friendly name) and the hostname (network name). When you change the Computer Name, macOS automatically creates a hostname version by removing special characters and adding ".local".

## References

https://man7.org/linux/man-pages/man1/hostname.1.html

## Revisions

- 2025/04/30 First revision