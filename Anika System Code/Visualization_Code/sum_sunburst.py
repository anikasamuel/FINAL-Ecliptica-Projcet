import pandas as pd
import plotly.express as px
import os
from difflib import get_close_matches

GOOD_KEYWORDS = [
    "agriculture", "climate change", "soil", "crop", "farmer", "irrigation", "yield", "resilience", "pesticide",
    "food security", "gender", "sustainability", "fertilizer", "drought", "farming systems", "smallholder",
    "rainfall", "carbon", "ecosystem", "nutrition", "biodiversity", "income", "market access", "land use",
    "subsidy", "rural development", "organic farming", "mechanization", "plant disease", "livestock", "carbon footprint",
    "supply chain", "seed", "agroforestry", "technology", "precision agriculture", "genetics", "GMOs", "pollination",
    "aquaculture", "water stress", "crop diversification", "microfinance", "access to credit", "education", "deforestation",
    "population growth", "renewable energy", "solar irrigation", "malnutrition", "migration", "urban agriculture",
    "labor", "income stabilization", "farm size", "training", "insurance", "weather forecasting", "global warming",
    "conflict", "policy", "cooperative", "digital tools", "climate finance", "land tenure", "crop insurance",
    "food systems", "pest management", "climate adaptation", "remittances", "data collection", "machine learning",
    "youth in agriculture", "women in agriculture", "health", "investment", "afforestation", "sub-Saharan Africa",
    "southeast Asia", "water harvesting", "crop modeling", "extension services", "soil salinity", "monitoring",
    "value chains", "sustainable intensification", "greenhouse gases", "input costs", "climate-smart ag",
    "plant breeding", "policy reform", "co-design", "conservation", "climate policy", "indigenous knowledge",
    "water availability", "technology adoption", "knowledge transfer", "disease outbreaks", "crop calendar"
]

def match_keyword(word):
    match = get_close_matches(word.lower(), GOOD_KEYWORDS, n=1, cutoff=0.6)
    return match[0] if match else None

def create_sunburst_chart(file_path, output_folder):
    df = pd.read_csv(file_path)
    if "Summary topic" not in df.columns or "Keywords" not in df.columns:
        print("The file must contain 'Summary topic' and 'Keywords' columns.")
        return

    df['Keywords'] = df['Keywords'].astype(str).str.split(';')
    df_exploded = df.explode('Keywords')
    df_exploded['Keywords'] = df_exploded['Keywords'].str.strip().str.lower()

    # Match keywords to top 100 curated list
    df_exploded['Mapped Keyword'] = df_exploded['Keywords'].apply(match_keyword)
    df_exploded = df_exploded.dropna(subset=["Mapped Keyword"])

    # Select top 5 per topic
    top_keywords_per_topic = (
        df_exploded.groupby(['Summary topic', 'Mapped Keyword'])
        .size().reset_index(name='Count')
        .sort_values(['Summary topic', 'Count'], ascending=[True, False])
    )

    final_rows = []
    for topic in top_keywords_per_topic['Summary topic'].unique():
        keywords = top_keywords_per_topic[top_keywords_per_topic['Summary topic'] == topic]
        top5 = keywords.head(5)
        # Fill in if < 5
        used = set(top5['Mapped Keyword'])
        needed = 5 - len(top5)
        if needed > 0:
            fillers = [k for k in GOOD_KEYWORDS if k not in used][:needed]
            for f in fillers:
                top5 = pd.concat([top5, pd.DataFrame([{"Summary topic": topic, "Mapped Keyword": f, "Count": 1}])])
        final_rows.append(top5)

    final_df = pd.concat(final_rows)

    fig = px.sunburst(
        final_df,
        path=["Summary topic", "Mapped Keyword"],
        values="Count",
        title="Sunburst Chart of Summary Topics and Keywords",
    )

    fig.update_layout(
        title_font_size=26,
        font=dict(size=18),
        title_x=0.5
    )

    vis_folder = os.path.join(output_folder, "Visualizations")
    os.makedirs(vis_folder, exist_ok=True)

    output_file = os.path.join(vis_folder, f"sunburst_chart_{os.path.basename(file_path).replace('.csv', '')}.html")
    fig.write_html(output_file)
    print(f"🌞 Sunburst chart saved to '{output_file}'")
