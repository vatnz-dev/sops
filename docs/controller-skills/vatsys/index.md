---
title: Strip Layouts
---

--8<-- "includes/abbreviations.md"

!!! note "Clickable Strip"
    - Clickable overview of the Strip found in vatSys.
    - Move the mouse over the panels to get the specific content shown.
    
    Idea stolen from [FlyByWire's 'Clickable Cockpit'](https://docs.flybywiresim.com/pilots-corner/a32nx-briefing/flight-deck/)

<style>
.imagemap {
    position: relative;
    display: inline-block;
    background-color: rgba(3,105,161,0.2);
    border: 1px solid #155e75;
}
.imagemap .imagemapname {
  visibility: hidden;

  background-color: rgba(29, 30, 38,.8);
  color: rgba(212, 212, 213, 1);
  text-align: center;
  padding: 5px 0;
  border-radius: 6px;

  /* Position the tooltip text - see examples below! */
  position: absolute;
  z-index: 1;
  width: 120px;
  top: 0%;
  left: 50%;
  margin-left: -60px; /* Use half of the width (120/2 = 60), to center the tooltip */
}
.imagemap:hover .imagemapname {
    visibility: visible;
}
.imagemap:hover {
    background-color: rgba(3,105,161,0.6);
    border: 1px solid black;
}
</style>

<div style="position: relative;">

  <img src="assets/stripExtend.png" style="width: 100%; height: auto;">

  <a href=""><div class="imagemap" style="position: absolute; left: 0.3%; top: 4%; width: 6.55%; height: 42%;"><span class="imagemapname">Aircraft Direction Indicator</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 0.3%; top: 48%; width: 6.55%; height: 20%;"><span class="imagemapname">Controlling Sector</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 0.3%; top: 70%; width: 6.55%; height: 24.5%;"><span class="imagemapname">FDR State</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 7.25%; top: 4%; width: 8.5%; height: 24.5%;"><span class="imagemapname">Callsign</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 17.8%; top: 4%; width: 1.8%; height: 24.5%;"><span class="imagemapname">CPDLC Status</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 19.5%; top: 4%; width: 1.8%; height: 24.5%;"><span class="imagemapname">VFR Indicator</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 7.25%; top: 28%; width: 6%; height: 18%;"><span class="imagemapname">Assigned SSR Code</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 15.3%; top: 28%; width: 6%; height: 18%;"><span class="imagemapname">Aircraft Type</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 7.25%; top: 49%; width: 6%; height: 18%;"><span class="imagemapname">CTOT</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 15.3%; top: 49%; width: 6%; height: 18%;"><span class="imagemapname">Destination</span></div></a>

  <a href=""><div class="imagemap" style="position: absolute; left: 7.25%; top: 70%; width: 14%; height: 24.5%;"><span class="imagemapname">Filtered FDR Remarks</span></div></a>


</div>