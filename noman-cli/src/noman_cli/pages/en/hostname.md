# hostname command

Display or set the system's host name.

## Overview

The `hostname` command displays or sets the current host name of the system. The host name is the name by which a network device is known on a network. This command is useful for identifying the current machine in scripts or when working across multiple systems.

## Options

### **-s, --short**

Display the short host name, cutting off any domain information.

```console
$ hostname -s
mycomputer
```

### **-f, --fqdn, --long**

Display the Fully Qualified Domain Name (FQDN).

```console
$ hostname -f
mycomputer.example.com
```

### **-d, --domain**

Display the DNS domain name.

```console
$ hostname -d
example.com
```

### **-i, --ip-address**

Display the IP address(es) of the host.

```console
$ hostname -i
192.168.1.100
```

### **-I, --all-ip-addresses**

Display all network addresses of the host.

```console
$ hostname -I
192.168.1.100 10.0.0.1 172.16.0.1
```

## Usage Examples

### Displaying the current hostname

```console
$ hostname
mycomputer.example.com
```

### Setting a new hostname (requires root privileges)

```console
$ sudo hostname newname
$ hostname
newname
```

### Using hostname in a script to identify the current machine

```console
$ echo "Running backup script on $(hostname)"
Running backup script on mycomputer.example.com
```

## Tips

### Permanent Hostname Changes

The `hostname` command only changes the hostname temporarily until the next reboot. For permanent changes:
- On systemd-based systems: Use `hostnamectl set-hostname newname`
- On Debian/Ubuntu: Edit `/etc/hostname`
- On RHEL/CentOS: Edit `/etc/sysconfig/network`

### Network Configuration

Changing your hostname might require updating other files like `/etc/hosts` to ensure proper name resolution.

### Hostname Restrictions

Hostnames should follow RFC 1178 guidelines: use only letters, digits, and hyphens, and should not exceed 63 characters.

## Frequently Asked Questions

#### Q1. What's the difference between hostname and FQDN?
A. A hostname is just the name of the machine (e.g., "mycomputer"), while the FQDN includes the domain (e.g., "mycomputer.example.com").

#### Q2. Why does my hostname reset after reboot?
A. The `hostname` command only makes temporary changes. For permanent changes, you need to modify system configuration files or use tools like `hostnamectl`.

#### Q3. Can I use special characters in my hostname?
A. It's recommended to use only letters, numbers, and hyphens in hostnames to ensure compatibility with all network services.

#### Q4. How do I find my hostname in a script?
A. Simply use the command `$(hostname)` in your script to get the current hostname.

## macOS Considerations

On macOS, the hostname command works similarly, but permanent changes should be made using:
- `sudo scutil --set HostName newname` for the hostname
- `sudo scutil --set LocalHostName newname` for the Bonjour hostname
- `sudo scutil --set ComputerName "New Name"` for the user-friendly computer name

## References

https://man7.org/linux/man-pages/man1/hostname.1.html

## Revisions

2025/05/04 First revision