# docker command

Manage containers, images, networks, and other Docker resources.

## Overview

Docker is a platform that uses containerization to package applications and their dependencies together. The `docker` command is the primary interface for interacting with Docker, allowing you to build, run, and manage containers, images, networks, volumes, and other Docker resources.

## Options

### **docker run**

Create and start a container from an image

```console
$ docker run -d -p 80:80 --name webserver nginx
e7cc5d2c8cdc5b05a152f613a5b938c39b5932e0b4d4c0efcf6f8a210f6ffb4d
```

### **docker ps**

List running containers (add `-a` to show all containers)

```console
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS                               NAMES
e7cc5d2c8cdc   nginx     "/docker-entrypoint.…"   10 seconds ago   Up 9 seconds    0.0.0.0:80->80/tcp, :::80->80/tcp   webserver
```

### **docker images**

List available images on your system

```console
$ docker images
REPOSITORY    TAG       IMAGE ID       CREATED         SIZE
nginx         latest    605c77e624dd   2 weeks ago     142MB
python        3.9       a5d7930b60cc   3 weeks ago     915MB
ubuntu        20.04     ba6acccedd29   1 month ago     72.8MB
```

### **docker build**

Build an image from a Dockerfile

```console
$ docker build -t myapp:1.0 .
[+] Building 25.6s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 215B                                       0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/node:14                 1.2s
 => [1/5] FROM docker.io/library/node:14@sha256:fcb6...                    0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 12.5kB                                        0.0s
 => [2/5] WORKDIR /app                                                     0.5s
 => [3/5] COPY package*.json ./                                            0.1s
 => [4/5] RUN npm install                                                 20.5s
 => [5/5] COPY . .                                                         0.1s
 => exporting to image                                                     3.1s
 => => exporting layers                                                    3.0s
 => => writing image sha256:d15f...                                        0.0s
 => => naming to docker.io/library/myapp:1.0                               0.0s
```

## Usage Examples

### Running a container with port mapping and volume mounting

```console
$ docker run -d -p 8080:80 -v $(pwd)/html:/usr/share/nginx/html --name web-server nginx
f7d4a5c8b9e6d3f2a1c0b9e8d7f6a5c4b3a2f1d0
```

### Executing a command in a running container

```console
$ docker exec -it web-server bash
root@f7d4a5c8b9e6:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
```

### Stopping and removing a container

```console
$ docker stop web-server
web-server
$ docker rm web-server
web-server
```

### Building and tagging an image

```console
$ docker build -t myapp:latest .
[+] Building 15.3s (10/10) FINISHED
...
$ docker tag myapp:latest username/myapp:latest
```

## Tips

### Use Docker Compose for Multi-Container Applications

Instead of managing multiple containers with complex `docker run` commands, use Docker Compose with a `docker-compose.yml` file to define and run multi-container applications.

### Clean Up Unused Resources

Docker can accumulate unused containers, images, and volumes over time. Use `docker system prune` to remove all stopped containers, dangling images, and unused networks.

### Use .dockerignore Files

Create a `.dockerignore` file similar to `.gitignore` to prevent unnecessary files from being included in your Docker builds, making them faster and smaller.

### Leverage Docker Hub Official Images

Official images on Docker Hub are maintained, secure, and follow best practices. Use them as base images when possible instead of creating everything from scratch.

## Frequently Asked Questions

#### Q1. What's the difference between `docker run` and `docker start`?
A. `docker run` creates and starts a new container from an image, while `docker start` starts an existing stopped container.

#### Q2. How do I view logs for a container?
A. Use `docker logs [container_name]` to view logs. Add `-f` to follow the logs in real-time.

#### Q3. How can I access a shell in a running container?
A. Use `docker exec -it [container_name] bash` (or `sh` if bash isn't available).

#### Q4. How do I remove unused Docker images?
A. Use `docker image prune` to remove dangling images or `docker image prune -a` to remove all unused images.

#### Q5. How do I update a running container?
A. You can't directly update a running container. The recommended approach is to build a new image with updates, stop the old container, and start a new one.

## macOS Considerations

On macOS, Docker runs in a lightweight virtual machine since Docker requires Linux kernel features. This means:

- File system performance may be slower than on Linux, especially for volume mounts
- The Docker daemon's default resource limits (CPU, memory) may need adjustment in Docker Desktop preferences
- Network port binding works differently; use `localhost` rather than `0.0.0.0` when accessing exposed ports

## References

https://docs.docker.com/engine/reference/commandline/cli/

## Revisions

- 2025/04/30 First revision