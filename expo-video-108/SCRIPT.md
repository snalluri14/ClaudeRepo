# Video 2: 108 Ambulance Dispatch Pilot (Arohak × Quanfluence)

**Purpose:** show how much faster QUBO-based routing gets a patient from the 108 call to the scene, then to the hospital, compared with the current 108 dispatch.
**Length:** about 80 seconds, 1080p, loops at the stall.
**Silent-first:** every scene has a big headline, a caption bar and on-screen clocks. A voice-over is optional.
**Video 1** (`expo-video/arohak_quantum_expo.mp4`) stays unchanged.

---

## The numbers (source: pilot deck, "Existing vs Quantum routing Comparison")

### Deck figures: travel time only (average minutes per call)

| Stage | Current 108 | QUBO routing | Saved |
|---|---|---|---|
| Call → reach scene | 22.6 | 9.8 | 12.8 min (−57%) |
| Scene → reach hospital | 37.9 | 7.7 | 30.2 min (−80%) |
| **Total** | **60.6** | **17.5** | **43.1 min (−71%)** |

### Video figures: with real-world buffers added

The deck figures leave out two fixed steps, which take the **same time in both systems**:
- **+15 min** for the patient to board the ambulance at the scene
- **+15 min** for the ambulance to hand the patient over at the hospital

| Milestone (cumulative clock from the 108 call) | Current 108 | QUBO routing | Saved |
|---|---|---|---|
| ① Ambulance reaches patient | 22.6 | 9.8 | 12.8 min (−57%) |
| ② Patient boarded (+15) | 37.6 | 24.8 | 12.8 min |
| ③ Ambulance reaches hospital | 75.6 | 32.5 | 43.1 min (−57%) |
| ④ Patient handed over (+15) | **90.6** | **47.5** | **43.1 min (−48%)** |

| Stage (duration) | Current 108 | QUBO routing | Saved |
|---|---|---|---|
| Reach scene | 22.6 | 9.8 | −57% |
| Scene → hospital, including 15 min boarding | 52.9 | 22.7 | −57% |
| **Call → patient handed over (end-to-end)** | **90.6** | **47.5** | **43.1 min, −48%** |

**Headline numbers for the video:**
- **47.5 min vs 90.6 min**, call to patient handed over at the hospital
- **43 minutes saved per emergency**
- **48% faster end to end**

**Notes on the numbers**
- In the deck, the existing stage times add up to 60.5 but its total says 60.6, a rounding difference. The video follows the deck's total, so the on-screen clocks stay consistent: hospital arrival 60.6 + 15 = **75.6**, and handover 75.6 + 15 = **90.6**.
- Adding the buffers changes the percentage, not the minutes saved. On travel time alone, QUBO is 71% faster. Once boarding and handover are included, it is 48% faster end to end, and the saving stays **43.1 minutes**. The 48% figure is the conservative, real-world one, and it's the one experts will trust.

---

## Scene-by-scene script

| # | Time | On screen (visual) | Headline / caption (what silent viewers read) | Voice-over (optional) |
|---|---|---|---|---|
| 1 | 0:00–0:06 | AROHAK TECHNOLOGIES × QUANFLUENCE lockup; ambulance icon with a pulse line | **108 Ambulance Dispatch: Pilot** · *QUBO routing on Quanfluence's Ising machine* | "Arohak and Quanfluence: our 108 ambulance dispatch pilot." |
| 2 | 0:06–0:13 | A phone rings; a red distress pin appears on a city map | **From the 108 call to the hospital, every minute matters** | "When someone calls 108, every minute until they reach the hospital matters." |
| 3 | 0:13–0:17 | Screen splits: left **Current 108** (grey), right **QUBO routing** (cyan); same call, same map; both clocks at 0:00 | **Same emergency. Two systems. Watch the clock.** | "Same emergency. Two systems." |
| 4 | 0:17–0:27 | **① Reach the patient.** Both ambulances drive to the pin; QUBO arrives first, and its clock freezes with a ✓ | **① Ambulance reaches patient** · Current **22.6 min** · QUBO **9.8 min** · badge **−57%** | "QUBO routing reaches the patient in 9.8 minutes, against 22.6 today." |
| 5 | 0:27–0:33 | **② Boarding.** Patient icon moves into the ambulance; a "+15 min" chip appears on **both** sides | **② Patient boards: 15 min on both sides** · clocks show **37.6** vs **24.8** | "Boarding takes the same fifteen minutes in both systems." |
| 6 | 0:33–0:45 | **③ To the hospital.** Both ambulances drive to hospital icons; QUBO arrives far earlier | **③ Ambulance reaches hospital** · clocks show **75.6** vs **32.5** | "QUBO routing reaches the hospital at 32.5 minutes. The current system takes 75.6." |
| 7 | 0:45–0:51 | **④ Handover.** "+15 min" chip on both sides; final clocks lock | **④ Patient handed over: 15 min on both sides** · final clocks **90.6** vs **47.5** | "After a fifteen-minute handover, the patient is in care at 47.5 minutes, instead of 90.6." |
| 8 | 0:51–0:59 | Two horizontal timeline bars split into 4 coloured segments (reach, board, drive, handover), drawn to scale; the gap between them is highlighted | **Call → patient in hospital care** · **47.5 min vs 90.6 min** · big badge **43 minutes saved** | "That's 43 minutes saved for every emergency." |
| 9 | 0:59–1:06 | Scorecard: three rows (reach scene −57% · scene → hospital incl. boarding −57% · end to end −48%) | **48% faster from call to care** · *Includes 15 min boarding + 15 min hospital handover in both systems* | "Even after boarding and handover, that's 48% faster from call to care." |
| 10 | 1:06–1:12 | 3-step graphic: live calls + ambulance GPS → **Arohak QUBO model** → **Quanfluence Ising machine** → best ambulance and route | **Why it's faster: Arohak models the routing as one optimisation, and Quanfluence's Ising machine solves it in moments** | "Arohak turns dispatch and routing into one optimisation, and Quanfluence's Ising machine solves it in moments." |
| 11 | 1:12–1:18 | The ambulance icon expands into ambulance, police and fire icons, then a **112** badge | **Proven on 108. Next: 112, with police, fire and ambulance as one** | "Proven on 108. Next, 112: police, fire and ambulance as one." |
| 12 | 1:18–1:23 | Closing lockup | **AROHAK × QUANFLUENCE** · *Visit our joint stall* | "Visit our joint stall." |

**Footnote on every results screen (small text):** *Average minutes per call, 108 pilot. Includes 15 min patient boarding and 15 min hospital handover, applied equally to both systems.*

---

## Honesty guardrails

- Each results screen says **"pilot"**. The video never calls this statewide or 112-wide.
- Scene 11 presents 112 as the **next step**, not as something already done.
- The 15-minute buffers are added **equally to both sides**, and the screen says so, so the comparison stays fair.
- The video uses *QUBO routing* and *Ising machine*, never "quantum computer".
- The map and routes are labelled *illustrative*. Only the minutes are real data.

---

## Please confirm before I build it

1. **Measured or expected?** Did the deck's figures come from live pilot calls, or are they a simulation or projection on pilot data? If they aren't measured on live calls, the footnote will say *"Pilot simulation on 108 call data"* instead of *"108 pilot"*.
2. **Pilot scope (optional):** the district, period and number of calls, for one line in scene 2.
