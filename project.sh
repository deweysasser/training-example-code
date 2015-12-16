#!/bin/bash

# Purpose:  run a docker container with the project code

runContainer() {
    docker build -t my-project -f docker/project/Dockerfile .
    # Ignore the result of this one
    docker rm -f my-project
    docker run  -p 5000:5000 --name my-project my-project
}


runTests() {
    dir="$1"

    saved=`pwd`
    cd $dir
    if [ -f Makefile ] ; then
	make
    else
	python -m unittest discover
    fi
    val=$?

    cd "$saved"

    return $val
}



if runTests; then
    runContainer || exit 1
fi
