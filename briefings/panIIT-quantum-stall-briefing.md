# Arohak @ Pan IIT Summit, Vijayawada: Quantum Stall Briefing
**For:** VP – Technology, Arohak
**Purpose:** Talk confidently and credibly about quantum with IIT alumni, industry visitors and the Hon'ble Chief Minister.

---

## 0. Read this first: how to come across as credible (not just impressive)

Many visitors at a Pan IIT stall will be engineers and PhDs. Some will know more physics than you. The people who look foolish at these events are the ones who **overclaim**. The ones who look senior can say clearly what quantum can do today, what it can't, and how they make it work in production. Your integration background is your edge here, so lean on it.

**Five rules:**
1. **Say "hybrid quantum-classical," not just "quantum."** Every real deployment today is hybrid. Saying this marks you as someone who has actually shipped.
2. **Don't say "quantum solves what classical can't" as an absolute.** Say: *"For these combinatorial problems, classical methods slow down sharply as the problem grows. Quantum and quantum-inspired methods let us search that space differently, and they put us on the path to real advantage as hardware matures."*
3. **Speak from your own lane:** architecture, integration, data pipelines, APIs, production readiness. Hand off deep physics to the team: *"Our quantum algorithms lead can go deeper on the circuit design. Let me introduce you."* (Have that person at the stall, or at least have their card.)
4. **Use only real numbers.** Get the actual pilot metrics from the delivery team before the summit (see the placeholders `[CONFIRM]` below). Never improvise a figure.
5. **Name a client only if Arohak actually did the work and you're allowed to say so.** See the note in Section 6.

---

## 1. Quantum in 5 minutes, explained through your own world

| Quantum concept | What it means | Analogy you already know |
|---|---|---|
| **Qubit** | Basic unit. Unlike a bit (0 or 1), it can be in a *superposition* of 0 and 1 until it is measured. | A message in flight that hasn't been routed yet. It can still go to many endpoints. |
| **Superposition** | n qubits represent 2ⁿ states at once. 50 qubits ≈ 10¹⁵ states. | Evaluating many branches of a decision flow together instead of one at a time. |
| **Entanglement** | Qubits become correlated, so measuring one tells you about the other. | Tightly coupled transactions: change one, the other is determined. |
| **Interference** | Algorithms amplify good answers and cancel bad ones. **This is where the power comes from**, not "trying everything in parallel." | A scoring or ranking engine that boosts good matches and suppresses noise. |
| **Measurement** | Reading qubits collapses them to one classical answer, so you run the circuit many times ("shots") and read the distribution. | Sampling. You get a probability distribution, not one deterministic return value. |
| **Decoherence / noise** | Qubits lose their quantum state quickly because of heat, vibration and stray signals. This is the main engineering challenge. | Message loss and timeouts. You need retries and error handling. |
| **Error correction / logical qubits** | Many noisy *physical* qubits are combined into one reliable *logical* qubit. | RAID or redundancy for reliability. |
| **NISQ era** | "Noisy Intermediate-Scale Quantum": where we are today, with roughly 100 to 1,000+ noisy qubits. | Early cloud. Useful in specific patterns, not a full replacement. |

**Key line to remember:**
> "A quantum computer isn't a faster classical computer. It's a different kind of processor, closer to a GPU-style accelerator, that we call for specific problem types inside a classical workflow."

### The main families of quantum use
1. **Optimization:** routing, scheduling, allocation, portfolio. *(This is where Arohak plays.)*
2. **Simulation:** molecules and materials, for drug discovery, batteries and fertilizers.
3. **Machine learning:** quantum kernels and feature maps; still early.
4. **Cryptography:** Shor's algorithm could break RSA/ECC on a future large fault-tolerant machine. This drives **Post-Quantum Cryptography (PQC)** migration now.
5. **Sensing and communication:** quantum sensors, QKD (Quantum Key Distribution).

### Hardware types (useful name-drops)
- **Superconducting:** IBM (Heron processors, Qiskit SDK), Google (Willow chip, 2024 error-correction milestone).
- **Trapped ion:** IonQ, Quantinuum. Higher fidelity, slower gates.
- **Neutral atom:** QuEra, Pasqal. Scaling quickly.
- **Photonic:** PsiQuantum, Xanadu.
- **Quantum annealing:** D-Wave. Built specifically for optimization (QUBO problems).

---

## 2. Vocabulary cheat sheet (use naturally, a couple per conversation)

- **QUBO:** *Quadratic Unconstrained Binary Optimization.* The standard way to turn a business optimization problem into something a quantum machine can solve. **Learn this one; it ties both use cases together.**
- **QAOA:** *Quantum Approximate Optimization Algorithm.* A gate-based algorithm for optimization problems.
- **VQE:** *Variational Quantum Eigensolver.* Used for chemistry and molecule simulation.
- **Quantum annealing:** The system "settles" into a low-energy state that represents a good solution.
- **Quantum-inspired algorithms:** Classical algorithms (e.g., simulated bifurcation, tensor networks) that borrow ideas from quantum. They run on GPUs today.
- **Hybrid solver:** Classical pre/post-processing plus a quantum core.
- **Circuit depth, gate fidelity, coherence time:** Hardware quality measures.
- **Quantum advantage:** Doing something useful better, faster or cheaper than the best classical method. *Be careful: proven advantage on real business problems is still emerging.*
- **PQC:** NIST published the first post-quantum standards in Aug 2024: ML-KEM (FIPS 203), ML-DSA (FIPS 204), SLH-DSA (FIPS 205).
- **"Harvest now, decrypt later":** Adversaries store encrypted data today and decrypt it once quantum machines are ready. This is why government data needs PQC planning now.

---

## 3. Why classical computers struggle: the combinatorial explosion

This is your core argument. Memorize the numbers.

| Problem size | Possible combinations | Comment |
|---|---|---|
| Route 10 stops | 10! ≈ 3.6 million | Trivial for a laptop |
| Route 20 stops | 20! ≈ 2.4 × 10¹⁸ | Brute force takes years |
| Route 30 stops | 30! ≈ 2.7 × 10³² | More than the age of the universe in nanoseconds |
| Assign 50 vehicles to 50 incidents, with constraints | 50! ≈ 3 × 10⁶⁴ | Close to the number of atoms in the Milky Way (~10⁶⁷–10⁶⁸) |

**How to say it:**
> "These are NP-hard problems. Every vehicle, incident or SKU you add multiplies the possibilities. Classical solvers handle this with heuristics: shortcuts that give 'good enough' answers. But in a real-time system you have seconds, not hours. As the problem grows, classical solution quality drops or response time rises. Quantum and hybrid approaches search that space differently, using superposition and interference, so we can find high-quality solutions within the time window. And the architecture we've built gets better automatically as the hardware scales."

**If an expert pushes back** ("Gurobi/OR-Tools can solve that"):
> "Absolutely. For many instances, a well-tuned classical solver is excellent, and we benchmark against one every time. That's our discipline: the quantum path goes into production only where it matches or beats the classical baseline on quality-in-time. Where it doesn't yet, the classical solver serves the request. Because it's hybrid, the client always gets the best answer available."

*(This answer shows maturity. IIT experts will respect it.)*

---

## 4. Use Case 1: AP Government Dial 112 Emergency Response (Pilot)

> ⚠️ Fill every `[CONFIRM]` with real figures from the delivery team before the summit. Adjust the problem framing below if the pilot focused on something different (e.g., patrol planning vs. live dispatch).

### The problem (in plain words)
Dial 112 is the single emergency number for police, fire and ambulance. At any moment, the control room has:
- many **incoming incidents** with different severity, location and type,
- many **response vehicles** (police patrol, ambulances, fire) with different locations, capabilities and availability,
- **constraints:** traffic, road network, jurisdiction boundaries, shift timings, vehicle type matching, hospital capacity.

**The question:** *Which vehicle goes to which incident, by which route, and where should idle vehicles be pre-positioned so the next call is answered fastest?*

### Why it's hard for classical computing
- It's a **dynamic vehicle routing plus assignment problem**, a well-known NP-hard class.
- It changes **every few seconds** (new calls, vehicles moving, traffic).
- Rule-based dispatch ("nearest free vehicle") is fast but **locally greedy**. Sending the nearest vehicle now can leave a whole zone uncovered for the next critical call.
- Optimizing **globally** (all vehicles, all incidents, plus future coverage) blows up combinatorially. Classical exact solvers can't finish in a dispatch-time window at state scale.

### How we solved it (your talk track)
1. **Data integration layer (your strength):** Real-time feeds from the 112 CAD/call-centre system, vehicle GPS/AVL, maps and traffic, historical incident data, all brought together through an integration/API layer. *"Most of the hard work in quantum projects is actually this layer. Quantum is only as good as the data you feed it."*
2. **Problem formulation:** We encoded assignment, routing and coverage as a **QUBO**: binary variables like "vehicle *i* assigned to incident *j*," with penalties for constraint violations (wrong vehicle type, out of jurisdiction, exceeding response-time SLA) and objectives (minimize response time, maximize zone coverage, prioritize severity).
3. **Decomposition:** We split the state into zones/clusters classically, so each sub-problem fits the size today's quantum hardware handles well.
4. **Hybrid solve:** We send sub-problems to a quantum/hybrid solver `[CONFIRM: platform, e.g., D-Wave hybrid / IBM Qiskit QAOA / quantum-inspired GPU solver]`, with a **classical solver running in parallel as baseline and fallback**.
5. **Decision and feedback:** The best solution goes to the dispatcher's screen as a **recommendation** (a human stays in the loop), and outcomes feed back to improve forecasting.

### Results to quote: `[CONFIRM ALL]`
- Average response time reduced by **[X]%** / **[X] minutes** in pilot zones
- Coverage, meaning the share of the area reachable within the SLA: **[X]%** improvement
- Scale: **[N] vehicles, [N] incidents/day, [districts]**
- Solve time: **[X] seconds** per optimization cycle

### One-liner
> "In emergency response, every minute matters. The nearest-vehicle rule is greedy. We optimize the whole fleet together, including where the *next* emergency is likely to come from. That's a combinatorial problem that fits quantum optimization very well."

---

## 5. Use Case 2: Consumer Health / Pharma Supply Chain Optimization

**Problem domain:** Large consumer-health and pharma companies (the J&J / Kenvue type: brands across OTC medicines, skin care, oral care) run **thousands of SKUs across many plants, warehouses and distributors** in many countries.

### The problem
**Production scheduling and distribution network optimization.** Specifically:
- Which plant makes which SKU, on which line, in which sequence (changeovers are costly, especially with pharma cleaning/validation rules)?
- How much inventory to place at which distribution centre, and which route to ship it by?
- Constraints: shelf-life/expiry, batch sizes, regulatory (GMP) rules, cold chain for some products, demand variability, promotions.

### Why classical struggles
- **Production line sequencing** is a scheduling problem. With 40 SKUs on one line, 40! ≈ 8 × 10⁴⁷ possible sequences, times multiple lines and plants.
- Planning tools (e.g., SAP IBP/APO-type systems) use heuristics plus MILP solvers that often **run overnight** and still return compromise plans. When demand shifts mid-week, re-planning is slow.

### How it was solved (talk track)
1. **Integration:** Pulled master data, demand forecasts, capacity and BOMs from **SAP S/4HANA / IBP via SAP BTP Integration Suite** *(your home turf: talk confidently here)*.
2. **Formulation:** Changeover sequencing plus inventory placement as a **QUBO / constrained optimization**.
3. **Hybrid solve:** Quantum/quantum-inspired solver for the hard combinatorial core (sequencing); classical solver for the linear parts (quantities, flows).
4. **Write-back:** Optimized schedule pushed back to SAP as a planning proposal for the planner to approve.
5. **Results:** `[CONFIRM or describe as target outcomes]`, for example changeover time reduction, inventory holding cost reduction, faster re-planning (overnight down to minutes).

### Alternative angle (if a pharma R&D person asks)
**Molecular simulation** for formulation/drug discovery using **VQE**: simulating molecules is natively quantum, so classical computers need exponential resources to simulate them exactly. *Feynman: "Nature isn't classical… if you want to make a simulation of nature, you'd better make it quantum mechanical."* Say this is the **long-term** value. Optimization is the **near-term** value.

---

## 6. ⚠️ Important: how to talk about the J&J / Kenvue use case

Claiming J&J or Kenvue as a client when Arohak didn't do that work could cause serious harm: a CM-level audience, IIT alumni who may *work at* J&J/Kenvue, and real legal and reputational risk. Also, many client contracts forbid naming the client even when the work is real.

**Pick the line that matches what's true:**
- **If Arohak delivered it and has permission to name them:** name them.
- **If Arohak delivered it but can't name them:** *"a global consumer-health major"* or *"a Fortune 500 pharma and consumer-health client."* This is standard practice and sounds *more* senior.
- **If it was an internal PoC / demo on representative data:** *"We've built a proof-of-concept for consumer-health supply chains, modelled on a large global CPG/pharma network, and we're in conversations to pilot it."*
- **If it's a pitch, not yet built:** *"This is the next use case we're taking to market."*

In every case the technical talk track in Section 5 stays the same. Only the claim about *who* changes.

---

## 7. Your differentiator: "Quantum-ready integration"

This is where you shine. Use it to steer any conversation back to your strength.

> "Everyone talks about qubits. Very few talk about how a quantum solver actually plugs into an enterprise. A quantum computer has no idea what an SAP order or a 112 incident is. Someone has to extract the data, formulate the problem, call the quantum service, handle failures, fall back to classical, and write the result back into the business system. That's what we do. We're the bridge between quantum hardware and real business systems."

**Architecture you can sketch on a napkin:**
```
[Source systems: SAP / 112 CAD / GPS / IoT]
        │  (webMethods / SAP BTP Integration Suite / APIs / events)
        ▼
[Data prep & problem formulation → QUBO]
        ▼
[Hybrid orchestrator] ──► Quantum cloud (IBM Quantum / AWS Braket / Azure Quantum / D-Wave Leap)
        │           └──► Classical solver (baseline + fallback)
        ▼
[Best-solution selection + explainability]
        ▼
[Write back to business system / dispatcher dashboard]
```

Key phrases: *"Quantum as a service through APIs," "solver-agnostic orchestration: we aren't locked to one hardware vendor," "classical fallback for reliability," "same integration patterns we've used for 15+ years, with a new kind of endpoint."* (Adjust years to your actual experience.)

---

## 8. Context for the Chief Minister and the AP Government

Use these to connect Arohak to the state's vision. *Verify the latest status before the summit; these were announced in 2025 and may have progressed.*
- **Amaravati Quantum Valley:** AP's flagship initiative to make Amaravati a quantum computing hub, announced with **IBM** (IBM Quantum System Two with a 156-qubit Heron processor), **TCS** and **L&T**. It is pitched as one of India's largest quantum computing installations.
- **National Quantum Mission (NQM):** Approved April 2023, **₹6,003.65 crore**, 2023-24 to 2030-31. The goal is intermediate-scale quantum computers (**50–1,000 physical qubits**) within 8 years. Four thematic hubs: **IISc Bengaluru** (computing), **IIT Madras** (communication), **IIT Bombay** (sensing and metrology), **IIT Delhi** (materials and devices).
- **The CM's track record:** Hyderabad's HITEC City and IT growth in the 1990s. The natural pitch is *"Quantum is to this decade what IT was to the 90s, and Andhra Pradesh is again moving first."*

### 60-second pitch for the CM
> "Sir, Arohak is an Andhra Pradesh technology company working on practical quantum applications. We've already run a pilot with the AP Government on **Dial 112**, using hybrid quantum optimization to dispatch and position emergency vehicles more effectively so citizens get help faster. `[one CONFIRMED result]`.
> Our strength is making quantum *usable*: connecting quantum computers to real government and enterprise systems. As Quantum Valley comes up in Amaravati, we want to be the company that turns that hardware into real outcomes for AP citizens: emergency services, agriculture supply chains, power grid balancing, traffic. We'd welcome the opportunity to scale the 112 pilot statewide and to be a delivery partner for Quantum Valley use cases."

**Keep it short.** Mention one result, one ask, one forward-looking line. Have a one-page leave-behind ready.

### Other AP-relevant use cases to mention if asked "What next?"
- **Agriculture / Rythu Bharosa supply chain:** crop procurement logistics, cold storage placement, PDS distribution routing.
- **Power grid (APTRANSCO/DISCOMs):** unit commitment and renewable (solar/wind) balancing, a classic optimization problem.
- **Traffic signal optimization** for Vijayawada / Visakhapatnam / Amaravati.
- **Disaster response** (cyclones, Krishna/Godavari floods): evacuation routing and relief allocation.
- **Health:** ambulance pre-positioning (extension of 112), hospital bed allocation.
- **Post-Quantum Cryptography readiness** for government data (land records, Aadhaar-linked systems, RTGS).

---

## 9. Anticipated questions and suggested answers

### A. Technical questions (IIT alumni, engineers, researchers)

**Q1. Did you run on actual quantum hardware or a simulator?**
`[CONFIRM the truth.]` Template: *"We used [hardware/hybrid service] for the quantum core, with simulators for development and testing. For production-like runs we use a hybrid solver, so the quantum processor handles the hardest combinatorial core and classical handles the rest."*

**Q2. How many qubits did you use?**
`[CONFIRM.]` *"Each decomposed sub-problem used about [N] variables/qubits. We deliberately decompose the state-level problem into zone-level sub-problems that fit current hardware well. Fitting the problem to the hardware is a big part of the engineering."*

**Q3. Did you actually achieve quantum advantage?**
*Be honest. This is a test.* *"Not in the strict academic sense; nobody has proven that for a real-world routing problem yet. What we showed is that the hybrid approach produces solutions [comparable to / better than] our classical baseline within the dispatch time window on our pilot instances. And the architecture is ready to benefit as hardware improves. We're building capability ahead of the curve, not claiming a miracle."*

**Q4. Isn't this just simulated annealing / a classical heuristic with a quantum label?**
*"Fair challenge. We always benchmark against classical heuristics, including simulated annealing and MILP solvers, and we only route to the quantum path where it earns its place. Part of our stack is quantum-inspired, and we're transparent about which part is which."*

**Q5. Gate-based or annealing? Why?**
*"For optimization in the near term, annealing and hybrid solvers are more mature at useful problem sizes. We also prototype with QAOA on gate-based systems because that's where long-term advantage lies, especially with error correction coming. Our orchestration layer is solver-agnostic."* (Adjust to what you actually used.)

**Q6. How do you handle noise/errors?**
*"Three ways: problem decomposition to keep circuits shallow, multiple shots with best-of-sample selection, and always validating the solution classically against constraints before it reaches a dispatcher. Nothing reaches an operator unless it passes classical feasibility checks."*

**Q7. How do you encode constraints in a QUBO?**
*"As penalty terms. If a constraint is violated, the energy (cost) goes up. Tuning the penalty weights is one of the trickier parts: too low and you get infeasible answers, too high and the solver ignores the actual objective."* (This answer will impress people who know the field.)

**Q8. What's the latency? Real-time dispatch needs seconds.**
`[CONFIRM.]` *"Each optimization cycle runs in about [X] seconds end-to-end, including the cloud round-trip. For truly instant decisions, the system uses the latest optimized plan plus a fast rule, and the optimizer re-plans continuously in the background."*

**Q9. Where is the data hosted? Is government data sent to foreign quantum clouds?**
*"Very important question. Only anonymized mathematical problem representations (the QUBO matrices, just numbers) go to the solver. No personal or citizen data leaves the government environment. The data integration and formulation run within [state data centre / approved cloud]. And as domestic quantum infrastructure comes up in Amaravati, we can move to it."*

**Q10. What about Shor's algorithm and encryption?**
*"Shor's algorithm could break RSA and ECC on a large, fault-tolerant quantum computer. That's still some years away, but 'harvest now, decrypt later' means sensitive data should move to post-quantum cryptography now. NIST standardized ML-KEM and ML-DSA in 2024. We help organizations take crypto inventory and plan PQC migration, which is fundamentally an integration and architecture exercise."*

**Q11. What's your team's quantum background?**
`[CONFIRM.]` *"Our quantum team includes [physicists / PhDs / Qiskit-certified engineers / partnerships with X institution]. I lead technology and architecture, making it work end-to-end in production."*

**Q12. Which SDKs/tools?**
`[CONFIRM.]` Common ones: **Qiskit** (IBM), **Cirq** (Google), **PennyLane** (Xanadu), **D-Wave Ocean**, **Amazon Braket**, **Azure Quantum**, **CUDA-Q** (NVIDIA).

### B. Business and strategic questions

**Q13. Why should a company invest in quantum now if advantage isn't proven?**
*"Three reasons: (1) The problem formulation, data pipelines and integration you build now carry over directly when hardware matures. (2) Quantum-inspired algorithms give value today on classical hardware. (3) Talent and know-how take years to build. The companies that start learning now will lead later. Pilots are low-cost; falling behind is high-cost."*

**Q14. What's the ROI?**
*"In the 112 pilot, the value is measured in response minutes saved, which means lives. In supply chain, it's changeover time, inventory cost and re-planning speed. We always start with a classical baseline, so ROI is measured against what you'd get anyway."*

**Q15. How long does a pilot take, and what does it cost?**
`[CONFIRM Arohak's commercial model.]` Typical framing: *"A focused pilot is usually [8–12 weeks]: problem discovery, formulation, hybrid solver, benchmark against classical, then a go/no-go on scale-up."*

**Q16. Who are your partners?**
`[CONFIRM: IBM / AWS / Microsoft / D-Wave / academic partners.]`

**Q17. How are you different from TCS, Infosys or big quantum startups?**
*"We're focused and practical: problem-first, not hardware-first. And our integration depth (SAP, webMethods, enterprise and government systems) means our quantum solutions actually go live inside real workflows instead of staying as research demos."*

### C. Questions the CM or officials may ask

**Q18. How will this help the common citizen?**
*"Faster ambulance and police response through 112. Better crop logistics for farmers so less produce is wasted. Stable power supply with more solar. Quantum is the engine underneath; the citizen sees faster service."*

**Q19. Can you scale the 112 pilot across the state?**
*"Yes. The architecture was designed for that. Scaling means integrating all districts' feeds and running zone-level optimization in parallel. We can propose a phased rollout: [N] districts in phase 1."*

**Q20. How can Arohak contribute to Amaravati Quantum Valley?**
*"Three ways: use-case delivery for government departments, integration of the quantum platform with state systems, and skilling. We'd be happy to run training programs with local engineering colleges so AP builds quantum-ready talent."*

**Q21. How many jobs / what skilling?**
`[CONFIRM Arohak's headcount and plans.]` Have a number ready.

### D. Curveballs

**Q22. Explain quantum computing to me like I'm a school student.**
*"A normal computer solves a maze by trying one path at a time. A quantum computer works more like a wave that spreads through all paths together. The wrong paths cancel out and the right path gets stronger. So for certain puzzles, it finds good answers much faster."*

**Q23. Are you a quantum physicist?**
*"No, and that's on purpose. I'm a technology and integration architect. Quantum value will come from people who can connect it to real systems, and that's my job. Our quantum scientists handle the physics. Let me introduce you to [name]."* (Confident, honest, and turns it into a strength.)

**Q24. What's the biggest limitation of quantum today?**
*"Noise and scale. Today's qubits are error-prone, and we need error correction, meaning many physical qubits per logical qubit. Google, IBM and others are making real progress (Google's Willow chip in 2024 showed errors decreasing as they scaled up), but large fault-tolerant machines are still some years out. That's exactly why hybrid is the right strategy today."*

**Q25. When will quantum computers be mainstream?**
*"Nobody knows exactly. IBM and others have roadmaps to fault-tolerant systems around the end of this decade. But useful hybrid applications are happening now, in optimization especially. It won't be one big switch-on moment; it'll be a gradual rise in which problems are worth sending to a quantum processor."*

**When you don't know the answer, say:**
> "That's a great question, and I don't want to give you a half answer. Let me connect you with our quantum lead, or share your card and we'll follow up in detail."

This is a *senior* response. Juniors bluff; VPs route.

---

## 10. Phrases to use and to avoid

| ✅ Use | ❌ Avoid |
|---|---|
| "hybrid quantum-classical" | "our quantum computer" (unless you own one) |
| "NP-hard / combinatorial explosion" | "quantum solves everything" |
| "we benchmark against classical baselines" | "classical computers can't do this at all" |
| "QUBO formulation" | "infinite parallel computing" |
| "solver-agnostic, classical fallback" | "quantum is 1 million times faster" (only with a specific, true citation) |
| "quantum-ready architecture" | specific numbers you can't back up |
| "near-term value in optimization, long-term in simulation" | naming clients you're not allowed to name |

---

## 11. Pre-summit checklist

- [ ] Get **real 112 pilot metrics** from the delivery team and fill all `[CONFIRM]` placeholders
- [ ] Confirm **exactly which solver/hardware** was used, and the qubit/variable counts
- [ ] Confirm the **true status** of the second use case and whether the client can be named (Section 6)
- [ ] Have the **quantum technical lead** at the stall, or available on call
- [ ] Prepare a **one-page leave-behind** for the CM and officials (pilot, results, ask)
- [ ] Prepare a **simple visual** for the stall screen: before/after map of vehicle coverage
- [ ] Check the **latest updates** on Amaravati Quantum Valley and NQM (news from the last 3 months)
- [ ] Practise the **60-second CM pitch** out loud 10 times
- [ ] Practise **Q3 (quantum advantage)** and **Q23 (are you a physicist)**; these are the trust tests

---

## 12. Pocket cheat card (print this)

```
WHAT:  Hybrid quantum-classical optimization, integrated into real systems
WHY:   NP-hard problems → combinatorial explosion (30 stops = 10^32 routes)
       Classical heuristics slow down / lose quality at real-time scale
HOW:   Integrate data → formulate QUBO → decompose → hybrid solve
       (quantum + classical baseline/fallback) → validate → write back
112:   Fleet-wide dispatch + pre-positioning, not "nearest vehicle"
       Result: [CONFIRM]% faster response, [CONFIRM]% better coverage
CPG:   SKU sequencing + inventory placement via SAP BTP integration
       Overnight planning → minutes re-planning [CONFIRM]
EDGE:  "We make quantum usable: the bridge between qubits and business systems"
HONEST:"No one has proven full quantum advantage on real routing yet;
        we benchmark every time and are ready as hardware scales"
TERMS: Qubit · Superposition · Entanglement · Interference · QUBO · QAOA
       VQE · Annealing · NISQ · Logical qubit · PQC (ML-KEM) · Hybrid
AP:    Amaravati Quantum Valley (IBM System Two, TCS, L&T)
INDIA: National Quantum Mission ₹6,003 cr, 2023–31, 50–1000 qubits
DON'T KNOW? → "Let me connect you with our quantum lead."
```
