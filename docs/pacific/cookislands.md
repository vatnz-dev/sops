---
  title: Cook Islands
---

--8<-- "includes/abbreviations.md"

| Name               | Callsign                  | Frequency | Login    | Notes                       |
| ------------------ | ------------------------- | --------- | -------- | --------------------------- |
| Rarotonga Control  | Rarotonga (Raro) Control  | 118.900   | NCRG_CTR |                             |
| Rarotonga Approach | Rarotonga (Raro) Tower    | 118.100   | NCRG_APP |                             |
| Rarotonga Delivery | Rarotonga (Raro) Delivery | 121.900   | NCRG_DEL | For use during Events only. |

<figure markdown> 
  ![Rarotonga Enroute](../oceanic/assets/raro-control.png){ width="700" }
  <figcaption>Right Click and open in a new tab to see full detail.</figcaption>
</figure>

## Enroute

* **NCRG_CTR** "Rarotonga Control" on 118.900
    * **Limits**: 5,500ft to FL245, with the lateral bounds indicated as above. Roughly 340nm by 260nm.
    * Provides an Enroute radar service within its' lateral bounds.
    * Additionally acts as the Enroute interface between NCRG_APP and either NTTT or NZZO FSS.
    * Provides a top-down service to NCRG when NCRG_APP is offline.

## TMA

* **NCRG_APP** "Rarotonga Tower" on 118.100
    * **Limits**: There are three layers to NCRG_APP's area of responsibility:
        * A circle of 30nm diameter centered on RG VOR from SFC to 5,500ft.
        * A circle of 50nm diameter centered on RG VOR from 5,500ft to 9,500ft.
        * A circle of 70nm diameter centered on RG VOR from 9,500ft to 14,500ft.
    *  Provides a combined Approach/Tower service for NCRG.

!!! info "Wait, another Approach station with a Tower callsign?"
    Similar to `NFTF_APP` above, we've had to implement this position with a `_APP` suffix, as the FSD restricts `_TWR` callsigns to a visibility range of 50nm. 
