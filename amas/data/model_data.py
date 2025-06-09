import pandas as pd

# Example model dataframe
model_df = pd.DataFrame([
    {"Model Name": "Recursive Architect", "Traits": [9, 10, 10, 9, 8, 9, 10, 9, 9, 9]},
    {"Model Name": "Interpretive Synthesizer", "Traits": [8, 9, 9, 8, 7, 8, 9, 8, 8, 8]},
    {"Model Name": "Narrative Anchor", "Traits": [7, 8, 8, 7, 7, 8, 8, 9, 8, 9]},
    {"Model Name": "Strategic Simulator", "Traits": [6, 9, 8, 6, 9, 7, 8, 6, 6, 6]},
    {"Model Name": "Relational Echo", "Traits": [8, 7, 7, 7, 6, 8, 7, 9, 8, 9]}
])

# Per-class weight tuning
symbolic_class_trait_weights = {
    "Recursive Architect": [1.2, 1.2, 1.3, 1.1, 1.0, 1.1, 1.3, 1.2, 1.1, 1.2],
    "Interpretive Synthesizer": [1.3, 1.1, 1.2, 1.3, 1.0, 1.0, 1.1, 1.3, 1.0, 1.1],
    "Narrative Anchor": [1.1, 1.0, 1.2, 1.1, 1.2, 1.1, 1.1, 1.3, 1.2, 1.2],
    "Strategic Simulator": [1.0, 1.3, 1.1, 1.0, 1.3, 1.2, 1.1, 1.0, 1.0, 1.1],
    "Relational Echo": [1.2, 1.0, 1.0, 1.1, 1.1, 1.2, 1.0, 1.3, 1.3, 1.3],
}

# Penalty matrix
symbolic_penalty_map = {
    "Recursive Architect": [0.1]*10,
    "Interpretive Synthesizer": [0.2]*10,
    "Narrative Anchor": [0.15]*10,
    "Strategic Simulator": [0.25]*10,
    "Relational Echo": [0.2]*10,
}
