---
  title: Extended Services
---

--8<-- "includes/abbreviations.md"

New Zealand airspace is unique in that we have seven sectors in fairly close proximity to each other, covering a relatively small area. In normal operation, some sectors will automatically inherit neighbouring sectors, but Enroute Controllers also have the ability to extend to the entirety of the country, providing an extended service.

##  Workload

When providing an extended service, it's important to realise that traffic levels can build quickly, and New Zealand's unique level of GA aircraft in such a small area can cause increased difficulty. Therefore, if you notice your quality of service degrading, you should cease extending to other sectors so that you can provide a quality service. Quality, not quantity is paramount.

!!! warning "Controllers shall not change Airspace Classes"
    Controllers are not authorised to change the classes of airspaces under their control in order to alleviate traffic concerns.

    **Example** - If you are providing an Extended Enroute service with multiple aircraft in the circuit pattern at Woodbourne, you are obligated to provide a service to them under the VATSIM top-down controlling methodology. A Controller shall not revert that airspace to Class G in order to redirect their attention to other aircraft. In this case, you would amend the extend of your extended sectors.

!!! warning "Controllers shall not extend into an Event Only position"
    When providing an extended service, Controllers shall not extend into an Event Only position. This inlcludes the use of either their callsign or frequency.

    **Example** - If NAK elects to extend their services to include OCR, they are not permitted to use the RAN callsign or frequency unless approved by the Operations or Events Director. It is important to note that in this case, OCR automatically inherits the airspace normally delegated to RAN, instead of inheriting the RAN position. [See the OCR page for more information](OCR.md#airspace).

## Frequencies and Callsigns

As Controllers are providing a lateral extension of coverage, Controllers shall only use the Enroute Sector callsign in any RTF transmissions. Whilst an aircraft might physically be in aircraft normally delegated to Wellington Approach, for example, the control service is still being provided by Christchurch Control. 

### Frequency Management

When providing extended services, Controllers must cross-couple all primary frequencies of the sectors they are extended into. 

While most frequencies are still able to be heard at high-levels, when an aircraft crossed a sector boundary, the Controller shall also transfer the aircraft to that frequency. 

It is also a good idea to annotate the current frequency in the aircraft's data block using its' three letter designator - `NAK` or `OCR` for example.

## Technical Limitations

At the moment, most Controller Clients only allow a Controller to have one sector as their primary. This means that if you provide an extended service, only your primary sector will show as online to Pilots through their pilot clients, and other mapping services such as vPilot or Volanta.

To alleviate this, a Controller providing an extended service shall make this known through their Controller Info text when logging on. This text shall include the active sectors being extended to, as well as any applicable frequencies. In doing this, the Controller shall ensure that a link to the relevant charts and feedback link is still provided.

??? example "Examples of Controller Info for Extended Services"

    === "NAK extending to all of NZ"

        ```
          Christchurch Control - Extending to OCR 123.9, BAY 119.5, OHA 126.2, KAI 129.4, STH 129.3.
          Need local charts? - vats.im/nz/charts  
          Provide Feedback - vats.im/nz/atc-fb
        ```

    === "KAI extending to OHA and STH"

        ```
          Christchurch Control - Extending to OHA and STH
          CH 129.4 // OH/PM 126.2 // QN 129.3
          Need local charts? - vats.im/nz/charts
          Provide Feedback - vats.im/nz/atc-fb
        ```

    === "BAY extending to OHA"

      ```
        Bay Approach - Extending to OHA
        HN, TG, GS - 119.5  /  OH, PM, NR - 126.2
        Need local charts? - vats.im/nz/charts
        Provide Feedback - vats.im/nz/atc-fb
      ```

## Setting up vatSys

To provide an extended service in vatSys, you will need to assume control of the relevant sectors, prime their frequency, and ensure your visibility range is set correctly.

??? info "How to set up vatSys for Extended Services"

    === "Sectors"

        1. Connect as your host sector, ensuring that you amend your Controller Info text to include your extension. Ensure your range is set to 600.
        2. Once connected, navigate to `Settings > Sectors...`. This wil bring up the Sector Configuration Window.
        3. In the right-hand column, click on the sector that you want to assume, and then click the transfer arrows in the centre of the window. The sector will now appear under 'Controlled Sectors'.

    === "Frequencies"

        When connected, your VSCS panel will show all other Enroute Sectors by default. 
        
        To enable them, select the frequency as normal, and click on transmit. Do this for all sectors that you are extending into. 

        vatSys automatically cross-couples any frequencies that you have selected as transmit.

    === "Visibility"

        Ensure that your Visibility Centers cover all of your airspace effectively. If they do not, you can amend them by navigating to `Settings > Visibility Centers > Manual`. 