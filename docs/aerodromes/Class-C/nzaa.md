---
  title: NZAA - Auckland
---

--8<-- "includes/abbreviations.md"

## Positions

| Position Name     | Shortcode | Callsign          | Login ID | Usage     |
| ----------------- | --------- | ----------------- | -------- | --------- |
| Auckland Delivery | DAA       | Auckland Delivery | NZAA_DEL | Secondary |
| Auckland SMC      | GAA       | Auckland Ground   | NZAA_GND | Secondary |
| Auckland ADC      | TAA       | Auckland Tower    | NZAA_TWR | Primary   |
| Auckland TMA      | ATMA      | Auckland Approach | NZAA_APP | Primary   |


## Event Only Positions

!!! Danger
    The following are designated as Event Only positions, and may only be staffed during a VATNZ event where approved, or if explicitly authorised by the Operations Director.


| Position Name           | Shortcode | Callsign            | Login ID   | Usage                       |
| ----------------------- | --------- | ------------------- | ---------- | --------------------------- |
| Auckland Finals         | AARR      | Auckland Finals     | NZAA-F_APP | Events - Traffic Management |
| Auckland Terminal Radar | ADEP      | Auckland Departures | NZAA_DEP   | Events - Traffic Management |

---

## Layout

Auckland Airport has one runway -  05R/23L, and is home to around 100 gates. Auckland is New Zealand's largest international aerodrome serving over 57 airports with 24 airlines. 

<figure markdown>
  ![NZAA Ground Movements](/assets/nzaa-ad.png) 
  <figcaption>Auckland Ground Movements</figcaption>
</figure>

## Pushback

Pushback and start up clearances are managed by the Ground Controller. Controllers should make use of the "tail facing" instruction to ensure that aircraft do not block apron entry and exit points. 

### Domestic 

Aircraft pushing from Gates 20 to 22 shall push either onto `D1/D2` or `B`, depending on other traffic. Aircraft on Gates 28 to 33 shall be pushed with the nose facing towards the active runway.

For Gates 28 to 33, the Controller shall ensure that `B4`, `B5` and `B6` are kept clear for other aircraft, which can be ensured through two methods:

- Instructing the aircraft to have their tail facing a certain way, or
- Instructing the aircraft to push clear of a taxiway.

Aircraft on the `C5` apron shall be instructed to push and start at their discretion, as it is not a part of the manoeuvring area but still requires a clearance.

### International 

All aircraft pushing from the International apron shall be given a tail facing instruction, and *may* be given a start location.

!!! example "International Apron: Push and Start"
    **Auckland Ground**: *"ANZ26, cleared push and start with the tail facing North"*

!!! info
    The start instruction is only utilised in the real-world to ensure tha the jet wash doesn't interfere with the aircraft stands on the opposite side of the taxiway. As this isn't an issue within the Simulator, it is up to Controller discretion.

## Taxiing 

As the runway utilises high-speed exits from the runway, the Controller shall avoid using taxiway `A` when there is a potential for conflict between the taxiway and any vacating traffic. 

When Runway 23L is in operation aircraft will vacate at either `A6` or `A8`, and `A7`, `A5` or `A3` when 05R is in use.

When RWY 05R is active any domestic aircraft shall be given taxi instructions via `B` and `L`. Taxiway `M` may be utilized by controllers in order to get aircraft past any queues at holding point `A9`.

### Use of Holding Points

Departures may occur from any runway intersection, providing that it does not interfere with the use of any high-speed exits. Controllers may apply the following rules without coordination from the Pilot:

| Type        |  Runway 23L   | Runway 05R |
| ----------- | :-----------: | :--------: |
| Large Jets  | `A1` or `A1A` |   `A10`    |
| Medium Jets |     `A2`      |    `A9`    |
| Turboprops  | `A2` or `A3A` |    `A9`    |

!!! important "Usage of the A3 and A8 Holding Points"
    The `A3` and `A8` holds are not to be used, as Pilots cannot visually check the approaches are clear before entering the runway.

## VFR Procedures

### Arrival

In order to lessen the amount of instructions given to VFR traffic, the Controller shall issue the `Mangere Bridge` VFR arrival where possible. Once the Pilot reports overhead Mangere Town, the Controller shall integrate them with the circuit. [AIP Chart refers](https://www.aip.net.nz/assets/AIP/Aerodrome-Charts/Auckland-NZAA/NZAA_35.1_35.2.pdf){ target=new }.

!!! important
    If instructed to join via the overhead, it is the Controller's responsibilty to ensure that the missed approach is protected. A non-circuit side join may be given instead.


### Departure

In order to lessen the amount of instructions given to VFR traffic, the Controller shall issue the `Mangere Bridge` VFR departure where possible. Once the Pilot reaches Mangere Bridge, the aircraft shall be handed off to UNICOM or Approach where appropriate. [AIP Chart refers](https://www.aip.net.nz/assets/AIP/Aerodrome-Charts/Auckland-NZAA/NZAA_64.1.pdf){ target=new }.

As flights to the West, North, and Northeast require a turn against the circuit direction, the Tower shall approve a turn against the circuit direction.

!!! example "Turn against the Circuit direction"
    **Auckland Tower**: *"On departure a left/right turn is approved. Runway 05R/23L, cleared for takeoff"*

### Helicopters

Helicopter operations are frequent within Auckland CTR/C, usually operating within one of the three sectors. Tower must ensure that no VFR aircraft are present within the Instrument Sector when an aircraft is either turning onto, or established on an approach. VFR aircraft are not authorised to operate under any approach path, or within 3nm laterally of the approach path.

## Departures

Aircraft departures shall be managed in-line with the [Runway Operations section](../../controller-skills/seperation#runway-operations). 

Some departures have immediate divergent turns once the aircraft passes `A005`, taking the aircraft away from the centreline, allowing for another aircraft to follow soon after.

### SID Assignment

International SIDs are straight-forward, in that all of them have a shallow climb gradient, suitable for most aircraft types. The Controller shall issue the SID that is suggested by their Controller Client.

For Domestic aircraft that are departing to the North or Northeast, the Controller shall issue the SID that is suggested by the Controller Client. If the aircraft is departing to the South, the following rules shall be applied:

| Runway | Procedure  | Allowed A/C Categories | Is divergent?                  | Notes                                                                                                                |
| ------ | ---------- | ---------------------- | ------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| 05R    | `BROOK #Q` | Cat A to C             | Yes - >30° turn passing `A005` | **Preferred departure for Props**. May be given to Jets without request.                                             |
| 05R    | `PAGLA #Q` | Cat A to D             | No                             | **Preferred departure for Jets**. Steep climb gradient - aircraft unable to meet this shall be given the `POLIS #Q`. |
| 05R    | `POLIS #Q` | Cat A to D             | No                             | Shallower climb gradient.                                                                                            |
| 05R    | `REKIS #Q` | Cat A to D             | Yes - >30° turn passing `A005` | May be given to jets provided they are comfortable with the 180kt limitation at `VINOD`.                             |
| 05R    | `EMRAG #B` | Cat A to D             | No                             | Least preferred departure due to manual vectoring required.                                                          |


| Runway | Procedure  | Allowed A/C Categories | Is divergent?                  | Notes                                                                                                     |
| ------ | ---------- | ---------------------- | ------------------------------ | --------------------------------------------------------------------------------------------------------- |
| 23L    | `LENGU #A` | Cat A to D             | No                             | Least preferred departure due to manual vectoring required.                                               |
| 23L    | `LENGU #P` | Cat A to D             | No                             |                                                                                                           |
| 23L    | `LEVRA #P` | Cat A to D             | No                             | **Preferred departure for Jets**.                                                                         |
| 23L    | `STEAL #P` | Cat A to D             | Yes - >30° turn passing `A005` | **Preferred departure for Props**. Shall not be initially issued to Jets, but may be issued if requested. |

### Assigned Headings

To ensure a divergent departure occurs due to traffic, AA TMA may request an aircraft be assigned a heading to fly once passing `A005`. This ensures a 30 degree offset from the centreline exists, and therefore another aircraft may then depart. These will usually be issued when an aircraft is at the holding point, and will be given to the Tower as a part of AA TMA's release of the aircraft.

!!! example "Issuing a departure heading"
    **Auckland Tower**: *"JST203, additional departure instructions, report ready to copy"*  
    **JST203**: *"JST203, ready to copy"*  
    **Auckland Tower**: *"JST203, on departure turn right heading 170, climb four thousand"*
    **JST203**: *"JST203, on departure turn right heading 170, climb four thousand"*  