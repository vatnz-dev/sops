---
  title: Auckland Terminal Area 
---

--8<-- "includes/abbreviations.md"

!!! note "Auckland Procedures"
    The ATMA procedures build upon information already contained in the [NZAA Aerodrome Procedures](../aerodromes/Class-C/nzaa.md), and any Controller logged on to ATMA should be familiar with those procedures.

## Positions

| Position Name | Shortcode | Callsign          | Frequency | Login ID | Usage     |
| ------------- | --------- | ----------------- | --------- | -------- | --------- |
| Auckland TMA  | ATMA      | Auckland Approach | 124.300   | NZAA_APP | Primary   |


### Event Only Positions

!!! Danger
    The following are designated as Event Only positions, and may only be staffed during a VATNZ event where approved, or if explicitly authorised by the Operations Director.

| Position Name       | Shortcode | Callsign          | Frequency | Login ID | Usage                       |
| ------------------- | --------- | ----------------- | --------- | -------- | --------------------------- |
| Auckland Departures | ADEP      | Auckland Approach | 129.600   | NZAA_DEP | Events - Traffic Management |

## Airspace

The Auckland CTA/C follows the lateral and vertical boundaries as shown below. 


<figure markdown>
  ![Auckland TMA](./assets/aatma-airspace.png) 
  <figcaption>Auckland TMA (CTA/C)</figcaption>
</figure>

### Transfer of Control Points

|Transfer Flow         | Requirements                                                  | Notes                                                                       | 
| -------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------------- | 
| Tower -> Approach    | Once the aircraft becomes airborne off the runway             | Tower shall instruct all aircraft to contact ATMA airborne                  |
| Approach -> Control  | Once the aircraft are approaching the lateral bounds          | Aircraft may be handed off when nothing further is required of the aircraft | 
| Control -> Approach  | Once the aircraft is approaching the cleared level by control | Aircraft may not always be cleared to A110 when handed to ATMA              | 
| Approach -> Tower    | Once established on final (ILS/LOC) or over the IAF (RNP)     |                                                                             |

## Departures

Departures should be assigned in accordance with the [SID Assignment guide](../aerodromes/Class-C/nzaa.md#sid-assignment). 

ATMA may climb departing aircraft as necessary to maintain separation and traffic flow, up to their requested flight level. International aircraft shall be instructed to climb to `FL250`, and shall get further climb once handed to OCR. 

!!! hint "RTF for re-joining a SID"
    Where an aircraft has been taken off their assigned SID, and is required to then re-join at a later point, the following RTF must be used:

    **ATMA**: *New Zealand 677, track direct LAKES to rejoin the SID/STAR*.

    

### Prop Departures

ATMA should note that all prop-preferential SIDs have a hold-down altitude restriction during their initial departure leg. Most pilots are not aware of these limitations, therefore ATMA should be aware of the limitations, particularly on the  `BROOK Q`, `REKIS #Q`, `AVDAT #Q`, `DOVON #Q`, `STEAL #P` and `ELSAP #P`. ATMA can use a stepped climb methodology to ensure that these limitations are met.


### Track Shortening SIDs

ATMA may issue aircraft inside it's bounds with track shortening instructions or assigned a headings, to assist with sequencing or separation. 

!!! note "Track Shortening"
    If a SID is cancelled or the aircraft is given a shortcut ATMA shall note in the tag where the departing aircraft is tracking.

ATMA shall instruct any aircraft on a radar heading to report their heading to the next sector. 

#### OCR 

ATMA shall handoff departing international flights to OCR as soon as practicable, ensuring that aircraft are:

- on their assigned SID.
- tracking to the SID endpoint.

***or***

- tracking to the SID transition or on a vector and will remain clear of all aircraft under control. 

**Exceptions to the above conditons are:**

- Aircraft with routes containing PEBLU, VELMO, GULUT, DUGAN, ELNOS may be tracked direct to these points by TMA.
- Aircraft with routes containing MADEP/UPLAR may be tracked to BOGUN/TAPAT respectivly.

#### RAN

Prior coordination or notification is not required for the following flights:

| Criteria to be met                                                   | Clearance Limit                          |
| -------------------------------------------------------------------- | ---------------------------------------- |
| DEST is not NZNP                                                     | Direct to: KARRL/NP/LAKAR                |
| Aircraft is west of KARRL, DEST is NZCH and is a jet                 | Direct to NS                             |
| DEST is not NZHN                                                     | Direct to HN                             |
| Aircraft Enters RAN sector east of LAKES-DROPT track and west of HN  | Direct to DROPT                          |
| Aircraft enters RAN sector west of KARRL                             | Direct to SILVO                          |
| Level is `A100` and below                                            | via FPR on non-standard routes           |

#### BAY

Prior coordination or notification is not required for the following flights:

| Criteria to be met                                                     | Clearance Limit                          |
| -------------------------------------------------------------------- | ---------------------------------------- |
| Level is `A100` and below and DEST is not NZTG                       | Direct to: TG                            |
| Aircraft is west of KARRL, DEST is NZCH and is a jet                 | Direct to TULMI                          |
| Level is `A100` and below                                            | via FPR on non-standard routes           |

**For any coordinated track shortening, controllers shall note the instruction given in the aircraft's tag.**

### Assigned Heading Departures

Assigned heading departures may be requested by tower or ATMA in order to allow for more efficient traffic flow from the runway. Controllers can use this method to ensure that a 30° divergence exists between tracks, either by keeping the go-around path clear, or by moving an aircraft away from another aircraft's departure path. 

These instrctions shall be issued in accordance with [NZAA - Assigned Headings](../aerodromes/Class-C/nzaa.md#assigned-headings).

- Due to the early turn required, assigned heading departures shall be given to prop aircraft only.

!!! example "RTF and coordination for an assigned heading departure"
    **AA TWR** -> **AA TMA**</span>: "Successive departures. Request ANZ631 assigned heading 190 degrees climbing five thousand then yours for vectors. Second in queue."  
    **AA TMA** -> **AA TWR**</span>: "ANZ631 approved heading 190 degrees climbing five thousand then my vectors. Copy second in line."
    

### Short-Sector STARs

ATMA is responsible for issuing STAR clearances for aircraft bound for NZHN and NZTG and shall do so without coordination. 

## Arrivals 

OCR, RAN or BAY will hand aircraft to ATMA no lower than `A110`, unless co-ordinated.

### Track Shortening STARs

ATMA should make use of track-shortening on STARs to allow for an efficient sequence to be applied. Where an aircraft has been taken away from the STAR and are subsequently required to re-join and follow the STAR, the following RTF shall be used:

!!! hint "RTF for re-joining a STAR"
    **ATMA**: *New Zealand 677, track direct VINCE to re-join the STAR. Descend to 5000ft, radar terrain*.

Provided separation standards are met, aircraft may be tracked direct `SABAV` and `GITUK` for their respective ILS, or to `ZORBA`, `ELBOP` or `ATAMA` their respective RNP (AR) approach. Due to the routing of international STARs, minimal track shortening shall be applied.

### Noise Abatement

NZAA runs noise abatement from 2300L until 0600L. The procedures contained in [NZAA - Noise Abatement](../aerodromes/Class-C/nzaa.md#noise-abatement) may be applied within this time.

Controllers shall note that only the RNP Y RWY 05R (AR) approach is authorised for use during noise abatement hours.

## Uncontrolled IFR 

For aircraft departing NZNE and NZAR, they shall be issued an uncontrolled IFR clearance. Depending on traffic levels outside controlled airspace, the controller may validate the clearance with the readback or on the taxi. 

For uncontrolled IFR aircraft leaving the ATMA control area, ATMA shall issue the appropriate STAR for that aerodrome, and clear the aircraft to leave controlled airspace on descent. 

If the aircraft is terminating underneath the ATMA control area, they shall be instructed to contact you on the ground to cancel their IFR flight plan. If their flight is terminating underneath another sector, such as OCR, they shall be instructed to contact that sector. This shall be coordinated.

!!! Example Clearance 
**ATMA**: *EAM Cleared to Rotorua via LAKES direct ESKER at 8,000ft, Squawk 5623*
**EAM**: *Cleared to Rotorua via LAKES direct ESKER at 8,000ft, Squawk 5623, EAM* 
**ATMA**: *EAM, Readback correct, clearance not vaild report on the taxi, Northland QNH 1015*
**EAM**: *Wilco, copy 1015, EAM*
**EAM**: *Auckland Approach, EAM taxis Runway 21 Ardmore*
**ATMA**: *EAM thanks your clearance now vaild cleared to enter controlled airspace on the REKIS1T departure climbing to 3,000ft, no reported IFR traffic outside of controlled airspace, report passing 2,500ft*
**EAM**: *Clearance vaild, cleared to enter controlled airspace on the REKIS1T departure climbing to 3,000ft, copy traffic, report passing 2,500ft, EAM*


## Coordination

### Auckland Tower

ATMA shall coordinate with TAA on any requested approach that is not nominated in the ATIS. 

### OCR, RAN and BAY

ATMA shall coordinate any track shortening outside of their control area that is not stated in [Departures - Track Shortening](#track-shortening-sids). 
