# docker run command

Create and start a new container from a specified image.

## Overview

The `docker run` command creates and starts a container from a Docker image. It combines the functionality of `docker create` and `docker start` in a single command. This command allows you to specify runtime parameters, environment variables, network settings, volume mounts, and other configuration options when launching a container.

## Options

### **-d, --detach**

Run the container in the background (detached mode) and print the container ID

```console
$ docker run -d nginx
3a41f9da42324b98a5f34d8c5c09c319f7e8e99cf24c573fc603ed52b11c42e7
```

### **-i, --interactive**

Keep STDIN open even if not attached, allowing interactive sessions

```console
$ docker run -i ubuntu /bin/bash
root@7c3bfd21a2a4:/#
```

### **-t, --tty**

Allocate a pseudo-TTY, typically used with `-i` for interactive terminal sessions

```console
$ docker run -it ubuntu
root@7c3bfd21a2a4:/# ls
bin  boot  dev  etc  home  lib  lib32  lib64  libx32  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

### **-p, --publish [host-port]:[container-port]**

Publish a container's port to the host

```console
$ docker run -p 8080:80 nginx
```

### **-v, --volume [host-path]:[container-path]**

Bind mount a volume from the host to the container

```console
$ docker run -v /host/path:/container/path nginx
```

### **-e, --env [key]=[value]**

Set environment variables inside the container

```console
$ docker run -e DB_HOST=localhost -e DB_PORT=5432 postgres
```

### **--name [name]**

Assign a name to the container

```console
$ docker run --name my-web-server nginx
```

### **--rm**

Automatically remove the container when it exits

```console
$ docker run --rm alpine echo "Hello, World!"
Hello, World!
```

### **--network [network]**

Connect a container to a network

```console
$ docker run --network my-network nginx
```

## Usage Examples

### Running a container in detached mode with port mapping

```console
$ docker run -d -p 8080:80 --name web-server nginx
3a41f9da42324b98a5f34d8c5c09c319f7e8e99cf24c573fc603ed52b11c42e7
```

### Running an interactive shell in a container

```console
$ docker run -it --rm ubuntu bash
root@7c3bfd21a2a4:/# echo "I'm in a container"
I'm in a container
root@7c3bfd21a2a4:/# exit
```

### Running a container with volume mounts and environment variables

```console
$ docker run -d \
  --name postgres-db \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -e POSTGRES_USER=myuser \
  -v pgdata:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

## Tips

### Use Named Volumes for Persistent Data

Instead of binding to specific host paths, use named volumes for better portability:

```console
$ docker run -v mydata:/app/data nginx
```

### Limit Container Resources

Use `--memory` and `--cpus` to limit container resource usage:

```console
$ docker run --memory=512m --cpus=0.5 nginx
```

### Use Environment Files for Multiple Variables

For containers requiring many environment variables, use an env file:

```console
$ docker run --env-file ./env.list nginx
```

### Cleanup Containers Automatically

Always use `--rm` for short-lived containers to avoid accumulating stopped containers.

## Frequently Asked Questions

#### Q1. What's the difference between `docker run` and `docker start`?
A. `docker run` creates and starts a new container from an image, while `docker start` restarts a stopped container that already exists.

#### Q2. How do I run a container in the background?
A. Use the `-d` or `--detach` flag: `docker run -d nginx`.

#### Q3. How can I access a running container's shell?
A. Use `docker run -it [image] bash` to start a new container with a shell, or `docker exec -it [container-id] bash` to access a shell in an already running container.

#### Q4. How do I expose multiple ports?
A. Use multiple `-p` flags: `docker run -p 80:80 -p 443:443 nginx`.

#### Q5. How do I run a container with a specific user?
A. Use the `--user` flag: `docker run --user 1000:1000 nginx`.

## References

https://docs.docker.com/engine/reference/commandline/run/

## Revisions

- 2025/05/04 First revision