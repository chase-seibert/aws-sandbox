# Docker

Docker is a service container abstraction layer.

## Install

Don't try to install on Mac with `brew`, it's out of date. See: [http://zaiste.net/2014/02/lightweight_docker_experience_on_osx/](http://zaiste.net/2014/02/lightweight_docker_experience_on_osx/)

- On Mac, see: [https://github.com/boot2docker/osx-installer/releases/latest](https://github.com/boot2docker/osx-installer/releases/latest)

Without these, you will get a /var/run/docker.sock: no such file or directory error

```bash
boot2docker init
boot2docker up
eval "$(boot2docker shellinit)"
docker run ubuntu:14.04 /bin/echo 'Hello world'
```

## Example flask app

See the `docker/flask` directory.

```bash
cd docker/flask
docker build -t cseibert/flask-example .
boot2docker ip
docker run -it -p 5000:5000 cseibert/flask-example
docker login
docker push cseibert/flask-example
```

## Manaully run on AWS

```bash
# NOTE: important to use an Amazon Linux image, which has docker
aws ec2 run-instances --image-id ami-e7527ed7 --key-name cseibert --instance-type t2.micro
ssh ex2-user@ec2-54-187-79-119.us-west-2.compute.amazonaws.com
sudo yum install -y docker; sudo service docker start
# NOTE: no need to login!
sudo docker run -it -p 8000:5000 cseibert/flask-example
```
