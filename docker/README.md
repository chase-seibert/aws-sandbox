# Docker

Docker is a service container abstraction layer.

## Install

Don't try to install on Mac with `brew`, it's out of date. See: [http://zaiste.net/2014/02/lightweight_docker_experience_on_osx/](http://zaiste.net/2014/02/lightweight_docker_experience_on_osx/)

- On Mac, see: [https://github.com/boot2docker/osx-installer/releases/latest](https://github.com/boot2docker/osx-installer/releases/latest)

```bash
boot2docker init
boot2docker up
# without these, you will get a /var/run/docker.sock: no such file or directory error
# Run the exports from boot2docker shellinit
docker run ubuntu:14.04 /bin/echo 'Hello world'
```

- On Linux, see: [https://docs.docker.com/installation/ubuntulinux/](https://docs.docker.com/installation/ubuntulinux/)

## Common Commands

```bash
docker images
docker search
docker pull
```

## Running a Python app

First, you need to install docker compose with:

```bash
virtualenv .virtualenv
source .virtualenv/bin/activate
pip install -U docker-compose
```

This will use [Docker compose](https://docs.docker.com/compose/). See the `flask` app directory, and run `docker-compose up`. You can access the flash app on the same IP that is shown with `boot2docker ip`, port `5000`, or just run `open "http://$(boot2docker ip):5000"`.

## Common Commands

```bash
docker-compose up -d
docker-compose ps
docker-compose logs
```

# Docker-machine

Docker machine automates some of this; it's kind of like virtualenv for Docker. You can also use it to create a VM for AWS along with the code. It doesn't even have a binary installer, you need to download a binary and copy it into your path.

```bash
wget https://github.com/docker/machine/releases/download/v0.1.0/docker-machine_darwin-amd64
chmod +x docker-machine_darwin-amd64
mv docker-machine_darwin-amd64 /usr/local/bin/docker-machine
```

To create the above docker VM, complete with downloading boot2docker, you can now just run:

```bash
docker-machine create --driver virtualbox test
# activate this docker
$(docker-machine env test)
docker-machine ls
docker-compose up  # this runs inside the new machine
```

## Deploying to AWS (EC2, not Elastic Beanstalk)

```bash
docker-machine create \
--driver amazonec2 \
--amazonec2-access-key your-aws-access-key \
--amazonec2-secret-key your-aws-secret-key \
--amazonec2-vpc-id your-aws-vpc-id \
--amazonec2-subnet-id your-aws-subnet-id \
--amazonec2-region us-east-1 \
--amazonec2-zone a \
ec2box
```

**Note**: You MUST have public IPs enabled, and provide that subnet info.


## Docker and Elastic Beanstalk

- [Official Documentation](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create_deploy_docker.html)

*Note*: there is a separate command line tool called `eb`, which you must install. Again, binaries! Or, you can just zip up the directory and install the docker app manually in their UI.

*Note2:* your project must be its own git repo.

```bash
cp -r flask/ ~/projects/flask
cd ~/projects/flask
git init .
eb init
# make sure to select the a stack w/ Docker available
eb start
# this will deploy the demo app, because you did not commit
git add .
git commit -m first\ commit
eb push  # you may need to pip install boto
```

Yes, this takes forever to start, but just the first time.

### Common Commands

``bash
eb logs
```
