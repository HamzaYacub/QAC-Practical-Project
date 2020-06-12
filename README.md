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
  * [CI Server](#ci-server)
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

## Risk Assessment

## Architecture

### Entity Relationship Diagrams

## Design

## Deployment

### CI Server

### Tools and Technologies

### Deployment Logs

### Git Branch and Merge Logs

## Testing

### Analysis

## Improvements for future




[trello-link]: https://trello.com/b/oL2ikEds/sfia2-practical-project
[trello-screenshot-link]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/Trello.png
[erd-link]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/ERD%20diagram%20v1.png
[erd2-link]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/ERD%20diagram%20v2.png
[ra-link]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/Risk%20assessment.png
[deploy-log]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/Deployment%20activities.png
[ci-server]: https://github.com/HamzaYacub/QAC-Practical-Project/blob/developer/Documentation/screenshots/CI%20Pipeline.png
[home-screenshot]:






