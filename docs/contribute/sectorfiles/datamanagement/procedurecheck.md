---
  title: Procedure Cross-Checking
---

--8<-- "includes/abbreviations.md"

The SFG has a utility that allows you to cross-check between the procedures stored in the database, and the procedures promulgated in the ANR Part 95 procedure sheets. There are some limitations that are described below.

The procedure sheets are updated every ANR cycle, and can be found under [ANR Part 3.2 and 3.3](https://www.aip.net.nz/document-category/Air-Navigation-Register). Additionally, it will be included with any advance copy of the ANR.

!!! warning "Final Checks"
    The Procedure Checker should be run as a part of the final release checks for the dataset. Even if you haven't amended any procedures, it can be useful in identifying any existing errors.

## Limitations

The ANR currently only describes procedures for RNAV or RNP procedures, so will not contain any radar or VOR-based departures, such as the NZPM `GOLF 2`. 

## Process

### Running the Checks

1. Navigate to the `Check Data` tab, and select which categories you wish to cross-check. By default categories A through D will be checked, with H disabled.
2. Click on ++"Check SID/STAR Names"++, which will open a dialog box. Navigate to the location where the ANR Check Files are stores, and using the ++"CTRL"++ key, select both the SID and STAR files, then click ++"Open"++. The SFG will then run its sequence.

!!! tip
    The SFG will save the output file in the same directory where the source files are located, and **not** the current AIRAC working directory.

### Understanding the Checks

The layout for the output is -

1. SIDs that are in the ANR Domestic Departure list, but not in the Database
2. SIDs that are in the Database, but do not exist in the ANR Domestic Departure list.
3. STARs that are in the ANR Domestic Arrivals list, but not in the Database.
4. STARs that are in the Database, but do not ecist in the ANR Domestic Arrivals list.

For points 2 or 4 above, this is where you will find non-RNAV approaches listed, such as radar departures, or VOR-based procedures such as the NZAR `CABLE 1` departure, or the NZNR `NR 2A` arrival.

### Responses

- For procedures that are listed in Section 1 and 3 above, you should investigate as to why there is a discrepency. These could be:
    - a completely missing procedure,
    - a mislabelled procedure, such as a misspelled waypoint name or an incorrect designator,
    - that the procedure has been assigned to the incorrect runway
        - in this case, the procedure should also be listed in Section 2 as existing in the database but not in the ANR.

!!! info "ANR File containing old data"
    Sometimes the ANR will contain historical data, where previously removed files still exist in the file, but newly released procedures have also been inserted. In this case, use the AIP website to confirm that these procedures no longer exist.


