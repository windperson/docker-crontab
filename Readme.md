#docker-crontab

A crontab replacement for running periodical jobs in server.

## Usage

First, you need to find out your current \*nix system time zone,
To get linux local time zone:

Ubuntu 12: ``cat /etc/timezone``

CentOS 6.x: ``cat /etc/sysconfig/clock | sed -n 's/ZONE="\(.*\)"/\1/p'``

CentOS 7.x: ``ls -l /etc/localtime | sed -n 's/.*\/zoneinfo\/\(.*\)/\1/p'``

## Develop

Build docker image using script in sh folder:

```./sh/devcli.sh -b```

you can change running python version by change the preceeding **PYTHON_VER** environemnt variable:

 ```PYTHON_VER=3 ./sh/devcli.sh -b```
 
 default value, will build Python 3.5.x image.
 
 
```PYTHON_VER=3.4 ./sh/devcli.sh -b```
 
build image using Python 3.4.x


```PYTHON_VER=2 ./sh/devcli.sh -b```

build image using Python 2.7.x

Or just run with omitting the *-b* parameter to go into docker cli to play with it. 

## Prepeare for distribute or running as docker container

Make distributable image:

```docker-compose build```

You can also prepend the **PYTHON_VER** envrionment varaible just as in previous section, to build different images with the specified version of Python. 

Run distributable image by following command:

```docker run --name cron -e TZ=$TZ -e crontab_paths=/test_cron/test.crontab -e CIRCUS_LOG_LEVEL=debug -v `pwd`/src:/proj -v `pwd`/config:/conf -v /etc/localtime:/etc/localtime:ro -it docker-crontab bash```
