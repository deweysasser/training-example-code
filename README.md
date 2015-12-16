training-example-code
=====================

Code, slides and docker support for a training seminar on coding
standards for team coding methodology for a team already somewhat
familiar with python.

I was one of several presenters, this module contains only my slides
and code examples and a bit of scaffolding.

Contents
========

* code/test -- code examples accompying the testing presentation
* docker/jenkins -- the Jenkins docker image used in this seminar (can
  also docker pull deweysasser/training-jenkins)
* code/project -- a placeholder for project code
* Makefile -- a driver for all of this

Usage
=====

'make project'
--------------

Assuming you have 'make' installed, you can type "make" or "make
project" and it will build a docker image containing code/project and
run the "app.py" in that directory (which defaults to a trivial flask
example).

'make jenkins'
--------------

This will build a new jenkins image and run it, preserving any state
you have in the jenkins-volume data container. (I.e. it will preserve
the build jobs you've already created.)

Seminar Outline
===============

* Day 1
    * Morning
        * OO development (Ian, 60m)
            * Inheritances vs. containment
            * Encapsulation
            * Polymorphism
            * Delegation
        * Testing (Dewey, 60m) <Testing%20Presentation.mm>
        * Build Pipelines (Ben, 30m)
            * Pipeline steps
            * Promotion levels
            * Best Practices
        * Group Exercise -- get Jenkins running on your system (Ben, 15 minutes)
    * Afternoon
        * Work on component parts with unit tests
        * Peer review
* Day 2 
    * Morning
        * MVC (Ian, 45-60m)
        * REST (Ian, 30m)
        * Python coding standards (Dewey, 30-60m) <Python%20coding%20standards.mm>
        * 5 minute overview of flask (Ian)
        * 5 minutes of html generation in python (Dewey)
    * Afternoon
        * Integrate small parts into MVC/REST framework
        * Peer review
* Day 3
    * Morning
        * Refactoring patterns (Dewey, 60m)
    * Afternoon
        * Putting it all together
        * Peer review

