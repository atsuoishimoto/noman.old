# docker build command

Build Docker images from a Dockerfile and a context.

## Overview

The `docker build` command creates Docker images from a Dockerfile and a build context. It executes the instructions in the Dockerfile to assemble a new image layer by layer. The build context is the set of files located in the specified PATH or URL.

## Options

### **-t, --tag**

Tag the built image with a name and optionally a tag in the 'name:tag' format.

```console
$ docker build -t myapp:1.0 .
[+] Building 10.5s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
 => => transferring dockerfile: 215B                                       0.0s
 => [internal] load .dockerignore                                          0.0s
 => => transferring context: 2B                                            0.0s
 => [internal] load metadata for docker.io/library/node:14                 1.2s
 => [1/5] FROM docker.io/library/node:14@sha256:123abc...                  0.0s
 => [internal] load build context                                          0.1s
 => => transferring context: 32.5kB                                        0.0s
 => [2/5] WORKDIR /app                                                     0.3s
 => [3/5] COPY package*.json ./                                            0.1s
 => [4/5] RUN npm install                                                  7.5s
 => [5/5] COPY . .                                                         0.2s
 => exporting to image                                                     1.0s
 => => exporting layers                                                    0.9s
 => => writing image sha256:def456...                                      0.1s
 => => naming to docker.io/library/myapp:1.0                               0.0s
```

### **-f, --file**

Specify the name of the Dockerfile (default is 'PATH/Dockerfile').

```console
$ docker build -f Dockerfile.prod -t myapp:prod .
[+] Building 12.3s (10/10) FINISHED
 => [internal] load build definition from Dockerfile.prod                  0.1s
 => => transferring dockerfile: 245B                                       0.0s
...
```

### **--no-cache**

Do not use cache when building the image.

```console
$ docker build --no-cache -t myapp .
[+] Building 25.7s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
...
```

### **--build-arg**

Set build-time variables defined in the Dockerfile with ARG.

```console
$ docker build --build-arg NODE_ENV=production -t myapp .
[+] Building 11.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
...
```

### **--target**

Set the target build stage to build in a multi-stage build.

```console
$ docker build --target development -t myapp:dev .
[+] Building 8.5s (8/8) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
...
```

## Usage Examples

### Building an image with a tag

```console
$ docker build -t myapp:latest .
[+] Building 15.2s (10/10) FINISHED
...
```

### Building with multiple tags

```console
$ docker build -t myapp:latest -t myapp:1.0 -t registry.example.com/myapp:1.0 .
[+] Building 15.5s (10/10) FINISHED
...
```

### Building from a Git repository

```console
$ docker build -t myapp https://github.com/user/repo.git#main
[+] Building 20.3s (10/10) FINISHED
...
```

### Building with a specific build context

```console
$ docker build -t myapp -f ./docker/Dockerfile ./app
[+] Building 14.8s (10/10) FINISHED
...
```

## Tips

### Use .dockerignore Files

Create a `.dockerignore` file to exclude files and directories from the build context, similar to `.gitignore`. This reduces build time and image size by preventing unnecessary files from being sent to the Docker daemon.

### Leverage Build Cache

Docker caches intermediate layers. Order your Dockerfile instructions so that the ones least likely to change (like installing dependencies) come before those that change frequently (like copying source code).

### Use Multi-stage Builds

Multi-stage builds allow you to use multiple FROM statements in your Dockerfile. This is useful for creating smaller production images by copying only the necessary artifacts from a build stage.

### Minimize Layer Count

Combine related commands with `&&` and clean up in the same RUN instruction to reduce the number of layers and image size.

## Frequently Asked Questions

#### Q1. What is the build context?
A. The build context is the set of files at a specified location (PATH or URL) that are sent to the Docker daemon during the build. The Dockerfile is usually located at the root of the build context.

#### Q2. How can I reduce Docker image size?
A. Use multi-stage builds, minimize the number of layers, clean up after package installations, and use a smaller base image like Alpine.

#### Q3. Why is my build slow?
A. Large build contexts, not using build cache, or complex build operations can slow down builds. Use `.dockerignore` to exclude unnecessary files and optimize your Dockerfile.

#### Q4. How do I pass environment variables to the build process?
A. Use the `--build-arg` flag to pass variables that can be used with ARG instructions in your Dockerfile.

#### Q5. How do I build only a specific stage in a multi-stage Dockerfile?
A. Use the `--target` flag followed by the name of the build stage you want to build up to.

## References

https://docs.docker.com/engine/reference/commandline/build/

## Revisions

- 2025/04/30 First revision