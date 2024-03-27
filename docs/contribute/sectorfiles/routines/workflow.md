---
title: AIRAC Workflow
---

--8<-- "includes/abbreviations.md"

``` mermaid
flowchart TB

id1([Receive Data from Aeropath]) -->
  id2[Ensure that all files are present - ANR, AIP Vol 2 & 3 and Supp/Bull] -->
  id3[Download files, and store in Google Drive] -->
  id4[Read]

  id3 -->|Request further Data if needed.|id1


``` 

``` mermaid
flowchart TB

subgraph Preperation
  prep1([Previous Cycle Releases]) -->
    prep2[[In the 'Controller Client Data' project planner, create 
    a new tracking issue for the next cycle using the template]] -->
    prep3[[Create new GitHub branches for NZZC, 
    AIS Database and EuroScope repositories]] -->
    prep4([Wait for Data to be sent])
end

prep4 --> rv1

subgraph Data review

  rv1([Receive Data from Aeropath]) -->
  rv2[Ensure that all files are present - ANR, AIP Vol 2 & 3 and Supp/Bull] -->
  rv3[Download Files and store in Google Drive] -->
  rv4[Review the AIP Bulletin Document, and create sub-tasks for
  each change in the 'Next NZZC Release Cycle column in the 
  project board] -->
  rv5[Review all changes in the AIP Vol 2 & 3, and add additional 
  information to the sub-task in the project board] -->
  rv7[Confirm if any SOP changes are necessary, and if so, create
    a 'Release Notes and Amendments: Cycle 2xxx' sub-task in 
    the project board, linking to an issue in the SOPs repo] 

  rv5 .-> rv6[If there are positions, frequencies or other non-ANR
    data that needs to change, discuss with Operations Dir
    and Team]

  rv6 .-> rv7
 

end

rv7 --> anr1

subgraph ANR Updating

  anr1[Ensure you are working on the 'airac-xxxx' branch
  of the ais-data-manager repository.] -->
  anr2[Perform a Manual Update of the Database using 
  the latest ANR data] -->
  anr3[Export the latest changes, and update the
    ais-data-management repo]

end

anr3 --> aip1

subgraph AIP Changes

  aip1

end



```