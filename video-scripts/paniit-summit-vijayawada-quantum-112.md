# Video Script: Quantum-Assisted Emergency Dispatch
### PanIIT Summit, Vijayawada · Pilot with the Government of Andhra Pradesh (112 / 108 Emergency Response)

**Runtime:** about 3 min 15 sec · **Voice-over:** about 430 words at a calm, confident pace (~130 wpm)
**Tone:** human first, then technology, then proof, then vision. Use warm, cinematic music that builds at the results section.
**Partners on screen:** Government of Andhra Pradesh · Arohak · Quanfluence (quanfluence.com)

---

## SCENE 1: The Golden Hour (0:00 – 0:20)

**VISUALS:** Night. Rain on a Guntur street. A phone screen lights up as someone dials **112**. Quick cuts: a worried family, an ambulance's beacon starting up, the clock on a control-room wall.
**ON-SCREEN TEXT:** *Every minute matters.*
**SFX:** Phone ring, then a heartbeat that slowly fades under the music.

**VOICE-OVER:**
> When someone in Andhra Pradesh dials 112, a clock starts ticking. For a cardiac arrest, a road accident or a difficult delivery, the minutes between that call and a hospital bed can decide whether a life is saved.

---

## SCENE 2: The Problem (0:20 – 0:50)

**VISUALS:** Animated map of the district with dozens of ambulance, fire and police icons, hospitals and incident pins appearing at the same moment. Lines tangle as conflicting choices pile up.
**ON-SCREEN TEXT:** *Many incidents · Limited units · District boundaries · Hospital suitability · Live road conditions*

**VOICE-OVER:**
> Behind every call is a hard decision. Which ambulance should go? Which hospital is right for this patient? Which route through real roads gets them there fastest?
> Traditional dispatch often just picks the "nearest" unit. But when many emergencies happen at once, units are limited, and district boundaries and hospital capabilities all matter, the nearest choice is not always the best one for the whole system.

---

## SCENE 3: The Idea, Quantum-Assisted Optimization (0:50 – 1:30)

**VISUALS:** The tangled map freezes and turns into a glowing grid of binary 0/1 cells (the QUBO matrix). The cells resolve into clean, colour-coded assignments: ambulance → patient → hospital.
**ON-SCREEN TEXT:** *Quantum-Assisted Multi-Service Emergency Dispatch & Resource Placement Optimization*
then *Real road-network travel times + QUBO-based assignment*

**VOICE-OVER:**
> So we asked a different question. What if we optimized every decision together instead of one at a time?
> Our system takes the incident location and all available response resources. It identifies the right district and candidate units, and pulls real road-network travel times, not straight-line distances.
> It then frames the whole dispatch problem as a QUBO, a Quadratic Unconstrained Binary Optimization model. Rules such as "one ambulance per patient" and "the right hospital for the case" are built in as constraint penalties.
> The same mathematical model can then be solved by a classical solver or by a quantum or quantum-inspired solver.

---

## SCENE 4: How It Works in the Real World (1:30 – 2:00)

**VISUALS:** A simple animated flow (taken from the status deck):
`Existing dispatch system → API integration → Quantum Optimize Solver → Assigned ambulance · Assigned hospital · Optimized route`
Then a screen recording of the **Route API traffic** dashboard (108.vijayawada.co) showing ambulance, hospital and the "To scene / To hospital" columns.
**ON-SCREEN TEXT:** *Integrated end to end with the live dispatch system*

**VOICE-OVER:**
> We didn't build this in a lab and leave it there. Working with the Government of Andhra Pradesh, we connected it to the existing emergency dispatch system through APIs.
> Call and fleet data flow in, and within seconds the solver sends back a complete decision: which ambulance to send, which hospital to go to, and the optimized road route for both legs of the journey, from the ambulance to the patient and from the patient to the hospital.

---

## SCENE 5: Pilot Results, Guntur District (2:00 – 2:40)

**VISUALS:** Bold animated counters on a clean background, one after another. Old number on the left in grey, new number on the right in bright teal, with a downward arrow.

| Counter | Existing | Quantum-optimized | Change |
|---|---|---|---|
| Avg. time to scene | 22.6 min | **9.8 min** | **−57%** |
| Avg. time to hospital | 37.9 min | **7.7 min** | **−80%** |
| Avg. total response | 60.6 min | **17.5 min** | **−71%** |

Supporting badges: **391 live API dispatch requests** · **99.2% success rate** · **Guntur region, from 5 September 2026**

**ON-SCREEN FOOTNOTE (small, for at least 4 seconds):**
*Pilot comparison: 5 Sept 2026 data from the existing 108 system vs. routes and times computed by the quantum system. Quantum figures exclude buffer time for patient boarding and hospital handover.*

**VOICE-OVER:**
> We ran the pilot in the Guntur region. The system handled 391 live dispatch requests with a 99.2 percent success rate.
> When we compared it with the existing dispatch on the same day's calls, the results were striking.
> The average time to reach the scene fell from 22.6 minutes to 9.8.
> The average time from scene to hospital fell from 37.9 minutes to 7.7.
> Overall, the projected total response time dropped from about one hour to under eighteen minutes, a reduction of seventy-one percent.

---

## SCENE 6: Partnership (2:40 – 2:55)

**VISUALS:** Logos animate in side by side: **Government of Andhra Pradesh**, **Arohak**, **Quanfluence**. Cut to the team at work in the control room.
**ON-SCREEN TEXT:** *In partnership with Arohak and Quanfluence* · *quanfluence.com*

**VOICE-OVER:**
> This project was delivered in partnership with Arohak and Quanfluence, working hand in hand with the Government of Andhra Pradesh and its emergency response teams.

---

## SCENE 7: The Vision & Close (2:55 – 3:15)

**VISUALS:** The map zooms out from Guntur to all of Andhra Pradesh, then to India. Ambulance, fire and police icons light up across districts. Final shot: the ambulance from Scene 1 arriving at a hospital and the patient being wheeled in. Fade to title card.
**ON-SCREEN TEXT (final card):**
**Quantum-Assisted Emergency Response**
*Faster help. Smarter decisions. More lives saved.*
*Pilot with the Government of Andhra Pradesh · In partnership with Arohak and Quanfluence*
*PanIIT Summit, Vijayawada*

**VOICE-OVER:**
> Today it's ambulances in Guntur. Tomorrow it can be ambulances, fire and police, planned together across every district, including where to station them before the call ever comes.
> Because in an emergency, the best technology is the one that gets help there sooner.
> Quantum-assisted emergency response, built in Andhra Pradesh, for India.

**MUSIC:** Resolves on the final line. Hold the logo card for 3 seconds.

---

## Production Notes

1. **Accuracy and claims:** Keep the Scene 5 footnote on screen. The quantum figures are *computed/expected* route times without boarding or handover buffer, so the voice-over says "projected" for the total. Don't drop that word.
2. **108 vs 112:** 112 is the unified emergency number and 108 is the ambulance service whose data was used. The script uses "112" for the citizen-facing story and "108" in the data footnote. Confirm the preferred wording with the AP government contact.
3. **Screen captures to use:** the Route API traffic dashboard (summary cards: 391 total / 388 succeeded / 99.2%) and the route table with To-Scene / To-Hospital columns. Blur any patient-identifying or precise location data before showing it publicly.
4. **Optional local touch:** Open Scene 1 with a short Telugu greeting such as "నమస్కారం" in the voice-over, or add Telugu subtitles for the Vijayawada audience.
5. **Shorter cut (~90 sec):** Use Scenes 1, 3 (first two lines only), 5, 6 and 7. Keep the partner credit.
6. **Partner credits:** The script credits Arohak and Quanfluence. The status deck also names Quurium and NTRVST as validating teams. Confirm whether they should appear on screen too.
