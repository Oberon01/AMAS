import pandas as pd

def validate_model_matrix(file_path):
    df = pd.read_csv(file_path)

    required_columns = [
        'Model Name', 'Symbolic Capacity', 'System Awareness',
        'Meta-Cognition', 'Paradigm Flexibility',
        'Cognitive Containment', 'Epistemic Clarity', 'Temporal Projection',
        'Narrative Coherence', 'Shadow Awareness', 'Alignment Receptivity'
    ]

    print("Validating trait matrix structure...")
    for col in required_columns:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    print("Checking trait value ranges (0–10)...")
    for trait in required_columns[1:]:
        invalid_rows = df[(df[trait] < 0) | (df[trait] > 10)]
        if not invalid_rows.empty:
            print(f"Invalid values in trait '{trait}':")
            print(invalid_rows)
            raise ValueError(f"Trait '{trait}' has values outside 0–10 range.")

    print("Validation complete. Matrix is valid.")

# Example usage:
validate_model_matrix('amas\\AMAS_Model_Matrix_Generated.csv')