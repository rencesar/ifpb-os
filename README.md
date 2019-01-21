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
