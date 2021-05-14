FROM ubuntu:trusty-20190425

# Load utilities and packages
RUN apt-get update
RUN apt-get install -y wget curl python
RUN curl https://bootstrap.pypa.io/get-pip.py | python 
RUN pip install flask
RUN pip install pyYaml
RUN pip install futures
RUN pip install requests
RUN pip install html

# Copy working files to directory
ADD code/project /project
WORKDIR /project

EXPOSE 5000
# Run the app
CMD [ "python", "app.py" ]
