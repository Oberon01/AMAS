# AMAS Phase 2 – Alignment Logic and Interpretation

This phase builds the **engine that interprets how well a person aligns to a given symbolic mental model** based on their trait profile.

---

## ✅ Phase 2 – Alignment Logic and Interpretation

### 2.1 Alignment Algorithm

We implement a **scoring mechanism** that compares an individual's 10-trait profile to each model's row in the `AMAS_Model_Matrix_FULL.csv`.

**Key Features:**
- Uses **weighted cosine similarity** or **normalized distance metric**
- Scores range from **0.00 (no alignment)** to **1.00 (perfect alignment)**

---

### 2.2 Interpretation Bands

Every alignment score is mapped to a category:

| Score Range | Label               | Description                                                                 |
|-------------|---------------------|-----------------------------------------------------------------------------|
| 0.90 – 1.00 | **Resonant Anchor** | This model is deeply embedded in the subject's cognitive architecture       |
| 0.75 – 0.89 | **Aligned Core**    | This model strongly supports decision-making or worldview                   |
| 0.60 – 0.74 | **Supportive Tool** | This model may be useful contextually, but not reflexively applied          |
| 0.40 – 0.59 | **Potential Seed**  | Latent model with room for symbolic reinforcement                           |
| 0.00 – 0.39 | **Misaligned**      | This model currently has little to no activation within the subject profile |

---

### 2.3 Output Format

The output is returned in structured format:

```json
{
  "subject_name": "Isabel",
  "top_models": [
    {
      "model": "Simulation Literacy",
      "score": 0.92,
      "category": "Resonant Anchor"
    },
    {
      "model": "Emergence Awareness",
      "score": 0.84,
      "category": "Aligned Core"
    }
  ],
  "lowest_models": [
    {
      "model": "Zero-Sum Fallacy",
      "score": 0.18,
      "category": "Misaligned"
    }
  ]
}
```

---

## Expansion Readiness

This logic structure is **compatible with CLI simulation tools**, **scenario testing**, and **cultural or symbolic overlays**.

