# Random Vehicle Generator

## Table of contents
* [Introduction](#introduction)
  * [Additional Requirements](#additional-requirements)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Architecture](#architecture)
  * [Entity Relationship Diagrams](#entity-relationship-diagrams)
* [Design](#design)
* [Deployment](#deployment)
  * [CI Pipeline](#ci-pipeline)
  * [Tools and Technologies](#tools-and-technologies)
  * [Deployment Logs](#deployment-log)
  * [Git Branch and Merge Logs](#git-branch-and-merge-logs)
* [Testing](#testing)
  * [Analysis](#analysis)
* [Improvements for future](#improvements-for-future)

## Introduction

The overall objective of this project was to create a service-orientated architecture consisting of at least 4 micro services that work together.

As I had full control over the topic of this project, I had decided to create a random vehicle and paint job generator that would give the user a special discount depending on the outcome of the vehicles and paint jobs.

The 4 micro services within this project are as follow:

* Service 1: Renders the Jinja2 templates based upon the outcome of service 4 as well as persisting the data in a SQL database
* Service 2: Generates random vehicle
* Service 3: Genrates random paintjob
* Service 4: Creates an object (discount) based upon the results of service 2 and 3 respectively.

### Additional Requirements

In addition to the objective, there were a minimum set of requirements which also had to have been met. These include:

* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
  * This could also provide a record of any issues or risks that you faced creating your project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.
  * If a change is made to a code base, then Web hooks should be used so that Jenkins recreates and redeploys the changed application
* The project must follow the Micro Services architecture that has been asked for
* The project must be deployed using containerisation and an orchestration tool.
* As part of the project you need to create an Ansible Playbook that will provision the environment that your application needs to run.

## Project Tracking

A [Trello][trello-link] board was used to organise this project of all of its respective requirements and tasks. This was done in accordance to the MoSCoW principles.

![Trello screenshot][trello-screenshot-link]

## Risk Assessment

![Risk Assessment][ra-link]

## Architecture

### Entity Relationship Diagrams

This was the initial design of the entity-relationship model which highlights the components and the relationships between the tables.

![ERD][erd-link]

However after careful consideration and a look at the requirements, it was clear that multiple tables were not necessary and therefore only 1 table was needed in order to persist all the required data.

![ERD2][erd2-link]

This updated ERD only shows the one table rather than the multiple tables I had before 

## Design

Here is the front end design for the application. As we were mainly focused on the backend and functionality of the project, the mark scheme does not go into any detail regarding the front end, only that it is functioning as it should. Therefore, only very basic CSS was used.

![Home page][home-screenshot]

## Deployment

### CI Pipeline

![CI Server diagram][ci-server]

### Tools and Technologies

* Python3 - Logic
* Flask - Web development framework
* Jinja2 - Web template for Python
* Jenkins - CI server
* Docker - Containerisation
* Docker swarm - Orchestration tool
* Ansible - Configuration management
* NGINX - Reverse proxying
* MySQL - Database
* Pytest - Unit testing
* Git - Version control system
* Trello - Project tracking
* Google cloud platform - Live environment

### Deployment Logs

![Deployment Logs][deploy-log]

### Git Branch and Merge Logs

Log at time of README update: 13/06/2020

* 6bce40d (HEAD -> developer, origin/developer) added screenshots
* 538f0c8 Update README.md
* 7a19714 Update README.md
* dc2f3c0 Create README.md
* 231d1ca Delete .DS_Store
* 2f2e32a added all documentation and screenshots
* 1c23985 acheived 100% coverage
* 839572a fixed requests url
* df29ec8 (origin/testing) deleted irrelevant requirements.txt
* 04b956a added testing for service 4
* 510c3c1 update script
* ffbcf24 updated testing
* 02fed1b added testing for service 3
* d96b0d9 tested service 2
* 9ced4f5 update
* 97982bb testing done for service 1
* c56912e added files to be ignored
* 9fd1fc9 changed implementation
* b8d66f1 update html
* d0c3f2f (origin/dev-test) change implementation
* f86ef2b changed implementation
* e6bd9f0 modified implementation
* e236caa added build command in pipeline
* e6e2f08 (origin/developer-2) test implementation 2
* 355837f update
* ea2a79e update html
* 5081605 (origin/jenkins) added implementation
* 6681a15 update script
* 1f90c68 updated scripts
* c9d46c0 updated scripts
* 29afff0 added Jenkinsfile
* 2e8ca25 added scripts
* 6150301 updated for docker stack
* 09e7c38 (origin/docker_swarm) added ansible playbooks
* a20e434 fixed requests error
* 81ce45a changed routes for services
* 8d8e1cb added docker-compose.yaml
* a4029b4 added Dockerfiles and requirements for all services
* 15e1b97 changed nginx.conf
* e378d59 added html pages
* 8a908bb completed routes for service 1
* f1d98ed added logic for service 4
* 69cb58d added generate.html
* ae0121e added route for generate page
* aa1c551 added service 1 logic
* c58da5d devised models for database
* 75d3f10 creation of tables
* aac9994 completed logic for service 4
* 31d28f6 added arguments to __init__.py
* 8631df6 added nginx.conf
* c445db6 changed ports for services
* e766279 fixed issue in previous modification
* 0a1e87f modified service 3
* 005f1d1 modified service 2
* c8ad7c5 added functionality for service 2
* c91bd78 added functionality for service 3
* 53175bd added functionality for service 3
* fcc2cce added service 3
* 383302e added service 2
* 95dba7a (origin/master, origin/HEAD, master) created template for project
* bea76e4 Initial commit

## Testing

Pytest, specifically Unit testing, has been used to test the code produced in this project. Selenium was planned to be used for Integration testing however it was not fully implemented and therefore not included at this time. Only the python files in the 4 services were tested since PyTest can only test python files. 

Here are the links to the coverage reports for each individual service:

* [Service 1][cov1]
* [Service 2][cov2]
* [Service 3][cov3]
* [Service 4][cov4]

### Analysis

Although a full coverage was met for all 4 services, I had some difficulty in reaching it. Services 1 - 3 were simple and only required 1 or 2 tests each to reach full coverage as they only had simple get requests. Service 4 on the other hand proved to be quite troublesome as along with the get requests, there was also a lot of logic depending on what got pulled from the get requests. Since the get requests pulled randomly from a CSV file, it was impossible to reach full coverage doing normal tests. I had initially attempted mocking but was unsuccessful in implementing it. In order to solve this problem, I had to make a small change to my routes.py. Instead of using the get requests from service 2 and 3, I included the them as parameters in the app.route function.

So instead of it being like this:

@app.route('/', methods=['GET', 'POST'])
def discount():
    
    vehicle = requests.get('http://service_2:5002').text
    paintjob = requests.get('http://service_3:5003').text
    v_discount = 0
    p_discount = 0
    total_discount = 0
    generous = False
    
I rewrote it as:

@app.route('/', methods=['GET', 'POST'])
def discount():
    
    vehicle = requests.get('http://service_2:5002').text
    paintjob = requests.get('http://service_3:5003').text
    v_discount = 0
    p_discount = 0
    total_discount = 0
    generous = False

## Improvements for future




[trello-link]: https://trello.com/b/oL2ikEds/sfia2-practical-project
[trello-screenshot-link]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/Trello.png
[erd-link]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/ERD%20diagram%20v1.png
[erd2-link]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/ERD%20diagram%20v2.png
[ra-link]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/Risk%20assessment.png
[deploy-log]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/Deployment%20activities.png
[ci-server]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/CI%20Pipeline.png
[home-screenshot]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/Home%20page.png
[cov1]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Service%201/test_results/service1%20cov.png
[cov2]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Service%202/test_results/service2%20cov.png
[cov3]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Service%203/test_results/service3%20cov.png
[cov4]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Service%204/test_results/service4%20cov.png
