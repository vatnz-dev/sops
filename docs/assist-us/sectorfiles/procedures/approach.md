---
title: Approaches
---

--8<-- "includes/abbreviations.md"

The Sector File Generator can currently handle RNP, RNP-AR, LOC and VOR approaches; although we don't model LOC or VOR approaches in our dataset.

These approaches are largely only useful for vatSys, and are used in Euroscope for information only. In vatSys, this data will automatically link with a STAR with a common IAF upon STAR assignment, allowing for route prediction far in advance.

These approaches are also given their own map layers - 

* `Maps/RNP` shows all RNP approaches in the country
* `Maps/RNP-AR` shows all RNP-AR approaches in the country
* `Maps/ICAO/XX RNP` shows all RNP approaches for that runway 
* `Maps/ICAO/XX RNP-AR` shows all RNP-AR approaches for that runway 
  * For the ICAO-specific maps, there is also an associated labels file that annotates some of the key waypoints.

As with the STAR section, the principles of procedure editing laid out in the [SID Section](departures.md) are also applicable here -

* Fixes should be entered in the order in which they are flown.
* For procedures with transitions, the base procedure should be added first, with the transitions added after.
* The delete buttons behave in the same way.
* The general screen layout is the same.


## Editor

### Adding a New Procedure

<figure markdown> 
  ![SID Screen](../assets/NewApproach.png){ width="100%" }
</figure>

Adding a new procedure is relatively simple. `RNP` should be chosen for normal GNSS based approaches, whereas `RNP-AR` should be chosen for high-accuracy procedures. This will be stipulated on the chart. An Alpha designator can be added if required.

<figure markdown> 
  ![SID Screen](../assets/PopulatedApproach.png){ width="100%" }
</figure>

The above image shows the RNP S RWY 23L (AR) approach into Auckland. As you can see, we have new markings next to some of the waypoints.

* The **Black Triangle** denotes the approach's Initial Fix (IF).
* The **Maltese Cross** denotes the approach's Final Approach Fix (FAF).
* The **Hollow Triangle** denotes the approach's or transition's Initial Approach Fix (IAF).

These can be designated by highlighting the fix, and clicking the respective button. This does a couple of things -

* Tells the SFG to create a text label for that waypoint in the various map layers.
    * All points designated as an IF, IAF or FAF will have a label generated.
* Will assist the SFG in automatically linking STARs and Approaches together in the export. 

!!! important
    You can have multiple waypoints designated as an IAF. For example, on most GNSS-based RNP approaches, the initial straight-in leg will typically be an IAF, in addition to 90 degree offset IAFs.

    For a RNP-AR approach, usually there is only one per transition.

### Modifying a Procedure

Procedures can be modified by finding the procedure in the main window, and then modifying the respective data. The data will save if you attempt to navigate away from the procedure by either closing the window or select another procedure.