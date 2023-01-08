---
title: Folder File Structure
---

--8<-- "includes/abbreviations.md"

The Sector File Generator works inside of its' own `AIRAC Testing` directory, which can be found in your `Documents` folder. This directory is organized into each AIRAC release, and these folders are generated when the SFG detects a change in set AIRAC cycle on the main screen. 

## Folder Structure

The overall file structure of the working directory is fairly simple. Most of these folders are generated automatically, and are discussed in detail below.

```
- 2210 Updates
  - NZ Euroscope Export
  - Test-NZ
  - Test-NZ Combined Oceanic
  - Vatsys-NZ
  - Vatsys-NZ Combined Oceanic
  - Procedure Maps
  ES_master.ese
  VATNZ Boundaries.geojson

```

### NZ EuroScope Export

This directory is created when the ++"Export Euroscope"++ button is clicked. Four files are generated in this folder - a single ESE and SCT2 for both NZZC and NZZO.

### Test-NZ

This is the SFG's main working directory for changes to NZZC data. Files found in here include:

* The original .pdf files for the ANR import, as well as the result of the PDFtoText conversion. Any files that have failed to be processed are also found here.
* All airspace conversions that are processed on the DB Update screen.
* Exported IFR and VFR Plan G fixes.
* Any Test Sector Files as generated from the Procedure Editor.

### Test-NZ Combined Oceanic

Same as above, but for Combined Oceanic data only.

### Vatsys-NZ

This is the folder where the SFG generates the latest vatSys release for NZZC. The file structure inside is identical to the Profile folders inside the main vatSys directory. Once the export has finished, you can copy the files from this folder into your vatSys Profiles folder for testing.

!!! info
    When the SFG goes through its' export routine, only the dynamic files are generated. Files such as `Sector.xml`, `Volumes.xml` are manual, and are checked during the export routine for data integrity. As such, if these files **do not** exist within this folder, the export will fail. Therefore, you should copy the most recent release version of the Dataset and paste it into the folder **before** performing your first export. This way the SFG will overwrite the necessary files, and all of the integrity checks will pass.

### Vatsys-NZ Combined Oceanic

This is the same as above, but for the Combined Oceanic Dataset. The same note applies.

### Procedure Maps

This folder contains individual procedure maps that have been generated using the ++"Create map for selected procedure"++ button within the Procedure Editor. 