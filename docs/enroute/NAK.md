---
  title: Christchurch - Taranaki (NAK)

---

## Positions

| Sector Name                     | Shortcode | Callsign             | Frequency | Login ID   |
| ------------------------------- | --------- | -------------------- | --------- | ---------- |
| Christchurch Control (Taranaki) | NAK       | Christchurch Control | 123.700   | NZCH-T_CTR |

## Airspace

NAK covers all airspace within the lateral bounds as found below, with the only exception being the airspace that has been delegated to WN TMA and OH TMA. The lower limit for most airspace is `A095`, dropping to `A065` in areas surrounding Mt Ruapehu and Nelson.

When WN TMA is offline, NAK automatically inherits and assumes responsibility for that sector. 

When NS TWR is offline, NAK automatically inherits the TWR and Procedural Approach services provided by NS TWR. See [the responsibilities section on NS TWR](#ns-twr). 

!!! error
    Add Airspace diagram for NAK

## Sector Responsibilities

NAK is the busiest sector in the NZZC FIR, and is largely responsible for managing the flow of traffic between NZAA, NZCH and NZQN, while managing the descent and sequencing of aircraft into NZWN.

### WN TMA

NAK shall ensure that an efficient arrival flow is managed into WN TMA.

### NS TWR

When NS TWR is offline, RAN is responsible for all functions of NS TWR, including the Procedural Tower service. 

When responsible for NS TWR, RAN may opt to provide a radar approach service, rather than a procedural approach service.

### NP TWR

When online, the NP Procedural Tower service shall be provided by RAN or OCR. If these sectors are offline, NAK may elect to provide the same service, although not mandatory. 

When responsible for NP TWR, RAN may opt to provide a radar approach service, rather than a procedural approach service.


## Coordination

### Oceanic

Oceanic-bound aircraft are required to cross the FIR boundary at their CFL and via a defined waypoint. 

NAK may clear Oceanic bound aircraft direct to their boundary crossing fix without coordination from ARO. If aircraft request an amendment to their RFL, this shall be coordinated with ARO.

NAK shall give ARO a **10 minute warning** of the aircraft's crossing of the FIR boundary.

### OCR

NAK shall assign STARs to any aircraft where the destination is within the lateral bounds of OCR without coordination.

NAK shall ensure that any aircraft crossing the OCR/NAK boundary is established on an airway. NAK may clear aircraft direct to a boundary fix, provided it is established on an airway once it reaches the direct-to fix.

If necessary, NAK may descend OCR bound aircraft to `FL200` without coordination.

### RAN

NAK shall assign STARs to any aircraft bound for NZAA without coordination, provided it is for the nominated runway and approach type as stated in the ATIS. A request for use of a non-nominated approach requires coordination from RAN, who will liaise with AA TMA and ADC.

While descent is normally provided by RAN, NAK may descend aircraft to `FL180` without coordination from RAN.

### OHA

NAK shall assign STARs to any aircraft bound for an aerodrome within OHA without coordination. 

While descent is normally provided by OHA, NAK may descend aircraft to `FL200` without coordination from OHA.

!!! note
    Note that while NZWU, NZOH and NZPM sit within the lateral bounds of NAK, any required coordination shall be done with OH TMA if online.

### KAI

NAK shall assign STARs to any aircraft bound for NZCH without coordination, provided it is for the nominated runway and approach type as stated in the ATIS. A request for use of a non-nominated approach requires coordination from KAI, who will liaise with CH TMA and ADC.

While descent is normally provided by KAI, NAK may descend aircraft to `FL200` without coordination from OHA.

### STH

NAK shall not normally assign STARs to aircraft bound for STH, due to the large distance between the NAK/STH border and NZQN, NZDN or NZNV. The only exception is when an aircraft is bound for an aerodrome within 150nm of the border, such as NZGM, NZHK or NZTU. In this case, a STAR may be issued by NAK with coordination from STH.

NAK shall not normally descend aircraft into STH sector unless bound for an aircraft within 150nm of the border. In this case, NAK may descend aircraft to `FL150` without coordination. 

If further descent is required, NAK shall clear the aircraft to leave controlled airspace on descent through `A135`, report to STH when on the ground, and hand the tag to STH. This shall be coordinated beforehand.

!!! hint "RTF for leaving CTA and transferring radar monitoring"
    **NAK**: *LDM inbound Hokitika on BOSLA arrival requests further descent. Request descent below CTA and transfer radar monitoring your frequency.*  
    **STH**: *LDM is cleared below CTA and I accept radar monitoring on this frequency.*

    **NAK**: *LDM, cleared to leave controlled airspace on descent through 13,500 feet. No reported traffic in the area. Christchurch Control accepts radar monitoring on their frequency, 129.400. Report on their frequency for IFR cancellation.*


### OH TMA

NAK shall assign STARs without coordination to any aircraft bound for NZPM and NZOH if not already done so. NAK may issue STARs for IFR aircraft bound for NZWU or NZFI with coordination from OH TMA.

NAK may descend aircraft to `A095` without coordination from OH TMA.

### WN TMA

NAK may issue STAR clearances to aircraft bound for any aerodrome within WN TMAs airspace without coordination, provided that the STAR links with the nominated runway and approach type as stated in the ATIS. A request for use of a non-nominated approach requires agreement from both the TMA and ADC Controller.

NAK may descend aircraft to `A110` without coordination from WN TMA.

If a sequencing conflict is to occur, NAK shall coordinate with AA TMA as to an ideal arrival order. 

NAK may clear aircraft direct to the STAR's WN TMA boundary fix without coordination, provided that they have been cleared to rejoin the STAR at that point. Aircraft may be cleared to track direct to a fix within WN TMA's boundary with co-ordination, subject to the same condition.

!!! hint "RTF for rejoining a STAR"
    **NAK**: *New Zealand 677, track direct RIPPA to rejoin the STAR. When ready descend A080*.

    **Note**: As `RIPPA` sits within WN TMA's airspace, co-ordination would be required.

### NP TWR

When NP TWR is offline, the top-down service shall be provided by RAN, with all NP TWR airspace that exists within NAK's lateral bounds being delegated to RAN.

NAK may descend NZNP bound traffic to `A065` without coordination.

### NS TWR

NAK shall issue STAR clearances for aircraft bound for NZNS, and may descend these aircraft to `A095` without coordination.