import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

def load_model_matrix(csv_path):
    df = pd.read_csv(csv_path)
    trait_columns = [col for col in df.columns if col not in ["Model Name", "Symbolic Class"]]
    model_names = df["Model Name"].tolist()
    model_vectors = df[trait_columns].values
    return df, model_vectors, model_names, trait_columns

def normalize_traits(data):
    scaler = StandardScaler()
    return scaler.fit_transform(data)

def calculate_alignment(subject_vector, model_vectors, model_names, trait_columns, top_n=5):
    subject_vector_np = np.array(subject_vector).reshape(1, -1)
    similarities = cosine_similarity(subject_vector_np, model_vectors).flatten()
    max_score = np.max(similarities)
    normalized_scores = similarities / max_score
    distance_from_top = max_score - similarities

    # Trait contribution (dot product per trait)
    trait_contributions = model_vectors * subject_vector_np

    results = pd.DataFrame({
        "Model Name": model_names,
        "Raw Score": similarities,
        "Normalized Score": normalized_scores,
        "Distance from Top": distance_from_top
    })

    for i, trait in enumerate(trait_columns):
        results[f"{trait} Contribution"] = trait_contributions[:, i]

    results.sort_values(by="Raw Score", ascending=False, inplace=True)
    return results.head(top_n), results

def cluster_models(model_vectors, model_names, n_clusters=3):
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(model_vectors)
    return dict(zip(model_names, labels))

def plot_radar(subject_vector, model_vector, trait_labels, model_name):
    angles = np.linspace(0, 2 * np.pi, len(trait_labels), endpoint=False).tolist()
    angles += angles[:1]
    subject_plot = subject_vector.tolist() + subject_vector[:1]
    model_plot = model_vector.tolist() + model_vector[:1]

    fig, ax = plt.subplots(figsize=(6,6), subplot_kw=dict(polar=True))
    ax.plot(angles, subject_plot, label='Subject')
    ax.fill(angles, subject_plot, alpha=0.25)
    ax.plot(angles, model_plot, label=model_name)
    ax.fill(angles, model_plot, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(trait_labels)
    ax.legend()
    plt.title("Trait Alignment Radar Chart")
    plt.show()

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 12:
        print("Usage: python algo_v2_test.py path_to_model_matrix trait1 trait2 ... trait10")
        exit(1)

    model_matrix_path = sys.argv[1]
    subject_traits = list(map(float, sys.argv[2:]))

    df, model_vectors, model_names, traits = load_model_matrix(model_matrix_path)
    top_matches, full_results = calculate_alignment(subject_traits, model_vectors, model_names, traits)

    print("\nTop AMAS Model Alignments with Trait Contributions:")
    print(top_matches.to_string(index=False))

    clusters = cluster_models(model_vectors, model_names)
    print("\nModel Clusters:")
    for model, label in clusters.items():
        print(f"{model}: Cluster {label}")

    best_model = top_matches.iloc[0]
    best_model_vector = df[df["Model Name"] == best_model["Model Name"]][traits].values[0]
    plot_radar(np.array(subject_traits), best_model_vector, traits, best_model["Model Name"])


    # Output to structured report file
    output_path = "alignment_report.txt"
    with open(output_path, "w") as report:
        report.write("Top AMAS Model Alignments with Trait Contributions:\n")
        report.write(top_matches.to_string(index=False))
        report.write("\n\nModel Clusters:\n")
        for model, label in clusters.items():
            report.write(f"{model}: Cluster {label}\n")

    print(f"\nReport saved to: {output_path}")
