# Video 2: 108 Ambulance Dispatch Pilot (Arohak × Quanfluence)

**Purpose:** show how much faster QUBO-based dispatch gets a patient from the distress call, to the ambulance arriving, to the right hospital, compared with the current 108 process.
**Length:** about 75 seconds, 1080p, loops at the stall.
**Silent-first:** every scene has a big headline, a caption bar and on-screen timers. A voice-over is optional.
**Video 1** (`expo-video/arohak_quantum_expo.mp4`) stays unchanged.

---

## Numbers needed from the pilot deck

The video uses only these values. Every `[A..]` / `[B..]` tag below is a placeholder until you send the real figures.

| Tag | Metric | Current 108 | QUBO pilot |
|---|---|---|---|
| A1 / B1 | **Call → ambulance assigned** (decision time) | [A1] | [B1] |
| A2 / B2 | **Ambulance → reaches patient** | [A2] | [B2] |
| A3 / B3 | **Patient → reaches right hospital** | [A3] | [B3] |
| AT / BT | **Total: call → hospital** | [AT] | [BT] |
| PCT | % faster overall | | [PCT] |
| SCOPE | Pilot district or city, duration, number of calls, number of ambulances, number of hospitals | [SCOPE] | |

Optional, if the deck has it: % of calls reached within the target time, km saved, number of cases sent to a better-suited hospital, solver time on the Ising machine.

---

## Scene-by-scene script

| # | Time | On screen (visual) | Headline / caption (what silent viewers read) | Voice-over (optional) |
|---|---|---|---|---|
| 1 | 0:00–0:06 | AROHAK TECHNOLOGIES × QUANFLUENCE lockup; ambulance icon with a pulse line | **108 Ambulance Dispatch: Pilot Results** · *QUBO optimisation on Quanfluence's Ising machine* | "Arohak and Quanfluence: results from our 108 ambulance dispatch pilot." |
| 2 | 0:06–0:14 | A phone rings; a red distress pin appears on a city map; a clock starts | **Every minute between the call and the hospital matters** · *108 must choose the right ambulance and the right hospital, instantly* | "When someone calls 108, every minute between the call and the hospital matters." |
| 3 | 0:14–0:21 | Map zooms out to the pilot area; counters tick up | **The pilot** · [SCOPE]: *[district] · [N] calls · [N] ambulances · [N] hospitals · [period]* | "We ran a live pilot on 108 ambulance dispatch in [district]." |
| 4 | 0:21–0:24 | Screen splits: left **Current 108** (grey), right **QUBO dispatch** (cyan); same call, same map, two clocks at 00:00 | **Same emergency. Two systems. Watch the clock.** | "Same emergency, two systems." |
| 5 | 0:24–0:32 | **Stage 1: Assign.** Left: ambulances checked one by one. Right: all ambulances and calls are considered together and one is locked in quickly | **① Call → ambulance assigned** · Current: **[A1]** · QUBO: **[B1]** | "First, assigning the ambulance. QUBO weighs every ambulance and every call together, and decides in [B1]." |
| 6 | 0:32–0:40 | **Stage 2: Reach.** Both ambulances drive to the pin; the QUBO ambulance takes a closer or better-routed unit and arrives first | **② Ambulance → reaches patient** · Current: **[A2]** · QUBO: **[B2]** | "Then reaching the patient: [B2] instead of [A2]." |
| 7 | 0:40–0:50 | **Stage 3: Hospital.** Hospital icons show distance, beds and specialty. Left goes to the nearest hospital; right goes to the best-suited one with capacity | **③ Patient → right hospital** · Current: **[A3]** · QUBO: **[B3]** | "Finally, the right hospital, with beds and specialty matched, in [B3]." |
| 8 | 0:50–0:58 | Both clocks stop; a total bar race: left bar [AT], right bar [BT]; a large badge appears | **Call to hospital: [BT] vs [AT]** · big badge: **[PCT] faster** | "From call to hospital: [BT] instead of [AT]. That's [PCT] faster." |
| 9 | 0:58–1:05 | Scorecard table (the 3 stages and the total) with green ticks on the QUBO column | **Pilot scorecard** · *Measured in the 108 pilot, [period]* | "Faster at every stage." |
| 10 | 1:05–1:11 | Simple 3-step graphic: Live calls + ambulance GPS + hospital beds → **Arohak QUBO model** → **Quanfluence Ising machine** → dispatch plus hospital in one decision | **Why it's faster: ambulance and hospital decided together, in one optimisation** | "Arohak models the whole decision, ambulance and hospital together, and Quanfluence's Ising machine solves it in moments." |
| 11 | 1:11–1:17 | The ambulance icon expands into ambulance, police and fire icons, then a **112** badge | **Proven on 108. Next: 112, with police, fire and ambulance as one** | "Proven on 108. Next, 112: police, fire and ambulance as one." |
| 12 | 1:17–1:22 | Closing lockup | **AROHAK × QUANFLUENCE** · *Visit our joint stall* | "Visit our joint stall." |

---

## Honesty guardrails built into the video

- The title and every results screen say **"Pilot"**. We don't call it statewide or 112-wide.
- Scene 11 presents 112 as the **next step**, not as something already done.
- Every number on screen comes from the deck. Any visual that isn't real data, such as the map or the routes, is labelled *illustrative*.
- The video uses *QUBO* and *Ising machine*, never "quantum computer".
- Scene 10 says "ambulance and hospital decided together". **Confirm this matches how the pilot actually worked.** If hospital selection wasn't part of the QUBO model, I'll reword it.

---

## What I need from you to build it

1. The **numbers** for the table at the top. You can paste them, or share the deck again; it didn't come through in this chat.
2. Confirm the **pilot scope** line: which district, how long, how many calls.
3. Confirm whether **hospital selection** was part of the QUBO optimisation.
