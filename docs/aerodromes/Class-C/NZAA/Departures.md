---
  title: Departures
---

--8<-- "includes/abbreviations.md"

### Standard Instrument Departures (SIDs)

#### Runway 05R

| Direction | SID     | Transitions                       | Notes                            |
| --------- | ------- | --------------------------------- | -------------------------------- |
| SW        | AKELA2Q | GULUT, PEBLU, VELMO               | Initial climb FL250              |
| N         | AVDAT1Q | BOVRU, KAWAU, PUHOI               | Turboprops only                  |
| W         | BATOS3Q | MADEP, UPLAR                      | Initial climb FL250              |
| NW        | BELRA2Q | BELRA                             | Initial climb FL250              |
| S         | BROOK2Q | KAPAI, KARRL                      | Turboprops only, Jets on request |
| W         | EMRAG2B | EMRAG                             |                                  |
| N         | KADMA2Q | DUGAN, ELNOS                      | Initial climb FL250              |
| E         | PAGLA3Q | KAPAI, KARRL, NUTRA, PELBU, VELMO | Default Medium Jet               |
| S         | POLIS2Q | KAPAI, KARRL, LAKES, TULMI        | Default Heavy Jet                |
| NE        | RAXIN2Q | AGREX, KALAG, SELKA, TARIB        | Initial climb FL250              |
| S         | REKIS3Q | KAPAI, KARRL, LAKES, NUTRA, TULMI | Defualt Turboprop                |
| E         | SATLA2Q | AGEDU, AKLOM, DABAS, IDSEM, OLBEX | Initial climb FL250              |

---

#### Runway 23L

| Direction | SID     | Transitions                       | Notes                            |
| --------- | ------- | --------------------------------- | -------------------------------- |
| N         | BELRA2P | DUGAN, ELNOS, SALAG               | Initial climb FL250              |
| N         | ELSAB1P | BOVRU, KOPPA, KYPRA, OTATA, WP    | Turboprops only                  |
| E         | FIRTH2P | AGEDU, AKLOM, DABAS, IDSEM, OLBEX | Initial climb FL250              |
| W         | LENGU2A | LENGU                             | If Oceanic, Initial climb FL250  |
| S         | LEVR1P  | KAPAI, KARRL, LAKES, TULMI        | Jets only   (Default Jet)        |
| NE        | MEMOR2P | AGREX, KALAG, SELKA, TARIB        | Initial climb FL250              |
| W         | OSRAP1P | GULUT, MADEP, PEBLU, UPLAR, VELMO | Initial climb FL250              |
| S         | STEAL1P | KARRL, LAKES, NUTRA, TULMI        | Turboprops only, Jets on request |

--- 


#### Special Use Departures

| Direction | SID         | Transitions   | Notes                 |
| --------- | ----------- | ------------- | --------------------- |
| Any       | AUCKLAND 4A | AA or vectors | Radar Departure (23L) |
| Any       | AUCKLAND 4B | AA or vectors | Radar Departure (05R) |

---

### International SIDs

There are three types of SID transition used where flights join their enroute phase of flight at the NZZC/NZZO boundary;

- Those starting the enroute phase at a waypoint that joins an airway. For example, the MADEP transition to airway N774,

- Those starting the enroute phase other than at a waypoint, the "custom" transition. This sometimes happens on VATSIM when the flight plan omits the transition fix. In the real world, occasionally a flight requests a straight line out from the end of the SID to an unevaluated route as opposed to a named waypoint transition connecting to an airway.

- Those associated only with the AUCKLAND radar, EMRAG or LENGU departures -  the oceanic transition. Refer to the SID chart for further information.

!!! info
    To avoid confusion, associate the phrase oceanic transition only with the EMRAG, LENGU, or AUCKLAND radar  departures.

##### Examples

> New Zealand 8, cleared to Sydney flight planned route. OSRAP1P departure, MADEP transition. Squawk 0214.

### Issuing STARs for short-routes

Due to to the short flight distance from Auckland to Tauranga and Hamilton, aircraft departing for these locations should have the STAR added into the departure clearance. Find the duty runway, the appropriate STAR at the destination, and issue the clearance - assuming the standard route clearances are used.

##### Examples

> Cleared AATG3 the URBUX1A arrival, 12000 feet, REKIS3Q departure..

> Cleared AAHN1 the YOGIT1B arrival, 8000 feet..

#### VFR Departures:

Assign VFR aircraft a departure procedure appropriate for the direction of flight. If the pilot is unfamiliar with a published procedure, a plain language clearance may be issued. Amend the flight strip to display the departure procedure given.

VFR departures from NZAA require ATC approval to start engines.

See more about VFR departures here: [Auckland VFR Procedures](../NZAA/index.md#vfr-procedures)

All VFR Procedures can be found on the [New Zealand AIP](https://www.aip.net.nz/assets/AIP/Aerodrome-Charts/Auckland-NZAA/NZAA_64.1.pdf) 

### General Rules of Thumb:

#### IFR Departures

Tower may clear aircraft for take-off without coordinating with the departure controller, also called "auto-release". The departure controller may cancel auto-release during periods of high workload. 

!!! Warning 
    Radar Controllers should not be cancelling auto-release unless it is during an event or during unforecast high workload

Where successive similar aircraft depart on the same SID to the same domestic destination, allow four minutes between them to avoid a sequencing problem for the radar controllers. 

For successive straight ahead departures, ensure the previous departure is at least 5nm off the end of the runway and above 2000 feet AGL, assuming aircraft with similar performance, e.g.,  jet-following jet or turboprop following turboprop.

For pilots that have requested an alternative departure procedure, co-ordinate with the radar controller while the aircraft is taxiing. For example, the pilot is cleared for the LEVRA1P departure runway 23L, but requests an early turn. Follow this example:

> **NZAA_TWR**: Auckland Approach, Auckland Tower, OGO requesting early turn

> **NZAA_APP**: Roger, OGO at 500ft cancel SID, turn left track direct KARRL, climb unrestricted FL280, hold. (The word "hold" reinforces auto-release cancellation)

> **NZAA_TWR**: At 500ft cancel SID turn left track direct KARRL unrestricted FL280, and hold, OGO**

> **NZAA_APP**: Correct

> **NZAA_TWR**: OGO DEPARTURE INSTRUCTIONS WHEN READY TO COPY

> **NZ-OGO**: OGO

> **NZAA_TWR**: OGO AT 500FT CANCEL SID TURN LEFT TRACK DIRECT KARRL RADAR TERRAIN climb UNRESTRICTED TO FL280

> **ZK-OGO**: CANCEL SID LEFT TURN 500FT DIRECT KARRL climb FL280 OGO

> **NZAA_TWR**: OGO READ BACK CORRECT, RUNWAY 23L LINE UP AND WAIT AWAITING RADAR RELEASE

> **NZAA_TWR**: Auckland Terminal, Auckland Tower OGO ready, request release

> **NZAA_APP**: OGO released

> **NZAA_TWR**: Released OGO thank you

> **NZAA_TWR**: OGO AIRBORNE CONTACT AUCKLAND APPROACH 124.3 RUNWAY 23L CLEARED FOR TAKE-OFF




The Approach Controller may assign aircraft alternative departure instructions where traffic permits and without the request of the pilot. Such as assigned headings. For example: 


**NZAA_TWR**: Auckland Tower, Auckland Approach, New Zealand 563 assigned passing 500 feet left heading 180 climbing FL380 

**NZAA_APP**: Roger, New Zealand 563 passing 500 feet left heading 180 climbing FL380 

**ANZ563**: Auckland Tower g'day New Zealand 563 ready A2

**NZAA_TWR**: New Zealand 563, Auckland Tower, new departure instructions when ready to copy

**ANZ563**: Go ahead

**NZAA_TWR**: New Zealand 563, passing 500ft turn left heading 180 climbing unrestricted FL380 

**ANZ563**: Thanks, passing 500ft turn left heading 180 climbing unrestricted FL380 

**NZAA_TWR**: New Zealand 563, correct runway 23L cleared for takeoff


Note: Approach Controllers may add `Hold` onto the end of the assigned heading during coordination for sequencing etc. This requires the Tower Controller to hold an aircraft on the ground till the Radar Controller tells you to `Released`. This refers to the cancellation of auto-release and as stated will require permission from the Approach Controller for the aircraft to be able to takeoff. 

