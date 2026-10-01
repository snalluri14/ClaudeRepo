# Video 2: 108 Ambulance Dispatch, Simulation Pilot (Arohak × Quanfluence)

**What the pilot is:** a **simulation pilot**. We replayed **real 108 call data** through QUBO-based dispatch and routing, and compared the results with how the live 108 system actually performed on those calls. **QUBO has not yet been deployed live.**
**Purpose:** show how much sooner QUBO routing *would* get an ambulance to the patient and the patient to hospital care, compared with the current live 108 system.
**Length:** about 80 seconds, 1080p, loops at the stall.
**Silent-first:** every scene has a big headline, a caption bar and on-screen clocks. A voice-over is optional.
**Video 1** (`expo-video/arohak_quantum_expo.mp4`) is a separate video and is not affected by this script.

---

## The numbers

**Sources**
- **Current 108 = live data.** These are actual 108 response times. They reflect real operations, so **no buffers are added**.
- **QUBO routing = simulation.** The same 108 calls, re-dispatched and re-routed by the QUBO model in simulation. Because a simulation leaves out real-world delays, buffers are **added to the QUBO side only**:
  - **+15 min** at the distress location, before leaving for the hospital (stabilising and boarding the patient)
  - **+15 min** to hand the patient over at the hospital

### Deck figures (average minutes per call)

| | Current 108 (live data) | QUBO (simulated, before buffers) |
|---|---|---|
| Call → reach scene | 22.6 | 9.8 |
| Scene → reach hospital | 37.9 | 7.7 |
| Total | 60.6 | 17.5 |

### Video figures: clock from the 108 call

| Milestone | Current 108 (live data) | QUBO routing (simulated + buffers) | Difference |
|---|---|---|---|
| ① Ambulance reaches patient | **22.6** | **9.8** | **12.8 min sooner (−57%)** |
| ② Leaves the scene | (included in live data) | 24.8 (+15) | |
| ③ Reaches hospital | **60.6** | **32.5** | **28.1 min sooner (−46%)** |
| ④ Patient handed over | (included in live data) | **47.5** (+15) | |
| **End to end** | **60.6** | **47.5** | **13.1 min sooner (−22%)** |

| Stage (duration) | Current 108 (live data) | QUBO routing (simulated) | Difference |
|---|---|---|---|
| Call → scene | 22.6 | 9.8 | −57% |
| Scene → hospital (QUBO includes 15 min at scene) | 38.0 | 22.7 | −40% |
| **Call → patient in hospital care** (QUBO includes 15 + 15 min buffers) | **60.6** | **47.5** | **−22%** |

**Headline numbers for the video** (always shown as simulated)
1. **In simulation, the ambulance reaches the patient 13 minutes sooner: 9.8 vs 22.6 min (−57%).** This is the lead message.
2. **In simulation, the patient reaches hospital care 13 minutes sooner: 47.5 vs 60.6 min,** even after adding 30 minutes of buffer to the QUBO side only.

**Notes on the numbers**
- In the deck, the existing stage times add up to 60.5 but its total says 60.6, a rounding difference. The video uses the deck's total of 60.6, so the live leg from the scene to the hospital is 60.6 − 22.6 = 38.0.
- The comparison is **deliberately conservative**: every buffer goes on the simulated QUBO side, none on live 108. Say it with confidence: *"even after we add 30 minutes of buffer to our own simulation."*

---

## Scene-by-scene script

| # | Time | On screen (visual) | Headline / caption (what silent viewers read) | Voice-over (optional) |
|---|---|---|---|---|
| 1 | 0:00–0:06 | AROHAK TECHNOLOGIES × QUANFLUENCE lockup; ambulance icon with a pulse line | **108 Ambulance Dispatch: Simulation Pilot** · *QUBO routing on Quanfluence's Ising machine, tested on real 108 call data* | "Arohak and Quanfluence: a simulation pilot of QUBO-based ambulance dispatch, on real 108 call data." |
| 2 | 0:06–0:13 | A phone rings; a red distress pin appears on a city map | **From the 108 call to the hospital, every minute matters** | "When someone calls 108, every minute until they reach care matters." |
| 3 | 0:13–0:18 | Screen splits. Left **Current 108**, tagged *LIVE DATA* (grey). Right **QUBO routing**, tagged *SIMULATED · same 108 calls* (cyan). Same call, same map; both clocks at 0:00 | **Live 108 vs QUBO simulated on the same calls. Watch the clock.** | "On the left, what really happened on 108. On the right, the same calls, simulated with QUBO routing." |
| 4 | 0:18–0:28 | **① Reach the patient.** Both ambulances drive to the pin. The QUBO side arrives first and its clock freezes with a ✓; the live side keeps driving | **① Ambulance reaches patient** · Live 108 **22.6 min** · QUBO (simulated) **9.8 min** · badge **13 min sooner (−57%)** | "In simulation, QUBO routing reaches the patient in 9.8 minutes. On live 108, it took 22.6. That's 13 minutes sooner at the patient's side." |
| 5 | 0:28–0:34 | **② At the scene.** QUBO side only: patient boards and a "+15 min" chip appears; the live side shows *"included in live data"* | **② +15 min at the scene, added to the simulation** · QUBO clock **24.8** | "Live data already includes time at the scene, so we add fifteen minutes to the simulation to stabilise and board the patient." |
| 6 | 0:34–0:44 | **③ To the hospital.** Both ambulances drive to hospital icons; the QUBO side arrives first | **③ Reaches hospital** · Live 108 **60.6** · QUBO (simulated) **32.5** | "In simulation, QUBO routing reaches the hospital at 32.5 minutes. On live 108, it took 60.6." |
| 7 | 0:44–0:50 | **④ Handover.** QUBO side only: "+15 min" chip; the clock locks at 47.5 | **④ +15 min hospital handover, added to the simulation** · final **47.5 vs 60.6** | "Even with fifteen more minutes added for handover, the simulated patient is in care at 47.5 minutes, against 60.6 on live 108." |
| 8 | 0:50–0:58 | Two timeline bars drawn to scale. Live: one grey bar, 60.6. QUBO: four segments (reach 9.8, scene 15, drive 7.7, handover 15) = 47.5. Gap highlighted | **Call → patient in hospital care** · **47.5 (simulated) vs 60.6 (live)** · badge **13 minutes sooner** · small: *30 min of buffers added to the simulation only* | "In simulation, that's 13 minutes sooner into care, even with 30 minutes of buffer added to our side only." |
| 9 | 0:58–1:06 | Scorecard, headed **Simulation results on real 108 call data**. Big top row: **13 min sooner at the patient (−57%)**. Below: scene → hospital −40% · call to care −22% | **Simulated: 13 minutes sooner at the patient's side** | "Simulated on real 108 calls: thirteen minutes sooner at the patient's side, and sooner all the way to the hospital." |
| 10 | 1:06–1:12 | 3-step graphic: 108 call records + ambulance locations → **Arohak QUBO model** → **Quanfluence Ising machine** → best ambulance and route | **How it works: Arohak models dispatch and routing as one optimisation, and Quanfluence's Ising machine solves it** | "Arohak turns dispatch and routing into one optimisation problem, and Quanfluence's Ising machine solves it." |
| 11 | 1:12–1:18 | Roadmap with three steps: **Simulation on 108 data ✓** → **Live 108 trial** → **112: police, fire and ambulance as one** | **Simulation done. Next: a live 108 trial, then 112** | "The simulation is done. Next comes a live trial on 108, and then 112, with police, fire and ambulance as one." |
| 12 | 1:18–1:23 | Closing lockup | **AROHAK × QUANFLUENCE** · *Visit our joint stall* | "Visit our joint stall." |

**Footnote on every results screen (small text):** *Current 108: live data, average minutes per call. QUBO: simulation on the same 108 call data, plus 15 min at the scene and 15 min hospital handover (added to QUBO only). Not yet deployed live.*

---

## Honesty guardrails

- Every QUBO number on screen and in the voice-over is labelled **"simulated"** or **"in simulation"**. Every 108 number is labelled **"live data"**.
- The video never says "deployed", "proven", "live pilot" or "we ran it on 108". It always says "simulation on real 108 call data".
- Scene 11 shows the honest roadmap: **simulation done → live 108 trial → 112**.
- All buffers go on the simulated QUBO side only, and the screen says so, which keeps the comparison conservative.
- No unverified speed claim is made for the solver ("in moments" has been removed). If the deck has a measured solver time, we can add it.
- The video uses *QUBO routing* and *Ising machine*, never "quantum computer".
- The map and routes are labelled *illustrative*. Only the minutes are real data.

---

## Built video: `arohak_108_simulation_pilot.mp4`

1080p, 83 seconds, loops. Scenes 4–7 run as one race on a **single shared clock** that starts at the 108 call, so both sides can be compared at every moment. When reading the voice-over live, use these cue points:

| Video time | Cue |
|---|---|
| 0:18 | Race starts (both clocks at 0) |
| 0:25 | QUBO (simulated) reaches the patient at 9.8 min |
| 0:29 | Live 108 reaches the patient at 22.6 min, with the "13 min sooner (−57%)" badge |
| 0:31 | QUBO: +15 min at the scene, leaves at 24.8 |
| 0:36 | QUBO reaches hospital at 32.5 |
| 0:38 | QUBO: +15 min handover, patient in care at 47.5 (0:42) |
| 0:48 | Live 108 reaches hospital at 60.6, with the "13 min sooner into hospital care (−22%)" badge |
| 0:50 | Timeline bars · 0:58 Scorecard · 1:06 How it works · 1:12 Roadmap · 1:18 Close |
