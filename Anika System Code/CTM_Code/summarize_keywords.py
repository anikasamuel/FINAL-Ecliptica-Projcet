import pandas as pd
import yake

# Expanded and domain-flexible keyword mapper
KEYWORD_EXPANSIONS = {
    "genet": "genetics",
    "gene_express": "gene expression",
    "obes": "obesity",
    "mutat": "mutation",
    "studi": "",
    "activ": "activation",
    "makeup": "",
    "use": "",
    "can": "",
    "system": "",
    "type": "",
    "develop": "development",
    "differ": "differentiation",
    "transcript": "transcription",
    "express": "expression",
    "yield": "crop yield",
    "fertil": "fertilizer",
    "irrig": "irrigation",
    "soil_moistur": "soil moisture",
    "crop_prod": "crop production",
    "resilienc": "resilience",
    "adapt": "adaptation",
    "sustain": "sustainability",
    "increas": "increase",
    "reduc": "reduction",
    "food_sec": "food security",
    "temperatur": "temperature",
    "precipit": "precipitation",
    "agricultur": "agriculture"  # General term for agriculture
}

FILLER_WORDS = {"use", "study", "system", "data", "based", "approach", "result", "analysis", "method", "effect"}

def clean_keywords(raw_keywords):
    tokens = [k.strip().lower() for k in raw_keywords.split(";")]
    expanded = []
    for t in tokens:
        if t in FILLER_WORDS or t == "":
            continue
        if t in KEYWORD_EXPANSIONS:
            new_term = KEYWORD_EXPANSIONS[t]
            if new_term:
                expanded.append(new_term)
        else:
            expanded.append(t)
    return " ".join(expanded)

def generate_summary_topics(input_file, output_file):
    df = pd.read_csv(input_file)
    df["Keywords"] = df["Keywords"].fillna("")

    kw_extractor = yake.KeywordExtractor(lan="en", n=2, top=1)

    summary_topics = []
    for row in df["Keywords"]:
        clean_text = clean_keywords(row)
        if not clean_text.strip():
            summary_topics.append("Unlabeled")
            continue
        keywords = kw_extractor.extract_keywords(clean_text)
        label = keywords[0][0] if keywords else "Unlabeled"
        summary_topics.append(label.title())

    df["Summary topic"] = summary_topics
    df.to_csv(output_file, index=False)
    return output_file
