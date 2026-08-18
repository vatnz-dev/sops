---
  title: Overview and General Rules
---

New Zealand has seven Enroute Sectors, six of which can be staffed routinely on the network. This section provides detailed information on how to run each sector's operations, and lists some nuances that may be associated with them. 

VATNZ Controllers are able to staff all six permanent Enroute Sectors at once, in a situation known as Extended Services. [You can find out more about Sector Inheritance and Extended Services here](../controller-skills/inheritance-extending.md).

<style>
  #enroute-map {
    position: relative;
    width: min(100%, 810px);
    margin: 1.5rem auto 2rem;
  }

  #enroute-map img,
  #enroute-map svg {
    display: block;
    width: 100%;
    height: auto;
  }

  #enroute-map svg {
    position: absolute;
    inset: 0;
  }

  #enroute-map polygon {
    cursor: pointer;
    fill: #64748b;
    fill-opacity: 0;
    stroke: transparent;
    stroke-width: 0;
    transition: fill-opacity 160ms ease;
  }

  #enroute-map a:hover polygon,
  #enroute-map a:focus polygon {
    fill-opacity: 0.3;
  }

  #enroute-map .sector-placard {
    position: absolute;
    z-index: 2;
    display: block !important;
    width: min(28rem, 72%);
    padding: 0.8rem 0.95rem;
    border: 1px solid #cbd5e1;
    border-radius: 0.4rem;
    background: #ffffff;
    box-shadow: 0 0.75rem 2rem rgba(15, 23, 42, 0.22);
    color: #111827;
    font-size: 0.78rem;
    line-height: 1.35;
    opacity: 0;
    pointer-events: none;
    transform: translateY(0.3rem);
    transition: opacity 160ms ease, transform 160ms ease;
  }

  #enroute-map .sector-placard strong,
  #enroute-map .sector-placard span {
    display: block;
  }

  #enroute-map .sector-placard strong {
    margin-bottom: 0.2rem;
    color: #111827;
    font-size: 0.9rem;
  }

  #enroute-map .sector-placard .sector-cta {
    margin-top: 0.35rem;
    color: #475569;
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
  }

  #enroute-map #ocr-card { left: 18%; top: 14%; }
  #enroute-map #ran-card { left: 45%; top: 24%; }
  #enroute-map #bay-card { left: 20%; top: 13%; }
  #enroute-map #oha-card { left: 40%; top: 36%; }
  #enroute-map #nak-card { left: 15%; top: 40%; }
  #enroute-map #kai-card { left: 36%; top: 55%; }
  #enroute-map #sth-card { left: 14%; top: 68%; }

  #enroute-map:has(#ocr-link:hover) #ocr-card,
  #enroute-map:has(#ocr-link:focus) #ocr-card,
  #enroute-map:has(#ran-link:hover) #ran-card,
  #enroute-map:has(#ran-link:focus) #ran-card,
  #enroute-map:has(#bay-link:hover) #bay-card,
  #enroute-map:has(#bay-link:focus) #bay-card,
  #enroute-map:has(#oha-link:hover) #oha-card,
  #enroute-map:has(#oha-link:focus) #oha-card,
  #enroute-map:has(#nak-link:hover) #nak-card,
  #enroute-map:has(#nak-link:focus) #nak-card,
  #enroute-map:has(#kai-link:hover) #kai-card,
  #enroute-map:has(#kai-link:focus) #kai-card,
  #enroute-map:has(#sth-link:hover) #sth-card,
  #enroute-map:has(#sth-link:focus) #sth-card {
    opacity: 1 !important;
    transform: translateY(0);
  }
</style>

<div id="enroute-map" aria-label="Interactive map of New Zealand FIR enroute sectors">
  <img src="../assets/nz-fir-airspace.png" alt="NZ FIR Airspace Sectors">

  <svg viewBox="0 0 810 1050" role="navigation" aria-label="Enroute sector page links">
    <a id="ocr-link" href="OCR/" aria-label="Open OCR sector page">
      <polygon points="468,33 554,40 632,81 680,151 700,200 548,213 550,249 565,269 558,354 503,355 484,256 407,404 359,378 326,340 306,285 310,189 330,128 381,72" />
    </a>
    <a id="ran-link" href="RAN/" aria-label="Open RAN sector page">
      <polygon points="484,256 548,274 565,295 558,354 503,355 484,322" />
    </a>
    <a id="bay-link" href="BAY/" aria-label="Open BAY sector page">
      <polygon points="548,213 700,200 751,242 724,346 680,309 616,318 558,354 565,295 548,274" />
    </a>
    <a id="oha-link" href="OHA/" aria-label="Open OHA sector page">
      <polygon points="616,318 680,309 724,346 650,508 626,501 626,457 585,457 575,391 558,354" />
    </a>
    <a id="nak-link" href="NAK/" aria-label="Open NAK sector page">
      <polygon points="407,404 503,355 558,354 575,391 585,457 626,457 626,501 650,508 630,559 596,551 540,633 495,587 407,560 391,515 392,458" />
    </a>
    <a id="kai-link" href="KAI/" aria-label="Open KAI sector page">
      <polygon points="630.5,575.1 560.5,692.1 523.9,657.5 513.4,618.2 506.6,573.7 508.6,569.3 512.9,560 524.5,544.8 527.6,538 554.4,543.5 555.7,543.8 576.1,543.3 592.4,552.8 611.3,549.7" />
    </a>
    <a id="sth-link" href="STH/" aria-label="Open STH sector page">
      <polygon points="407,560 495,587 536,631 596,643 482,953 316,882 324,849 298,798 304,735 333,684 379,650 392,600" />
    </a>
  </svg>

  <div id="ocr-card" class="sector-placard" style="display: none;">
    <strong>Auckland - Oceanic Radar (OCR)</strong>
    <span>NZAA_CTR | Auckland Control | 123.900</span>
    <span>Sequences NZAA and NZWP arrivals.</span>
    <span class="sector-cta">Click for more information</span>
  </div>

  <div id="ran-card" class="sector-placard" style="display: none;">
    <strong>Auckland - Raglan (RAN)</strong>
    <span style="color: #b91c1c; font-weight: 700;">EVENT ONLY</span>
    <span>NZAA-R_CTR | Auckland Control | 126.000</span>
    <span class="sector-cta">Click for more information</span>
  </div>

  <div id="bay-card" class="sector-placard" style="display: none;">
    <strong>Christchurch - Bays (BAY)</strong>
    <span>NZCH-B_CTR | Bay Approach | 119.500</span>
    <span>Manages East Coast flow into AA TMA and OHA.</span>
    <span class="sector-cta">Click for more information</span>
  </div>

  <div id="oha-card" class="sector-placard" style="display: none;">
    <strong>Ohakea (OHA)</strong>
    <span>NZOH_CTR | Ohakea Control | 126.200</span>
    <span>Links prop and military traffic around OH TMA.</span>
    <span class="sector-cta">Click for more information</span>
  </div>

  <div id="nak-card" class="sector-placard" style="display: none;">
    <strong>Christchurch - Taranaki (NAK)</strong>
    <span>NZCH-T_CTR | Christchurch Control | 123.700</span>
    <span>Primary NZAA, NZCH, NZQN and NZWN flow sector.</span>
    <span class="sector-cta">Click for more information</span>
  </div>

  <div id="kai-card" class="sector-placard" style="display: none;">
    <strong>Christchurch - Kaikoura (KAI)</strong>
    <span>NZCH-K_CTR | Christchurch Control | 129.400</span>
    <span>Manages northbound and southbound NZCH traffic.</span>
    <span class="sector-cta">Click for more information</span>
  </div>

  <div id="sth-card" class="sector-placard" style="display: none;">
    <strong>Christchurch - South (STH)</strong>
    <span>NZCH-S_CTR | Christchurch Control | 129.300</span>
    <span>Manages NZQN, NZDN, NZNV and western NZCH flows.</span>
    <span class="sector-cta">Click for more information</span>
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
