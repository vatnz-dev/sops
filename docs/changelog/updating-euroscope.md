---
  title: Updating your EuroScope Client
---

--8<-- "includes/abbreviations.md"

AIRAC Cycle updates must be made manually for the EuroScope client. We highly suggest Controllers use vatSys, as it is easier to manage, in addition to being more representative of the real-world Air Traffic Management system used in New Zealand.

## Files

VATNZ has two packages available:
  - **SkyLine**: Contains all of the required position and frequency definitions alongside the Sector Files. 
  - **Sector Files**: Only contains the Sector Files.

For most cycles, Controllers will only need to replace the Sector Files. Controllers will be explicitly instructed in the Changelogs should they need to replace the entire SkyLine package.

## Sector Files

1. [Download the latest Sector Files from the VATNZ website](https://www.vatnz.net/airspace/sector_files/){ target=blank }. This will download a file named "VATNZ-NZZC_xxyy", where `xx` is the year, and `yy` is the cycle.
2. In Windows, open an explorer window for where your EuroScope files are stored. By default this is in the `Documents\EuroScope\` directory.
3. Archive the current VATNZ NZZC files, and drag the new files into this directory.
4. Open EuroScope. A dialogue will appear notifying you that the active sector file cannot be found. **Click No**.
5. A file selection dialogue will appear. Select the new `.sct2` file, and click 'Open'.
6. Another dialogue box will appear, notifying you that the file has been loaded. **Click Yes** to make this the new active sector file.
7. When EuroScope loads, ensure that no error messages appear in the System box.

## SkyLine Package

!!! important "Backing up your Settings"
    Files in the `/Settings/` folder may be overwritten by the new SkyLine package, losing all of your display and list settings. Before updating, we recommend you back-up your `List.txt` and `Screen.txt` files, and reimporting them after you replace the rest of the package.

    It is important that you back-up only those two files, as other files in the `/Settings/` folder would have changed.

1. [Download the latest SkyLine Package from the VATNZ website](https://www.vatnz.net/airspace/sector_files/){ target=blank }. This will download a file named "VATNZ-SKYLINE_xxyy", where `xx` is the year, and `yy` is the cycle.
2. In Windows, open an explorer window for where your EuroScope files are stored. By default this is in the `Documents\EuroScope\` directory.
3. Archive your current VATNZ SkyLine files, and drag the new files into the directory - making sure to follow the note above about preserving your settings.
4. Open EuroScope. A dialogue will appear notifying you that the active sector file cannot be found. **Click No**.
5. A file selection dialogue will appear. Select the new `.sct2` file, and click 'Open'.
6. Another dialogue box will appear, notifying you that the file has been loaded. **Click Yes** to make this the new active sector file.
7. When EuroScope loads, ensure that no error messages appear in the System box.