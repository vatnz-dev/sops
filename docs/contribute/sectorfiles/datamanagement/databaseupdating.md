---
  title: Database Updating
---

--8<-- "includes/abbreviations.md"

The SFG uses the ANR as the primary source of data for the NZZC dataset.  For the Pacific dataset, the primary source is a locally stored copy of the Navigraph database.

The ANR data released by Airways is on a 56-day release schedule, usually meaning that the Dataset will vary between a minor and major release every cycle. 

**Minor releases** are releases where the ANR *has not* been updated, and is usually a great time to implement new features or positions or fix errors in the dataset. **Major releases** are releases where the ANR *has* been updated, and usually requires a significant rework of locally defined procedures within the dataset.

## Updating the ANR Data

There are two methods of updating the ANR data - automatic and manual. The automatic mode will download the ANR from the AIP website, convert them from PDF to text, before running them against regex patterns to process and import them into the database.

### Import Process

When importing `.pdf` files, the SFG will first convert them from a PDF to a text file. The SFG then parses that text file. If there are any import errors that need rectification, you should edit the `.txt` file, **not** the .pdf or the cleaned txt.

### Automated Updates

The automatic ANR update will download the latest documents from the AIP website, convert them from PDF to Text, before running them against various regex patterns to process and import them into various database tables.

To perform an automatic update, navigate to the `DB Update` tab and click on ++"Extract and Import all eAIP Data"++. You should now see the progress bar, alongside the file currently being worked. 

!!! important
    It is normal to see various errors during the import process, particularly with the Aerodrome and Airways imports. The SFG will notify you of errors as they occur - so make a note. The error prompt will also notify you of the suggested fix.

    You will most likely encounter an error when importing the Part 95 Routes file, which contains all airways for both NZZC and NZZO. The error prompt will alert you to the specific Type, Identifier and Sequence that is producing the error. This will require you to manually review and fix the faulting sequence(s).

    You will then be required to import the amended file through the manual import process.

### Manual Updates

Manual ANR updates are easy, thanks to an automated import. On receipt of an advance copy of the ANR, open the SFG, and navigate to the Utilities screen. Just above the orange Extract button, select the `Use ANR Zip File` button, then click the orange Extract button.

This will then prompt you to select a file. Select the `.zip` file you have just downloaded. The SFG will then process the files as per an automated import.

## Updating the Pacific data

Due to the Pacific having multiple data sources, it is easier to pull from the Navigraph data. This unfortunately means that the data is always a cycle behind, but it is preferential against having to go digging through the French AIP.

To achieve this, the SFG will find the locally stored vatSys copy of the Navigraph data, and will import that depending on various checks.

### Automatic Update

!!! information
    As the SFG pulls from the vatSys copy of Navigraph data, you will need to make sure you have the latest version. This can be done by opening vatSys and navigating to `Settings > Navigraph > Check for Updates`.

To perform an automatic update, navigate to the `DB Update` tab and click on ++"Import Pacific Data"++. You should now see the progress bar, alongside the file currently being worked. 

### How the data is processed

The Pacific data imported, as well as some of the exported data, is filtered by two boundaries defined in `AIRAC Testing/SFG Data/NZZC NZZO Check Boundaries.xml`. 

The NZZO Check Boundary is the boundary of the NZZO, NTTT and TSN sectors. Only data that exists within these boundaries are imported from the Navigraph data.

The NZZC Check Boundary is a boundary 4nm inside the actual NZZC FIR boundary. This is used during the export process to specifically exclude some of the data from being produced the in the Pacific dataset, such as airways and fixes inside the NZZC. This is located 4nm inside the FIR to ensure that FIR Boundary fixes are exported.

There are eAIP formatted versions of these two boundaries in the same data directory that can be adjusted, although it shouldn't be necessary.

## Solving Errors

Occasionally you will get parsing errors where there are errors in the `.pdf` files. The SFG will alert you to the file that is faulting, and then instruct you to reimport it manually. 

When editing the text file, ensure you are double checking the parsed PDFtoText file with the original PDF. Common issues include poor formatting, duplicated entries, and mismatched sequences. If you encounter any of these, you should let the author of the PDFs know.

After solving the error, you will need to reimport the file manually. You can do this by clicking the corresponding button on the `DB Update` screen, and then selecting the file.

| Required Import Button | Files                                                                                                                                                                                                                                                                                                |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Airports               | Aerodrome Coordinates                                                                                                                                                                                                                                                                                |
| Airspace               | Common Frequency Zone (CFZ)  <br>Controlled Airspace (CTA)  <br>Controlled Airspace (CTR)  <br>Controlled Airspace (OCA)  <br>Danger Areas (D)<br>Flight Information Regions (FIR)<br>Mandatory Broadcast Zones (MBZ)<br>Military Operating Areas (MOA)<br>Restricted Areas (R)<br>Holding (Enroute) |
| VFR Fixes              | Visual Reporting Points (VRPs)                                                                                                                                                                                                                                                                       |
| IFR Fixes              | Designated Points (ICAO)                                                                                                                                                                                                                                                                             |
| Navaids                | Navaids                                                                                                                                                                                                                                                                                              |
| Airways                | Routes                                                                                                                                                                                                                                                                                               |
| Not Used               | General Aviation Areas (GAA)<br>Low Flying Zones (LFZ)<br>Mountainous Zones (NZMZ)<br>Parachute Landing Areas (PLA)<br>Transit Lanes (T)<br>Volcanic Hazard Zones (VHZ)<br>Right Hand Circuits                                                                                                       |
