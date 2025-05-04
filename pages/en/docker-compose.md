# docker-compose command

Define and run multi-container Docker applications.

## Overview

Docker Compose is a tool for defining and running multi-container Docker applications. With a YAML file, you configure your application's services, networks, and volumes, then start all services with a single command. It simplifies the process of managing multiple containers that work together as part of an application.

## Options

### **-f, --file FILE**

Specify an alternate compose file (default: docker-compose.yml)

```console
$ docker-compose -f custom-compose.yml up
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_db_1  ... done
```

### **-p, --project-name NAME**

Specify an alternate project name (default: directory name)

```console
$ docker-compose -p myproject up
Creating network "myproject_default" with the default driver
Creating myproject_web_1 ... done
Creating myproject_db_1  ... done
```

### **--verbose**

Show more output

```console
$ docker-compose --verbose up
compose.config.config.find: Using configuration files: ./docker-compose.yml
docker.auth.find_config_file: Trying paths: ['/home/user/.docker/config.json', '/home/user/.dockercfg']
docker.auth.find_config_file: Found file at path: /home/user/.docker/config.json
...
```

### **--log-level LEVEL**

Set log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

```console
$ docker-compose --log-level INFO up
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_db_1  ... done
```

## Common Commands

### **up**

Create and start containers

```console
$ docker-compose up -d
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_db_1  ... done
```

### **down**

Stop and remove containers, networks, images, and volumes

```console
$ docker-compose down
Stopping myapp_web_1 ... done
Stopping myapp_db_1  ... done
Removing myapp_web_1 ... done
Removing myapp_db_1  ... done
Removing network myapp_default
```

### **ps**

List containers

```console
$ docker-compose ps
    Name                  Command               State           Ports
-----------------------------------------------------------------------------
myapp_db_1    docker-entrypoint.sh mysqld      Up      3306/tcp, 33060/tcp
myapp_web_1   docker-php-entrypoint php-fpm    Up      9000/tcp
```

### **logs**

View output from containers

```console
$ docker-compose logs
Attaching to myapp_web_1, myapp_db_1
db_1   | 2025-05-04T10:15:30.123456Z 0 [Note] mysqld: ready for connections.
web_1  | [04-May-2025 10:15:32] NOTICE: fpm is running, pid 1
```

### **exec**

Execute a command in a running container

```console
$ docker-compose exec web php -v
PHP 8.2.0 (cli) (built: Dec 6 2024) (NTS)
Copyright (c) The PHP Group
Zend Engine v4.2.0, Copyright (c) Zend Technologies
```

### **build**

Build or rebuild services

```console
$ docker-compose build
Building web
Step 1/10 : FROM php:8.2-fpm
 ---> 123456789abc
Step 2/10 : WORKDIR /var/www/html
 ---> Using cache
 ---> abcdef123456
...
Successfully built 987654321fed
Successfully tagged myapp_web:latest
```

## Usage Examples

### Basic Web Application with Database

```console
$ cat docker-compose.yml
version: '3'
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: myapp

$ docker-compose up -d
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_db_1  ... done
```

### Scaling Services

```console
$ docker-compose up -d --scale web=3
Creating network "myapp_default" with the default driver
Creating myapp_web_1 ... done
Creating myapp_web_2 ... done
Creating myapp_web_3 ... done
Creating myapp_db_1  ... done
```

## Tips

### Use Environment Variables

Store sensitive information like passwords in a `.env` file instead of hardcoding them in your docker-compose.yml file.

```console
$ cat .env
DB_PASSWORD=secretpassword

$ cat docker-compose.yml
version: '3'
services:
  db:
    image: mysql:8.0
    environment:
      MYSQL_ROOT_PASSWORD: ${DB_PASSWORD}
```

### Use Profiles for Selective Service Startup

Profiles allow you to start only specific services when needed.

```console
$ cat docker-compose.yml
version: '3.9'
services:
  app:
    image: myapp
  db:
    image: mysql
  test:
    image: myapp-test
    profiles:
      - testing

$ docker-compose --profile testing up
```

### Use Docker Compose Override Files

Create a `docker-compose.override.yml` file to override settings in your main compose file without modifying it.

```console
$ cat docker-compose.yml
version: '3'
services:
  web:
    image: nginx

$ cat docker-compose.override.yml
version: '3'
services:
  web:
    ports:
      - "8080:80"
    volumes:
      - ./html:/usr/share/nginx/html
```

## Frequently Asked Questions

#### Q1. What's the difference between `docker-compose up` and `docker-compose up -d`?
A. `docker-compose up` starts containers and shows their output in the terminal. The `-d` flag (detached mode) runs containers in the background.

#### Q2. How do I update a single service without affecting others?
A. Use `docker-compose up -d --no-deps --build service_name` to rebuild and update a specific service without restarting dependent services.

#### Q3. How can I view logs for a specific service?
A. Use `docker-compose logs service_name` to view logs for a specific service. Add `-f` to follow the logs in real-time.

#### Q4. Can I use Docker Compose in production?
A. While Docker Compose can be used in production, Docker Swarm or Kubernetes are often preferred for production deployments due to their additional orchestration features.

#### Q5. How do I clean up unused volumes?
A. Use `docker-compose down -v` to remove containers, networks, and volumes defined in your compose file.

## References

https://docs.docker.com/compose/reference/

## Revisions

2025/05/04 First revision