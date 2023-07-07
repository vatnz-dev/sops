---
  title: Auckland Terminal Area 
---

--8<-- "includes/abbreviations.md"

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

|Transfer Flow         | Requirements                                                 | Notes                                                                       | 
| -------------------- | ------------------------------------------------------------ | --------------------------------------------------------------------------- | 
| Tower -> Approach    | Once the aircraft becomes airborne off the runway            | Tower shall instruct all aircraft to contact ATMA airborne                  |
| Approach -> Control  | Once the aircraft are approaching the lateral bounds         | Aircraft may be handed off when nothing further is required of the aircraft | 
| Control -> Approach  | Once the aircraft is appraching the cleared level by control | Aircraft may not always be cleared to A110 when handed to ATMA              | 
| Approach -> Tower    | Once established on final (ILS/LOC) or over the IAF (RNP)    |                                                                             |

## Departures

Aircraft released to ATMA may be tracked direct to a fix or assigned a heading to aid with sequencing or for the benifit of the pilot. 

ATMA shall note that all Prop SIDs out of AA contain a hold down of `A050`. ATMA shall climb the aircraft as required. Note that not all pilots will be aware of this hold down, therefore if an aircraft is to be held down at `A050` the pilot shall be told to *"Climb to 5000"*. It shall also be noted that the `BROOK #Q` has a altitude restriction of between `A025` and `A040`. 

Aircraft must climb to `A030` on the extended runway centreline before turning North on departure. Aircraft may be turned South passing A005. 

ATMA may track aircraft direct to the following positions without coordintation to OCR, RAN and BAY. Any waypoint before or abeam NP in RAN including LAKAR. And other waypoints such as HN, TAPAT and BOGUN. 

### STAR Clearances 

ATMA is responsible for issuing STAR clearances for aircraft bound for Hamilton and Tauranga. With coordination to BAY and/or HTMA (if online) on the appropriate STAR. IFR Training is popular between AR and HN so if there are any special details of an aircraft or a specific request from the pilot this shall also be passed onto HTMA (or BAY if HTMA offline). 

### Assigned Headings 

As per [Assigned Headings](../aerodromes/Class-C/nzaa.md#assigned-headings) ATMA shall endevour to coordinate assigned headings with TAA as soon as practical. Assigned heading shall be issued in the instance that a departing aircraft will be taking off close to an arriving aircraft, or for track shortening. This heading ensures the missed approach path is clear for the arriving aircraft incase of a go-around. Controllers shall note that only aircraft departing to the South may be assigned a heading, as aircraft departing north may not turn until passing `A030` therefore an assigned heading becomes impractical. 


## Arrivals 

Aircraft recivced from OCR, RAN and BAY shall be assigned the standard level of `A110`, or at times aircraft may be assigned different levels depending on the traffic levels etc. 

Controllers are expected to be aware of the different STARs leading into AA, AR and WP and what STARs lead to what approach, therefore the following track shortening in low levels of traffic or for sequencing shall be applied. 

For track shortening aircraft may be tracked direct SABAV and GITUK for the ILS or ZORBA, ELBOP, and ATAMA for RNP-ARs.  Any International arrivals shall expect mininimal track shortening as due to the layout of the STARs. 

In relation to [Noise Abatement](../terminal/atma.md#noiseabatement) Controllers shall also note that the RNAV (RNP) S, U, X  for all runways and the RNP Y RWY 23L are only available between 0700 and 2200 local. However the RNAV (RNP) Y RWY 05R is available H24. 



## Noise Abatement

!!! warning "Use of Noise Abatement Operations"
    The use of Noise Abatement Operations on the network is **not** mandatory, and Controllers may elect to provide a normal control service if they wish. As the primary Controller affected, the decision to implement Noise Abatement Operations sits with AA TMA.

      *Auckland employs noise abatement procedures from 2300 until 0600 local in order to minimise disturbances over populated areas.*

### Use of the Preferential Runway System

Use of the Preferential Runway System is not authorised and Controllers shall nominate a single runway direction for both take-off and landing.

### Departures

#### Runway 05R

Aircraft operating from RWY 05R shall not be taken off the SID until passing `A030`. Aircraft shall not overfly the City lower than `A050` unless established on an approach or departure path.

For all international departures the Controller shall issue the SID that is suggested by their Controller Client. For Domestic departures, Controllers shall observe the following SID assignment preferences:

| Priority | Runway | Procedure      | Allowed A/C Categories | Notes                                                                                  |
| -------- | ------ | -------------- | ---------------------- | -------------------------------------------------------------------------------------- |
| 1        | 05R    | `BROOK #Q`     | Cat A to C             | AA TMR approval not required during Noise Abatement hours.                             |
| 2        | 05R    | `REKIS #Q`     | Cat A to D             | **Preferred departure for Props**. Shall not be issued to Jets during Noise Abatement. |
| 3        | 05R    | `POLIS #Q`     | Cat A to D             | **Preferred departure for Cat D Jets, or heavies**. Shallower climb gradient.          |
| 4        | 05R    | All other SIDs |                        | Use of the `PAGLA #Q` departure shall be avoided.                                      |


#### Runway 23L

Aircraft operating from Rwy 23L must climb to `A030` on the extended runway centreline before turning to the right on departure. Aircraft may turn left once above `A005`.

There are no limits on the issuing of SIDs for Rwy 23L.

### Arrivals

#### Domestic

There are no limitations on the assignment of STARs for Domestic traffic, however Controllers should avoid the issuing of RNP-linking STARs.

#### International

OCR has three Noise Abatement STARs that shall be issued as first preference. If track shortening is provided, Controllers shall ensure that aircraft do not overfly the city.

| Runway | Procedure  | Transitions                                                             | Allowed A/C Categories |
| ------ | ---------- | ----------------------------------------------------------------------- | ---------------------- |
| 23L    | `BASIV #N` | `ELNOS` `SALAG` `UPLAR`                                                 | All                    |
| 05R    | `RIKDI #N` | `KALAG` `AGREX` `TARIB` `SELKA` `AGEDU` `IDSEM` `DABAS` `AKLOM` `OLBEX` | All                    |
| 23L    | `TAZEY #N` | `PEBLU` `VELMO`                                                         | All                    |

## Uncontrolled IFR 

### Departures 

IFR aircraft on the ground shall call ATMA prior to taxi to obtain IFR clearance. After a correct readback shall be told to report at the holding point for validation of their IFR clearance, and are cleared to enter controlled airspace on a SID and are advised to report prior to entering controlled airspace (Will normally be `A025` out of both North Shore and Ardmore). 

### Arrivals

For arriving IFR aircraft, ATMA shall issue the most appropriate STAR, and shall ask what approach they are antcipating. ATMA shall clear aircraft to leave controlled airspace via an approach, and get them to report on the ground to terminate thier flight plan


## Coordination

### TAA

ATMA shall coordinated with TAA and OCR/RAN/BAY as seen fit including any request for the non-nominated approach. 

### OCR, RAN and BAY

ATMA shall coordinate any track shortening not stated in [Departures](../terminal/atma.md#departures). 