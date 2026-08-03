---
  title: Tonga and Niue
---

--8<-- "includes/abbreviations.md"

!!! info "This is a work in progress!"
    This page is currently being worked on by the team. It'll be here soon! If you want to help out, [have a look how you can help](../contribute/index.md)! For the meantime, you should apply the comments made here in line with the skills taught in the VATNZ Controller Training Syllabus.



| Position Name      | Shortcode | Callsign              | Frequency | Login ID | Usage     |
| ------------------ | --------- | --------------------- | --------- | -------- | --------- |
| Fua'Amotu TMA      | TTF       | Fua'Amotu Tower       | 118.500   | NFTF_APP |           |
| Fua'Amotu SMC      | GTF       | Fua'Amotu Ground      | 121.900   | NFTF_GND | Secondary |
| Vava'u FIS         | VFS       | Vava'u Flight Service | 118.100   | NFTV_TWR |           |
| Vava'u SMC         | GTV       | Vava'u Ground         | 121.900   | NFTV_GND | Secondary |
| Niue FIS           | NFS       | Niue Flight Service   | 118.100   | NIUE_TWR |           |


## TMA

* **NFTF_APP** "Fua'Amotu Tower" on 118.500
    * **Limits**: There are three layers to NFTF_APP's area of responsibility:
        * A circle 23nm in diameter, centered on TBU VOR from SFC to 3,500ft.
        * A circle 75nm in diameter, centered on TBU VOR from 3,500ft to 9,500ft.
        * A circle 100nm in diameter, centered on TBH VOR from 9,500ft to 19,500ft.
    * Fua'Amotu would hand aircraft off to NZZO_FSS upon crossing the boundary.

!!! info "Why is their callsign Tower, not Approach?"
    We've had to implement this position with a `_APP` suffix, as the FSD restricts `_TWR` callsigns to a visibility range of 50nm. 

## Towers

None! NFTF_TWR is covered by NFTF_APP.

## AFIS

* **NFTV_TWR**: "Vava'u Flight Service" on 118.100

Vava'u has a Flight Information Service and weirdly has a Ground service on 121.900. The FIS provides only traffic information. This will be modelled as **NFTV_TWR**, with a standard Tower visibility range of 50nm. The Tower is to provide a traffic information service, in addition to relaying IFR clearances from NZZO_FSS.

Clearances remain **invalid** until Auckland Radio advises that they are released.

Refer to the **AFIS** [guide](../../controller-skills/flight-service.md#standard-phraseology).

## Niue

Niue only has a Flight Information Service, providing only traffic information. This will be modelled as **NIUE_TWR**, with a standard Tower visibility range of 50nm. The Tower is to provide a traffic information service, in addition to relaying IFR clearances from NZZO_FSS.

Refer to the **AFIS** [guide](../../controller-skills/flight-service.md#standard-phraseology).

**Departing** 

Departing aircraft should make contact with NZZO_FSS upon passing 20DME from `NU`. If unable to gain contact, they are to remain with NIUE_TWR until they have positive contact.
 
**Arriving** 

Arriving aircraft will be given clearance to leave Controlled Airspace on descent through FL245, however should maintain a listening watch on NZZO_FSS. Aircraft should attempt to make contact with NIUE_TWR around 40 DME, and shall report that positive contact to NZZO_FSS before dropping that frequency. NIUE_TWR will report your landing back to NZZO_FSS in order to close your flightplan.


