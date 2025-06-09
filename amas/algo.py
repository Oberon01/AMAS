import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_model_matrix(csv_path):
    df = pd.read_csv(csv_path)
    trait_columns = [col for col in df.columns if col != "Model Name"]
    return df, df[trait_columns].values, trait_columns

def calculate_alignment(subject_vector, model_vectors, model_names):
    subject_vector_np = np.array(subject_vector).reshape(1, -1)
    similarities = cosine_similarity(subject_vector_np, model_vectors).flatten()
    result_df = pd.DataFrame({
        "Model Name": model_names,
        "Alignment Score": similarities
    })
    result_df.sort_values(by="Alignment Score", ascending=False, inplace=True)
    return result_df

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 12:
        print("Usage: python amas_alignment_algorithm.py path_to_model_matrix trait1 trait2 ... trait10")
        exit(1)
    model_matrix_path = sys.argv[1]
    subject_traits = list(map(float, sys.argv[2:]))
    df, model_vectors, _ = load_model_matrix(model_matrix_path)
    model_names = df["Model Name"].values
    results = calculate_alignment(subject_traits, model_vectors, model_names)
    print(results.to_string(index=False))