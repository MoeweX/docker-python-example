# Docker Python Example

This example starts a docker image with a Flask web server that outputs the name of the host and greets whoever is specified in the Dockerfile's ENV variable **Name**.
The example is partly based on the content of Docker's official [getting started guide](https://docs.docker.com/get-started/).

Note, that the example does not use a Redis server for persistence (as in the getting started guide). Instead, the number of visits is stored either in the container itself, or in a persistent volume (see commands below). It is possible to start multiple containers that update the same volume, but note that no concurrency mechanisms are implemented.

## Commands of interest

* `docker info`
* `docker image ls`
* `docker container ls`
* `docker build -t docker-python-example .` - Builds the container
* `docker run -p 4000:80 docker-python-example` - Starts container on port 4000 (add -d to run in background)
* `docker run -p 4000:80 -v dataShare:/data docker-python-example` - Starts container on port 4000, mounts the dataShare volume (create first with `docker volume create --name dataShare`)
* `docker container stop <<id>>`

To remove all images and containers:
```
#!/bin/bash
# Delete all containers
docker rm $(docker ps -a -q)
# Delete all images
docker rmi $(docker images -q)
```
