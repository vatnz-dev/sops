---
  title: Tonga and Niue
---

--8<-- "includes/abbreviations.md"



| Name               | Callsign                  | Frequency | Login    | Notes                       |
| ------------------ | ------------------------- | --------- | -------- | --------------------------- |
| Rarotonga Control  | Rarotonga (Raro) Control  | 118.900   | NCRG_CTR |                             |
| Rarotonga Approach | Rarotonga (Raro) Tower    | 118.100   | NCRG_APP |                             |
| Rarotonga Delivery | Rarotonga (Raro) Delivery | 121.900   | NCRG_DEL | For use during Events only. |

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

* **NFTL_FIS**: "Lifuka Radio" on 118.100.
* **NFTV_FIS**: "Vava'u Flight Service" on 118.100
    * This aerodrome weirdly has a Ground service on 121.900, but only an AFIS over top.

!!! warning
    These are not yet modelled on the network.

## Niue

Niue only has a Flight Information Service, providing only traffic information. This will be modelled as **NIUE_TWR**, with a standard Tower visibility range of 50nm. The Tower is to provide a traffic information service, in addition to relaying IFR clearances from NZZO_FSS.

**Departing** 

Departing aircraft should make contact with NZZO_FSS upon passing 20DME from `NU`. If unable to gain contact, they are to remain with NIUE_TWR until they have positive contact.
 
**Arriving** 

Arriving aircraft will be given clearance to leave Controlled Airspace on descent through FL245, however should maintain a listening watch on NZZO_FSS. Aircraft should attempt to make contact with NIUE_TWR around 40 DME, and shall report that positive contact to NZZO_FSS before dropping that frequency. NIUE_TWR will report your landing back to NZZO_FSS in order to close your flightplan.


