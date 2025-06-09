# AMAS Alignment Algorithm – Mathematical Layer

This document outlines the structure and logic behind the mathematical layer of the AMAS (Archetypal Model Alignment System) alignment engine. This layer is responsible for producing numerical alignment scores between a subject profile and a catalog of symbolic mental models.

---

## 🔧 Step 1: Input Requirements

The algorithm accepts two inputs:

1. **Subject Profile**  
   A 10-dimensional vector representing a subject’s scores across the ten AMAS traits (1–10 scale).

2. **Model Matrix**  
   A static CSV file containing trait vectors for each of the 30 symbolic mental models.

---

## 🧮 Step 2: Alignment Formula

Alignment is calculated using **cosine similarity**:

\[
\text{Cosine Similarity} = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\| \times \|\vec{B}\|}
\]

Where:
- \( \vec{A} \) is the subject vector
- \( \vec{B} \) is a model vector
- Output ranges from -1 (inverse alignment) to 1 (perfect alignment)

Cosine similarity is ideal for symbolic reasoning because it emphasizes **directional resonance** over magnitude.

---

## 🧪 Step 3: Implementation Plan

The algorithm will be implemented as a Python function that:

1. Loads `AMAS_Model_Matrix_COMPLETE.csv`
2. Accepts a subject trait vector as input
3. Computes cosine similarity against all models
4. Sorts results in descending order
5. Outputs the top-aligned symbolic mental models

---

## 🧠 Step 4: Output Format

Each alignment result will contain:
- **Model Name**
- **Similarity Score** (0.0000–1.0000)
- *(Optional)* Symbolic commentary (added in hybrid overlay layer)

---

## ⚙️ Notes

- This function will be used in both the CLI interface and symbolic simulation toolkits
- Results can be filtered by use-case scenario in later phases
