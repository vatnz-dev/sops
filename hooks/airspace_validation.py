import re
import logging
import csv

log = logging.getLogger("airspace_validation")

errors = []

config_state = {
    'doValidation': True,
    'errorOnValidationFail': True
}

class Cache:
    waypoints = set()
    sidstars = set()

def on_config(config):
    config_state['errorOnValidationFail'] = config.get('extra', {}).get('error_on_validation_fail', True)

    try:
        with open('build/ap_aids.txt', newline='') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                if row[4] in ('IFR_FIX', 'VOR', 'NDB'):
                    Cache.waypoints.add(row[1])

        with open('build/procedures.txt', newline='') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                if row[4] in ('STAR', 'SID'):
                    Cache.sidstars.add(f"{row[3]} {row[7]}".strip())
    except FileNotFoundError:
        print("Data not found - skipping validation")
        config_state['doValidation'] = False


def on_page_markdown(markdown, page, **kwargs):
    if config_state['doValidation'] == False:
        return
    
    if page.file.src_path.startswith("contribute/") or page.file.src_path.startswith("changelog"):
        return

    sidstarpattern = r"[A-Z]{5}\s#[A-Z]"
    waypointpattern = r"`([A-Z]{5})`"

    matches = re.findall(sidstarpattern, markdown)

    for match in matches:
        sidstarwaypoint = match[:5]
        sidstaralpha = match[-1]
        if not f"{sidstarwaypoint} {sidstaralpha}" in Cache.sidstars:
            errors.append(f"{page.file.src_path}: SID/STAR {match} found but not valid")

    matches = re.findall(waypointpattern, markdown)

    for match in matches:
        if not match in Cache.waypoints:
            errors.append(f"{page.file.src_path}: Waypoint {match} found but not valid")

def on_post_build(config):
    if errors:
        log.warning("Validation issues found:")
        for e in errors:
            log.warning(f" - {e}")

        if config_state['errorOnValidationFail']:
            raise SystemExit("Validation errors occurred - not continuing")
