JENKINS_IMAGE=deweysasser/training-jenkins

# By default make will execute on the first target.  This will make that run your project by default
all:  project

# Run project unit tests
project-test:
	cd code/project; test -f Makefile && make || python -m unittest discover

# Run a docker volume containing project, listening on port 5000
project: project-test
	docker build -t my-project -f docker/project/Dockerfile .
	-@docker rm -f my-project
	docker run  -p 5000:5000 --name my-project my-project

# Create an up-to-date, running jenkins.  Recreates jenkins each time, but data will be preserved in jenkins-volume
jenkins:  jenkins-image jenkins-volume
	@-docker rm -f tjenkins
	docker run -d -p 8080:8080 -v /var/run/docker.sock:/var/run/docker.sock --volumes-from jenkins-volume --name tjenkins $(JENKINS_IMAGE)

# Ensure existence of a jenkins-volume data container to preserve jenkins state.  If one already exists it will be used.
jenkins-volume: jenkins-image
	docker ps -a | grep -q jenkins-volume  && echo Volume exists || docker create --name jenkins-volume $(JENKINS_IMAGE)

# Build the actual jenkins image
jenkins-image: 
	docker build -t $(JENKINS_IMAGE) docker/jenkins

# Run the testing presentation example code
test-example:
	cd code/testing; make