---
  title: Tonga and Niue
---

--8<-- "includes/abbreviations.md"

| Position Name      | Shortcode | Callsign              | Frequency | Login ID | Usage     |
| ------------------ | --------- | --------------------- | --------- | -------- | --------- |
| Auckland Radio     | ARO       | Auckland Radio        | 129.000   | NZZO_FSS |           | 
| Fua'Amotu TWR      | TTF       | Fua'Amotu Tower       | 118.500   | NFTF_APP |           |
| Fua'Amotu SMC      | GTF       | Fua'Amotu Ground      | 121.900   | NFTF_GND | Secondary |
| Vava'u FIS         | VFS       | Vava'u Flight Service | 118.100   | NFTV_TWR |           |
| Vava'u SMC         | GTV       | Vava'u Ground         | 121.900   | NFTV_GND | Secondary |
| Niue FIS           | NFS       | Niue Flight Service   | 118.100   | NIUE_TWR |           |


## Tower

!!! info "Why is their callsign Tower, not Approach?"
    We've had to implement this position with a `_APP` suffix, as the FSD restricts `_TWR` callsigns to a visibility range of 50nm. 

**NFTF_APP** "Fua'Amotu Tower" on 118.500

### Airspace

**Limits**: There are three layers to NFTF_APP's area of responsibility:

- A circle 23nm in diameter, centered on TBU VOR from SFC to 3,500ft.

- A circle 75nm in diameter, centered on TBU VOR from 3,500ft to 9,500ft.

- A circle 100nm in diameter, centered on TBH VOR from 9,500ft to 19,500ft.

Fua'Amotu TWR shall instruct aircraft to contact ARO passing `FL240`. Ie. "Passing `FL240` contact Auckland Radio 129.0"


## AFIS NFTV/NIUE

Vava'u and Niue have a Flight Information Service, while only Vava'u weirdly has a Ground service on 121.900. The FIS provides only traffic information. This will be modelled as **NFTV_TWR** or **NIUE_TWR**, with a standard Tower visibility range of 50nm. The Tower is to provide a traffic information service, in addition to relaying IFR clearances from NZZO_FSS.

Clearances remain **invalid** until Auckland Radio advises that they are released.

Refer to the **AFIS** [guide](../../controller-skills/flight-service.md#standard-phraseology).


### Departures

#### NIUE 

NFS shall instruct aircraft that are climbing above `FL245` to contact ARO passing `FL240`, prior to aircraft vacating the MBZ. Otherwise aircraft should change to Advisory on `122.8`. 

#### NFTV  


### Arrivals

Arriving aircraft will be given clearance to leave Controlled Airspace on descent through FL245. Aircraft should attempt to make contact with NIUE_TWR around 40 DME. If aircraft are unable to make contact with NIUE_TWR, they should call NZZO_FSS, who should call Nuie on the landline to attempt to make contact. NIUE_TWR will report your landing back to NZZO_FSS in order to close your flightplan.
