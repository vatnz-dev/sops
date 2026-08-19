---
  title: Overview
---

This section covers aerodrome specific procedures, separated by airspace class.

!!! tip "Interactive Aerodrome Map"
    Hover over an aerodrome marker to view its classification, then select it to open the relevant procedure page.

<style>
  #aerodrome-map {
    position: relative;
    width: min(100%, 46rem);
    margin: 1.5rem auto 2rem;
  }

  #aerodrome-map img,
  #aerodrome-map svg {
    display: block;
    width: 100%;
    height: auto;
  }

  #aerodrome-map svg {
    position: absolute;
    inset: 0;
  }

  #aerodrome-map .aerodrome-marker {
    cursor: pointer;
    fill: transparent;
    stroke: transparent;
    stroke-width: 0;
  }

  #aerodrome-map .aerodrome-marker:focus,
  #aerodrome-map a:hover .aerodrome-marker {
    fill: #ffffff;
    fill-opacity: 0.22;
    stroke: #ffffff;
    stroke-opacity: 0.9;
    stroke-width: 8;
  }

  #aerodrome-map .aerodrome-placard {
    position: absolute;
    z-index: 2;
    display: block !important;
    width: min(18rem, 66%);
    padding: 0.75rem 0.9rem;
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

  #aerodrome-map .aerodrome-placard strong,
  #aerodrome-map .aerodrome-placard span {
    display: block;
  }

  #aerodrome-map .aerodrome-placard strong {
    margin-bottom: 0.2rem;
    font-size: 0.9rem;
  }

  #aerodrome-map .aerodrome-placard .aerodrome-cta {
    margin-top: 0.35rem;
    color: #475569;
    font-size: 0.68rem;
    font-weight: 700;
    text-transform: uppercase;
  }

  #aerodrome-map #nzaa-card { left: 53%; top: 25%; }
  #aerodrome-map #nzhn-card { left: 55%; top: 30%; }
  #aerodrome-map #nztg-card { left: 62%; top: 29%; }
  #aerodrome-map #nzro-card { left: 63%; top: 34%; }
  #aerodrome-map #nzoh-card { left: 56%; top: 45%; }
  #aerodrome-map #nzpm-card { left: 54%; top: 47%; }
  #aerodrome-map #nznr-card { left: 61%; top: 41%; }
  #aerodrome-map #nzns-card { left: 37%; top: 51%; }
  #aerodrome-map #nzwb-card { left: 42%; top: 53%; }
  #aerodrome-map #nzwn-card { left: 49%; top: 51%; }
  #aerodrome-map #nzch-card { left: 31%; top: 66%; }
  #aerodrome-map #nzqn-card { left: 15%; top: 76%; }
  #aerodrome-map #nzmf-card { left: 7%; top: 74%; }
  #aerodrome-map #nzdn-card { left: 25%; top: 81%; }
  #aerodrome-map #nznv-card { left: 15%; top: 85%; }

  #aerodrome-map:has(#nzaa-link:hover) #nzaa-card,
  #aerodrome-map:has(#nzaa-link:focus) #nzaa-card,
  #aerodrome-map:has(#nzhn-link:hover) #nzhn-card,
  #aerodrome-map:has(#nzhn-link:focus) #nzhn-card,
  #aerodrome-map:has(#nztg-link:hover) #nztg-card,
  #aerodrome-map:has(#nztg-link:focus) #nztg-card,
  #aerodrome-map:has(#nzro-link:hover) #nzro-card,
  #aerodrome-map:has(#nzro-link:focus) #nzro-card,
  #aerodrome-map:has(#nzoh-link:hover) #nzoh-card,
  #aerodrome-map:has(#nzoh-link:focus) #nzoh-card,
  #aerodrome-map:has(#nzpm-link:hover) #nzpm-card,
  #aerodrome-map:has(#nzpm-link:focus) #nzpm-card,
  #aerodrome-map:has(#nznr-link:hover) #nznr-card,
  #aerodrome-map:has(#nznr-link:focus) #nznr-card,
  #aerodrome-map:has(#nzns-link:hover) #nzns-card,
  #aerodrome-map:has(#nzns-link:focus) #nzns-card,
  #aerodrome-map:has(#nzwb-link:hover) #nzwb-card,
  #aerodrome-map:has(#nzwb-link:focus) #nzwb-card,
  #aerodrome-map:has(#nzwn-link:hover) #nzwn-card,
  #aerodrome-map:has(#nzwn-link:focus) #nzwn-card,
  #aerodrome-map:has(#nzch-link:hover) #nzch-card,
  #aerodrome-map:has(#nzch-link:focus) #nzch-card,
  #aerodrome-map:has(#nzqn-link:hover) #nzqn-card,
  #aerodrome-map:has(#nzqn-link:focus) #nzqn-card,
  #aerodrome-map:has(#nzmf-link:hover) #nzmf-card,
  #aerodrome-map:has(#nzmf-link:focus) #nzmf-card,
  #aerodrome-map:has(#nzdn-link:hover) #nzdn-card,
  #aerodrome-map:has(#nzdn-link:focus) #nzdn-card,
  #aerodrome-map:has(#nznv-link:hover) #nznv-card,
  #aerodrome-map:has(#nznv-link:focus) #nznv-card {
    opacity: 1 !important;
    transform: translateY(0);
  }
</style>

<div id="aerodrome-map" aria-label="Interactive map of New Zealand aerodromes">
  <img src="../assets/interactive-sops-map.png" alt="New Zealand aerodromes and their controlling sectors">

  <svg viewBox="0 0 3563 4500" role="navigation" aria-label="Aerodrome procedure page links">
    <a id="nzaa-link" href="Class-C/nzaa/" aria-label="Open Auckland procedure page"><circle class="aerodrome-marker" cx="2202" cy="1168" r="42" /></a>
    <a id="nzhn-link" href="Class-D/nzhn/" aria-label="Open Hamilton procedure page"><circle class="aerodrome-marker" cx="2332" cy="1392" r="42" /></a>
    <a id="nztg-link" href="Class-D/nztg/" aria-label="Open Tauranga procedure page"><circle class="aerodrome-marker" cx="2516" cy="1364" r="42" /></a>
    <a id="nzro-link" href="Class-D/nzro/" aria-label="Open Rotorua procedure page"><circle class="aerodrome-marker" cx="2636" cy="1556" r="42" /></a>
    <a id="nzoh-link" href="Class-D/nzoh/" aria-label="Open Ohakea procedure page"><circle class="aerodrome-marker" cx="2316" cy="2072" r="42" /></a>
    <a id="nzpm-link" href="Class-D/nzpm/" aria-label="Open Palmerston North procedure page"><circle class="aerodrome-marker" cx="2348" cy="2120" r="42" /></a>
    <a id="nznr-link" href="Procedural/nznr/" aria-label="Open Napier procedure page"><circle class="aerodrome-marker" cx="2652" cy="1896" r="42" /></a>
    <a id="nzns-link" href="Procedural/nzns/" aria-label="Open Nelson procedure page"><circle class="aerodrome-marker" cx="1852" cy="2352" r="42" /></a>
    <a id="nzwb-link" href="Class-D/nzwb/" aria-label="Open Woodbourne procedure page"><circle class="aerodrome-marker" cx="2012" cy="2416" r="42" /></a>
    <a id="nzwn-link" href="Class-C/nzwn/" aria-label="Open Wellington procedure page"><circle class="aerodrome-marker" cx="2176" cy="2364" r="42" /></a>
    <a id="nzch-link" href="Class-C/nzch/" aria-label="Open Christchurch procedure page"><circle class="aerodrome-marker" cx="1696" cy="3020" r="42" /></a>
    <a id="nzqn-link" href="Class-C/nzqn/" aria-label="Open Queenstown procedure page"><circle class="aerodrome-marker" cx="948" cy="3464" r="42" /></a>
    <a id="nzmf-link" href="Flight%20Service/nzmf/" aria-label="Open Milford Sound procedure page"><circle class="aerodrome-marker" cx="792" cy="3384" r="42" /></a>
    <a id="nzdn-link" href="Procedural/nzdn/" aria-label="Open Dunedin procedure page"><circle class="aerodrome-marker" cx="1260" cy="3696" r="42" /></a>
    <a id="nznv-link" href="Procedural/nznv/" aria-label="Open Invercargill procedure page"><circle class="aerodrome-marker" cx="908" cy="3876" r="42" /></a>
  </svg>

  <div id="nzaa-card" class="aerodrome-placard" style="display: none;"><strong>Auckland (NZAA)</strong><span>Class C aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzhn-card" class="aerodrome-placard" style="display: none;"><strong>Hamilton (NZHN)</strong><span>Class D aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nztg-card" class="aerodrome-placard" style="display: none;"><strong>Tauranga (NZTG)</strong><span>Class D aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzro-card" class="aerodrome-placard" style="display: none;"><strong>Rotorua (NZRO)</strong><span>Class D aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzoh-card" class="aerodrome-placard" style="display: none;"><strong>Ohakea (NZOH)</strong><span>Class D aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzpm-card" class="aerodrome-placard" style="display: none;"><strong>Palmerston North (NZPM)</strong><span>Class D aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nznr-card" class="aerodrome-placard" style="display: none;"><strong>Napier (NZNR)</strong><span>Procedural tower aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzns-card" class="aerodrome-placard" style="display: none;"><strong>Nelson (NZNS)</strong><span>Procedural tower aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzwb-card" class="aerodrome-placard" style="display: none;"><strong>Woodbourne (NZWB)</strong><span>Class D aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzwn-card" class="aerodrome-placard" style="display: none;"><strong>Wellington (NZWN)</strong><span>Class C aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzch-card" class="aerodrome-placard" style="display: none;"><strong>Christchurch (NZCH)</strong><span>Class C aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzqn-card" class="aerodrome-placard" style="display: none;"><strong>Queenstown (NZQN)</strong><span>Class C aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzmf-card" class="aerodrome-placard" style="display: none;"><strong>Milford Sound (NZMF)</strong><span>Flight Service aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nzdn-card" class="aerodrome-placard" style="display: none;"><strong>Dunedin (NZDN)</strong><span>Procedural tower aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
  <div id="nznv-card" class="aerodrome-placard" style="display: none;"><strong>Invercargill (NZNV)</strong><span>Procedural tower aerodrome</span><span class="aerodrome-cta">Select for procedure information</span></div>
</div>

## Class C

Class C airspace is applied to CTRs at large international aerodromes, associated CTAs, and en‑route airspace covering principal domestic air routes.

In this airspace IFR and VFR traffic are separated from each other at all times. Within a CTR, IFR aircraft are separated from special VFR (operating below visual meteorological conditions) aircraft, and special VFR aircraft are separated from each other when visibility is less than 5 km.

Where separation is not being provided, air traffic controllers are required to pass appropriate traffic information to VFR aircraft about other VFR aircraft, or special VFR aircraft when visibility is less than 5 km. VFR aircraft, however, must maintain their own separation from each other.

All aircraft require an ATC clearance to be in Class C airspace.

## Class D

Class D airspace normally applies to CTRs and CTAs surrounding regional aerodromes, such as Rotorua and Nelson.

IFR aircraft are separated from other IFR aircraft, but VFR aircraft are not separated from any IFR or other VFR aircraft. Within a CTR only, during special VFR conditions, IFR aircraft are separated from special VFR aircraft, and pecial VFR aircraft are separated from other special VFR aircraft when visibility is less than 5 km.

Pilots of VFR and IFR aircraft operating within Class D airspace must use a good lookout to separate themselves from each other as ATC separation is not provided. 

## Tier 2 (Procedural Tower) Positions 

As per the [VATSIM Global Controller Administration Policy](https://vatsim.net/docs/policy/global-controller-administration-policy), the positions within VATNZ FIRs that are of a procedural nature fall under the Tier 2 Designation. In order to staff these positions, VATNZ controllers must undergo a Procedural Tower endorsement through the training department. More information on this course can be found on the [VATNZ Website](https://www.vatnz.net/training/courses/procedural-tower/)

Our procedural aerodromes are Gisborne (NZGS), Napier (NZNR), New Plymouth (NZNP), Nelson (NZNS), Dunedin (NZDN) and Invercargill (NZNV). These aerodromes are all Class D, therefore Class D airspace rules apply to these aerodromes. 

--8<-- "includes/abbreviations.md"

