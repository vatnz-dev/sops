---
  title: Overview and General Rules
---

New Zealand has seven Enroute Sectors, six of which can be staffed routinely on the network. This section provides detailed information on how to run each sector's operations, and lists some nuances that may be associated with them. 

VATNZ Controllers are able to staff all six permanent Enroute Sectors at once, in a situation known as Extended Services. [You can find out more about Sector Inheritance and Extended Services here](../controller-skills/inheritance-extending.md).

!!! tip "Interactive Sector Map"
    Hover over a sector to view basic position information, then click the sector to open the full procedure page.

<style>
  #enroute-map {
    position: relative;
    width: min(100%, 810px);
    margin: 1.5rem auto 2rem;
  }

  #enroute-map img {
    display: block;
    width: 100%;
    height: auto;
  }

  #enroute-map .map-hotspots {
    position: absolute;
    inset: 0;
  }

  #enroute-map .map-hotspots a {
    position: absolute;
    inset: 0;
    cursor: pointer;
    clip-path: polygon(var(--points));
  }

  #enroute-map .map-hotspots a:focus {
    outline: 3px solid #ffffff;
    outline-offset: -3px;
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

  <div class="map-hotspots" aria-label="Enroute sector page links">
    <a id="ocr-link" href="OCR/" aria-label="Open OCR sector page" style="--points: 57.78% 3.14%, 68.40% 3.81%, 78.02% 7.71%, 83.95% 14.38%, 86.42% 19.05%, 67.65% 20.29%, 67.90% 23.71%, 69.75% 25.62%, 68.89% 33.71%, 62.10% 33.81%, 59.75% 24.38%, 50.25% 38.48%, 44.32% 36%, 40.25% 32.38%, 37.78% 27.14%, 38.27% 18%, 40.74% 12.19%, 47.04% 6.86%;"></a>
    <a id="ran-link" href="RAN/" aria-label="Open RAN sector page" style="--points: 59.75% 24.38%, 67.65% 26.10%, 69.75% 28.10%, 68.89% 33.71%, 62.10% 33.81%, 59.75% 30.67%;"></a>
    <a id="bay-link" href="BAY/" aria-label="Open BAY sector page" style="--points: 67.65% 20.29%, 86.42% 19.05%, 92.72% 23.05%, 89.38% 32.95%, 83.95% 29.43%, 76.05% 30.29%, 68.89% 33.71%, 69.75% 28.10%, 67.65% 26.10%;"></a>
    <a id="oha-link" href="OHA/" aria-label="Open OHA sector page" style="--points: 76.05% 30.29%, 83.95% 29.43%, 89.38% 32.95%, 80.25% 48.38%, 77.28% 47.71%, 77.28% 43.52%, 72.22% 43.52%, 70.99% 37.24%, 68.89% 33.71%;"></a>
    <a id="nak-link" href="NAK/" aria-label="Open NAK sector page" style="--points: 50.25% 38.48%, 62.10% 33.81%, 68.89% 33.71%, 70.99% 37.24%, 72.22% 43.52%, 77.28% 43.52%, 77.28% 47.71%, 80.25% 48.38%, 77.78% 53.24%, 73.58% 52.48%, 66.67% 60.29%, 61.11% 55.90%, 50.25% 53.33%, 48.27% 49.05%, 48.40% 43.62%;"></a>
    <a id="kai-link" href="KAI/" aria-label="Open KAI sector page" style="--points: 77.84% 54.77%, 69.20% 65.91%, 64.68% 62.62%, 63.38% 58.88%, 62.54% 54.64%, 62.79% 54.22%, 63.32% 53.33%, 64.75% 51.89%, 65.14% 51.24%, 68.44% 51.76%, 68.60% 51.79%, 71.12% 51.74%, 73.14% 52.65%, 75.47% 52.35%;"></a>
    <a id="sth-link" href="STH/" aria-label="Open STH sector page" style="--points: 50.25% 53.33%, 61.11% 55.90%, 66.17% 60.10%, 73.58% 61.24%, 59.51% 90.76%, 39.01% 84%, 40% 80.86%, 36.79% 76%, 37.53% 70%, 41.11% 65.14%, 46.79% 61.90%, 48.40% 57.14%;"></a>
  </div>

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
