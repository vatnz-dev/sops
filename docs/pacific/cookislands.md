---
  title: Cook Islands
---

--8<-- "includes/abbreviations.md"    

| Position Name      | Shortcode | Callsign                  | Frequency | Login ID | Usage      |
| ------------------ | --------- | ------------------------- | --------- | -------- | ---------- |
| Auckland Radio     | ARO       | Auckland Radio            | 129.000   | NZZO_FSS |            |
| Rarotonga Control  | RAR       | Rarotonga (Raro) Control  | 118.900   | NCRG_CTR |            |
| Rarotonga Tower    | TRA       | Rarotonga (Raro) Tower    | 118.100   | NCRG_APP |            |
| Rarotonga Delivery | DRA       | Rarotonga (Raro) Delivery | 121.900   | NCRG_DEL | Event only |

<figure markdown> 
  ![Rarotonga Enroute](../pacific/assets/raro-control.png)

## Enroute

* **NCRG_CTR** "Rarotonga Control" on 118.900
    * **Limits**: 5,500ft to FL245, with the lateral bounds indicated as above. Roughly 340nm by 260nm.
    * Provides an Enroute radar service within its' lateral bounds.
    * Additionally acts as the Enroute interface between NCRG_APP and NZZO FSS.
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
