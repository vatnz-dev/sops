---
  title: Auckland Terminal Area 
---

--8<-- "includes/abbreviations.md"

!!! note "Auckland Procedures"
    The ATMA procedures build upon information already contained in the [NZAA Aerodrome Procedures](../aerodromes/Class-C/nzaa.md), and any Controller logged on to ATMA shall be familiar with those procedures.

## Positions

| Position Name | Shortcode | Callsign          | Frequency | Login ID | Usage   |
| ------------- | --------- | ----------------- | --------- | -------- | ------- |
| Auckland TMA  | ATMA      | Auckland Approach | 124.300   | NZAA_APP | Primary |


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

| Transfer Flow       | Requirements                                                             | Notes                                                                                                                                      |
| ------------------- | ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| Tower -> Approach   | Once the aircraft becomes airborne off the runway                        | Tower shall instruct all aircraft to contact ATMA airborne                                                                                 |
| Approach -> Control | Once the aircraft are approaching the lateral or vertical bounds of ATMA | Aircraft may also be handed off when clear of all conflicts, provided the next sector accepts the early handover.                          |
| Control -> Approach | Aircraft is approaching the vertical and lateral bounds of the TMA       | Aircraft may not always be cleared to `A110` when handed to ATMA. Aircraft may be handed off early, provided that ATMA is happy to accept. |
| Approach -> Tower   | Once established on approach, or within AA TWR's CTA/C.                  | Aircraft cleared for a visual approach may be cleared to contact sooner for separation against circuit traffic.                            |

## Departures

Departures shall be assigned in accordance with the [SID Assignment guide](../aerodromes/Class-C/nzaa.md#sid-assignment). 

ATMA may climb aircraft as necessary up to their RFL. International departures may be cleared up to a maximum of `FL250`, with further available on coordination with OCR.

Aircraft shall leave the ATMA tracking a waypoint. Where aircraft are vacating on an assigned heading, coordination shall occur with the next sector to accept the aircraft. ATMA shall instruct any aircraft on an assigned heading to report their heading to the next sector on transfer.

### Prop Departures

All prop-preferred SIDs have a hold-down altitude restriction during their initial departure segment. Most Pilots are unaware of these limitations, therefore ATMA should be aware of the limitations, particularly on the  `BROOK #Q`, `REKIS #Q`, `AVDAT #Q`, `DOVON #Q`, `STEAL #P` and `ELSAB #P`. Controllers may use a stepped climb methodology to ensure that these limitations are met.


### Track Shortening on SIDs

TMA may utilise SID track-shortening where necessary. Where an aircraft is issued a direct to another point on the SID, they shall be instructed to then rejoin the procedure.

!!! note "Track Shortening"
    If a SID is cancelled, or the aircraft is given a shortcut, ATMA shall note in the tag where the departing aircraft is tracking.

!!! hint "RTF for re-joining a SID"
    Where an aircraft has been taken off their assigned SID, and is required to then re-join at a later point, the following RTF must be used:

    **ATMA**: *New Zealand 677, track direct ORIDI to rejoin the SID/STAR*.


#### OCR 

ATMA shall handoff departing international flights to OCR as soon as practicable, ensuring that aircraft are tracking via their assigned SID. 

Additionally, ATMA may perform the following qualified actions:

- Aircraft with routes containing `PEBLU`, `VELMO`, `GULUT`, `DUGAN`, `ELNOS` may be tracked direct to these points by TMA.
- Aircraft with routes containing `MADEP`/`UPLAR` may be tracked to `BOGUN`/`TAPAT` respectivly.

#### RAN

Prior coordination or notification is not required for the following flights:

| Criteria to be met                                                            | Clearance Limit                         |
| ----------------------------------------------------------------------------- | --------------------------------------- |
| DEST is not NZNP                                                              | Direct to: `IGBAT`, `NP VOR` or `LAKAR` |
| Aircraft is west of `IGBAT`, DEST is NZCH and is a jet                        | Direct to `NS VOR`                      |
| DEST is not NZHN                                                              | Direct to `HN VOR`                      |
| Aircraft Enters RAN sector east of `ORIDI`-`DROPT` track and west of `HN VOR` | Direct to `DROPT`                       |
| Aircraft enters RAN sector west of `IGBAT`                                    | Direct to `SILVO`                       |
| Level is `A100` or below                                                      | via FPR on non-standard routes          |

#### BAY

Prior coordination or notification is not required for the following flights:

| Criteria to be met                                     | Clearance Limit                    |
| ------------------------------------------------------ | ---------------------------------- |
| Level is `A100` or below, and DEST is not NZTG         | Direct to: `TG VOR`                |
| Aircraft enters BAY sector via TULMI                   | Direct to `TULMI`                  |
| Level is `A100` and below                              | via FPR on **non-standard** routes |

!!! note "Silent Coordination"
    For any coordinated track shortening, Controllers shall note the instruction given in the aircraft's tag.

### Assigned Heading Departures

Assigned heading departures may be requested by Tower or ATMA in order to allow for more efficient traffic flow from the runway. Controllers can use this method to ensure that a 30° divergence exists between tracks, either by keeping the go-around path clear, or by moving an aircraft away from another aircraft's departure path. 

These instrctions shall be issued in accordance with [NZAA - Assigned Headings](../aerodromes/Class-C/nzaa.md#assigned-headings).    

### Issuing STARs for Short Sectors

ATMA is responsible for issuing STAR clearances for aircraft bound for NZHN and NZTG and shall do so without coordination. 

## Arrivals 

OCR, RAN or BAY will hand aircraft to ATMA no lower than `A110`, unless coordinated.

### Track Shortening STARs

ATMA may make use of track-shortening on STARs to allow for an efficient sequence to be applied. Where an aircraft has been taken away from the STAR and are subsequently required to re-join and follow the STAR, the following RTF shall be used:

!!! hint "RTF for re-joining a STAR"
    **ATMA**: *New Zealand 677, track direct VINCE to re-join the STAR. Descend to 5000ft, radar terrain*.

Provided separation standards are met, aircraft may be tracked direct `SABAV` and `GITUK` for their respective ILS, or to `ZORBA`, `ELBOP` or `ATAMA` their respective RNP (AR) approach. Due to the routing of international STARs, minimal track shortening shall be applied.

### Noise Abatement

NZAA runs noise abatement from 2300L until 0600L. The procedures contained in [NZAA - Noise Abatement](../aerodromes/Class-C/nzaa.md#noise-abatement) may be applied within this time.

Controllers shall note that only the RNP Y RWY 05R (AR) approach is authorised for use during noise abatement hours.

## Uncontrolled IFR 

Aircraft departing NZNE and NZAR shall be issued an uncontrolled IFR clearance. Depending on traffic levels inside Controlled Airspace, and the potential for conflict, the Controller may validate the clearance either on readback, or on the taxi.

For IFR aircraft leaving ATMA and controlled airspace on descent, ATMA shall issue the appropirate STAR for that aerodrome, and clear the aircraft to leave controlled airspace on descent.

If the aircraft is terminating their FPL underneath ATMA, they shall be instructed to contact you on the ground to cancel their IFR flight plan. If their flight is terminating underneath another sector, such as OCR, they shall be instructed to contact that sector. This shall be coordinated.

!!! Example Clearance 
    **ATMA**: *EAM Cleared to Rotorua via `ORIDI`, direct `ESKER` at 8,000ft, Squawk 5623*

    **EAM**: *Cleared to Rotorua via `ORIDI`, direct `ESKER` at 8,000ft, Squawk 5623, EAM* 

    **ATMA**: *EAM, Readback correct, clearance not vaild, report on the taxi, Northland QNH 1015*

    **EAM**: *Wilco, copy 1015, EAM*

    **EAM**: *Auckland Approach, EAM taxis Runway 21 Ardmore*

    **ATMA**: *EAM, your clearance is now vaild, cleared to enter controlled airspace on the `REKIS 1T` departure climbing to 3,000ft, no reported IFR traffic outside of controlled airspace, report passing 2,500ft*

    **EAM**: *Clearance vaild, cleared to enter controlled airspace on the `REKIS 1T` departure climbing to 3,000ft, copy traffic, report passing 2,500ft, EAM*


## Coordination

Alongside the event-specific coordination requires stated in the above sub-sections, the following shall apply.

### Auckland Tower

ATMA shall coordinate with TAA on any requested approach that is not nominated in the ATIS. 

### OCR, RAN and BAY

ATMA shall coordinate any track shortening outside of their control area that is not stated in [Departures - Track Shortening](#track-shortening-sids). 
