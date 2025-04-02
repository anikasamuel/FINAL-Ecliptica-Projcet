import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Same cleaning logic
KEYWORD_EXPANSIONS = {
    "genet": "genetics", "gene_express": "gene expression", "obes": "obesity",
    "mutat": "mutation", "studi": "", "activ": "activation", "makeup": "",
    "use": "", "can": "", "system": "", "type": "", "develop": "development",
    "differ": "differentiation", "transcript": "transcription", "express": "expression",
    "yield": "crop yield", "fertil": "fertilizer", "irrig": "irrigation",
    "soil_moistur": "soil moisture", "crop_prod": "crop production",
    "resilienc": "resilience", "adapt": "adaptation", "sustain": "sustainability",
    "increas": "increase", "reduc": "reduction", "food_sec": "food security",
    "temperatur": "temperature", "precipit": "precipitation", "agricultur": "agriculture"
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

AGRI_TOPICS = [
    "Crop Yield Optimization", "Soil Health and Fertility", "Climate Resilience", "Water Use Efficiency",
    "Sustainable Farming Practices", "Food Security and Nutrition", "Agricultural Technology",
    "Pest and Disease Management", "Irrigation and Water Use", "Fertilizer Management",
    "Carbon Sequestration in Agriculture", "Precision Agriculture", "Agroecology", "Biodiversity in Farming",
    "Organic Agriculture", "Agroforestry", "Soil Erosion Control", "Drought Resistance", "Weed Management",
    "Livestock Health", "Farm Mechanization", "Seed Quality Improvement", "Agri-Business Models",
    "Climate-Smart Agriculture", "Agricultural Education", "Crop Rotation Practices", "Compost and Manure Use",
    "Sustainable Supply Chains", "Pollination and Ecosystem Services", "Agricultural Labor Practices",
    "Post-Harvest Loss Reduction", "Food System Equity", "Agroclimatic Zoning", "Integrated Pest Management",
    "Soil Carbon Monitoring", "Water Harvesting Techniques", "Land Tenure and Access", "GMOs and Biotechnology",
    "Digital Agriculture and AI", "Farmer Decision Support Tools", "Mobile Apps for Agriculture",
    "Satellite Monitoring in Agriculture", "Soil Nutrient Monitoring", "Regenerative Agriculture",
    "Agricultural Trade and Markets", "Crop Diversification", "Micro-irrigation Systems",
    "Farmer Cooperatives", "Policy and Governance in Agriculture", "Youth in Agriculture",
    "Women in Agriculture", "Sustainable Land Use", "Remote Sensing in Agriculture", "Agricultural Waste Management",
    "Plant Breeding", "Farming in Marginal Lands", "Resilient Crop Varieties", "Agri-Finance and Loans",
    "Land Degradation", "Climate Adaptation Finance", "Hydroponics and Vertical Farming",
    "Urban Agriculture", "Soil Salinity Management", "Land Use Modeling", "Pest Forecasting Systems",
    "Irrigation Infrastructure", "Climate Variability Impact", "Smallholder Farm Productivity",
    "Nutrition-Sensitive Agriculture", "Agri-Insurance", "Sustainable Food Systems", "Rainfed Agriculture",
    "Crop Modeling and Forecasting", "Biofertilizers and Biopesticides", "Farmer Knowledge Sharing",
    "Agricultural Value Chains", "Agricultural Logistics", "Circular Economy in Agriculture",
    "Water Quality in Agriculture", "Monitoring Greenhouse Gas Emissions", "Land-Use Change Detection",
    "Traceability in Food Systems", "Mobile Weather Advisory Services", "Farming with Indigenous Knowledge",
    "Farmer-Led Innovation", "Food Loss and Waste", "Desertification Control", "Soil pH and Acidity Management",
    "Adaptation to Flooding", "Seed Bank Conservation", "Food Distribution Systems", "Farm Income Stabilization",
    "Policy for Crop Insurance", "Crop Pest Surveillance", "Farmer Training Programs", "Food Reserves",
    "Agricultural Emissions Reduction", "Biosecurity in Agriculture", "Pesticide Regulation and Safety"
]

def generate_summary_topics(input_file, output_file):
    df = pd.read_csv(input_file)
    df["Keywords"] = df["Keywords"].fillna("")
    cleaned_keywords = df["Keywords"].apply(clean_keywords)

    all_texts = cleaned_keywords.tolist() + AGRI_TOPICS
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(all_texts)

    keyword_vecs = tfidf_matrix[:len(df)]
    topic_vecs = tfidf_matrix[len(df):]

    sim_matrix = cosine_similarity(keyword_vecs, topic_vecs)

    assigned_topics = set()
    summary_topics = []

    for row_sim in sim_matrix:
        sorted_indices = row_sim.argsort()[::-1]  # Highest similarity first
        for idx in sorted_indices:
            topic = AGRI_TOPICS[idx]
            if topic not in assigned_topics:
                assigned_topics.add(topic)
                summary_topics.append(topic)
                break
        else:
            summary_topics.append("Unlabeled")

    df["Summary topic"] = summary_topics
    df.to_csv(output_file, index=False)
    return output_file
