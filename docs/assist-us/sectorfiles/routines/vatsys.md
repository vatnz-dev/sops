---
title: vatSys
---

--8<-- "includes/abbreviations.md"

This page describes the routine process for updating the vatSys datasets. The process is relatively straight forward, however can be complicated by the addition of positions, procedures, airspace or features. The process is largely the same between the NZZC and Combined Oceanic datasets, with minor source data changes.

## Domestic Dataset (NZZC)

The Domestic Dataset follows an update schedule of every 28 days, and should be released on the effective date of the AIRAC cycle. 

In order to achieve this, processing is required in advance of the release date which poses a handful of issues, mainly surrounding the fact that the ANR and procedure data isn't made public until the effective date of the AIRAC. Therefore, our working relationship with New Zealand's ANSP is paramount to gaining access to the data early.

### Step 1 - Find changes

The changes being made to data can be found in the Bulletin. This covers changes within the GEN, ENR and AD sections, in addition to covering all AD 2 Chart changes. 

We use GitHub Issues to track the incoming changes to our data - you can see an [example here](https://github.com/vatnz-dev/new-zealand-dataset/issues/29){ target=new }. You should make a subtask for each change that needs to be replicated in our data.

### Step 2 - Importing the new data

!!! danger
    Before you update the database, make sure you are using the latest version. Refer to the [Loading the Database from a GitHub Repo](../setup.md#loading-the-database-from-a-github-repo) section of the Setup.

Once using the latest version of the database, update the database by -

- [Performing an automatic update of the ANR data](../datamanagement/databaseupdating.md#automated-updates), or
- [Performing a manual update of the ANR data](../datamanagement/databaseupdating.md#manual-updates)

If there are any errors with the import, you may need to fix the file and reimport it. More information on that [can be found here](../datamanagement/databaseupdating.md#solving-errors).

### Making the Changes

Now is your time to make all the changes! 

* You can see how to make changes to procedures in the [Procedure Editor section](../procedures/index.md).
* You can see how to add positions in the [Data Management section](../datamanagement/ManualDefinitions.md).

!!! danger
    After you've made your changes, remember to update the database repository!

### Exporting the Dataset

After you've finished your changes, it's time for export! This can be done by clicking the ++"Export vatSys"++ button on the main SFG screen.

A few points:

* You should make sure that the current AIRAC version is set correctly on the main Export page.
* The ++"Export vatSys"++ button also exports the Combined Oceanic Dataset at the same time.
* After you export the dataset, it can be found in the `Documents/AIRAC Testing/XXXX Updates/` folder, and then under the `Vatsys-NZ` folder. You will have to copy this into your vatSys directory to test the dataset. If you make any changes afterwards, you will then have to copy the changes from the export folder to your vatSys folder again.

#### Updating the Profile file

You will also need to update the `Profile.xml` file prior to release. This is the file that vatSys reads to ascertain the current release, and dictates whether the user is prompted to update their dataset or not.

``` XML title="Profile.xml"

<Version AIRAC="2208" Revision="a" PublishDate="20220811" UpdateURL="https://vatsys.sawbe.com/downloads/data/New%20Zealand/" />

```

The `Version` line should be updated, with the `AIRAC` field updated for the version you are releasing, as well as annotating the effective date in the `PublishDate` attribute. The `Revision` attribute should always be `a`, unless you are releasing a correction to the data outside of the scheduled release timetable.

### Pushing your changes to GitHub

!!! danger
    Before you push your changes to GitHub, you should ensure that all of the changed files are what you want to release. At times other files generated can slip in - these can be ignored my right clicking file name in the GitHub window, and clicking on Discard.

When pushing your changes to GitHub, you should have a descriptive commit comment that is short, concise, and is semantic. For example - `routine: Cycle 2210 ANR changes`, `feat: Add new Queenstown procedures` or `fix: Change ATIS pronunciations`.

After committing your changes to the working repository under the vatnz-dev organisation, you need to open a pull request from that Repo into the main vatSys release repo. This PR will then be reviewed by either the Operations Director, or another individual.

## Combined Oceanic Dataset

To be added once COD is released.