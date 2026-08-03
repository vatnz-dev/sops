---
  title: Overview and General Rules
---

New Zealand has seven Enroute Sectors, six of which can be staffed routinely on the network. This section provides detailed information on how to run each sector's operations, and lists some nuances that may be associated with them. 

VATNZ Controllers are able to staff all six permanent Enroute Sectors at once, in a situation known as Extended Services. [You can find out more about Sector Inheritance and Extended Services here](../controller-skills/inheritance-extending.md).

<div class="enroute-map" aria-label="Interactive map of New Zealand FIR enroute sectors">
  <div class="enroute-map__canvas">
    <img src="../assets/nz-fir-airspace.png" alt="NZ FIR Airspace Sectors">

    <svg class="enroute-map__overlay" viewBox="0 0 810 1050" aria-label="Enroute sector page links" role="navigation">
      <a class="enroute-map__sector enroute-map__sector--ocr" href="OCR/" aria-label="Open OCR sector page">
        <polygon points="468,33 554,40 632,81 680,151 700,200 548,213 550,249 565,269 558,354 503,355 484,256 407,404 359,378 326,340 306,285 310,189 330,128 381,72" />
      </a>
      <a class="enroute-map__sector enroute-map__sector--ran" href="RAN/" aria-label="Open RAN sector page">
        <polygon points="484,256 548,274 565,295 558,354 503,355 484,322" />
      </a>
      <a class="enroute-map__sector enroute-map__sector--bay" href="BAY/" aria-label="Open BAY sector page">
        <polygon points="548,213 700,200 751,242 724,346 680,309 616,318 558,354 565,295 548,274" />
      </a>
      <a class="enroute-map__sector enroute-map__sector--oha" href="OHA/" aria-label="Open OHA sector page">
        <polygon points="616,318 680,309 724,346 650,508 626,501 626,457 585,457 575,391 558,354" />
      </a>
      <a class="enroute-map__sector enroute-map__sector--nak" href="NAK/" aria-label="Open NAK sector page">
        <polygon points="407,404 503,355 558,354 575,391 585,457 626,457 626,501 650,508 630,559 596,551 540,633 495,587 407,560 391,515 392,458" />
      </a>
      <a class="enroute-map__sector enroute-map__sector--kai" href="KAI/" aria-label="Open KAI sector page">
        <polygon points="495,587 540,633 596,551 650,508 596,643 536,631" />
      </a>
      <a class="enroute-map__sector enroute-map__sector--sth" href="STH/" aria-label="Open STH sector page">
        <polygon points="407,560 495,587 536,631 596,643 482,953 316,882 324,849 298,798 304,735 333,684 379,650 392,600" />
      </a>
    </svg>

    <span class="enroute-map__panel enroute-map__panel--ocr">
      <strong>Auckland - Oceanic Radar (OCR)</strong>
      <span>NZAA_CTR | Auckland Control | 123.900</span>
      <span>Sequences NZAA and NZWP arrivals, with RAN, BAY and AA TMA inheritance when offline.</span>
    </span>

    <span class="enroute-map__panel enroute-map__panel--ran">
      <strong>Auckland - Raglan (RAN) | EVENT ONLY</strong>
      <span>NZAA-R_CTR | Auckland Control | 126.000</span>
      <span>Event-only sector managing NZAA sequencing, departures and HN TMA traffic.</span>
    </span>

    <span class="enroute-map__panel enroute-map__panel--bay">
      <strong>Christchurch - Bays (BAY)</strong>
      <span>NZCH-B_CTR | Bay Approach | 119.500</span>
      <span>Manages East Coast flow into AA TMA and traffic crossing into OHA.</span>
    </span>

    <span class="enroute-map__panel enroute-map__panel--oha">
      <strong>Ohakea (OHA)</strong>
      <span>NZOH_CTR | Ohakea Control | 126.200</span>
      <span>Links prop and military traffic around OH TMA, NZAA and NZWN flows.</span>
    </span>

    <span class="enroute-map__panel enroute-map__panel--nak">
      <strong>Christchurch - Taranaki (NAK)</strong>
      <span>NZCH-T_CTR | Christchurch Control | 123.700</span>
      <span>Primary NZAA, NZCH, NZQN and NZWN flow sector, including WN TMA inheritance.</span>
    </span>

    <span class="enroute-map__panel enroute-map__panel--kai">
      <strong>Christchurch - Kaikoura (KAI)</strong>
      <span>NZCH-K_CTR | Christchurch Control | 129.400</span>
      <span>Manages northbound and southbound NZCH traffic, including CH TMA inheritance.</span>
    </span>

    <span class="enroute-map__panel enroute-map__panel--sth">
      <strong>Christchurch - South (STH)</strong>
      <span>NZCH-S_CTR | Christchurch Control | 129.300</span>
      <span>Manages NZQN, NZDN, NZNV and western NZCH flows, with QN TMA inheritance.</span>
    </span>
  </div>

  <div class="enroute-map__cards" aria-label="Enroute sector links">
    <a href="OCR/"><strong>OCR</strong><span>Auckland Control | 123.900</span></a>
    <a href="RAN/"><strong>RAN | EVENT ONLY</strong><span>Auckland Control | 126.000</span></a>
    <a href="BAY/"><strong>BAY</strong><span>Bay Approach | 119.500</span></a>
    <a href="OHA/"><strong>OHA</strong><span>Ohakea Control | 126.200</span></a>
    <a href="NAK/"><strong>NAK</strong><span>Christchurch Control | 123.700</span></a>
    <a href="KAI/"><strong>KAI</strong><span>Christchurch Control | 129.400</span></a>
    <a href="STH/"><strong>STH</strong><span>Christchurch Control | 129.300</span></a>
  </div>
</div>

## General Rules of Thumb for ENR

This section outlines some general rules for Enroute Controllers. More specific rules for each sector can be found on the individual sector pages.

### ATIS Connection Management

Controllers are permitted to create up to 4 ATIS connections on the network and they should adhere to the following guidance when creating ATIS connections;

| Position                   | Primary ATIS Aerodromes    | Additional ATIS Aerodromes (Inherited Sectors) |
| -------------------------- | -------------------------- | ---------------------------------------------- |
| NZAA_CTR (OCR)             | NZAA, NZWP                 | NZNP (RAN) NZHN, NZTG, NZRO, NZGS (BAY)        |
| NZCH-B_CTR (BAY)           | NZTG, NZRO, NZGS           | NZHN (RAN)                                     |
| NZOH_CTR (OHA)             | NZPM, NZOH, NZNR           | None                                           |
| NZCH-T_CTR (NAK)           | NZWN, NZNS, NZWB           | NZPM, NZOH, NZNR (OHA)                         |
| NZCH-K_CTR (KAI)           | NZCH                       | None                                           |
| NZCH-S_CTR (STH)           | NZDN, NZQN, NZNV           | NZCH (KAI)                                     |

!!! important
    Controllers should create **at least one** ATIS connection for aerodromes within their primary sector before aerodromes within inherited or extended sectors.

    Controllers may create an ATIS connection at an aerodrome with high levels of traffic if that aerodrome falls within an inherited or extended sector.
    

!!! note
    Should a controller find that an ATIS has already been created by a controller below them, they should attempt to satisfy the requirements of the above logic table. 
    
    ATIS connections within extended or inherited sectors should be surrendered if another controller logs onto that position, unless prior co-ordination has been made.

### STARs

Generally, if an aircraft's destination is in a bordering sector, you should ensure that a STAR clearance has been issued. In most cases a STAR clearance will be issued by the sector immediately before it's destination sector.

### Altitude Management

In most cases aircraft should cross an ENR border either at their RFL, or in climb to their RFL.

If an aircraft requires a descent into an **ENR** sector, they can be descended to `FL200` if northbound, or `FL190` if southbound without coordination from the next sector.

If an aircraft requires a descent into a **TMA** or **Procedural TWR** sector, they can be descended to that airspace's Upper Limit without coordination from the that sector.

### Direct Routing

Aircraft should never be routed directly to a fix that is outside of your sector without coordination first. 

Enroute sectors may clear an aircraft directly to a ENR boundary fix without coordination, provided that they fly on an established airway thereafter.

Enroute sectors may clear an aircraft directly to a TMA STAR boundary fix, provided they have then been cleared to track by the STAR thereafter. Additionally, an aircraft may be cleared direct to a point on the STAR, provided that it has been coordinated, and they have been told to rejoin the STAR thereafter.
