---
  title: Best Practices
---

--8<-- "includes/abbreviations.md"

When contributing to this project, please follow these best practices to ensure that the SOPs are formatted in a standardised method.


## File and Folder Names

Ensure that new filenames and folders are lowercase only, so that the menu items are sorted in a predicable way.


## Links

Links that navigate a user away from the SOPs site should have `{ target=new }` appended - this opens the link in a new tab.

=== "Internal Link"

    ``` md
    [Internal Link](enroute.md)
    ```

=== "External Link"

    ``` md
    [External Link](https://vatnz.net){target=new}
    ```

!!! warning
    All external links should use the `https` protocol.


## Sector Names

Where possible, controller positions should be referred to by their abbreviation (e.g. OCR for Auckland Control). Where multiple positions are discussed in close proximity, consider **bolding** the sector names. The `abbreviations.md` file contains a list of all sector abbreviations and creates a tooltip with their full name for clarification.


## Altitudes

For altitudes, you should use the following format:

* `Axxx` for altitudes below 14,999ft
* `FLxxx` for altitudes above 15,000ft.

!!! example
    ``` md
    Departures should climb to `A060`
    ```

    Arrivals shall be descended to `FL160`.


## Waypoints

### IFR

IFR waypoints should always be encapsulated by backticks, and should always be in capitals - e.g. waypoint `UMAGA` or `DAVEE`.

### Visual Reporting Points

VFR waypoints, more commonly known as VRPs, shall be encapsulated in backticks, and should always be in Sentence Case - e.g. `Kaituna Bridge`, or `Gulf Harbour Marina`.


## SIDs and STARs

It's first important to understand how a SID or STAR name is constructed. In this case, we'll use the `DAVEE 7A` as an example -

* `DAVEE` is the procedure feeder fix. It is typically the waypoint that all transitions link back to. 
* `7` is the iteration designator. Each time this approach is updated, this designator is increased by one.
* `A` is the type designator. You can read more about this in the Sector Files SOPs.

!!! important
    It is important to know that the Procedure Feeder Fix, and the Type Designator never change, and are 'locked' to a runway, and type of use. Therefore, if you were to refer to the `DAVEE #A` arrival, you will effectively cover any iterations of that procedure down the line.

SIDs and STARs change often, so should very rarely be referred to by their full designation. If you need to refer to a SID or STAR, you should replace the iteration designator with a `#`, but keep the type designator, which is the letter that comes after the iteration designator. 

If you need to refer to a SID or STAR, you should separate the IFR waypoint from the designators with a space to enhance readability - e.g. `DAVEE #A`, or `MESIX #E`.

Where the procedure is a VOR-based, radar-based departure or arrival, you should ensure a space is between the name, and iteration designator - e.g. `CABLE 1`, or `NZWN #C`.

## Radio Calls & Coordination

It is recommended to include an example highlighting any unique or lesser-known radio calls which apply to a procedure, and to indicate any coordination requirements assoicated with a position.

### Radio Frequencies

If you need to list any radio frequencies, you should use full six-digit notation - e.g. 129.400. 

You do not need to append 'MHz' to any frequencies, however if you use HF and VHF frequencies in close proximity, you should annotate them as such - e.g. 8.832 (HF), or 123.9 (VHF).

### Radio Calls

Radio calls should take the following format:

``` md
**STATION NAME**: *"Message"*
```

!!! example
    **OCR**: *"ANZ352, when ready, descend to FL150"*  
    **ANZ352**: *"When ready down to FL150, ANZ352"*

### Coordination

Coordination examples should take the following format:  

``` md
**INITIATING SECTOR** -> **RECEIVING SECTOR**: "Message"
```

The sector names (including the arrow) should be wrapped in a `<span>` and given a class of either `hotline` or `coldline` to denote which coordination method should be used.  

``` md
<span class="coldline">**INITIATING SECTOR** -> **RECEIVING SECTOR**</span>: "Message"
```

As a general rule of thumb, coldlines should be used in most circumstances.

!!! example
    <span class="coldline">**QN TWR** -> **QN TMA**</span>: "ANZ352, Departing NZQN ANPOV #A, Request backtrack Runway 23"  
    <span class="coldline">**QN TMA** -> **QN TWR**</span>: "Aircraft on RNP Y passing through 10,000. ANZ352 cleared backtrack"    
    <span class="coldline">**QN TWR** -> **QN TMA**</span>: "Backtrack 23, ANZ352" 