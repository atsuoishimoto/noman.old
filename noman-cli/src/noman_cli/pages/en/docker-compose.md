# docker-compose command

Define and run multi-container Docker applications.

## Overview

Docker Compose is a tool for defining and running multi-container Docker applications. With a YAML file, you configure your application's services, networks, and volumes, then start all services with a single command. It simplifies the process of managing complex applications that require multiple interconnected containers.

## Options

### **up**

Start containers defined in the docker-compose.yml file

```console
$ docker-compose up
Creating network "myproject_default" with the default driver
Creating myproject_db_1    ... done
Creating myproject_redis_1 ... done
Creating myproject_web_1   ... done
Attaching to myproject_db_1, myproject_redis_1, myproject_web_1
```

### **down**

Stop and remove containers, networks, images, and volumes

```console
$ docker-compose down
Stopping myproject_web_1   ... done
Stopping myproject_redis_1 ... done
Stopping myproject_db_1    ... done
Removing myproject_web_1   ... done
Removing myproject_redis_1 ... done
Removing myproject_db_1    ... done
Removing network myproject_default
```

### **ps**

List containers managed by docker-compose

```console
$ docker-compose ps
       Name                     Command               State           Ports
-----------------------------------------------------------------------------------
myproject_db_1      docker-entrypoint.sh mysqld      Up      3306/tcp, 33060/tcp
myproject_redis_1   docker-entrypoint.sh redis ...   Up      6379/tcp
myproject_web_1     docker-entrypoint.sh php-fpm     Up      9000/tcp
```

### **logs**

View output from containers

```console
$ docker-compose logs web
Attaching to myproject_web_1
web_1  | [30-Apr-2025 10:15:30] NOTICE: fpm is running, pid 1
web_1  | [30-Apr-2025 10:15:30] NOTICE: ready to handle connections
```

### **build**

Build or rebuild services

```console
$ docker-compose build
Building web
Step 1/10 : FROM php:7.4-fpm
 ---> 2a78649a8a79
Step 2/10 : RUN apt-get update
 ---> Using cache
 ---> 7f41c1f2c2d3
...
Successfully built 3a7e6d23f5a2
Successfully tagged myproject_web:latest
```

## Usage Examples

### Starting containers in detached mode

```console
$ docker-compose up -d
Creating myproject_db_1    ... done
Creating myproject_redis_1 ... done
Creating myproject_web_1   ... done
```

### Scaling a specific service

```console
$ docker-compose up -d --scale web=3
Creating myproject_db_1    ... done
Creating myproject_redis_1 ... done
Creating myproject_web_1   ... done
Creating myproject_web_2   ... done
Creating myproject_web_3   ... done
```

### Running a command in a service container

```console
$ docker-compose exec web php artisan migrate
Migration table created successfully.
Migrating: 2023_04_30_create_users_table
Migrated:  2023_04_30_create_users_table
```

### Viewing logs with follow option

```console
$ docker-compose logs -f
Attaching to myproject_web_1, myproject_redis_1, myproject_db_1
web_1    | [30-Apr-2025 10:15:30] NOTICE: fpm is running, pid 1
redis_1  | 1:C 30 Apr 2025 10:15:30.000 # oO0OoO0OoO0Oo Redis is starting oO0OoO0OoO0Oo
db_1     | 2025-04-30T10:15:30.000000Z 0 [Note] mysqld: ready for connections.
```

## Tips

### Use Environment Variables

Store sensitive information like passwords in a `.env` file instead of hardcoding them in your docker-compose.yml file.

```console
$ cat .env
DB_PASSWORD=secret
```

### Version Control Your Compose File

Keep your docker-compose.yml in version control, but exclude the .env file to avoid exposing sensitive information.

### Use Named Volumes for Persistence

Named volumes ensure your data persists even when containers are removed.

```yaml
volumes:
  db_data:
```

### Use docker-compose.override.yml

Create a `docker-compose.override.yml` file for environment-specific settings that shouldn't be in version control.

## Frequently Asked Questions

#### Q1. What's the difference between `docker-compose up` and `docker-compose start`?
A. `up` creates and starts containers based on your configuration, while `start` only starts existing containers that were previously created and stopped.

#### Q2. How do I update a single service?
A. Use `docker-compose up --build <service_name>` to rebuild and update a specific service.

#### Q3. Can I use Docker Compose in production?
A. While possible, Docker Compose is primarily designed for development and testing. For production, consider Docker Swarm or Kubernetes.

#### Q4. How do I specify a different compose file?
A. Use the `-f` flag: `docker-compose -f custom-compose.yml up`.

## References

https://docs.docker.com/compose/

## Revisions

- 2025/04/30 First revision