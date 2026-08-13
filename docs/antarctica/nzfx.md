---
title: NZFX - Phoenix Field
---

--8<-- "includes/abbreviations.md"

## Positions

| Position Name | Shortcode | Callsign              | Frequency | Login ID  | Usage   |
| ------------- | --------- | --------------------- | --------- | --------- | ------- |
| Williams TMA  | WTMA      | Williams Approach     | 126.200   | NZWD_APP  | Primary |


### Event Only Positions

!!! Danger "Important"
    The following are designated as Event Only positions, and may only be staffed during a VATNZ event where approved, or if explicitly authorised by the Operations Director.

| Position Name | Shortcode | Callsign            | Frequency | Login ID  | Usage      |
| ------------- | --------- | ------------------- | --------- | --------- | ---------- |
| Phoenix DLV   | DFX       | Phoenix Delivery    | 128.600   | NZFX_DEL  | Event Only | 
| Phoenix SMC   | GFX       | Phoenix Ground      | 121.800   | NZFX_GND  | Event Only | 
| Phoenix ADC   | TFX       | Phoenix Field Tower | 126.200   | NZFX_TWR  | Event Only |



!!! note "Event only aerodrome positions"
    The NZFX local aerodrome positions are event only positions and should only be opened when they are published for an event or otherwise approved.

    `NZWD_APP` is not event only. It provides the overlying approach service for the wider Williams Field terminal area and will be covered in the separate NZWD airport/TMA SOP.

## Responsibilities

Phoenix Field Tower is responsible for aircraft operating within the Phoenix Field `Class D` airspace. This includes aerodrome control, traffic information, IFR departure instructions, VFR operations, and local non-radar arrival/departure services when delegated or required.

Phoenix Field Tower may also provide a non-radar approach service to aircraft operating in the surrounding `Class E` airspace when `NZWD_APP` is not online or where coordinated with the overlying controller.

## Airspace

### Class D

Phoenix Field has `Class D` airspace within a `4.3 NM` radius of the aerodrome, from the surface up to and including `A025` AGL.

Aircraft must establish two-way radio communications with Phoenix Field Tower before entering the `Class D` airspace.

<figure markdown>
  ![Phoenix Field Control Zone](./assets/nzfx-airspace.png) 
  <figcaption>Phoenix Field Control Zone (CTR/D)</figcaption>
</figure>

### Class E

The surrounding `Class E` airspace extends within `100 NM` of the Williams Field or Pegasus Field TACANs, excluding `Class D` airspace, from the surface up to but not including `FL245`.

Within `Class E` airspace:

- IFR aircraft are separated from other IFR aircraft.
- IFR aircraft receive traffic information about VFR aircraft as far as practicable.
- VFR aircraft may receive flight following on request, workload permitting.
- Hazard alerts should be passed to known VFR aircraft.

VFR aircraft do not require a clearance to enter `Class E` airspace, but should monitor the appropriate frequency, avoid published IFR routes and holding patterns where possible, and make broadcasts when required to avoid conflict.

## Clearances

IFR clearances should be issued using FAA phraseology or standard VATNZ IFR phraseology. VFR phraseology should remain in line with standard VATNZ practice.

### IFR Departures

IFR aircraft will call for clearance before departure. Tower, or Delivery when staffed during an event, shall relay the IFR clearance and issue departure instructions.

FAA-style IFR clearances may include:

- Destination airport.
- Assigned SID, if applicable.
- Route, such as `THEN AS FILED` or `AS FILED`.
- Initial altitude or `CLIMB VIA SID`, as applicable.
- Additional instructions or information where required.

If no SID is assigned, clear the aircraft to destination as filed and assign the appropriate initial altitude.

### VFR Departures

VFR aircraft shall be issued appropriate VFR departure information. Plain language instructions may be used where they are clear and unambiguous.

## Ground Movements

Ground movements are normally straightforward and should be managed by Tower unless `NZFX_GND` is staffed during an event.

Aircraft should obtain start clearance before taxi when operating IFR. Departing aircraft should be taxied to the active runway holding point and transferred to Tower when ready, or instructed to monitor Tower before reaching the holding point during high traffic events.

## Tower

### Departures

Tower is responsible for sequencing departures and ensuring the departure path is clear before issuing takeoff clearance.

For IFR departures, ensure the aircraft has received its IFR clearance and departure instructions before takeoff. Transfer IFR departures to `NZWD_APP`, or to `NZCM_FSS`/UNICOM if no relevant overlying controller is online.

### Arrivals

Arriving aircraft should normally contact Phoenix Field Tower no closer than `10 NM` from the aerodrome for landing instructions, unless otherwise coordinated.

Aircraft operating in the `Class D` airspace should remain at or above `A010` AGL, or `A005` AGL for helicopters, until commencing final descent.

## Coordination

### NZFX_TWR to NZWD_APP

Coordinate IFR departure releases, arrival sequencing, visual approaches, and any aircraft requiring a non-standard operation with `NZWD_APP`.

Departing IFR aircraft should be transferred to `NZWD_APP` once airborne and clear of immediate aerodrome traffic, unless otherwise coordinated.

### NZFX_TWR to NZCM_FSS

When `NZWD_APP` is not online and `NZCM_FSS` is providing the overlying service, coordinate IFR arrivals and departures with Mac Center.
