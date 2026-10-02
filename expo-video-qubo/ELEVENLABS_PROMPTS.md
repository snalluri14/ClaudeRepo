# ElevenLabs prompts: Arohak × Quanfluence AV (112 pilot use case)

Based on `SCRIPT.md` in this folder. About 2 min 53 s, 16:9, 1080p.

## How to use this (read first)

AI video models **cannot reliably draw logos, text or numbers**. They distort them. So build the AV in three layers:

1. **Voice-over:** generate it in ElevenLabs text-to-speech (Part A).
2. **Background clips:** generate one short clip per scene with ElevenLabs video generation (Part B). Every clip prompt says *no text, no logos*.
3. **Logos, text and numbers:** add the **real logo files** and the exact on-screen text as overlays in ElevenLabs Studio's timeline, or in CapCut or Canva (Part C). That's the only way to get logos and numbers exactly right.

For the opening logo scenes, if the video tool offers **image-to-video** (upload a start image), upload the actual logo PNG as the first frame and use the prompt in Part B, scene 0a/0b. Even then, check that the logo isn't altered. If it is, use a plain animated background and overlay the logo file instead.

---

## Part A: Voice-over

### Voice settings / voice design prompt
> Indian English, male, 40s, calm, confident and warm. A senior technology leader presenting to government officials. Clear diction, measured pace (about 130 words per minute), slight gravitas, never salesy. Pause briefly between sentences.

Settings: **Stability** medium-high · **Similarity** high · **Style** low. Generate each scene as its own clip so you can line them up with the video.

### Narration (paste one block per scene)

**0a (0:00):**
Arohak Technologies.

**0b (0:04):**
In partnership with Quanfluence.

**1 (0:08):**
Two fourteen AM. A distress call... a sixty-two-year-old man with chest pain.

**2 (0:16):**
Three decisions, made in seconds. Which ambulance. Which route. And which hospital.

**3 (0:28):**
And the nearest hospital isn't always the right one. A heart patient needs a cardiac centre with a free bed... not a children's hospital.

**4 (0:43):**
Now multiply that by every call, every ambulance and every hospital in the state. The number of possible plans explodes... and the best one changes every minute.

**5 (1:03):**
Step one. Arohak turns every choice into a simple yes-or-no switch. Does ambulance A take call one? Does this patient go to the cardiac centre?

**6 (1:18):**
Step two. We write it as a QUBO: one score, where lower is better. Travel time adds cost. Breaking a rule, like sending a heart patient to a children's hospital, adds a heavy penalty.

**7 (1:33):**
Step three. Fitting the problem to the hardware. We split the state into zones, so each piece fits the machine. This is a big part of the engineering.

**8 (1:48):**
Step four. Quanfluence's Ising machine. Each spin is a pulse of light travelling in a fibre loop. The pulses interact, and settle into their lowest-energy state... and that state is the best plan.

**9 (2:03):**
Step five. The spins become the dispatch plan.

**10 (2:08):**
Tested on real 108 call data: today, help reaches the patient in twenty-two point six minutes on average. With our routing... nine point eight. That's thirteen minutes sooner.

**11 (2:23):**
And into hospital care: forty-seven point five minutes instead of sixty point six, even after we add thirty minutes of buffer to our own numbers.

**12 (2:38):**
We started with ambulances. Next comes a live trial... and then all of 112: police, fire and ambulance, as one.

**13 (2:46):**
Arohak and Quanfluence. Quantum-inspired today. Quantum-ready tomorrow.

*Tip: write numbers out in words ("twenty-two point six"), as above. Text-to-speech then reads them clearly. "QUBO" is pronounced "KEW-boh"; if the voice says it wrong, write it as "Kew-bo".*

---

## Part B: Video clip prompts

### Style line: add this to the start of every clip prompt
> Cinematic 16:9, dark navy background (#081120), glowing cyan (#3DD6F5) and soft gold (#F5B83D) accents, clean minimal motion-graphics style, smooth slow camera movement, high-end tech keynote look, shallow depth of field. **No text, no letters, no numbers, no logos, no watermarks.**

### Scene prompts (with clip length)

**0a · Arohak logo (4 s)**
*If you're using image-to-video, upload the Arohak logo PNG as the start frame:*
> The logo stays perfectly still and unchanged in the centre while a soft horizontal light sweep passes across it. Subtle particles drift in the dark background. Do not alter, redraw or animate the logo itself.

*Without image-to-video:*
> An empty, elegant dark stage with a soft light sweep passing across the centre and gentle particles, leaving clear empty space in the middle for a logo overlay.

**0b · Partnership (4 s)**
> Two soft glowing points of light on the left and right of a dark screen, joined by a thin cyan line that draws across the middle. Calm, premium and symmetrical, with empty space on both sides for logo overlays.

**1 · Distress call (8 s)**
> Night. An overhead view of a dark stylised map of a South Indian state with faint glowing roads. A single red location pin pulses softly. A smartphone screen lights up nearby, vibrating. Tense, quiet mood.

**2 · Three decisions (12 s)**
> Overhead dark map. Around a pulsing red pin, three glowing icons appear one after another: an ambulance, a winding road and a hospital building. Slow push-in.

**3 · Right hospital (15 s)**
> Overhead dark map with two hospital buildings. The closer hospital glows soft red and dims. A farther hospital, marked by a heart symbol, glows green. A cyan path draws from the red pin past the near hospital to the farther green one.

**4 · Complexity (20 s)**
> Slow zoom out over a dark stylised state map. Dozens of red pins, ambulance icons and hospital icons appear, connected by many tangled, flickering lines of light, growing chaotic and dense. Feeling of overwhelming complexity.

**5 · Yes/no switches (15 s)**
> An abstract grid of small glowing toggle switches floating in dark space, rows and columns, each flipping between off (dim) and on (bright cyan) one by one. Clean, mathematical and elegant.

**6 · QUBO cost score (15 s)**
> The glowing switch grid feeds streams of light into a single vertical energy meter. Small glowing rule tiles (a clock, an ambulance, a hospital with a heart, a bed) snap onto the grid. Some connections flash gold when penalised. The meter level drops.

**7 · Fit to hardware (15 s)**
> A dark stylised state map splits into several zones along glowing borders. Each zone lifts up, compresses into a neat cube of light points, and slides smoothly into a sleek glowing slot, like puzzle pieces fitting perfectly.

**8 · Optical Ising machine (15 s)**
> Close-up of a glowing coiled optical fibre loop in darkness. Bright pulses of light travel around the loop. The pulses flicker and interact, then gradually synchronise into a calm, stable rhythmic pattern. Scientific, beautiful and precise. Laser-lab aesthetic.

**9 · Decode to plan (5 s)**
> Points of light fly out of the fibre loop and land on a dark map, forming clean cyan routes from ambulance icons to a patient pin and on to a hospital with a heart symbol. Everything turns calm and green.

**10 · Race (15 s)**
> Split screen, two identical dark maps. On the left, a grey ambulance takes a long winding route. On the right, a cyan ambulance takes a direct route and arrives much earlier; its destination pin turns green. Leave clear space at the top of each half for clock overlays.

**11 · Comparison bars (15 s)**
> Two horizontal bars of light grow from left to right on a dark background. The top grey bar grows longer; the bottom bar, made of cyan and gold segments, stops noticeably shorter. A soft green glow highlights the gap. Clean infographic motion.

**12 · Roadmap (8 s)**
> Three glowing circular nodes connected by a cyan dotted line on a dark background. The first node fills green with a check-mark-like glow; the line travels on to the second (ambulance icon) and the third (three emergency icons together: police car, fire engine, ambulance).

**13 · Closing (7 s)**
> Elegant dark background with slow-drifting cyan and gold light particles and a soft central glow, with clear empty space for two logos side by side and a tagline below.

---

## Part C: Overlays to add in the editor (exact text)

| Scene | Overlay |
|---|---|
| 0a | **Arohak Technologies logo (real file)**, centred · *Arohak Technologies Pvt Ltd* |
| 0b | Arohak logo (left) · **Quanfluence logo (right)** · **in partnership with Quanfluence** · *Quantum-inspired optimisation on an optical Ising machine* |
| All scenes 1–12 | Small co-brand tag, top-left: Arohak logo × Quanfluence logo |
| 1 | **2:14 AM. A distress call.** · *Chest pain. 62-year-old man.* |
| 2 | **Which ambulance? Which route? Which hospital?** |
| 3 | **The nearest hospital is not always the right hospital.** |
| 4 | **Many calls × many ambulances × many hospitals** |
| 5 | **① Every decision becomes a yes/no switch** |
| 6 | **② QUBO: one cost score. Lower = better.** · *A wrong hospital costs heavily* |
| 7 | **③ Split by zone so each piece fits the machine** |
| 8 | **④ Quanfluence Ising machine: each spin is a pulse of light in a fibre loop** |
| 9 | **⑤ Spins → dispatch plan** · *Right ambulance · fastest route · right hospital* |
| 10 | Left: **Current 108 · LIVE DATA · 22.6 min** · Right: **Ising-machine routing · SIMULATED · 9.8 min** · badge **13 min sooner (−57%)** |
| 11 | **Call → hospital care: 60.6 vs 47.5 min** · badge **13 min sooner (−22%)** · *with 30 min of buffer added to our side only* |
| 12 | ✓ **Simulation on 108 data** → **Live 108 trial** → **112** · **Ambulance today. All of 112 next.** |
| 13 | **Both real logos**, side by side · **Arohak Technologies × Quanfluence** · *Quantum-inspired today. Quantum-ready tomorrow.* |
| 10–11 footnote | *Current 108: live data, average minutes per call. Ising-machine routing: simulation on the same 108 calls, with 15 min at the scene and 15 min hospital handover added to the simulated side only. Not yet deployed live.* |

**Final checks before 3 October**
- Numbers must match exactly: 22.6 / 9.8 / 60.6 / 47.5 / −57% / −22%.
- Results screens must keep the labels "LIVE DATA" and "SIMULATED", and the footnote.
- Confirm hospital-specialty matching was part of the simulation. If it wasn't, change scenes 3, 6 and 9 to say *"the model can include…"*.
- Get Quanfluence's approval for its logo and for the scene 8 wording.
