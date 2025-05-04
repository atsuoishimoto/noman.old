# docker command

Manage Docker containers, images, networks, and other Docker objects.

## Overview

Docker is a platform that allows you to develop, ship, and run applications in containers. The `docker` command is the primary interface for interacting with Docker, enabling you to build, run, and manage containers, images, networks, volumes, and other Docker resources. It provides a consistent environment for applications to run regardless of the host system.

## Options

### **docker run**

Create and start a new container from an image

```console
$ docker run -d --name web nginx
e7cc5d2c8cdc5b05a4f37ce6cf15e9f0e0a5bd2bec30cc5415917d669de12857
```

### **docker ps**

List running containers (add `-a` to show all containers including stopped ones)

```console
$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS     NAMES
e7cc5d2c8cdc   nginx     "/docker-entrypoint.…"   10 seconds ago   Up 9 seconds    80/tcp    web
```

### **docker images**

List available images on your local system

```console
$ docker images
REPOSITORY   TAG       IMAGE ID       CREATED        SIZE
nginx        latest    a6bd71f48f68   2 weeks ago    187MB
ubuntu       latest    3b418d7b466a   4 weeks ago    77.8MB
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
 => => transferring context: 1.25kB                                        0.0s
 => [2/5] WORKDIR /app                                                     0.5s
 => [3/5] COPY package*.json ./                                            0.1s
 => [4/5] RUN npm install                                                 20.5s
 => [5/5] COPY . .                                                         0.1s
 => exporting to image                                                     3.1s
 => => exporting layers                                                    3.1s
 => => writing image sha256:a1b2c3d4e5f6...                                0.0s
 => => naming to docker.io/library/myapp:1.0                               0.0s
```

### **docker stop/start**

Stop or start existing containers

```console
$ docker stop web
web

$ docker start web
web
```

### **docker exec**

Run a command in a running container

```console
$ docker exec -it web bash
root@e7cc5d2c8cdc:/# ls
bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var
root@e7cc5d2c8cdc:/# exit
```

## Usage Examples

### Running a container with port mapping

```console
$ docker run -d -p 8080:80 --name webserver nginx
f499cc406d7e9d92537dec4182f2d0f9f9dbf74e2d9651c3c4c94a7b8a023c15

$ curl http://localhost:8080
<!DOCTYPE html>
<html>
<head>
<title>Welcome to nginx!</title>
...
```

### Building and running a custom application

```console
$ docker build -t myapp:latest .
[+] Building 15.3s (10/10) FINISHED
...

$ docker run -d -p 3000:3000 --name myapplication myapp:latest
a72f4623b8bfb647e8b108f770e5758eed96a37638e929278169a105ea86c912
```

### Managing container data with volumes

```console
$ docker volume create mydata
mydata

$ docker run -d --name database -v mydata:/var/lib/mysql mysql:8.0
b8a1c375e3c2a9c0293bb9d4f9a6b1e7f2d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9
```

## Tips

### Use Docker Compose for Multi-Container Applications

Instead of managing multiple containers with complex `docker run` commands, use Docker Compose with a `docker-compose.yml` file to define and run multi-container applications.

```console
$ docker-compose up -d
```

### Clean Up Unused Resources

Docker can accumulate unused containers, images, and volumes over time. Use these commands to clean up:

```console
$ docker system prune  # Remove all stopped containers, unused networks, dangling images
$ docker system prune -a  # Also remove unused images, not just dangling ones
$ docker volume prune  # Remove unused volumes
```

### Use Multi-Stage Builds for Smaller Images

Multi-stage builds in Dockerfiles help create smaller production images by separating build-time dependencies from runtime dependencies.

```dockerfile
FROM node:14 AS build
WORKDIR /app
COPY . .
RUN npm ci && npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
```

### Use .dockerignore

Create a `.dockerignore` file similar to `.gitignore` to prevent unnecessary files from being included in your Docker build context, which speeds up builds and reduces image size.

## Frequently Asked Questions

#### Q1. What's the difference between `docker run` and `docker start`?
A. `docker run` creates and starts a new container from an image, while `docker start` restarts a stopped container that already exists.

#### Q2. How do I access logs from a container?
A. Use `docker logs [container_name]` to view logs. Add `-f` to follow the logs in real-time.

#### Q3. How can I copy files between my host and a container?
A. Use `docker cp [source] [destination]`. For example: `docker cp ./file.txt mycontainer:/app/` or `docker cp mycontainer:/app/file.txt ./`.

#### Q4. How do I remove containers and images?
A. Use `docker rm [container_id]` to remove a container and `docker rmi [image_id]` to remove an image. Add `-f` to force removal.

#### Q5. How can I see resource usage of my containers?
A. Use `docker stats` to see CPU, memory, network, and disk usage of running containers.

## References

https://docs.docker.com/engine/reference/commandline/cli/

## Revisions

- 2025/05/04 First revision