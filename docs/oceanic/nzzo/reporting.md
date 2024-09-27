---
  title: Procedures
---

--8<-- "includes/abbreviations.md"

## Methods of Communication

The primary method of communication is via HF Voice.

CPDLC is not yet supported but may be offered as a secondary means of communication if available. ARO's CPDLC logon code shall be `NZZO`.

### HF

Simulated HF radio is used as the primary long-range radio communications medium. The nature of HF radio makes it highly vulnerable to atmospheric distortion and noise, so radiotelephony procedures on HF tend to be more formal to maximize clarity.

#### SELCAL

Given the background noise level experienced on HF radio frequencies, flight crews usually prefer to turn down the audio level of their HF receiver. SELCAL uses a unique 4-letter code for each aircraft (e.g. `QR-AC`), transmitted over the communications frequency to sound an alert for the flight crew.

Controllers must check each aircraft’s flight plan for a discrete SELCAL code. If aircraft have nominated a discrete code (for example, `QR-AC`), a SELCAL check shall be completed on initial contact.

!!! important "Use of SELCAL"
    Where a SELCAL check has been completed successfully, all subsequent communications shall be conducted prefaced by a SELCAL chime.

!!! example "RTF Example for readback of a Position Report"
    **Auckland Radio**: *"UAE412, standby SELCAL check."*  
    Aircraft awaits the SELCAL chime before replying. 
    **UAE412**: *"SELCAL check OK, ANZ254."*    
    Then continue with routine communications.

### CPDLC

!!! info "Not yet supported in NZZO"


## Position Reports

As NZZO is procedural airspace, pilots are required to provide regular position reports to ATC, which can then be entered into your Controller Client software.

A Position Report will contain the following elements:

- Callsign
- Position & Time
- Flight level
- Next position and time over
- Ensuing significant point
- Specified Speed (if assigned)

If an aircraft fails to report its position within 3 minutes of its estimated time, controllers must attempt to establish contact with that aircraft and obtain a position report.

ATC shall acknowledge a position report by using the aircraft's callsign. A readback of the report is not required unless the controller needs to confirm the information provided.

!!! example "RTF Example for readback of a Position Report"
    **UAE412**: *"Auckland Radio, Auckland Radio. UAE412 with position."*  
    **Auckland Radio**: *"UAE412, pass position report."*    
    **UAE412**: *"UAE412 is position TATAS time 1853. Estimating SAMAD at 1953. OSUGA next."*  
    **Auckland Radio**: *"UAE412, Auckland Radio copies position report."*  

## Transfer of Control Point

### NZZC Enroutes to ARO

NZZC enroute sectors must provide a 10-minute warning to Auckland Radio (ARO) before an aircraft crosses the FIR boundary.

### ARO to NZZC Enroutes

Aircraft entering an NZZC enroute sector must do so via a named fix at their assigned flight level. Pilots shall be instructed to contact the appropriate NZZC sector frequency when crossing the boundary fix.

Since aircraft crossing into NZZC enter a surveillance environment, prior coordination with NZZC sectors is not required provided the aircraft meets the conditions above.

!!! example "RTF Example for handing off to a NZZC sector"
    **Auckland Radio**: *"UAE412, at position PEBLU, contact Auckland Control on 123.900."*    
    **UAE412**: *"UAE412 at position PEBLU, contact Auckland Control on 123.900."*

#### Oceanic Airspace delegated to STH

ARO delegates airspace to the STH sector along the western boundary of the NZZC FIR near NZQN. Aircraft within this delegated airspace follow a 130nm arc from the `QN VOR`, which includes four waypoints: `BEBOB`, `DADLU`, `MADOK`, and `EKODA`. These waypoints are boundary fixes and serve as the transfer of control points between STH and ARO, in both directions.

### ARO to other Oceanic FIRs

For flights leaving NZZO to enter other oceanic FIRs, voiceless transfers may be used. There shall be no changes to the route or cleared flight level (CFL) within 15 minutes of the FIR boundary.

#### Transferring to YBBB or YMMM

Most airways over the Tasman Sea have only two waypoints within the NZZO FIR, both being boundary fixes. As a result, flights may receive contact instructions for the next sector during their initial radio call with ARO. ARO shall retain control over the flight tag until the common airspace boundary.

For flights that include an additional waypoint within the NZZO sector, contact instructions for the next sector shall be issued at the waypoint immediately preceding the boundary fix.

!!! example "RTF Example for short Tasman routes"   
    **ANZ204**: *"Auckland Radio, Auckland Radio. ANZ204 with position."*  
    **Auckland Radio**: *"ANZ204, pass position report"*      
    **ANZ204**: *"ANZ204 is position PEBLU time 1832. Estimating SASRO at 1911. MIKEG next."*  
    **Auckland Radio**: *"ANZ204, Auckland Radio copies position report. Standby SELCAL check."*    
    Aircraft waits for the SELCAL chime before replying. <br />
    **ANZ204**: *"Auckland Radio, ANZ204 on SELCAL."*  
    **Auckland Radio**: *"ANZ204, Auckland Radio accepts primary guard on 129.000, negative secondary. At SASRO, contact Brisbane Radio on primary 124.650."*  
    **ANZ204**: *"Auckland Radio, ANZ204 primary guard on 129.000, negative secondary. At SASRO, contact Brisbane Radio on primary 124.650."*  

## NZCI to NZZC below FL245

ARO shall not pass IFR clearances to aircraft requesting to operate below FL245 whilst on the ground or following departure from the Chatham Islands. ARO shall not accept radio guard for aircraft operating below FL245.

- The aircraft shall broadcast their position on UNICOM, and shall monitor ARO's frequency.
- Aircraft may be passed traffic information at their requested altitude or levels.

Before reaching the NZZO boundary, the aircraft shall be instructed to contact the NZZC sector for clearance into controlled airspace.

!!! example "RTF Example for NZZC clearance instructions"   
    **Auckland Radio**: *"CVA554, prior to position ATABU, contact Ohakea Control on 126.200 for clearance into controlled airspace."* 