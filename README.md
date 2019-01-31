# IFPB - OS
Operational Systems Project, behave analyzes of Django Web App.


## Set-up

This application works with Docker Compose, thereupon We first need to install Docker, and Docker Compose, and Git.

### Installing Docker

1. Following this tutorial you can install docker:
    https://docs.docker.com/install/linux/docker-ce/debian/

1. Install docker Compose
    https://docs.docker.com/compose/install/
  
### Pulling the code

1. Install git

```
$ apt-get install git
```

2. Pulling the code
```
$ git clone https://github.com/rencesar/ifpb-os.git
```

### Starting App

1. Access Project Folder

1. Generate your Django Secret Key
    * Access this [link](https://www.miniwebtool.com/django-secret-key-generator/) and generate your secret key

1. Add environment variables
    * You can add them permanently
        ```
        $ echo 'export DJANGO_SECRET_KEY="PUT YOUR SECRET KEY HERE"' >> ~/.bashrc
        ```
        Be aware that if you go with this option you must restart your terminal.

    * or temporarily
        ```
        $ export DJANGO_SECRET_KEY="PUT YOUR SECRET KEY HERE"
        ```
1. Change file permissions
    ```
    $ chmod +x entrypoint.sh
    ```
1. Install Docker and Docker-compose
    * Follow this [tutorial](https://docs.docker.com/install/)
1. Running applications
    ```
    $ docker-compose up --build
    ```
1. Access the page
    Open your browser and go to http://127.0.0.1
    
## Info

This application works Django(Web App), Postgres(DataBase), Nginx(Http Server), Docker Compose, Docker.

## Activities

### Activities 3

* Monitoring application
Knowing that this is a Web application We can not use time on the server because the idea is that it will be running all the time, so what We are going to do here is use `curl` to measure the response of the server.

1. With Empty database:
    ```
    $ time curl -X GET http://127.0.0.1/section/
    []
    real 0m0.021s
    user 0m0.004s
    sys  0m0.000s
    ```
2. Pushing data to the database
   ```
    $ time curl -H "Accept: application/json" -H "Content-Type: application/json" --request POST --data '{"name": "fruit", "max_allowed_items": 3000, "description": "Sells fruits", "temperature": 25}' http://127.0.0.1/section/
    {"name":"fruit","max_allowed_items":3000,"description":"Sells fruits","temperature":25}
    real    0m0.142s
    user    0m0.004s
    sys     0m0.000s
   ```

   ```
    $ time curl -H "Accept: application/json" -H "Content-Type: application/json" --request POST --data '{"name": "fruit", "max_allowed_items": 3000, "description": "Sells fruits", "temperature": 25}' http://127.0.0.1/section/
    {"name":"fruit","max_allowed_items":3000,"description":"Sells fruits","temperature":25}
    real    0m0.023s
    user    0m0.008s
    sys     0m0.000s
   ```


  ENV           |  OPERATION                 |  1        |  2        |  3        |  4        |  5        |  6        |  7        |  8        |  9        |  10     
 ---------------|----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------
 1CPU - 2GB RAM |**Getting data** - `real`   | 0m0.021s  | 0m0.012s  | 0m0.013s  | 0m0.018s  | 0m0.023s  | 0m0.016s  | 0m0.024s  | 0m0.025s  | 0m0.029s  | 0m0.013s
 1CPU - 2GB RAM |**Getting data** - `user`   | 0m0.004s  | 0m0.000s  | 0m0.004s  | 0m0.004s  | 0m0.000s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.000s
 1CPU - 2GB RAM |**Getting data** - `sys`    | 0m0.000s  | 0m0.004s  | 0m0.004s  | 0m0.000s  | 0m0.004s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.004s
 ---------------|----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------
 1CPU - 2GB RAM |**Inserting data** - `real` | 0m0.142s  | 0m0.029s  | 0m0.021s  | 0m0.023s  | 0m0.025s  | 0m0.026s  | 0m0.022s  | 0m0.019s  | 0m0.022s  | 0m0.020s
 1CPU - 2GB RAM |**Inserting data** - `user` | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.000s  | 0m0.004s  | 0m0.004s
 1CPU - 2GB RAM |**Inserting data** - `sys`  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.004s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.004s  | 0m0.000s  | 0m0.000s
 ---------------|----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------
 2CPU - 2GB RAM |**Getting data** - `real`   | 0m0.131s  | 0m0.015s  | 0m0.014s  | 0m0.016s  | 0m0.015s  | 0m0.014s  | 0m0.013s  | 0m0.015s  | 0m0.017s  | 0m0.013s
 2CPU - 2GB RAM |**Getting data** - `user`   | 0m0.004s  | 0m0.004s  | 0m0.000s  | 0m0.004s  | 0m0.000s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s
 2CPU - 2GB RAM |**Getting data** - `sys`    | 0m0.000s  | 0m0.000s  | 0m0.004s  | 0m0.000s  | 0m0.004s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.000s
 ---------------|----------------------------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------|-----------
 2CPU - 2GB RAM |**Inserting data** - `real` | 0m0.022s  | 0m0.021s  | 0m0.021s  | 0m0.016s  | 0m0.017s  | 0m0.020s  | 0m0.022s  | 0m0.016s  | 0m0.016s  | 0m0.017s
 2CPU - 2GB RAM |**Inserting data** - `user` | 0m0.004s  | 0m0.000s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s  | 0m0.004s
 2CPU - 2GB RAM |**Inserting data** - `sys`  | 0m0.000s  | 0m0.004s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.000s  | 0m0.000s


* Monitoring with command `top`

![TOP command result](/info/images/top.png)

You can check that docker-compose and gunicorn are using arround 1.4% for docker-compose and 1.7% for gunicorn, of memory and both are using 0.3% of the CPU.
But what is gunicorn? Gunicorn is a Python WSGI HTTP Server for UNIX, in the end my webapp.


* Monitoring with `strace`

 - Strace on Getting data
```
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0        37           read
  0.00    0.000000           0         2           write
  0.00    0.000000           0        42         6 open
  0.00    0.000000           0        40           close
  0.00    0.000000           0         4         4 stat
  0.00    0.000000           0        37           fstat
  0.00    0.000000           0         2           poll
  0.00    0.000000           0        84           mmap
  0.00    0.000000           0        68           mprotect
  0.00    0.000000           0         1           munmap
  0.00    0.000000           0         6           brk
  0.00    0.000000           0        18           rt_sigaction
  0.00    0.000000           0         1           rt_sigprocmask
  0.00    0.000000           0         1           ioctl
  0.00    0.000000           0        35        35 access
  0.00    0.000000           0         1           pipe
  0.00    0.000000           0         2           socket
  0.00    0.000000           0         1         1 connect
  0.00    0.000000           0         1           sendto
  0.00    0.000000           0         1           recvfrom
  0.00    0.000000           0         1           getsockname
  0.00    0.000000           0         1           getpeername
  0.00    0.000000           0         4           setsockopt
  0.00    0.000000           0         1           getsockopt
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         2           fcntl
  0.00    0.000000           0         1           getrlimit
  0.00    0.000000           0         1           arch_prctl
  0.00    0.000000           0         1           futex
  0.00    0.000000           0         1           set_tid_address
  0.00    0.000000           0         1           set_robust_list
  0.00    0.000000           0         1           getrandom
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000                   400        46 total
```

 - Strace on Inserting data

```
% time     seconds  usecs/call     calls    errors syscall
------ ----------- ----------- --------- --------- ----------------
  0.00    0.000000           0        37           read
  0.00    0.000000           0         1           write
  0.00    0.000000           0        42         6 open
  0.00    0.000000           0        40           close
  0.00    0.000000           0         4         4 stat
  0.00    0.000000           0        37           fstat
  0.00    0.000000           0         6           poll
  0.00    0.000000           0        84           mmap
  0.00    0.000000           0        68           mprotect
  0.00    0.000000           0         1           munmap
  0.00    0.000000           0         6           brk
  0.00    0.000000           0        24           rt_sigaction
  0.00    0.000000           0         1           rt_sigprocmask
  0.00    0.000000           0         1           ioctl
  0.00    0.000000           0        35        35 access
  0.00    0.000000           0         1           pipe
  0.00    0.000000           0         2           socket
  0.00    0.000000           0         1         1 connect
  0.00    0.000000           0         1           sendto
  0.00    0.000000           0         1           recvfrom
  0.00    0.000000           0         1           getsockname
  0.00    0.000000           0         1           getpeername
  0.00    0.000000           0         4           setsockopt
  0.00    0.000000           0         1           getsockopt
  0.00    0.000000           0         1           execve
  0.00    0.000000           0         2           fcntl
  0.00    0.000000           0         1           getrlimit
  0.00    0.000000           0         1           arch_prctl
  0.00    0.000000           0         1           futex
  0.00    0.000000           0         1           set_tid_address
  0.00    0.000000           0         1           set_robust_list
  0.00    0.000000           0         1           getrandom
------ ----------- ----------- --------- --------- ----------------
100.00    0.000000                   409        46 total
```