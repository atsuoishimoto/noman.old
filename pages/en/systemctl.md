# systemctl command

Control the systemd system and service manager.

## Overview

`systemctl` is a command-line utility used to control and manage systemd, the system and service manager for Linux. It allows users to start, stop, restart, enable, disable, and check the status of system services. systemd is the init system used by most modern Linux distributions to bootstrap the user space and manage system processes.

## Options

### **-t, --type=TYPE**

Filter units by their type (e.g., service, socket, timer)

```console
$ systemctl -t service
UNIT                               LOAD   ACTIVE SUB     DESCRIPTION
accounts-daemon.service            loaded active running Accounts Service
apparmor.service                   loaded active exited  AppArmor initialization
avahi-daemon.service               loaded active running Avahi mDNS/DNS-SD Stack
bluetooth.service                  loaded active running Bluetooth service
...
```

### **-a, --all**

Show all loaded units, including inactive ones

```console
$ systemctl -a
UNIT                                  LOAD      ACTIVE   SUB     DESCRIPTION
proc-sys-fs-binfmt_misc.automount     loaded    active   running Arbitrary Executable File Formats File System
sys-devices-pci0000:00-0000:00:14.0-usb1-1\x2d1-1\x2d1.1-1\x2d1.1:1.0-bluetooth-hci0.device loaded active plugged /sys/devices/pci0000:00/0000:00:14.0/usb1/1-1/1-1.1/1-1.1:1.0/bluetooth/hci0
...
```

### **--state=STATE**

Filter units by their state (e.g., active, failed)

```console
$ systemctl --state=failed
UNIT                  LOAD   ACTIVE SUB    DESCRIPTION
mysql.service         loaded failed failed MySQL Database Server
docker.service        loaded failed failed Docker Application Container Engine
```

### **--failed**

Show only failed units

```console
$ systemctl --failed
UNIT                  LOAD   ACTIVE SUB    DESCRIPTION
mysql.service         loaded failed failed MySQL Database Server
docker.service        loaded failed failed Docker Application Container Engine
```

### **-l, --full**

Don't ellipsize unit names, status text, or truncate unit descriptions

```console
$ systemctl status sshd.service -l
● ssh.service - OpenBSD Secure Shell server
     Loaded: loaded (/lib/systemd/system/ssh.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2025-05-04 10:15:23 UTC; 2h 30min ago
       Docs: man:sshd(8)
             man:sshd_config(5)
    Process: 1190 ExecStartPre=/usr/sbin/sshd -t (code=exited, status=0/SUCCESS)
   Main PID: 1226 (sshd)
      Tasks: 1 (limit: 4611)
     Memory: 6.5M
        CPU: 236ms
     CGroup: /system.slice/ssh.service
             └─1226 "sshd: /usr/sbin/sshd -D [listener] 0 of 10-100 startups"
```

## Usage Examples

### Starting a service

```console
$ sudo systemctl start nginx.service
```

### Stopping a service

```console
$ sudo systemctl stop nginx.service
```

### Restarting a service

```console
$ sudo systemctl restart nginx.service
```

### Checking service status

```console
$ systemctl status nginx.service
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Mon 2025-05-04 12:34:56 UTC; 2h ago
       Docs: man:nginx(8)
   Main PID: 1234 (nginx)
      Tasks: 5 (limit: 4611)
     Memory: 6.2M
        CPU: 123ms
     CGroup: /system.slice/nginx.service
             ├─1234 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             ├─1235 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             ├─1236 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" 
             ├─1237 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
             └─1238 "nginx: worker process" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
```

### Enabling a service to start at boot

```console
$ sudo systemctl enable nginx.service
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /lib/systemd/system/nginx.service.
```

### Disabling a service from starting at boot

```console
$ sudo systemctl disable nginx.service
Removed /etc/systemd/system/multi-user.target.wants/nginx.service.
```

### Viewing system boot logs

```console
$ systemctl list-jobs
JOB UNIT                      TYPE  STATE  
423 systemd-backlight@backlight:acpi_video0.service start running
425 systemd-rfkill.service    start running
426 systemd-update-utmp-runlevel.service start running
427 multi-user.target         start running
```

## Tips

### Use Tab Completion

systemctl supports tab completion for unit names, making it easier to manage services without remembering exact names.

### Check Service Dependencies

Use `systemctl list-dependencies [unit]` to see what other services a particular service depends on or what depends on it.

### Mask a Service

If you want to completely prevent a service from being started (even manually), use `systemctl mask [service]`. This creates a symlink to /dev/null, making it impossible to start.

### Reload vs. Restart

Use `systemctl reload [service]` when you only want to reload configuration files without interrupting the service. Use `restart` when you need to completely stop and start the service.

### View Service Logs

Combine systemctl with journalctl to view logs for a specific service: `journalctl -u [service]`.

## Frequently Asked Questions

#### Q1. What's the difference between "enable" and "start"?
A. `enable` configures a service to start automatically at boot time, while `start` immediately starts a service. A service can be enabled but not currently running, or running but not enabled.

#### Q2. How do I see all available services?
A. Use `systemctl list-unit-files --type=service` to see all available service units and their enabled/disabled status.

#### Q3. How can I check if a service is enabled to start at boot?
A. Use `systemctl is-enabled [service]` which will return "enabled" or "disabled".

#### Q4. What does "masked" status mean for a service?
A. A masked service is completely prevented from being started, either manually or automatically. It's a stronger form of "disabled".

#### Q5. How do I restart all services that depend on a specific service?
A. Use `systemctl restart --all [service]` to restart the service and all its dependent services.

## References

https://www.freedesktop.org/software/systemd/man/systemctl.html

## Revisions

- 2025/05/04 First revision