
import pandas as pd
import numpy as np
from amas.algo.overlay import symbolic_resonance_filter_fuzzy
from amas.algo.ensemble import ensemble_rank_alignment
from amas.data.model_data import model_df, symbolic_class_trait_weights, symbolic_penalty_map
from amas.data.metadata import symbolic_metadata_loaded, narrative_neighbors
from amas.data.traits import trait_names
from report_generator import generate_symbolic_report

# Define your subject here (example)
subject = {
    "name": "Example Subject",
    "traits": [9, 10, 10, 9, 8, 9, 10, 9, 9, 9]
}

subject_vector = subject["traits"]
subject_dict = dict(zip(trait_names, subject_vector))

# Fuzzy symbolic resonance filtering
qualified_models = symbolic_resonance_filter_fuzzy(subject_dict, symbolic_metadata_loaded, fuzziness=0.5)

# Ensemble alignment computation
top_df, ensemble_df = ensemble_rank_alignment(
    subject_vector,
    model_df,
    trait_weights_map=symbolic_class_trait_weights,
    symbolic_penalty=symbolic_penalty_map,
    ensemble_n=3
)

# Narrative neighborhood evaluation
filtered_df = ensemble_df[ensemble_df["Model Name"].isin(qualified_models)].reset_index(drop=True)
top_model = filtered_df.iloc[0]["Model Name"] if not filtered_df.empty else "None"
match_status = "Exact" if top_model in qualified_models else "Conflict"
cluster_neighbors = narrative_neighbors.get(top_model, [])
ensemble_top3 = list(filtered_df["Model Name"].values[:3])

# Result
print("Subject:", subject["name"])
print("Top Match:", top_model)
print("Cluster Neighbors:", cluster_neighbors)
print("Ensemble Top 3:", ensemble_top3)
generate_symbolic_report(subject["name"], subject_vector, top_model, match_status)