# AV Script: "From a 108 Call to Light Pulses": Arohak Quantum Capability (112 pilot use case)

**Purpose:** show *how* Arohak solves emergency dispatch. A call becomes a QUBO, the QUBO becomes Ising spins, and the spins are solved on Quanfluence's optical Ising machine. Then show the time saved compared with the current system.
**Audience:** government officials, IIT alumni, industry. Technical enough to earn expert credibility, simple enough for non-experts.
**Length:** about 2 min 53 s, 1080p. Works without sound (big on-screen text in every scene); the voice-over is optional.
**Pilot scope:** the 112 vision covers police, fire and ambulance. The **pilot** covers the **ambulance (108) arm**, as a **simulation on real 108 call data**.

> Values marked **[CONFIRM]** must be checked with Quanfluence or the project team before the AV is built.

---

## Opening: logos (0:00–0:08)

| # | Time | Visual | On-screen text | Voice-over |
|---|---|---|---|---|
| 0a | 0:00–0:04 | Black screen. The **Arohak Technologies logo** (official file) fades in at the centre with a soft light sweep | *Arohak Technologies Pvt Ltd* · tagline **[CONFIRM: Arohak's official tagline, if any]** | "Arohak Technologies." |
| 0b | 0:04–0:08 | The Arohak logo moves to the left. A thin line draws across, and the **Quanfluence logo** (official file) fades in on the right | **in partnership with Quanfluence** · *Quantum-inspired optimisation on an optical Ising machine* | "In partnership with Quanfluence." |

## Act 1: The problem (0:08–0:43)

| # | Time | Visual | On-screen text | Voice-over |
|---|---|---|---|---|
| 1 | 0:08–0:16 | Black screen. Phone rings. **2:14 AM**. Red pin pulses on a dark map of Andhra Pradesh | **2:14 AM. A distress call.** *Chest pain. 62-year-old man.* | "2:14 AM. A distress call: a 62-year-old man with chest pain." |
| 2 | 0:16–0:28 | Three questions pop up around the pin, each with an icon: 🚑 · 🛣️ · 🏥 | **Which ambulance? Which route? Which hospital?** | "Three decisions, made in seconds: which ambulance, which route, and which hospital." |
| 3 | 0:28–0:43 | The map shows two hospitals: the nearest one is a **children's hospital ✗** and a farther one is a **cardiac centre with a free ICU bed ✓** | **The nearest hospital is not always the right hospital.** *A heart patient needs cardiac care, not a children's hospital.* | "And the nearest hospital isn't always the right one. A heart patient needs a cardiac centre with a free bed, not a children's hospital." |

## Act 2: Why it's hard (0:43–1:03)

| # | Time | Visual | On-screen text | Voice-over |
|---|---|---|---|---|
| 4 | 0:43–1:03 | Zoom out: dozens of calls, ambulances and hospitals across the state; tangled lines flicker | **Many calls × many ambulances × many hospitals** · *Every combination is a possible plan* | "Now multiply that by every call, every ambulance and every hospital in the state. The number of possible plans explodes, and the best one changes every minute." |

## Act 3: How Arohak solves it (1:03–2:08)

| # | Time | Visual | On-screen text | Voice-over |
|---|---|---|---|---|
| 5 | 1:03–1:18 | **Step 1: Model.** Each choice becomes a switch (0/1) in a grid: rows are ambulances, columns are calls, plus hospital choices for each call | **① Every decision becomes a yes/no switch** · *Ambulance A → Call 1? Patient → Cardiac centre?* | "Step one: Arohak turns every choice into a simple yes-or-no switch. Does ambulance A take call 1? Does this patient go to the cardiac centre?" |
| 6 | 1:18–1:33 | **Step 2: QUBO.** The switches feed one "cost" meter. Rule cards snap on: ⏱ travel time · 1️⃣ one ambulance per call · 🚑 each ambulance used once · 🏥 **specialty match** (cardiac → cardiac centre) · 🛏 bed available | **② QUBO: one cost score. Lower = better.** *Rules become penalties: a wrong hospital costs heavily* | "Step two: we write it as a QUBO, one score where lower is better. Travel time adds cost. Breaking a rule, like sending a heart patient to a children's hospital, adds a heavy penalty." |
| 7 | 1:33–1:48 | **Step 3: Fit to hardware.** The state map splits into **zones**; each zone becomes a small block of spins. Each block shows a counter: **[CONFIRM N] spins ≤ [CONFIRM 128] capacity** | **③ Split by zone so each piece fits the machine** · *Each zone ≈ [CONFIRM N] spins · capacity [CONFIRM 128] fully connected spins* | "Step three: fitting the problem to the hardware. We split the state into zones so each piece fits the machine: about [N] spins per zone, within its [128] fully connected spins. This is a big part of the engineering." |
| 8 | 1:48–2:03 | **Step 4: Solve on light.** A glowing **fibre loop**. Pulses of light circulate; each pulse is labelled ↑ or ↓. They flicker, interact, then settle. An energy meter drops to its lowest point | **④ Quanfluence Ising machine: each spin is a pulse of light in a fibre loop** · *The pulses settle into the lowest-energy state = the best plan* | "Step four: Quanfluence's Ising machine. Each spin is a pulse of light travelling in a fibre loop. The pulses interact and settle into their lowest-energy state, and that state is the best plan." |
| 9 | 2:03–2:08 | **Step 5: Decode.** Spins turn back into lines on the map: ambulance → patient → cardiac centre ✓. Zone results stitch together | **⑤ Spins → dispatch plan** · *Right ambulance · fastest route · right hospital* | "Step five: the spins become the dispatch plan: the right ambulance, the fastest route and the right hospital." |

## Act 4: The result (2:08–2:38)

| # | Time | Visual | On-screen text | Voice-over |
|---|---|---|---|---|
| 10 | 2:08–2:23 | Split screen with one clock. **Current 108 (live data)** vs **Ising-machine routing (simulated)** race on the same call | **Reach the patient: 22.6 → 9.8 min** · badge **13 min sooner (−57%)** | "Tested on real 108 call data: today, help reaches the patient in 22.6 minutes on average. With our routing, 9.8. That's thirteen minutes sooner." |
| 11 | 2:23–2:38 | Timeline bars: 60.6 (grey) vs 47.5 (cyan, with gold buffer segments) | **Call → hospital care: 60.6 → 47.5 min** · badge **13 min sooner (−22%)** · small: *with 30 min of buffer added to our side only* | "And into hospital care: 47.5 minutes instead of 60.6, even after we add thirty minutes of buffer to our own numbers." |

## Act 5: Next and close (2:38–2:53)

| # | Time | Visual | On-screen text | Voice-over |
|---|---|---|---|---|
| 12 | 2:38–2:46 | Roadmap: ✓ Simulation on 108 data → Live 108 trial → **112: police, fire & ambulance** | **Ambulance today. All of 112 next.** | "We started with ambulances. Next comes a live trial, and then all of 112: police, fire and ambulance as one." |
| 13 | 2:46–2:53 | **Both official logos** side by side (Arohak left, Quanfluence right) | **Arohak Technologies × Quanfluence** · *Quantum-inspired today. Quantum-ready tomorrow.* | "Arohak and Quanfluence. Quantum-inspired today, quantum-ready tomorrow." |

**Footnote on the results screens (10–11):** *Current 108: live data, average minutes per call. Ising-machine routing: simulation on the same 108 calls, with 15 min at the scene and 15 min hospital handover added to the simulated side only. Not yet deployed live.*

---

## The numbers used

| | Current 108 (live data) | Ising-machine routing (simulated) | Difference |
|---|---|---|---|
| Call → reach patient | 22.6 min | 9.8 min | **12.8 min sooner (−57%)** |
| Call → hospital care | 60.6 min | 47.5 min (9.8 + 15 at scene + 7.7 drive + 15 handover) | **13.1 min sooner (−22%)** |

---

## Logo files needed

- **Arohak Technologies logo** and **Quanfluence logo**, as official files. **SVG or PNG with a transparent background**, at least 1000 px wide, is best.
- If either logo has a dark-background (white) version, send that too. The AV uses a dark navy background.
- Logos are used on the opening (0a, 0b), in a small co-brand tag in the top-left corner of every scene, and on the closing screen (13).
- Quanfluence should approve the use of its logo.

## Must confirm before building

1. **[CONFIRM N]:** average spins per zone sub-problem.
2. **[CONFIRM 128]:** the machine's fully connected spin capacity.
3. **Specialty and bed matching:** was hospital choice (cardiac → cardiac centre, bed availability) actually part of the QUBO in the simulation? If it was only ambulance and route, I'll change scenes 3, 6 and 9 to say "next step" instead of presenting it as done.
4. **Number of zones** (optional): for example "AP split into [X] zones". It adds credibility in scene 7.
5. **Quanfluence approval** of the scene 8 description: "each spin is a pulse of light in a fibre loop."

## Technical backup for Q&A (not shown on screen)

- **Variables:** x(a,c) = 1 if ambulance *a* takes call *c*; y(c,h) = 1 if call *c* goes to hospital *h*.
- **Objective:** minimise travel time (ambulance → patient → hospital), weighted by severity.
- **Constraints as penalties:** each call gets exactly one ambulance; each ambulance takes at most one call; each patient goes to exactly one hospital; the hospital must match the patient's condition and have a free bed.
- **QUBO → Ising:** substitute x = (1 + s) / 2, so each binary variable becomes a spin s = ±1.
- **Decomposition:** each zone is solved as its own sub-problem so it fits the machine. **[CONFIRM]** how ambulances near zone borders are handled.
- **Plan check:** **[CONFIRM]** whether each decoded plan is checked against the rules before use. Only say this if it's true.
