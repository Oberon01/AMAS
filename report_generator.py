import os
from amas.data.traits import trait_names
from amas.data.metadata import narrative_neighbors
from amas.data.model_data import model_df

# Narrative metadata for symbolic reporting
model_narratives = {
    "Recursive Architect": {
        "summary": "You perceive systems within systems, always searching for recursive logic and symbolic scaffolding that explains the whole.",
        "metaphor": "A cathedral builder of logic in an infinite spiral staircase.",
        "bias_risks": ["Overfitting logic patterns", "Neglecting emotional clarity", "Conceptual detachment"]
    },
    "Interpretive Synthesizer": {
        "summary": "You draw meaning from scattered inputs, constantly weaving symbolic threads into a coherent worldview.",
        "metaphor": "A loom of meaning spun from intangible threads.",
        "bias_risks": ["Narrative distortion", "Over-association", "Mythic delusion"]
    },
    "Narrative Anchor": {
        "summary": "You provide grounding through story, coherence, and values. Meaning becomes your stabilizer and lens.",
        "metaphor": "A compass embedded in the mythic map of identity.",
        "bias_risks": ["Rigid narrative loops", "Echo chamber formation", "Resistance to paradigm shift"]
    },
    "Strategic Simulator": {
        "summary": "You engage the world through mental simulation, anticipating moves and assembling causal maps.",
        "metaphor": "A grandmaster thinking 10 steps ahead in the architecture of consequence.",
        "bias_risks": ["Emotional detachment", "Instrumental reasoning bias", "Over-control"]
    },
    "Relational Echo": {
        "summary": "You mirror others' needs, emotions, and meanings — building resonance and intimate symbolic rapport.",
        "metaphor": "An emotional tuning fork in the chamber of connection.",
        "bias_risks": ["Loss of self-definition", "Over-identification", "Emotional fusion"]
    }
}

def generate_symbolic_report(subject_name, subject_vector, top_match, match_status, out_path="reports"):
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    model_info = model_narratives.get(top_match, None)
    if model_info is None:
        summary = "No symbolic interpretation available for this model."
        metaphor = "-"
        risks = []
    else:
        summary = model_info["summary"]
        metaphor = model_info["metaphor"]
        risks = model_info["bias_risks"]

    neighbors = narrative_neighbors.get(top_match, [])
    trait_lines = "\n".join([
        f"| {trait_names[i]:<27} |   {subject_vector[i]}   |"
        for i in range(len(subject_vector))
    ])

    content = f"""# Subject Report: {subject_name}

## Symbolic Alignment Summary
Top Match: {top_match}
Match Status: {match_status}
Cluster Neighbors: {", ".join(neighbors)}

## Narrative Summary
{summary}

## Symbolic Metaphor
{metaphor}

## Bias Profile
{"\n".join("- " + risk for risk in risks)}

## Trait Breakdown
| Trait                     | Score |
|---------------------------|--------|
{trait_lines}
"""

    with open(os.path.join(out_path, f"{subject_name.replace(' ', '_')}_symbolic_report.md"), "w") as f:
        f.write(content)
