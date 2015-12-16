#!/bin/bash

# Purpose:  make sure we have a running Jenkins

JENKINS_IMAGE=deweysasser/training-jenkins

docker build -t ${JENKINS_IMAGE} docker/jenkins

docker ps -a | grep -q jenkins-volume  && echo Volume exists || docker create --name jenkins-volume ${JENKINS_IMAGE}

# allowed to fail
docker rm -f tjenkins > /dev/null 2>&1
docker run -d -p 8080:8080 --volumes-from jenkins-volume --name tjenkins ${JENKINS_IMAGE}
