---
  title: Overview and General Rules
---

New Zealand has seven Enroute Sectors, six of which can be staffed routinely on the network. This section provides detailed information on how to run each sector's operations, and lists some nuances that may be associated with them. 

VATNZ Controllers are able to staff all six permanent Enroute Sectors at once, in a situation known as Extended Services. [You can find out more about Sector Inheritance and Extended Services here](../controller-skills/inheritance-extending.md).

<svg id="enroute-sector-map" width="100%" viewBox="0 0 810 1050" role="img" aria-labelledby="enroute-map-title enroute-map-desc">
  <title id="enroute-map-title">NZ FIR Airspace Sectors</title>
  <desc id="enroute-map-desc">Interactive map of New Zealand FIR enroute sectors. Select a sector to open its page.</desc>
  <image href="../assets/nz-fir-airspace.png" width="810" height="1050" preserveAspectRatio="xMidYMid meet" />

  <style>
    #enroute-sector-map a polygon {
      cursor: pointer;
      fill: #64748b;
      fill-opacity: 0;
      stroke: #ffffff;
      stroke-linejoin: round;
      stroke-opacity: 0;
      stroke-width: 4;
      transition: fill-opacity 160ms ease, stroke-opacity 160ms ease;
    }

    #enroute-sector-map a:hover polygon,
    #enroute-sector-map a:focus polygon {
      fill-opacity: 0.3;
      stroke-opacity: 0.95;
    }

    #enroute-sector-map .sector-panel {
      opacity: 0;
      pointer-events: none;
      transition: opacity 160ms ease;
    }

    #enroute-sector-map:has(#ocr-link:hover) #ocr-panel,
    #enroute-sector-map:has(#ocr-link:focus) #ocr-panel,
    #enroute-sector-map:has(#ran-link:hover) #ran-panel,
    #enroute-sector-map:has(#ran-link:focus) #ran-panel,
    #enroute-sector-map:has(#bay-link:hover) #bay-panel,
    #enroute-sector-map:has(#bay-link:focus) #bay-panel,
    #enroute-sector-map:has(#oha-link:hover) #oha-panel,
    #enroute-sector-map:has(#oha-link:focus) #oha-panel,
    #enroute-sector-map:has(#nak-link:hover) #nak-panel,
    #enroute-sector-map:has(#nak-link:focus) #nak-panel,
    #enroute-sector-map:has(#kai-link:hover) #kai-panel,
    #enroute-sector-map:has(#kai-link:focus) #kai-panel,
    #enroute-sector-map:has(#sth-link:hover) #sth-panel,
    #enroute-sector-map:has(#sth-link:focus) #sth-panel {
      opacity: 1;
    }
  </style>

  <a id="ocr-link" href="OCR/" aria-label="Open OCR sector page">
    <polygon id="ocr-shape" points="468,33 554,40 632,81 680,151 700,200 548,213 550,249 565,269 558,354 503,355 484,256 407,404 359,378 326,340 306,285 310,189 330,128 381,72">
      <title>Auckland - Oceanic Radar (OCR) | NZAA_CTR | Auckland Control | 123.900</title>
      <set attributeName="fill-opacity" to="0.26" begin="mouseover;ocr-link.focusin" end="mouseout;ocr-link.focusout" />
      <set attributeName="stroke-opacity" to="0.95" begin="mouseover;ocr-link.focusin" end="mouseout;ocr-link.focusout" />
    </polygon>
  </a>

  <a id="ran-link" href="RAN/" aria-label="Open RAN sector page">
    <polygon id="ran-shape" points="484,256 548,274 565,295 558,354 503,355 484,322">
      <title>Auckland - Raglan (RAN) | EVENT ONLY | NZAA-R_CTR | Auckland Control | 126.000</title>
      <set attributeName="fill-opacity" to="0.34" begin="mouseover;ran-link.focusin" end="mouseout;ran-link.focusout" />
      <set attributeName="stroke-opacity" to="0.95" begin="mouseover;ran-link.focusin" end="mouseout;ran-link.focusout" />
    </polygon>
  </a>

  <a id="bay-link" href="BAY/" aria-label="Open BAY sector page">
    <polygon id="bay-shape" points="548,213 700,200 751,242 724,346 680,309 616,318 558,354 565,295 548,274">
      <title>Christchurch - Bays (BAY) | NZCH-B_CTR | Bay Approach | 119.500</title>
      <set attributeName="fill-opacity" to="0.28" begin="mouseover;bay-link.focusin" end="mouseout;bay-link.focusout" />
      <set attributeName="stroke-opacity" to="0.95" begin="mouseover;bay-link.focusin" end="mouseout;bay-link.focusout" />
    </polygon>
  </a>

  <a id="oha-link" href="OHA/" aria-label="Open OHA sector page">
    <polygon id="oha-shape" points="616,318 680,309 724,346 650,508 626,501 626,457 585,457 575,391 558,354">
      <title>Ohakea (OHA) | NZOH_CTR | Ohakea Control | 126.200</title>
      <set attributeName="fill-opacity" to="0.28" begin="mouseover;oha-link.focusin" end="mouseout;oha-link.focusout" />
      <set attributeName="stroke-opacity" to="0.95" begin="mouseover;oha-link.focusin" end="mouseout;oha-link.focusout" />
    </polygon>
  </a>

  <a id="nak-link" href="NAK/" aria-label="Open NAK sector page">
    <polygon id="nak-shape" points="407,404 503,355 558,354 575,391 585,457 626,457 626,501 650,508 630,559 596,551 540,633 495,587 407,560 391,515 392,458">
      <title>Christchurch - Taranaki (NAK) | NZCH-T_CTR | Christchurch Control | 123.700</title>
      <set attributeName="fill-opacity" to="0.28" begin="mouseover;nak-link.focusin" end="mouseout;nak-link.focusout" />
      <set attributeName="stroke-opacity" to="0.95" begin="mouseover;nak-link.focusin" end="mouseout;nak-link.focusout" />
    </polygon>
  </a>

  <a id="kai-link" href="KAI/" aria-label="Open KAI sector page">
    <polygon id="kai-shape" points="495,587 540,633 596,551 650,508 596,643 536,631">
      <title>Christchurch - Kaikoura (KAI) | NZCH-K_CTR | Christchurch Control | 129.400</title>
      <set attributeName="fill-opacity" to="0.3" begin="mouseover;kai-link.focusin" end="mouseout;kai-link.focusout" />
      <set attributeName="stroke-opacity" to="0.95" begin="mouseover;kai-link.focusin" end="mouseout;kai-link.focusout" />
    </polygon>
  </a>

  <a id="sth-link" href="STH/" aria-label="Open STH sector page">
    <polygon id="sth-shape" points="407,560 495,587 536,631 596,643 482,953 316,882 324,849 298,798 304,735 333,684 379,650 392,600">
      <title>Christchurch - South (STH) | NZCH-S_CTR | Christchurch Control | 129.300</title>
      <set attributeName="fill-opacity" to="0.26" begin="mouseover;sth-link.focusin" end="mouseout;sth-link.focusout" />
      <set attributeName="stroke-opacity" to="0.95" begin="mouseover;sth-link.focusin" end="mouseout;sth-link.focusout" />
    </polygon>
  </a>

  <g id="ocr-panel" class="sector-panel">
    <rect x="145" y="150" width="455" height="140" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <text x="172" y="204" fill="#111827" font-size="22" font-weight="700">Auckland - Oceanic Radar (OCR)</text>
    <text x="172" y="237" fill="#111827" font-size="18">NZAA_CTR | Auckland Control | 123.900</text>
    <text x="172" y="265" fill="#111827" font-size="16">Sequences NZAA and NZWP arrivals.</text>
    <text x="172" y="283" fill="#475569" font-size="14" font-weight="700">Click for more information</text>
    <set attributeName="opacity" to="1" begin="ocr-shape.mouseover;ocr-link.focusin" end="ocr-shape.mouseout;ocr-link.focusout" />
  </g>

  <g id="ran-panel" class="sector-panel">
    <rect x="365" y="230" width="410" height="145" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <text x="387" y="284" fill="#111827" font-size="22" font-weight="700">Auckland - Raglan (RAN)</text>
    <text x="387" y="314" fill="#b91c1c" font-size="17" font-weight="700">EVENT ONLY</text>
    <text x="387" y="340" fill="#111827" font-size="17">NZAA-R_CTR | Auckland Control | 126.000</text>
    <text x="387" y="362" fill="#475569" font-size="14" font-weight="700">Click for more information</text>
    <set attributeName="opacity" to="1" begin="ran-shape.mouseover;ran-link.focusin" end="ran-shape.mouseout;ran-link.focusout" />
  </g>

  <g id="bay-panel" class="sector-panel">
    <rect x="190" y="135" width="470" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <text x="212" y="188" fill="#111827" font-size="22" font-weight="700">Christchurch - Bays (BAY)</text>
    <text x="212" y="222" fill="#111827" font-size="18">NZCH-B_CTR | Bay Approach | 119.500</text>
    <text x="212" y="250" fill="#111827" font-size="16">Manages East Coast flow into AA TMA and OHA.</text>
    <text x="212" y="272" fill="#475569" font-size="14" font-weight="700">Click for more information</text>
    <set attributeName="opacity" to="1" begin="bay-shape.mouseover;bay-link.focusin" end="bay-shape.mouseout;bay-link.focusout" />
  </g>

  <g id="oha-panel" class="sector-panel">
    <rect x="325" y="370" width="430" height="140" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <text x="347" y="424" fill="#111827" font-size="22" font-weight="700">Ohakea (OHA)</text>
    <text x="347" y="457" fill="#111827" font-size="18">NZOH_CTR | Ohakea Control | 126.200</text>
    <text x="347" y="485" fill="#111827" font-size="16">Links prop and military traffic around OH TMA.</text>
    <text x="347" y="503" fill="#475569" font-size="14" font-weight="700">Click for more information</text>
    <set attributeName="opacity" to="1" begin="oha-shape.mouseover;oha-link.focusin" end="oha-shape.mouseout;oha-link.focusout" />
  </g>

  <g id="nak-panel" class="sector-panel">
    <rect x="125" y="405" width="465" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <text x="147" y="460" fill="#111827" font-size="22" font-weight="700">Christchurch - Taranaki (NAK)</text>
    <text x="147" y="494" fill="#111827" font-size="18">NZCH-T_CTR | Christchurch Control | 123.700</text>
    <text x="147" y="522" fill="#111827" font-size="16">Primary NZAA, NZCH, NZQN and NZWN flow sector.</text>
    <text x="147" y="544" fill="#475569" font-size="14" font-weight="700">Click for more information</text>
    <set attributeName="opacity" to="1" begin="nak-shape.mouseover;nak-link.focusin" end="nak-shape.mouseout;nak-link.focusout" />
  </g>

  <g id="kai-panel" class="sector-panel">
    <rect x="310" y="570" width="460" height="140" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <text x="332" y="624" fill="#111827" font-size="22" font-weight="700">Christchurch - Kaikoura (KAI)</text>
    <text x="332" y="657" fill="#111827" font-size="18">NZCH-K_CTR | Christchurch Control | 129.400</text>
    <text x="332" y="685" fill="#111827" font-size="16">Manages northbound and southbound NZCH traffic.</text>
    <text x="332" y="703" fill="#475569" font-size="14" font-weight="700">Click for more information</text>
    <set attributeName="opacity" to="1" begin="kai-shape.mouseover;kai-link.focusin" end="kai-shape.mouseout;kai-link.focusout" />
  </g>

  <g id="sth-panel" class="sector-panel">
    <rect x="110" y="690" width="465" height="150" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <text x="132" y="745" fill="#111827" font-size="22" font-weight="700">Christchurch - South (STH)</text>
    <text x="132" y="779" fill="#111827" font-size="18">NZCH-S_CTR | Christchurch Control | 129.300</text>
    <text x="132" y="807" fill="#111827" font-size="16">Manages NZQN, NZDN, NZNV and western NZCH flows.</text>
    <text x="132" y="829" fill="#475569" font-size="14" font-weight="700">Click for more information</text>
    <set attributeName="opacity" to="1" begin="sth-shape.mouseover;sth-link.focusin" end="sth-shape.mouseout;sth-link.focusout" />
  </g>
</svg>

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
