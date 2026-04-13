# Changelog Entry Template

Use this file as a starting point for creating consistent AIRAC changelog entries in `docs/changelog/YYYY/XXXX.md`.

## Required structure

```md
---
  title: Cycle XXXX (DD MMM)
---

--8<-- "includes/abbreviations.md"

## Data Changes

- Summary of dataset changes.

## Aerodrome

### NZXX: Location

#### RWY NN

- The following STARs/SIDs/RNP procedures have been added/amended/disestablished: `NAME`
    - Short note describing the change.

## Standard Routes

- Summary of standard route additions/amendments/removals.

## Other Dataset Changes

- Summary of other dataset-level changes.
```

## Writing tips

- Use consistent heading levels and keep the format aligned with existing `2025/` and `2026/` entries.
- Group changes by aerodrome and runway when applicable.
- Use bullet lists for each procedure or route update.
- Keep notes short and procedural.
- Order of procedures should be SIDs, STARs, and then RNP. Additions should be first, alterations second, disestablished last.
- For RNP procedures, use the base name only (e.g. `RNP 30`) unless the procedure's *Type* column in the source explicitly includes `(AR)`. 
    - If the Type column contains `(AR)`, append ` (AR)` to the name (e.g. `RNP 30 (AR)`).
    - In practice: check the source Type field when drafting entries and only include `(AR)` when that field lists it.
- All SIDs, STARs, or RNP approaches should be listed on the same line. When multiple procedures share the same reason, consolidate them under one bullet point with the common reason below (e.g., "The following SIDs have been amended: `NAME1`, `NAME2`. - Procedure reviewed."). For procedure-specific reasons, list them separately or append to the names (e.g., "`NAME1`, `NAME2`: minor track changes."). If no reason is given, no short note should be added.

## Example section labels

- `Data Changes`
- `Aerodrome`
- `Standard Routes`
- `Other Dataset Changes`

## Common language patterns

- "The following STAR has been added: `NAME`"
- "The following SID has been amended and resequenced: `NAME`"
- "Procedure reviewed; minor track change."
- "Procedure disestablished back in AIRAC 2XXX."

## How to use

Copy the skeleton above into a new file under `docs/changelog/YYYY/XXXX.md`, then replace placeholders with the specific AIRAC changes.
