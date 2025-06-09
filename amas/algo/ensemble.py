import numpy as np
import pandas as pd

def ensemble_rank_alignment(subject_vector, model_df, trait_weights_map, symbolic_penalty, ensemble_n=3):
    results = []
    for _, row in model_df.iterrows():
        model_name = row["Model Name"]
        model_vector = row["Traits"]
        weights = trait_weights_map[model_name]
        penalties = symbolic_penalty[model_name]

        weighted_diff = [
            weights[i] * abs(subject_vector[i] - model_vector[i]) + penalties[i]
            for i in range(len(subject_vector))
        ]
        score = -sum(weighted_diff)  # Lower difference = better score
        results.append({"Model Name": model_name, "Score": score})

    df = pd.DataFrame(results).sort_values("Score", ascending=False).reset_index(drop=True)
    return df.head(1), df.head(ensemble_n)
