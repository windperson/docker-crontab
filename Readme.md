#### Usage

First, you need to find out your current \*nix system time zone,
To get linux local time zone:

Ubuntu 12: `cat /etc/timezone`

CentOS 6.x: `cat /etc/sysconfig/clock | sed -n 's/ZONE="\(.*\)"/\1/p'`

CentOS 7.x: `ls -l /etc/localtime | sed -n 's/.*\/zoneinfo\/\(.*\)/\1/p'`

Build docker image on project root folder:

`docker build -t docker-crontab .`

Then run it use following command:

```docker run --name cron -e TZ=$TZ -v `pwd`/src:/proj -v `pwd`/config:/conf -v /etc/localtime:/etc/localtime:ro -it docker-crontab bash```
