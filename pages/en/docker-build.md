# docker build command

Build an image from a Dockerfile.

## Overview

The `docker build` command builds Docker images from a Dockerfile and a "context". The context is the set of files located in the specified PATH or URL. The build process can refer to any of the files in the context. The Dockerfile contains instructions that Docker uses to create a new image.

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
 => [5/5] COPY . .                                                         0.1s
 => exporting to image                                                     1.1s
 => => exporting layers                                                    1.1s
 => => writing image sha256:def456...                                      0.0s
 => => naming to docker.io/library/myapp:1.0                               0.0s
```

### **-f, --file**

Specify the name of the Dockerfile (default is 'PATH/Dockerfile').

```console
$ docker build -f Dockerfile.prod -t myapp:prod .
[+] Building 12.3s (10/10) FINISHED
 => [internal] load build definition from Dockerfile.prod                  0.1s
 => => transferring dockerfile: 256B                                       0.0s
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

Set build-time variables defined in the Dockerfile using ARG instructions.

```console
$ docker build --build-arg NODE_ENV=production -t myapp .
[+] Building 11.2s (10/10) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
...
```

### **--target**

Set the target build stage to build when using multi-stage builds.

```console
$ docker build --target development -t myapp:dev .
[+] Building 8.3s (8/8) FINISHED
 => [internal] load build definition from Dockerfile                       0.1s
 => [internal] load .dockerignore                                          0.0s
 => [internal] load metadata for docker.io/library/node:14                 1.2s
 => [development 1/4] FROM docker.io/library/node:14@sha256:123abc...      0.0s
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
$ docker build -t myapp:latest -t myapp:1.0 -t registry.example.com/myapp:latest .
[+] Building 14.8s (10/10) FINISHED
...
```

### Building from a specific context

```console
$ docker build -t myapp https://github.com/user/repo.git#main
[+] Building 22.5s (10/10) FINISHED
...
```

### Building with a specific Dockerfile and target stage

```console
$ docker build -f Dockerfile.multistage --target production -t myapp:prod .
[+] Building 18.7s (12/12) FINISHED
...
```

## Tips

### Use .dockerignore Files

Create a `.dockerignore` file to exclude files and directories from the build context. This reduces build time and size by preventing unnecessary files from being sent to the Docker daemon.

### Leverage Build Cache

Docker caches intermediate layers. Order your Dockerfile commands from least to most frequently changing to maximize cache usage. For example, install dependencies before copying application code.

### Use Multi-stage Builds

Multi-stage builds allow you to use multiple FROM statements in your Dockerfile. This is useful for creating smaller production images by copying only necessary artifacts from a build stage.

### Minimize Layer Count

Combine related commands with `&&` in a single RUN instruction to reduce the number of layers, which helps create smaller images.

## Frequently Asked Questions

#### Q1. What's the difference between `docker build` and `docker image build`?
A. They are the same command. `docker image build` is the more explicit form that was introduced with Docker's command restructuring, but `docker build` is still supported and more commonly used.

#### Q2. How do I build an image without using cache?
A. Use the `--no-cache` option: `docker build --no-cache -t myapp .`

#### Q3. How can I pass environment variables to the build process?
A. Use the `--build-arg` option: `docker build --build-arg VAR_NAME=value -t myapp .`

#### Q4. How do I specify which stage to build in a multi-stage Dockerfile?
A. Use the `--target` option: `docker build --target stage_name -t myapp .`

#### Q5. Can I build from a Git repository?
A. Yes, you can specify a Git repository URL as the build context: `docker build -t myapp https://github.com/user/repo.git`

## References

https://docs.docker.com/engine/reference/commandline/build/

## Revisions

- 2025/05/04 First revision