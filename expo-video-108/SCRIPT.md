# Video 2: 108 Ambulance Dispatch Pilot (Arohak × Quanfluence)

**Purpose:** compare live 108 dispatch performance with the QUBO routing forecast from the pilot. The comparison runs from the distress call, to the scene, to the hospital.
**Length:** about 80 seconds, 1080p, loops at the stall.
**Silent-first:** every scene has a big headline, a caption bar and on-screen clocks. A voice-over is optional.
**Video 1** (`expo-video/arohak_quantum_expo.mp4`) stays unchanged.

---

## The numbers

**Sources**
- **Current 108:** live 108 data. It reflects real operations, so **no buffers are added**.
- **QUBO routing:** forecast from the pilot. Real-world buffers are **added to the QUBO side only**:
  - **+20 min** at the distress location, before leaving for the hospital (stabilising and boarding the patient)
  - **+15 min** to hand the patient over at the hospital

### Deck figures (average minutes per call)

| | Current 108 (live) | QUBO (forecast, before buffers) |
|---|---|---|
| Call → reach scene | 22.6 | 9.8 |
| Scene → reach hospital | 37.9 | 7.7 |
| Total | 60.6 | 17.5 |

### Video figures: clock from the 108 call

| Milestone | Current 108 (live) | QUBO routing (forecast + buffers) | Saved |
|---|---|---|---|
| ① Ambulance reaches patient | **22.6** | **9.8** | **12.8 min (−57%)** |
| ② Leaves the scene | (included in live data) | 29.8 (+20) | |
| ③ Reaches hospital | **60.6** | **37.5** | **23.1 min (−38%)** |
| ④ Patient handed over | (included in live data) | **52.5** (+15) | |
| **End to end** | **60.6** | **52.5** | **8.1 min (−13%)** |

| Stage (duration) | Current 108 (live) | QUBO routing | Saved |
|---|---|---|---|
| Call → scene | 22.6 | 9.8 | −57% |
| Scene → hospital (QUBO includes 20 min at scene) | 38.0 | 27.7 | −27% |
| **Call → patient in hospital care** (QUBO includes 20 + 15 min buffers) | **60.6** | **52.5** | **−13%** |

**Headline numbers for the video**
1. **The ambulance reaches the patient 13 minutes sooner: 9.8 vs 22.6 min (57% faster).** This is the lead message, since the first minutes on scene matter most.
2. **The patient is in hospital care 8 minutes sooner: 52.5 vs 60.6 min,** even after adding 35 minutes of buffer to the QUBO forecast only.

**Notes on the numbers**
- In the deck, the existing stage times add up to 60.5 but its total says 60.6, a rounding difference. The video uses the deck's total of 60.6, so the live leg from the scene to the hospital is 60.6 − 22.6 = 38.0.
- The end-to-end comparison is **deliberately conservative**: every buffer goes on the QUBO side. That makes it hard to challenge, so say it with confidence: *"even after we add 35 minutes of buffer to our own forecast."*

---

## Scene-by-scene script

| # | Time | On screen (visual) | Headline / caption (what silent viewers read) | Voice-over (optional) |
|---|---|---|---|---|
| 1 | 0:00–0:06 | AROHAK TECHNOLOGIES × QUANFLUENCE lockup; ambulance icon with a pulse line | **108 Ambulance Dispatch: Pilot** · *QUBO routing on Quanfluence's Ising machine* | "Arohak and Quanfluence: our 108 ambulance dispatch pilot." |
| 2 | 0:06–0:13 | A phone rings; a red distress pin appears on a city map | **From the 108 call to the hospital, every minute matters** | "When someone calls 108, every minute until they reach care matters." |
| 3 | 0:13–0:18 | Screen splits. Left **Current 108**, tagged *LIVE DATA* (grey). Right **QUBO routing**, tagged *PILOT FORECAST* (cyan). Same call, same map; both clocks at 0:00 | **Live 108 vs QUBO forecast. Same emergency. Watch the clock.** | "Live 108 data against our QUBO routing forecast. Same emergency." |
| 4 | 0:18–0:28 | **① Reach the patient.** Both ambulances drive to the pin. QUBO arrives first and its clock freezes with a ✓; the live side keeps driving | **① Ambulance reaches patient** · Live 108 **22.6 min** · QUBO **9.8 min** · badge **13 min sooner (−57%)** | "QUBO routing reaches the patient in 9.8 minutes. Today it takes 22.6. That's 13 minutes sooner at the patient's side." |
| 5 | 0:28–0:34 | **② At the scene.** QUBO side only: patient boards and a "+20 min" chip appears; the live side shows *"included in live data"* | **② 20 min at the scene, added to the QUBO forecast** · QUBO clock **29.8** | "We add twenty minutes at the scene to our forecast, to stabilise and board the patient." |
| 6 | 0:34–0:44 | **③ To the hospital.** Both ambulances drive to hospital icons; QUBO arrives first | **③ Reaches hospital** · Live 108 **60.6** · QUBO **37.5** | "QUBO routing reaches the hospital at 37.5 minutes. The live system takes 60.6." |
| 7 | 0:44–0:50 | **④ Handover.** QUBO side only: "+15 min" chip; the clock locks at 52.5 | **④ 15 min hospital handover, added to the QUBO forecast** · final **52.5 vs 60.6** | "Even after fifteen more minutes for handover, the patient is in care at 52.5 minutes, against 60.6 today." |
| 8 | 0:50–0:58 | Two timeline bars drawn to scale. Live: one grey bar, 60.6. QUBO: four segments (reach 9.8, scene 20, drive 7.7, handover 15) = 52.5. Gap highlighted | **Call → patient in hospital care** · **52.5 vs 60.6 min** · badge **8 minutes sooner** · small: *with 35 min of buffers added to QUBO only* | "That's 8 minutes sooner into care, even with 35 minutes of buffer added to our side only." |
| 9 | 0:58–1:06 | Scorecard. Big top row: **13 min sooner at the patient (−57%)**. Below: scene → hospital −27% · call to care −13% | **13 minutes sooner at the patient's side** | "Thirteen minutes sooner at the patient's side, and faster all the way to the hospital." |
| 10 | 1:06–1:12 | 3-step graphic: live calls + ambulance GPS → **Arohak QUBO model** → **Quanfluence Ising machine** → best ambulance and route | **Why it's faster: Arohak models dispatch and routing as one optimisation, and Quanfluence's Ising machine solves it in moments** | "Arohak turns dispatch and routing into one optimisation, and Quanfluence's Ising machine solves it in moments." |
| 11 | 1:12–1:18 | The ambulance icon expands into ambulance, police and fire icons, then a **112** badge | **Piloted on 108. Next: 112, with police, fire and ambulance as one** | "Piloted on 108. Next, 112: police, fire and ambulance as one." |
| 12 | 1:18–1:23 | Closing lockup | **AROHAK × QUANFLUENCE** · *Visit our joint stall* | "Visit our joint stall." |

**Footnote on every results screen (small text):** *Current 108: live data, average minutes per call. QUBO: pilot forecast, plus 20 min at the scene and 15 min hospital handover (added to QUBO only).*

---

## Honesty guardrails

- The QUBO side is always tagged **"Pilot forecast"** and the 108 side **"Live data"**. The video never presents the forecast as measured.
- Scene 11 says **"Piloted on 108"**, not "proven", because the QUBO figures are forecasts. 112 is presented as the **next step**.
- All buffers go on the QUBO side only, and the screen says so, which keeps the comparison conservative.
- The video uses *QUBO routing* and *Ising machine*, never "quantum computer".
- The map and routes are labelled *illustrative*. Only the minutes are real data.
