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

### Step 2 - Updating the Database

!!! danger
    Before you update the database, make sure you are using the latest version. Refer to the [Loading the Database from a GitHub Repo](../setup.md#loading-the-database-from-a-github-repo) section of the Setup.

Once using the latest version of the database, update the database by -

- [Performing an automatic update of the ANR data](../datamanagement/databaseupdating.md#automated-updates), or
- [Performing a manual update of the ANR data](../datamanagement/databaseupdating.md#manual-updates)

If there are any errors with the import, you may need to fix the file and reimport it. More information on that [can be found here](../datamanagement/databaseupdating.md#solving-errors).



## Combined Oceanic Dataset