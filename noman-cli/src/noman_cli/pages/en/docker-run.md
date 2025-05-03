# docker run command

Create and start a new container from a specified image.

## Overview

`docker run` creates and starts a container from a Docker image. It combines the functionality of `docker create` and `docker start` in a single command, allowing you to configure container settings, map ports, attach volumes, and execute commands inside the container.

## Options

### **-d, --detach**

Run the container in the background (detached mode)

```console
$ docker run -d nginx
e7cc5d3c8a14a02ad38c5f5509b9e38d2f5a253c7e387e7c19a38f11c7791893
```

### **-p, --publish [host_port]:[container_port]**

Map a port from the container to the host

```console
$ docker run -p 8080:80 nginx
```

### **-v, --volume [host_path]:[container_path]**

Mount a volume from the host to the container

```console
$ docker run -v /local/path:/container/path nginx
```

### **-e, --env**

Set environment variables

```console
$ docker run -e DB_HOST=localhost -e DB_PORT=5432 postgres
```

### **--name**

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

### **-it**

Run the container interactively with a terminal

```console
$ docker run -it ubuntu bash
root@7b2496ed8520:/#
```

## Usage Examples

### Running a web server and mapping ports

```console
$ docker run -d -p 8080:80 --name webserver nginx
3a67d1a87e116e54d8e7f8cd949619c4b5d2c9cef8ac31ce520fb024aed52bd9

$ curl localhost:8080
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

### Running a container with environment variables and volumes

```console
$ docker run -d \
  --name my-postgres \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -v pgdata:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:13
```

### Running a container interactively and removing it after exit

```console
$ docker run --rm -it alpine sh
/ # ls
bin    dev    etc    home   lib    media  mnt    opt    proc   root   run    sbin   srv    sys    tmp    usr    var
/ # exit
```

## Tips

### Use Named Volumes for Persistent Data

Instead of binding to host directories, use named volumes for better portability:
```console
$ docker run -v mydata:/app/data nginx
```

### Limit Container Resources

Control CPU and memory usage with `--cpus` and `--memory`:
```console
$ docker run --cpus=0.5 --memory=512m nginx
```

### Use Environment Files for Multiple Variables

For containers requiring many environment variables, use an env file:
```console
$ docker run --env-file ./env.list nginx
```

### Specify Restart Policies

Ensure containers restart after system reboots or crashes:
```console
$ docker run --restart=always nginx
```

## Frequently Asked Questions

#### Q1. What's the difference between `docker run` and `docker start`?
A. `docker run` creates and starts a new container, while `docker start` restarts an existing stopped container.

#### Q2. How do I run a container in the background?
A. Use the `-d` or `--detach` flag: `docker run -d nginx`.

#### Q3. How can I access a running container's shell?
A. Use `docker run -it [image] [shell]` when starting, or `docker exec -it [container] [shell]` for an already running container.

#### Q4. How do I stop a container started with `docker run`?
A. Use `docker stop [container_id or name]` to gracefully stop it.

#### Q5. Can I run Windows containers on Linux or vice versa?
A. No, containers share the host's kernel, so Linux containers require a Linux host (or WSL2 on Windows) and Windows containers require a Windows host.

## References

https://docs.docker.com/engine/reference/commandline/run/

## Revisions

- 2025/04/30 First revision