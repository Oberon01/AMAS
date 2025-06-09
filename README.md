# System Overview: AMAS – Archetypal Model Alignment System

## Core Functionality

AMAS evaluates cognitive and symbolic profiles against five consolidated mental models using a hybrid numeric-symbolic method.

### 1. Trait-Based Vector Alignment
Each subject is defined using a 10-dimensional trait vector:
1. Symbolic Capacity
2. System Awareness
3. Meta-Cognition
4. Paradigm Flexibility
5. Cognitive Containment
6. Epistemic Clarity
7. Temporal Projection
8. Narrative Coherence
9. Shadow Awareness
10. Alignment Receptivity

### 2. Ensemble Scoring
Weighted trait similarity and symbolic penalties yield a ranked list of candidate models.

### 3. Overlay Filtering
Symbolic metadata filters dissonant matches through fuzzy resonance thresholds.

### 4. Narrative Neighborhoods
Symbolically adjacent matches are accepted through cluster logic, enabling approximate symbolic alignment.

---

## Key Files
- `amas/` – Core modules
- `amas_overlay_simulation.py` – Sample simulation runner
- `AMAS_Symbolic_Metadata.json` – Symbolic overlay rulebase
- Class-level trait weight map and penalty models

---

## Simulation Example

Input:
```
[9, 10, 10, 9, 8, 9, 10, 9, 9, 9]
```

Output:
```
Top Match: Recursive Architect
Cluster Neighbors: Interpretive Synthesizer, Strategic Simulator
Status: Exact Match
```

---

## Future Extensions
- Model deviation scoring
- Real-time symbolic profiling via UI
- Integration into larger symbolic cognition frameworks
