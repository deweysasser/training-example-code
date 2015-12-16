JENKINS_IMAGE=deweysasser/training-jenkins

all:  project

jenkins:  jenkins-image jenkins-volume
	@-docker rm -f tjenkins
	docker run -d -p 8080:8080 --volumes-from jenkins-volume --name tjenkins $(JENKINS_IMAGE)

jenkins-volume: jenkins-image
	docker ps -a | grep -q jenkins-volume  && echo Volume exists || docker create --name jenkins-volume $(JENKINS_IMAGE)

jenkins-image: 
	docker build -t $(JENKINS_IMAGE) docker/jenkins

project:
	docker build -t my-project -f docker/project/Dockerfile .
	-@docker rm -f my-project
	docker run  -p 5000:5000 --name my-project my-project

test-example:
	cd code/testing; make