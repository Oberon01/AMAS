
def symbolic_resonance_filter_fuzzy(subject_dict, metadata, fuzziness=0.5):
    qualified = []
    for model, meta in metadata.items():
        if "Symbolic Capacity" in subject_dict and subject_dict["Symbolic Capacity"] >= 7:
            qualified.append(model)
    return qualified
