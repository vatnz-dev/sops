---
title: Set Up
---

--8<-- "includes/abbreviations.md"

## Introduction

The Controller Client data is managed through GitHub repositories under the vatnz-dev organization. If you require access to the vatnz-dev organization, let the Operations Director know.

There are a number of repositories of note:

* [**ais-data-manager**](https://github.com/vatnz-dev/ais-data-manager){target=new} - Contains the most recent version of `nzsectorfiles.sql`,
* [**auckland-radio-dataset**](https://github.com/vatnz-dev/auckland-radio-dataset){target=new} - Development repo of the Auckland Radio Dataset,
* [**new-zealand-dataset**](https://github.com/vatnz-dev/new-zealand-dataset){target=new} - Development repo of the New Zealand Domestic Dataset,
* [**SectorFiles**](https://github.com/vatnz-dev/SectorFiles){target=new} - Release repo of our EuroScope releases.
* [**vrpsForLittleNavMap**](https://github.com/vatnz-dev/vrpsForLittleNavMap) - Release repo of our LittleNavMap VRPs.

## Requirements

The SFG app should run on any PC running Windows 7, 10 or 11. The system must have at least .Net Framework 4 installed.

Prior to installing the SFG app, you will need to set up the following:

*  [**WAMP**](https://www.wampserver.com/en/){target=new} - WAMP is an Apache distribution that contains a MySQL server, replicating a live server on your local machine.
*  [**GitHub Desktop**](https://desktop.github.com/){target=new} - Needed in order to manage the EuroScope releases, vatSys Datasets and database.

When setting up WAMP and MySQL, you have the option to set a username and password for the root user. If you set your own, you're able to set this under `Export > User Options`.
