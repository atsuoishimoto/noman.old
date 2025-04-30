# systemctl command

Control and manage systemd system and service manager.

## Overview

`systemctl` is a command-line utility used to control and interact with the systemd system and service manager. It allows users to start, stop, restart, enable, disable, and check the status of system services. Systemd is the init system and service manager for many modern Linux distributions, replacing the traditional SysV init system.

## Options

### **status**

Display the status of a service, including whether it's running, recent log entries, and other details.

```console
$ systemctl status nginx
● nginx.service - A high performance web server and a reverse proxy server
     Loaded: loaded (/lib/systemd/system/nginx.service; enabled; vendor preset: enabled)
     Active: active (running) since Wed 2025-04-30 10:15:23 UTC; 2h 34min ago
       Docs: man:nginx(8)
   Main PID: 1234 (nginx)
      Tasks: 2 (limit: 4915)
     Memory: 3.2M
        CPU: 250ms
     CGroup: /system.slice/nginx.service
             ├─1234 "nginx: master process /usr/sbin/nginx -g daemon on; master_process on;"
             └─1235 "nginx: worker process"
```

### **start/stop/restart**

Control the running state of a service.

```console
$ systemctl start nginx
$ systemctl stop nginx
$ systemctl restart nginx
```

### **enable/disable**

Configure whether a service starts automatically at boot.

```console
$ systemctl enable nginx
Created symlink /etc/systemd/system/multi-user.target.wants/nginx.service → /lib/systemd/system/nginx.service.
$ systemctl disable nginx
Removed /etc/systemd/system/multi-user.target.wants/nginx.service.
```

### **list-units**

Show loaded systemd units and their states.

```console
$ systemctl list-units --type=service
UNIT                               LOAD   ACTIVE SUB     DESCRIPTION
accounts-daemon.service            loaded active running Accounts Service
apparmor.service                   loaded active exited  AppArmor initialization
apport.service                     loaded active exited  LSB: automatic crash report generation
avahi-daemon.service               loaded active running Avahi mDNS/DNS-SD Stack
```

## Usage Examples

### Checking if a service is running

```console
$ systemctl is-active nginx
active
```

### Reloading a service configuration

```console
$ systemctl reload nginx
```

### Viewing all failed services

```console
$ systemctl --failed
UNIT           LOAD   ACTIVE SUB    DESCRIPTION
mysql.service  loaded failed failed MySQL Database Server
```

### Viewing system boot logs

```console
$ systemctl list-jobs
JOB UNIT                      TYPE  STATE
123 nginx.service             start running
124 mysql.service             start waiting
```

## Tips

### Use `systemctl daemon-reload` After Modifying Unit Files

After editing any systemd unit files, run `systemctl daemon-reload` to ensure systemd recognizes your changes.

### Check Service Dependencies

Use `systemctl list-dependencies [service]` to see what other services a particular service depends on, which is helpful for troubleshooting.

### View Service Logs with journalctl

While not part of systemctl itself, you can use `journalctl -u [service]` to view logs for a specific service, which complements systemctl's functionality.

### Mask Services to Prevent Activation

Use `systemctl mask [service]` to completely prevent a service from being started, even manually. This is stronger than disable.

## Frequently Asked Questions

#### Q1. What's the difference between `systemctl stop` and `systemctl disable`?
A. `stop` terminates a running service immediately but doesn't affect boot behavior. `disable` prevents a service from starting at boot but doesn't affect currently running services.

#### Q2. How do I make changes to a service configuration take effect?
A. Edit the service file, run `systemctl daemon-reload`, then `systemctl restart [service]`.

#### Q3. How can I see all available services?
A. Use `systemctl list-unit-files --type=service` to see all service files, regardless of whether they're currently loaded.

#### Q4. How do I create a custom service?
A. Create a .service file in /etc/systemd/system/, then run `systemctl daemon-reload` and `systemctl enable` your service.

#### Q5. What's the difference between `restart` and `reload`?
A. `restart` stops and starts a service completely, while `reload` just makes the service reread its configuration files without stopping.

## References

https://www.freedesktop.org/software/systemd/man/systemctl.html

## Revisions

- 2025/04/30 First revision