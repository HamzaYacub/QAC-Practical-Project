# Random Vehicle Generator

## Table of contents
* [Introduction](#introduction)
  * [Additional Requirements](#additional-requirements)
* [Project Tracking](#project-tracking)
* [Risk Assessment](#risk-assessment)
* [Architecture](#architecture)
  * [Database](#database)
  * [Entity Relationship Diagrams](#entity-relationship-diagrams)
* [Design](#design)
* [Deployment](#deployment)
  * [Tools and Technologies](#tools-and-technologies)
  * [Pipeline](#pipeline)
  * [CI server](#ci-server)
  * [Configuration Management](#configuration-management)
  * [Git Branch and Merge Logs](#git-branch-and-merge-logs)
* [Testing](#testing)
  * [Analysis](#analysis)
* [Improvements for future](#improvements-for-future)

## Introduction

The overall objective of this project was to create a service-orientated architecture consisting of at least 4 micro services that work together.

As I had full control over the topic of this project, I had decided to create a random vehicle and paint job generator that would give the user a special discount depending on the outcome of the vehicles and paint jobs.

The 4 micro services within this project are as follow:

* Service 1: Renders the Jinja2 templates based upon the outcome of service 4 as well as persisting the data in a SQL                    database
* Service 2: Generates random vehicle
* Service 3: Genrates random paintjob
* Service 4: Creates an object (discount) based upon the results of service 2 and 3 respectively.

### Additional Requirements

In addition to the objective, there were a minimum set of requirements which also had to have been met. These include:

* An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
  * This could also provide a record of any issues or risks that you faced creating your project.
* An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be     built through a CI server and deployed to a cloud-based virtual machine.
  * If a change is made to a code base, then Web hooks should be used so that Jenkins recreates and redeploys the changed       application
* The project must follow the Micro Services architecture that has been asked for
* The project must be deployed using containerisation and an orchestration tool.
* As part of the project you need to create an Ansible Playbook that will provision the environment that your application     needs to run.

## Project Tracking

A [Trello][trello-link] board was used to organise this project of all of its respective requirements and tasks. This was done in accordance to the MoSCoW principles.

![Trello screenshot][trello-screenshot-link]

## Risk Assessment

![Risk Assessment][ra-link]

## Architecture

### Database

Since there needed to be some data persistance, a database was required. The database used for this project was a MySQL instance hosted by GCP. As I had already used this for another project and was comfortable with it, I decided on this rather than a MySQL image deployed by Docker. What needed to be stored in the database was the vehicle, the paint job and the discount produced from these two constraints.

### Entity Relationship Diagrams

Before creating the database, it is crucial to make and stick to a design. This is done so that the objectives are always clear at all times. This was the initial design of the entity-relationship model which highlights the components and the relationships between the tables.

![ERD][erd-link]

However after careful consideration and a look at the requirements, it was clear that multiple tables were not necessary and therefore only 1 table was needed in order to persist all the required data.

![ERD2][erd2-link]

This updated ERD only shows the one table rather than the multiple tables I had before 

## Design

Here is the front end design for the application. As we were mainly focused on the backend and functionality of the project, the mark scheme does not go into any detail regarding the front end, only that it is functioning as it should. Therefore, only very basic CSS was used.

![Home page][home-screenshot]

## Deployment

![CI Server diagram][ci-server]

### Tools and Technologies

* Python3 - Logic
* Flask - Web development framework
* VS Code - IDE
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

This all starts from the Trello board, where tasks are tracked and organised. Once a task has been chosen, code was then developed in VS Code using Python3 and Flask. Once a task had been complete, it could be commited and pushed to GitHub, the version control system of choice for this project. Once pushed, the Trello board can be updated to complete the task. Before taking on a new task, the code had to be pulled from GitHub to ensure that the latest code is being worked on. 

Afterwards, a CI server was implemented, in this case, Jenkins. Webhooks were created between GitHub and Jenkins so that when any code was pushed to the Developer branch, the pipeline would automatically start building. The pipeline was made up of shell scripts and a Jenkinsfile which ran the various steps required to deploy the project. Docker and specifically, Dockerfiles, was used to build the images of all the micro services. These images would then get pushed to DockerHub. Ansible was used in this pipeline as a configuration management tool, which essentially configures all the VMs included so that they are ready for the Docker swarm to deploy the application. NGINX was then used as a reverse proxy for the ports being used. In this case, port 5001, was being reverse proxied to port 80. This entire process was automated through Jenkins and no further configuration is required.

### CI server

![Deployment Logs][deploy-log]

Jenkins was used as the CI server for this project. A pipeline was made which followed a combination of build steps to deploy the application. As seen in the deployment log above, the first step that occurred was pulling the latest code pushed from GitHub which was automated through the use of a webhook. The second step was to change the permissions of the scripts so that they were executable so that they can actually run. These scripts are what make up the following steps in the deployment. The first script to run exports all the environment variables required. Next, Ansible is installed and configures the VMs that the application will be deployed on. The final involves rebuilding the images for each of the four services and subsequently pushing them to Docker Hub. After this, Docker swarm is then initiated across the VMs that were configured earlier by Ansible.

### Configuration Management



### Git Branch and Merge Logs

Log at time of README update: 13/06/2020

~~~
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
~~~

In this project, Git was used in order to:

* Keep track of the build history for all the files in this project.
* Enable the gradual integration of working features.
* Allow new features to be developed and tested in separate branches. Once complete they can merge back into the developer   branch.
* Enable webhooks for the CI server so that the pipeline can automatically build when something is pushed to GitHub.
* Ignore files that do not need to be pushed to GitHub with the use of a .gitignore file. 

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

~~~
@app.route('/', methods=['GET', 'POST'])
def discount():
    
    vehicle = requests.get('http://service_2:5002').text
    paintjob = requests.get('http://service_3:5003').text
    v_discount = 0
    p_discount = 0
    total_discount = 0
    generous = False
~~~

I rewrote it as:

~~~
@app.route('/', methods=['GET', 'POST'])
def discount(vehicle, paintjob, generous):
    
    #vehicle = requests.get('http://service_2:5002').text
    #paintjob = requests.get('http://service_3:5003').text
    v_discount = 0
    p_discount = 0
    total_discount = 0
    #generous = False
~~~~

Doing this allowed me to check that every vehicle and paintjob was being correctly utilised as well as checking my second implementation for service 4 - generous discounts - was functional.

## Improvements for future

Initially, it was planned to include full CRUD functionality for the application. A user would have been able to choose either a vehicle or paintjob from an exisiting table and then randomise the other option. So if they chose a vehicle, the paint job would be randomised and vice versa. They would also be able to update the record if they wanted to and re-randomise the paint job again. And finally, if wanted, they could also delete the record.

In order to achieve this:

* The database would have to be modified to look like the initial erd plan.
* WTForms would have to be utilised to allow the user to pick their respective options.

If this implementation was applied, then it could have been improved further to inlcude a login system so that users can only see their past vehicle combinations rather than everyone's choices.

With regards to the CI pipeline:

* Deploy to more nodes.
* Create more replicas for each respective node.
* Change update method to incorporate polling DockerHub webhooks.
* Expand after-deployment processing to automate merge requests.

To improve testing:

* Testing could be expanded to include stress testing of containers.
* Testing could be expanded to include stress testing of VMs.
* Selenium testing could be utilised to test the front end for its functionality


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
