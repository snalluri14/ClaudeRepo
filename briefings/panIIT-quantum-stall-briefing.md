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
- **Coherent Ising Machines (CIM), photonic:** NTT/Stanford pioneered them; **Quanfluence** (Bengaluru, IIT Madras-incubated) builds them in India. Also built specifically for optimization (Ising/QUBO problems), and they run at **room temperature**. *This is what Arohak used for 112. See Section 4A.*

---

## 2. Vocabulary cheat sheet (use naturally, a couple per conversation)

- **QUBO:** *Quadratic Unconstrained Binary Optimization.* The standard way to turn a business optimization problem into something a quantum machine can solve. **Learn this one; it ties both use cases together.**
- **Ising model / Ising machine:** A physics model of spins (±1) that settle into the lowest-energy arrangement. An Ising machine is hardware that finds that arrangement physically. Mathematically equivalent to QUBO. **Your 112 pilot ran on one.**
- **Coherent Ising Machine (CIM):** A photonic Ising machine where laser pulses in a fibre loop act as spins.
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

> ✅ **Confirmed:** The 112 work is a **pilot** (not yet a statewide production rollout), and the optimization was formulated as a **QUBO**.
> ⚠️ Still fill the remaining `[CONFIRM]` items (results, solver platform, scale) with real figures from the delivery team.

### How to talk about pilot status (say this confidently, not apologetically)
Calling it a pilot makes you *more* credible. Experts know quantum optimization is at the pilot stage everywhere in the world, so "we're in production statewide" would make them suspicious.
- ✅ *"We completed a pilot with AP Government on Dial 112."*
- ✅ *"The pilot validated the QUBO formulation and the hybrid approach on real 112 data. The next step is a phased scale-up."*
- ✅ *"It's a pilot today. We designed the architecture from day one so it can scale statewide."*
- ❌ Don't say "deployed across AP," "live in production," or "112 now runs on quantum."
- `[CONFIRM]` the pilot mode: **historical/replay data**, **shadow mode** (running alongside dispatchers without controlling dispatch), or **live recommendations in selected zones**. Use only the one that's true.

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
2. **Problem formulation (QUBO, confirmed):** We encoded assignment, routing and coverage as a **QUBO** (Quadratic Unconstrained Binary Optimization): binary variables like "vehicle *i* assigned to incident *j*," with penalties for constraint violations (wrong vehicle type, out of jurisdiction, exceeding response-time SLA) and objectives (minimize response time, maximize zone coverage, prioritize severity).
3. **Decomposition:** We split the state into zones/clusters classically, so each sub-problem fits the size today's quantum hardware handles well.
4. **Solve on the Quanfluence Ising machine:** We converted each zone-level QUBO into Ising form and ran it on **Quanfluence's photonic Coherent Ising Machine**, with a **classical solver running in parallel as baseline and fallback**.
5. **Validation and comparison:** In the pilot, every QUBO solution was checked classically for feasibility and compared with current dispatch outcomes and a classical baseline. In a scaled rollout, the best solution would go to the dispatcher's screen as a **recommendation** (a human always stays in the loop). `[CONFIRM: whether pilot recommendations were shown to dispatchers or evaluated offline.]`

### Explaining the QUBO in simple terms (you *will* be asked)
> "QUBO means we express the whole problem as yes/no decisions. For example: *does vehicle 7 go to incident 23? yes or no.* Each yes/no is a binary variable, which maps naturally to a qubit. Then we write one cost equation. Response time adds cost, and breaking a rule (wrong vehicle type, outside jurisdiction, two vehicles on one incident, one vehicle on two incidents) adds a large penalty. The solver's job is to find the combination of yes/no answers with the lowest total cost. A quantum annealer does this physically: the system naturally settles into its lowest-energy state, and that state is our best dispatch plan."

**The formula, if someone technical asks:** minimize **xᵀQx**, where **x** is a vector of 0/1 decisions and **Q** is a matrix. The diagonal holds individual costs (e.g., travel time for vehicle *i* to incident *j*). The off-diagonal holds pairwise interactions (e.g., penalties when two decisions conflict).

**Example constraint as a penalty:** "Each incident gets exactly one vehicle" becomes **P·(Σᵢ xᵢⱼ − 1)²**. This is zero when exactly one vehicle is assigned and positive otherwise. **P** is the penalty weight.

**QUBO → Ising (why the Ising machine can run it):** QUBO uses 0/1 variables (x). The Ising model uses spins of −1/+1 (s). They're mathematically equivalent through **x = (1 + s) / 2**. So our QUBO becomes an Ising problem: *find the spin arrangement with the lowest energy.* That's exactly what an Ising machine is built to do.

**Why QUBO is the right fit:** It's the native input format for quantum annealers (D-Wave) and maps directly onto the Ising model. It's also the standard input for QAOA on gate-based machines and for quantum-inspired solvers. *"QUBO keeps us hardware-agnostic: the same formulation can run on an annealer, a gate-based machine, or a classical/quantum-inspired solver for benchmarking."*

### Pilot results to quote: `[CONFIRM ALL]` (always say "in the pilot")
- Average response time reduced by **[X]%** / **[X] minutes** in pilot zones
- Coverage, meaning the share of the area reachable within the SLA: **[X]%** improvement
- Scale: **[N] vehicles, [N] incidents/day, [districts]**
- Solve time: **[X] seconds** per optimization cycle

### One-liner
> "In emergency response, every minute matters. The nearest-vehicle rule is greedy. We optimize the whole fleet together, including where the *next* emergency is likely to come from. That's a combinatorial problem that fits quantum optimization very well."

---

## 4A. The hardware: Quanfluence Coherent Ising Machine (CIM)

> Source: public information about Quanfluence (news coverage of its 2024 seed round led by pi Ventures, plus the company's own material). `[CONFIRM]` the exact machine version and spin count Arohak used with Quanfluence, and whether you're allowed to name them as a partner (you probably are, since it's a joint Indian success story, but check).

### Quick facts about Quanfluence
- **Bengaluru-based** quantum/photonics startup, founded in **2021**.
- **Incubated at IIT Madras.** Co-founder **Prof. Anil Prabhakar (IIT Madras, Electrical Engineering)** researched the optical Ising machine that became their core product. *This is a great point at a Pan IIT summit: "IIT-born hardware, applied to an AP Government problem."*
- Other co-founders include Sujoy Chakravarty, Ravi Mehta and Biman Chattopadhyay (long semiconductor/chip-design careers, including at Texas Instruments), plus Aditi Vaidya and Sandeep Goyal.
- Raised about **$2M seed (Dec 2024), led by pi Ventures.**
- Their optical Ising machine publicly handled about **128 fully interconnected variables (spins)**, with a much larger next-generation version announced. `[CONFIRM the size of the machine you used.]`
- **Runs at room temperature,** using **telecom-grade optical components.** No dilution refrigerator, unlike superconducting machines (IBM, Google) that need about −273 °C.

### How a Coherent Ising Machine works (your 30-second explanation)
> "Instead of qubits on a chip, it uses **pulses of laser light travelling in a fibre loop**. Each pulse represents one variable: a 'spin' that settles into one of two phase states, which we read as +1 or −1 (0 or 1 in our QUBO). The pulses are coupled to each other according to our problem matrix. As the system is pumped, the light pulses collectively settle into the **lowest-energy arrangement**, and that arrangement is the solution to our optimization problem. Physics does the searching, instead of a CPU trying combinations one by one."

**A bit deeper (for photonics/EE alumni):**
- **Time-multiplexed:** One fibre loop carries many pulses one after another. Each pulse is one spin.
- **Bistable states:** Each pulse settles into one of two phases (0 or π). In Quanfluence's design, a biased **Mach-Zehnder Modulator** creates the bistability.
- **Measurement-feedback coupling:** Each pulse's state is measured, and an **FPGA** computes the coupling (from the Ising/QUBO matrix J) and feeds it back into the loop on the next round trip. That's how you get **all-to-all connectivity**, a big advantage over chips where qubits connect only to their neighbours.
- **Bifurcation:** As gain increases past a threshold, the system "chooses" a low-energy configuration of the whole network at once.

### Why this choice is a strength (use these)
1. **Purpose-built for optimization.** 112 dispatch is an optimization problem, and an Ising machine is built for exactly that. *"We used the right tool for the problem, not the most famous tool."*
2. **All-to-all connectivity.** Every variable can interact with every other, so dense dispatch problems map without the heavy embedding overhead that many qubit chips need.
3. **Room temperature, compact, lower cost.** Realistic for deployment in a government data centre.
4. **Made in India, IIT-incubated.** Data sovereignty and self-reliance (Atmanirbhar Bharat), well aligned with the National Quantum Mission and AP's Quantum Valley vision. *Strong point for the CM.*
5. **Fast.** Ising machines find good solutions in milliseconds per run, so you can run many times and keep the best one.

### ⚠️ The honesty point: "Is a CIM a real quantum computer?"
Someone at an IIT summit **will** ask this. Know the nuance:
- A CIM is **not a gate-based, universal quantum computer** like IBM's or Google's. It can't run Shor's or Grover's algorithm. It's a **special-purpose physical (analog) optimizer**, like an annealer.
- Researchers **debate** how much the result depends on quantum effects. Measurement-feedback CIMs are often described as **"quantum-inspired" or "physics-based" photonic Ising machines.** Quanfluence describes its work as quantum and quantum-inspired photonic computing.
- **Your safe vocabulary:** say **"photonic Coherent Ising Machine"** or **"physics-based quantum-optical optimizer."** Call the variables **spins**, not qubits. Don't call it "a quantum computer with N qubits."

**Your answer:**
> "Good question. It's not a universal gate-based quantum computer; it's a special-purpose photonic Ising machine, built specifically for optimization problems like ours. Whether CIMs get a true quantum speed-up is an open research question, and we don't claim one. What matters to us is that it takes our QUBO directly, gives high-quality solutions very fast at room temperature, and we benchmark it against classical solvers every time. And because our formulation is QUBO, the same model runs on annealers or gate-based machines (QAOA) as those mature. We aren't locked in."

This answer will earn respect from physicists in the room.

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
[Hybrid orchestrator] ──► Quantum/Ising solver (Quanfluence CIM, used in 112; also IBM / D-Wave / Braket)
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
> "Sir, Arohak is an Andhra Pradesh technology company working on practical quantum applications. We've completed a pilot with the AP Government on **Dial 112**, using quantum-optical optimization (a QUBO model run on an **Indian-made photonic Ising machine from Quanfluence, incubated at IIT Madras**) to dispatch and position emergency vehicles more effectively so citizens get help faster. `[one CONFIRMED result]`.
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

**Q1. Did you run on actual hardware or a simulator?**
*"On actual hardware: a **photonic Coherent Ising Machine from Quanfluence**, a Bengaluru startup incubated at IIT Madras. We converted our QUBO to Ising form, ran zone-level sub-problems on the machine, and validated every result classically."* `[CONFIRM: whether runs were on-premise at Quanfluence or via their cloud/API access.]`

**Q2. How many qubits did you use?**
*Gently correct the term; that shows you know the field.* *"An Ising machine uses **spins**, not qubits. Each spin is a light pulse in the fibre loop. Each zone-level sub-problem used about `[CONFIRM N]` spins, within the machine's capacity of `[CONFIRM, e.g., 128]` fully connected spins. We decompose the state-level problem by zone so each piece fits. Fitting the problem to the hardware is a big part of the engineering."*

**Q3. Did you actually achieve quantum advantage?**
*Be honest. This is a test.* *"Not in the strict academic sense; nobody has proven that for a real-world routing problem yet. What we showed is that the hybrid approach produces solutions [comparable to / better than] our classical baseline within the dispatch time window on our pilot instances. And the architecture is ready to benefit as hardware improves. We're building capability ahead of the curve, not claiming a miracle."*

**Q4. Isn't this just simulated annealing / a classical heuristic with a quantum label?**
*"Fair challenge. We always benchmark against classical heuristics, including simulated annealing and MILP solvers, and we only route to the quantum path where it earns its place. Part of our stack is quantum-inspired, and we're transparent about which part is which."*

**Q5. Why an Ising machine and not IBM/Google gate-based or D-Wave?**
*"Dispatch is an optimization problem, and Ising machines are built specifically for optimization. Today's gate-based machines are still too noisy to run QAOA at useful sizes. The CIM gives us all-to-all connectivity, room-temperature operation, very fast solves, and it's Indian hardware, which matters for government data and for the ecosystem. Our QUBO formulation is portable, so we can run the same model on D-Wave or on gate-based QAOA for comparison."*

**Q5b. How is a CIM different from a D-Wave annealer?**
*"Both minimize Ising energy. D-Wave uses superconducting qubits cooled to millikelvin, with limited connectivity, so large problems need 'minor embedding'. A CIM uses optical pulses at room temperature, and measurement-feedback gives all-to-all coupling without embedding. D-Wave is larger and more established; CIMs are newer, cheaper and easier to deploy."*

**Q6. How do you handle noise/errors?**
*"Ising machines are heuristic and analog, so each run can land in a good but not perfect state. We handle that three ways: many repeated runs (they take milliseconds) keeping the best, careful tuning of penalty weights and pump/feedback parameters, and classical post-processing: a feasibility check plus a quick local search to repair any rule violations. Nothing reaches an operator unless it passes classical feasibility checks."*

**Q7. How do you encode constraints in a QUBO?**
*"As penalty terms. If a constraint is violated, the energy (cost) goes up. Tuning the penalty weights is one of the trickier parts: too low and you get infeasible answers, too high and the solver ignores the actual objective."* (This answer will impress people who know the field.)

**Q8. What's the latency? Real-time dispatch needs seconds.**
`[CONFIRM.]` *"In the pilot, each QUBO optimization cycle ran in about [X] seconds end-to-end. For a live rollout, the design is that instant decisions use the latest optimized plan plus a fast rule, while the optimizer re-plans continuously in the background every few seconds."*

**Q9. Where is the data hosted? Is government data sent to foreign quantum clouds?**
*"Very important question. Only anonymized mathematical problem representations (the QUBO matrices, just numbers) go to the solver. No personal or citizen data leaves the government environment. The data integration and formulation run within [state data centre / approved cloud]. The solver itself is **Indian hardware from Quanfluence**, so even the numbers stay in India. And as Quantum Valley comes up in Amaravati, we can run on that infrastructure too."* `[CONFIRM data-flow details.]`

**Q10. What about Shor's algorithm and encryption?**
*"Shor's algorithm could break RSA and ECC on a large, fault-tolerant quantum computer. That's still some years away, but 'harvest now, decrypt later' means sensitive data should move to post-quantum cryptography now. NIST standardized ML-KEM and ML-DSA in 2024. We help organizations take crypto inventory and plan PQC migration, which is fundamentally an integration and architecture exercise."*

**Q11. What's your team's quantum background?**
`[CONFIRM.]` *"Our quantum team includes [physicists / PhDs / Qiskit-certified engineers / partnerships with X institution]. I lead technology and architecture, making it work end-to-end in production."*

**Q12. Which SDKs/tools?**
`[CONFIRM.]` For 112: the **Quanfluence Ising machine and its API/interface**, plus a QUBO formulation layer `[CONFIRM: e.g., Python with PyQUBO / dimod / custom]`, and a classical baseline `[CONFIRM: e.g., OR-Tools / Gurobi / simulated annealing]`. Other common tools worth knowing: **Qiskit** (IBM), **Cirq** (Google), **PennyLane** (Xanadu), **D-Wave Ocean**, **Amazon Braket**, **Azure Quantum**, **CUDA-Q** (NVIDIA).

### B. Business and strategic questions

**Q13. Why should a company invest in quantum now if advantage isn't proven?**
*"Three reasons: (1) The problem formulation, data pipelines and integration you build now carry over directly when hardware matures. (2) Quantum-inspired algorithms give value today on classical hardware. (3) Talent and know-how take years to build. The companies that start learning now will lead later. Pilots are low-cost; falling behind is high-cost."*

**Q14. What's the ROI?**
*"In the 112 pilot, the value is measured in response minutes saved, which means lives. In supply chain, it's changeover time, inventory cost and re-planning speed. We always start with a classical baseline, so ROI is measured against what you'd get anyway."*

**Q15. How long does a pilot take, and what does it cost?**
`[CONFIRM Arohak's commercial model.]` Typical framing: *"A focused pilot is usually [8–12 weeks]: problem discovery, formulation, hybrid solver, benchmark against classical, then a go/no-go on scale-up."*

**Q16. Who are your partners?**
*"For the 112 pilot, our hardware partner was **Quanfluence**, an IIT Madras-incubated photonic quantum startup in Bengaluru. Arohak brings the problem formulation, the integration with government systems, and the end-to-end solution."* `[CONFIRM any other partners.]`

**Q17. How are you different from TCS, Infosys or big quantum startups?**
*"We're focused and practical: problem-first, not hardware-first. And our integration depth (SAP, webMethods, enterprise and government systems) means our quantum solutions actually go live inside real workflows instead of staying as research demos."*

### C. Questions the CM or officials may ask

**Q18. How will this help the common citizen?**
*"Faster ambulance and police response through 112. Better crop logistics for farmers so less produce is wasted. Stable power supply with more solar. Quantum is the engine underneath; the citizen sees faster service."*

**Q19a. Is the 112 system live / in production?**
*"It's a pilot today. We validated the QUBO formulation and the hybrid approach on real 112 data `[CONFIRM: historical / shadow / selected zones]`, and the results were `[CONFIRM headline result]`. The next step is a phased rollout, and we're discussing that with the department."*

**Q19b. Why isn't it in production yet? / What did the pilot prove?**
*"A pilot is the right first step for any critical public-safety system. You never put emergency response on a new technology without proving it first. The pilot proved three things: the problem can be cleanly formulated as a QUBO, the hybrid solver gives `[comparable/better]` plans than the current method within the time window, and the integration with 112 data sources works. Scale-up is mainly about integrating all districts, hardening for 24×7 availability, and dispatcher training."*

**Q19c. Why QUBO and not a standard MILP solver?**
*"We ran a classical baseline too. QUBO gives us one formulation that runs on quantum annealers, gate-based machines via QAOA, and quantum-inspired solvers, so we can benchmark them side by side and switch as hardware improves. MILP stays as our classical comparison and fallback."*

**Q19d. How many binary variables did your QUBO have?**
`[CONFIRM.]` *"Around [N] variables per zone-level sub-problem. A full-state problem would be far larger, which is why we decompose. Vehicles × incidents grows fast: 50 × 50 is already 2,500 binary variables before routing and coverage terms."*

**Q19. Can you scale the 112 pilot across the state?**
*"Yes. The architecture was designed for that. Scaling means integrating all districts' feeds and running zone-level optimization in parallel. We can propose a phased rollout: [N] districts in phase 1."*

**Q20. How can Arohak contribute to Amaravati Quantum Valley?**
*"Three ways: use-case delivery for government departments, integration of the quantum platform with state systems, and skilling. We'd be happy to run training programs with local engineering colleges so AP builds quantum-ready talent."*

**Q21. How many jobs / what skilling?**
`[CONFIRM Arohak's headcount and plans.]` Have a number ready.

### D. Curveballs

**Q21b. What exactly is an "Ising machine"? Why that name?**
*"It's named after the Ising model, a physics model from the 1920s of tiny magnets (spins) that each point up or down and influence their neighbours. The magnets naturally settle into the arrangement with the lowest energy. We disguise our dispatch problem as a set of magnets: 'up' means this vehicle goes to that incident. Then we let the machine find the lowest-energy arrangement, which is our best plan."*

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
- [ ] Confirm the **pilot mode** (historical replay / shadow / live in selected zones) and the **QUBO size** (number of spins per sub-problem)
- [ ] Confirm the **Quanfluence machine version/spin count**, the access mode (on-premise or cloud/API), and permission to name them as a partner
- [ ] Practise the **"Is a CIM a real quantum computer?"** answer (Section 4A); this is your toughest question
- [ ] If possible, invite someone from Quanfluence/IIT Madras to stop by the stall, or have a joint slide
- [ ] Practise the **"explain QUBO simply"** answer (Section 4)
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
HOW:   Integrate data → formulate QUBO → decompose by zone → convert to Ising
       → solve on Quanfluence photonic Coherent Ising Machine (+ classical
       baseline/fallback) → validate → write back
HW:    Quanfluence CIM: laser pulses in a fibre loop = spins (not qubits);
       FPGA feedback = all-to-all coupling; room temperature; IIT Madras-
       incubated (Prof. Anil Prabhakar), Bengaluru. ~128 spins [CONFIRM]
       NOT a universal gate-based QC; a special-purpose optimizer. Say so.
112:   PILOT with AP Govt. Formulated as QUBO (yes/no: vehicle i → incident j)
       Cost = response time + big penalties for broken rules → find min
       Fleet-wide dispatch + pre-positioning, not "nearest vehicle"
       Pilot result: [CONFIRM]% faster response, [CONFIRM]% better coverage
       Next: phased statewide scale-up
CPG:   SKU sequencing + inventory placement via SAP BTP integration
       Overnight planning → minutes re-planning [CONFIRM]
EDGE:  "We make quantum usable: the bridge between qubits and business systems"
HONEST:"No one has proven full quantum advantage on real routing yet;
        we benchmark every time and are ready as hardware scales"
TERMS: Ising · Spin · CIM · QUBO↔Ising (x=(1+s)/2) · Bifurcation · All-to-all
       Qubit · Superposition · Entanglement · Interference · QAOA
       VQE · Annealing · NISQ · Logical qubit · PQC (ML-KEM) · Hybrid
AP:    Amaravati Quantum Valley (IBM System Two, TCS, L&T)
INDIA: National Quantum Mission ₹6,003 cr, 2023–31, 50–1000 qubits
DON'T KNOW? → "Let me connect you with our quantum lead."
```

---

### Sources (Quanfluence facts)
- [Inc42: Quanfluence nets $2 Mn led by pi Ventures](https://inc42.com/buzz/quantum-technology-startup-quanfluence-nets-2-mn-led-by-pi-ventures/)
- [pi Ventures portfolio: Quanfluence](https://www.piventures.in/portfolio/quanfluence)
- [The Quantum Insider: pi Ventures invests in Quanfluence](https://thequantuminsider.com/2024/12/18/lighting-the-future-pi-ventures-invests-in-the-next-gen-computing-platform-by-quanfluence/)
- [Quantum Zeitgeist: Quanfluence seed funding for optical Ising machine](https://quantumzeitgeist.com/quanfluence-raises-2-million-in-a-seed-funds-for-optical-ising-machine/)
- [Quanfluence blog: How Coherent Ising Machines work](https://quanfluence.com/reimagining-computation-how-coherent-ising-machines-are-solving-the-unsolvable/)
- [VARINDIA: Bengaluru start-up unveils room-temperature quantum computer](https://www.varindia.com/news/bengaluru-start-up-unveils-room-temperature-quantum-computer)
- [Prof. Anil Prabhakar, IIT Madras](https://sites.google.com/ee.iitm.ac.in/anilprabhakar/home)
- [Science (2016): A fully programmable 100-spin coherent Ising machine](https://www.science.org/doi/10.1126/science.aah5178)
