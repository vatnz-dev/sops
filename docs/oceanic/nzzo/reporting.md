---
  title: Position Reporting
---

--8<-- "includes/abbreviations.md"

NZZO is procedural airspace. Pilots must provide regular position reports so controllers can maintain an accurate traffic picture in the Controller Client.

## Oceanic Reporting Tool

Before passing an oceanic position report on HF, establish communication with Auckland Radio. The controller or radio operator can then locate your flight details and amend them while you make your report.

!!! example "Initial HF call"
    **ZK-OGO**: *AUCKLAND RADIO AUCKLAND RADIO ZULU KILO OSCAR GOLF OSCAR POSITION REPORT*  
    Use the full callsign until the controller abbreviates it.

    **NZZO_FSS**: *ZULU GOLF OSCAR AUCKLAND RADIO PASS YOUR MESSAGE*  
    Continue with the position report once instructed.

!!! info "Edit fields: generate an oceanic position report"
    <style>
    #ortInput {
      width: 100%;
    }

    #ortInput .fieldInfo {
      display: block;
      margin-top: 0.15rem;
      font-size: 0.8em;
      color: var(--md-default-fg-color--light);
    }

    #ortInput input,
    #ortInput select {
      max-width: 18rem;
      width: 100%;
      font: inherit;
    }

    #ortInput th {
      width: 25%;
      min-width: 9rem;
      text-align: left;
      vertical-align: top;
    }

    #ortInput td {
      vertical-align: top;
    }

    #ortInput .section label {
      font-weight: 700;
    }

    #report {
      font-size: 1.35em;
      line-height: 1.5;
    }

    #report .value {
      font-weight: 700;
    }

    #report .missingValue {
      color: var(--md-code-hl-string-color);
      font-style: italic;
    }
    </style>

    !!! success "Oceanic Position Report"
        <div id="report"></div>

    <table id="ortInput" class="table" cellspacing="2">
  <tbody>
    <tr>
      <th><label for="callsign">Callsign</label></th>
      <td><input id="callsign" type="text" value="New Zealand 83"><span class="fieldInfo">Your callsign.</span></td>
    </tr>
    <tr>
      <th><label for="position">Position</label></th>
      <td><input id="position" type="text" value="ANULI"><span class="fieldInfo">The position you are reporting at.</span></td>
    </tr>
    <tr>
      <th><label for="time">Time at Position</label></th>
      <td><input id="time" type="text" value="1002" inputmode="numeric"><span class="fieldInfo">The UTC time at the reported position, in HHMM format.</span></td>
    </tr>
    <tr>
      <th><label for="flightLevel">Flight Level</label></th>
      <td><input id="flightLevel" type="text" value="350" inputmode="numeric"><span class="fieldInfo">Your current flight level.</span></td>
    </tr>
    <tr>
      <th><label for="next">Next Position</label></th>
      <td><input id="next" type="text" value="VIROG"><span class="fieldInfo">The position you are tracking to next.</span></td>
    </tr>
    <tr>
      <th><label for="nextETA">Next Position ETA</label></th>
      <td><input id="nextETA" type="text" value="1042" inputmode="numeric"><span class="fieldInfo">Your UTC estimate for the next position, in HHMM format.</span></td>
    </tr>
    <tr>
      <th><label for="then">Then</label></th>
      <td><input id="then" type="text" value="IGEVO"><span class="fieldInfo">The position after your next waypoint.</span></td>
    </tr>
    <tr>
      <td colspan="2">
        <div class="section">
          <label for="sectionMach">Assigned Mach speed</label> <input id="sectionMach" type="checkbox">
          <span class="fieldInfo">Only report Mach and groundspeed when ATC has assigned a Mach speed.</span>
        </div>
      </td>
    </tr>
    <tr class="sectionMach" style="display: none;">
      <th><label for="machSpeed">Mach Speed</label></th>
      <td><input id="machSpeed" type="text" value=".84"><span class="fieldInfo">Your assigned Mach speed. M0.80 is read as "decimal eight zero".</span></td>
    </tr>
    <tr class="sectionMach" style="display: none;">
      <th><label for="groundSpeed">Groundspeed</label></th>
      <td><input id="groundSpeed" type="text" value="510" inputmode="numeric"><span class="fieldInfo">Your current groundspeed.</span></td>
    </tr>
    <tr>
      <td colspan="2">
        <div class="section">
          <label for="sectionWx">Weather-reporting waypoint</label> <input id="sectionWx" type="checkbox">
          <span class="fieldInfo">If you are unsure, leave this unticked unless ATC requests weather information.</span>
        </div>
      </td>
    </tr>
    <tr class="sectionWx" style="display: none;">
      <th><label for="temperature">Temperature</label></th>
      <td><input id="temperature" type="text" value="-25" inputmode="numeric"><span class="fieldInfo">The outside air temperature at your current position.</span></td>
    </tr>
    <tr class="sectionWx" style="display: none;">
      <th><label for="windDirection">Wind Direction</label></th>
      <td><input id="windDirection" type="text" value="160" inputmode="numeric"><span class="fieldInfo">The wind direction at your current flight level.</span></td>
    </tr>
    <tr class="sectionWx" style="display: none;">
      <th><label for="windSpeed">Wind Speed</label></th>
      <td><input id="windSpeed" type="text" value="15" inputmode="numeric"><span class="fieldInfo">The wind speed at your current flight level.</span></td>
    </tr>
    <tr class="sectionWx" style="display: none;">
      <th><label for="turbulence">Turbulence</label></th>
      <td>
        <select id="turbulence">
          <option value="none">None</option>
          <option value="light">Light</option>
          <option value="moderate">Moderate</option>
          <option value="severe">Severe</option>
        </select>
        <span class="fieldInfo">The level of turbulence encountered at your current flight level.</span>
      </td>
    </tr>
    <tr class="sectionWx" style="display: none;">
      <th><label for="icing">Icing</label></th>
      <td>
        <select id="icing">
          <option value="none">None</option>
          <option value="light">Light</option>
          <option value="moderate">Moderate</option>
          <option value="severe">Severe</option>
        </select>
        <span class="fieldInfo">The level of icing encountered at your current flight level.</span>
      </td>
    </tr>
    <tr class="sectionWx" style="display: none;">
      <th><label for="thunderstorms">Thunderstorms</label></th>
      <td>
        <select id="thunderstorms">
          <option value="none">None</option>
          <option value="active">Yes</option>
          <option value="active with hail">With hail</option>
        </select>
        <span class="fieldInfo">Thunderstorm activity encountered at your current position or flight level.</span>
      </td>
    </tr>
    <tr>
      <td colspan="2">
        <div class="section">
          <label for="simrate">Sim rate</label>
          <span class="fieldInfo">2x and 4x sim rates are available at specific altitudes in oceanic airspace, subject to ATC approval. Requests are usually declined during events.</span>
        </div>
      </td>
    </tr>
    <tr>
      <th><label for="simrate">Current Sim Rate</label></th>
      <td>
        <select id="simrate">
          <option value="1x">1x</option>
          <option value="2x">2x</option>
          <option value="4x">4x</option>
        </select>
        <span class="fieldInfo">The sim rate you are currently running.</span>
      </td>
    </tr>
  </tbody>
</table>

<script type="text/javascript">
function getValue(id, fallback) {
  const value = document.getElementById(id).value.trim();
  return value.length > 0 ? value : `(${fallback})`;
}

function valueSpan(text) {
  const span = document.createElement('span');
  span.className = text.startsWith('(') && text.endsWith(')') ? 'missingValue' : 'value';
  span.textContent = text;
  return span;
}

function appendText(parent, text) {
  parent.appendChild(document.createTextNode(text));
}

function appendValue(parent, id, fallback) {
  parent.appendChild(valueSpan(getValue(id, fallback)));
}

function selectedValue(id) {
  return document.getElementById(id).value;
}

function toggleRows(sectionClass, show) {
  document.querySelectorAll(`.${sectionClass}`).forEach(function(row) {
    row.style.display = show ? 'table-row' : 'none';
  });
}

function updateReport() {
  const hasMach = document.getElementById('sectionMach').checked;
  const hasWeather = document.getElementById('sectionWx').checked;
  const report = document.getElementById('report');

  toggleRows('sectionMach', hasMach);
  toggleRows('sectionWx', hasWeather);

  report.replaceChildren();

  appendValue(report, 'callsign', 'Callsign');
  appendText(report, ' is position ');
  appendValue(report, 'position', 'Position');
  appendText(report, ' at time ');
  appendValue(report, 'time', 'Time');
  appendText(report, ', flight level ');
  appendValue(report, 'flightLevel', 'Flight Level');
  appendText(report, ', estimating ');
  appendValue(report, 'next', 'Next Position');
  appendText(report, ' at ');
  appendValue(report, 'nextETA', 'Next Position ETA');
  appendText(report, ', ');
  appendValue(report, 'then', 'Then');
  appendText(report, ' next');

  if (hasMach) {
    appendText(report, '. Mach ');
    appendValue(report, 'machSpeed', 'Mach Speed');
    appendText(report, ', groundspeed ');
    appendValue(report, 'groundSpeed', 'Groundspeed');
  }

  if (hasWeather) {
    appendText(report, '. Temperature ');
    appendValue(report, 'temperature', 'Temperature');
    appendText(report, ', wind ');

    if (selectedValue('windSpeed') !== '0') {
      appendValue(report, 'windDirection', 'Wind Direction');
      appendText(report, ' degrees ');
      appendValue(report, 'windSpeed', 'Wind Speed');
      appendText(report, ' knots');
    } else {
      appendText(report, 'calm');
    }

    if (selectedValue('turbulence') !== 'none') {
      appendText(report, ', turbulence ');
      report.appendChild(valueSpan(selectedValue('turbulence')));
    }

    if (selectedValue('icing') !== 'none') {
      appendText(report, ', icing ');
      report.appendChild(valueSpan(selectedValue('icing')));
    }

    if (selectedValue('thunderstorms') !== 'none') {
      appendText(report, ', thunderstorms ');
      report.appendChild(valueSpan(selectedValue('thunderstorms')));
    }
  }

  if (selectedValue('simrate') !== '1x') {
    appendText(report, '. Sim rate ');
    appendValue(report, 'simrate', 'Sim Rate');
  }
}

document.querySelectorAll('#ortInput input, #ortInput select').forEach(function(field) {
  field.addEventListener('input', updateReport);
  field.addEventListener('change', updateReport);
});

updateReport();
</script>
