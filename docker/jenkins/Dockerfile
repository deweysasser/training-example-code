FROM jenkins:latest

USER root
RUN apt-get update
RUN apt-get -y install python-pip make
RUN pip install mock coverage pytest
RUN pip install html
USER jenkins
ENV JAVA_OPTS=-Duser.timezone=America/New_York