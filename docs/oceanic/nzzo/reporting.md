---
  title: Position Reporting
---

--8<-- "includes/abbreviations.md"


As NZZO is procedural airspace, pilots are required to provide regular position reports to ATC, which can then be entered into the Controller Client software.

## Oceanic Reporting Tool

Before passing oceanic position reports on HF, please first establish communication. The controller/radio operator can then find your details and amend them as you make your report.

!!! example
    **ZK-OGO**: *AUCKLAND RADIO AUCKLAND RADIO ZULU KILO OSCAR GOLF OSCAR* (note the full call sign is used until the controller abbreviates it) *POSITION REPORT*

    **NZZO_FSS**: *ZULU GOLF OSCAR AUCKLAND RADIO PASS YOUR MESSAGE* (note how the call sign is abbreviated)

    then continue as below. 
  
Edit the data in the fields below to produce your position report.

<style>
#ortInput .fieldInfo {
  font-size: 0.8em;
  color: #777676;
}

#ortInput input {
  border-bottom: 1px solid black;
  font-size: 1em;
}

#ortInput th {
  width: 25%;
  text-align: left;
}

#report {
  font-size: 1.5em;
}

</style>
!!! success "Oceanic Position Report"
    <div id="report"><span class="value">New Zealand 83</span> is position <span class="value">ANULI</span> at time <span class="value">1002</span>, flight level <span class="value">350</span>, estimating <span class="value">VIROG</span> at <span class="value">1042</span>, <span class="value">IGEVO</span> next.</div>

<table id="ortInput" class="table" cellspacing="2">
  <tbody>
    <tr>
      <th>Callsign</th>
      <td><input id="callsign" onkeyup="updateReport();" type="text" value="New Zealand 83"><br class="visible-xs-bm"><span class="fieldInfo">Your callsign</span></td>
    </tr>
    <tr>
      <th>Position</th>
      <td><input id="position" onkeyup="updateReport();" type="text" value="ANULI"><br class="visible-xs-bm"><span class="fieldInfo">The position you're reporting at.</span></td>
    </tr>
    <tr>
      <th>Time at Position</th>
      <td><input id="time" onkeyup="updateReport();" type="text" value="1002"><br class="visible-xs-bm"><span class="fieldInfo">The time of your position report. hhmm in UTC.</span></td>
    </tr>
    <tr>
      <th>Flight Level</th>
      <td><input id="flightLevel" onkeyup="updateReport();" type="text" value="350"><br class="visible-xs-bm"><span class="fieldInfo">Your current flight level.</span></td>
    </tr>
    <tr>
      <th>Next Position</th>
      <td><input id="next" onkeyup="updateReport();" type="text" value="VIROG"><br class="visible-xs-bm"><span class="fieldInfo">The position you are heading to next.</span></td>
    </tr>
    <tr>
      <th>Next Position ETA</th>
      <td><input id="nextETA" onkeyup="updateReport();" type="text" value="1042"><br class="visible-xs-bm"><span class="fieldInfo">Your estimated arrival time at the next position, hhmm in UTC.</span></td>
    </tr>
    <tr>
      <th>Then</th>
      <td><input id="then" onkeyup="updateReport();" type="text" value="IGEVO"><br class="visible-xs-bm"><span class="fieldInfo">The position you are planning to head to after your next waypoint.</span></td>
    </tr>
    <tr>
      <td colspan="2">
        <div class="section">
          <label>Have you been assigned a Mach speed by ATC?</label> <input id="sectionMach" onclick="updateReport();" type="checkbox">
          <div class="fieldInfo">Unless you are specifically assigned a mach speed to fly by ATC, you do not need to report your speed.</div>
        </div>
      </td>
    </tr>
    <tr class="sectionMach" style="display: none;">
      <th>Mach Speed</th>
      <td><input id="machSpeed" onkeyup="updateReport();" type="text" value=".84"><br class="visible-xs-bm"><span class="fieldInfo">Your current Mach Speed. M0.80 would be read as "decimal eight zero"</span></td>
    </tr>
    <tr class="sectionMach" style="display: none;">
      <th>Ground Speed</th>
      <td><input id="groundSpeed" onkeyup="updateReport();" type="text" value="510"><br class="visible-xs-bm"><span class="fieldInfo">Your current ground speed.</span></td>
    </tr>
    <tr>
      <td colspan="2">
        <div class="section">
          <label>Are you at a weather-reporting waypoint?</label> <input id="sectionWx" onclick="updateReport();" type="checkbox">
          <div class="fieldInfo">If you are unsure, assume you are not unless specifically requested for weather info by ATC.</div>
        </div>
      </td>
    </tr>
    <tr style="display: none;">
      <th>Temperature</th>
      <td><input id="temperature" onkeyup="updateReport();" type="text" value="-25"><br class="visible-xs-bm"><span class="fieldInfo">The outside air temperature at your current position.</span></td>
    </tr>
    <tr style="display: none;">
      <th>Wind Direction</th>
      <td><input id="windDirection" onkeyup="updateReport();" type="text" value="160"><br class="visible-xs-bm"><span class="fieldInfo">The direction component of the winds at your current flight level.</span></td>
    </tr>
    <tr style="display: none;">
      <th>Wind Speed</th>
      <td><input id="windSpeed" onkeyup="updateReport();" type="text" value="15"><br class="visible-xs-bm"><span class="fieldInfo">The speed component of the winds at your current flight level.</span></td>
    </tr>
    <tr style="display: none;">
      <th>Turbulence</th>
      <td>
        <select id="turbulence" onchange="updateReport();">
          <option value="none">None</option>
          <option value="light">Light</option>
          <option value="moderate">Moderate</option>
          <option value="severe">Severe</option>
        </select>
        <br class="visible-xs-bm"><span class="fieldInfo">The level of turbulence encountered at your current flight level.</span>
      </td>
    </tr>
    <tr style="display: none;">
      <th>Icing</th>
      <td>
        <select id="icing" onchange="updateReport();">
          <option value="none">None</option>
          <option value="light">Light</option>
          <option value="moderate">Moderate</option>
          <option value="severe">Severe</option>
        </select>
        <br class="visible-xs-bm"><span class="fieldInfo">The level of icing encountered at your current flight level.</span>
      </td>
    </tr>
    <tr style="display: none;">
      <th>Thunderstorms</th>
      <td>
        <select id="thunderstorms" onchange="updateReport();">
          <option value="none">None</option>
          <option value="active">Yes</option>
          <option value="active with hail">With Hail</option>
        </select>
        <br class="visible-xs-bm"><span class="fieldInfo">Thunderstorm activity encountered at your current position/flight level.</span>
      </td>
    </tr>
    <tr>
      <td colspan="2">
        <div class="section">
          <label>Are you travelling at an increased sim rate?</label>
          <div class="fieldInfo">2x and 4x sim rates are available at specific altitudes in Oceanic airspace, <strong>subject to ATC approval</strong>.<br>Note: Requests for accelerated sim rates will usually be declined during events.</div>
        </div>
      </td>
    </tr>
    <tr>
      <th>Sim Rate</th>
      <td>
        <select id="simrate" onchange="updateReport();">
          <option value="1x">1x</option>
          <option value="2x">2x</option>
          <option value="4x">4x</option>
        </select>
        <br class="visible-xs-bm"><span class="fieldInfo">The sim rate you are running your simulator at.</span>
      </td>
    </tr>
  </tbody>
</table>
<p>
<script type="text/javascript">// <![CDATA[
function v(name,label)
{
  var val = document.getElementById(name).value;
  if (val.length>0) return '<span class="value">'+val+'</span>';
  return '<span class="missingValue">('+label+')</span>';
}
function sv(name,decorate)
{
  var val = document.getElementById(name).options[document.getElementById(name).selectedIndex].value;
  if (decorate) return '<span class="value">'+val+'</span>';
  return val;
}
function toggleRows(testId,resultIds)
{
    var show = document.getElementById(testId).checked;
    for(var n=0;n<resultIds.length;n++)
    {
        var e = document.getElementById(resultIds[n]);
        while(e!=null&&e.nodeName!='TR')
        {
            e = e.parentNode;
        }
        if(e!=null)
        {
            try{e.style.display=show?'table-row':'none';} catch(err) {e.style.display='block';}
        }
    }
}
function updateReport()
{
    toggleRows('sectionMach',['machSpeed','groundSpeed']);
    toggleRows('sectionWx',['temperature','windDirection','windSpeed','turbulence','icing','thunderstorms']);
    document.getElementById('report').innerHTML=v('callsign','Callsign')+
' is position '+
v('position','Position')+
' at time '+
v('time','Time')+
', flight level '+
v('flightLevel','Flight Level')+
', estimating '+
v('next','Next Position')+
' at '+
v('nextETA','Next Position ETA')+
', '+
v('then','Then')+
' next'+
(document.getElementById('sectionMach').checked?
'. Mach '+
v('machSpeed','Mach Speed')+
', groundspeed '+
v('groundSpeed','Ground Speed'):'')+
(document.getElementById('sectionWx').checked?
'. Temperature '+
v('temperature','Temperature')+
', wind '+
(document.getElementById('windSpeed').value!=0?
v('windDirection','Wind Direction')+
' degrees '+
v('windSpeed','Wind Speed')+
' knots':
'calm')+
(sv('turbulence')!='none'?', turbulence '+sv('turbulence',true):'')+
(sv('icing')!='none'?', icing '+sv('icing',true):'')+
(sv('thunderstorms')!='none'?', thunderstorms '+sv('thunderstorms',true):''):'')+
(/*document.getElementById('sectionSimRate').checked&& */document.getElementById('simrate').value!='1x'?'. Sim rate: '+
v('simrate','Sim Rate'):'')//+
//'."</p>';
}
updateReport();
// ]]></script></p></div>
