---
title: Master .ese File
---

--8<-- "includes/abbreviations.md"

# Understanding the ES_master.ese File

The Master .ESE file dictates a few functions in the SFG -

- Defines all of the Positions in the Datasets (FSS, ENR, TMA, TWR, ATIS)
- Defines all of the master Airspace outlines for ES (Both SectorLines and SECTORs)
- Defines all FIR_COPX definitions
- Can contain additional Free Text, which is exported to both vatSys and ES
- Defines all RADAR positions for both vatSys and ES.

## Modifying the Data

### Writing

You can export the Master .ESE by clicking on ++"Write Master .ese"++ in the Export window of the SFG.

### Updating

You can import the Master .ESE by clicking on ++"Import ESE"++ in the DB Update window of the SFG.

## Positions Master

This section defines all positions within the Dataset, in addition to ATIS connections, and adjacent sectors for hand-offs and error checking. These definitions follow the standard position nomenclature as defined in the [EuroScope documentation](https://www.euroscope.hu/wp/ese-files-description/){ target=blank }.

```
// Format
<name of position>:<radio callsign>:<frequency>:<identifier>:<middle letter>:<prefix>:<suffix>:<not used>:<not used>:<A code start of range>:<A code end of range>[:<VIS center1 latitude>:<VIS center1 longitude>[: ... ]]

// Example
NZOH_TWR:Ohakea Tower:134.500:TOH:T:NZOH:TWR:-:-:6601:6700

```

!!! note
    A stations identifier should be unique, and easily identifiable. For example, Ohakea Tower has the TOH identifier, whereas Approach has Oa, and Ground has GOH. 

    Manual VIS center definitions should not be used.

### ATIS Positions

All aerodrome ATIS' should be entered in the `[POSITION]` register. The start of these entries are denoted by a semi-colon (`;`) to tell the SFG that they are not Control Positions.

```
// Format
;<ATIS Name>:<Freq>:<ICAO>:ATIS

// Example
;Ohakea ATIS:135.000:NZOH:ATIS
```

### Adjacent Sectors

It's good pratice to also include adjacent sectors in our `[POSITIONS]` definition. This makes sure that they are shown in the online sectors list, and any handover or co-ordination pop-ups. 

These follow the same format as shown above, but should have `#` appended to the name of the position. This makes sure that that sector is **not** included in the vatSpy testing dialog box.

```
// Example
BN-INS_FSS#:Brisbane Radio:129.250:INS:O:BN-INS:FSS:-:-:-:-
```

### Usage of this Data

These position populate the `POF` database table. 

During an export, the `POF` table is used to -

- The callsigns in `Sectors.xml` are compared to the `POF` table, and all frequencies are cross-checked. If there is a difference, the sectors file is updated to the frequency listed in the `POF` table.
- The SFG checks that all entries in the POF table are included in `Sectors.xml` - if not, they are added. They won't have a volume defined, so they won't be used or appear in the sector list. 
    - This is how we have adjacent sectors like `BN-TSN` show up in `Sectors.xml`, but not in the manual sector selection window.
- A check is also run to see if a Callsign in `Sectors.xml` does not exist in the `POF` table. If this is the case, it'll alert you to update the Master ESE.


!!! info
    You will be alerted if the SFG makes changes to any data.

## Master Airspace Outlines

The master airspace outlines are contained within the `[AIRSPACE]` section.

This section is exclusively used for EuroScope to define the lateral limits of a airspace sector.

!!! hint
    These `COORD` definitions can be converted from eAIP definitions to Sectorline or Sector File outputs using the Airspace Converter utility.

### Sectorlines

The Sectorline definitions should follow the standard as defined in the [EuroScope documentation](https://www.euroscope.hu/wp/ese-files-description/){ target=blank }.

These are typically discrete sections of airspace, that can be added together to form an outline of the airspace you're wanting to define. These are added together in a separate `SECTOR` definitions, underneath the Sectorline definitions.

### Sector Definitions

The Sector definitions then add all of the Sectorlines together to form an outline of the airspace. These are fairly straightforward, and the current examples in the Sector Files should be used as a guide.

## FIR_COPX (Coordination Points)

These are a list of all manual co-ordination points in EuroScope. These are 