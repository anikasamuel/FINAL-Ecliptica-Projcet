import pandas as pd
import plotly.express as px
import os
from difflib import get_close_matches

# List of 100 meaningful agricultural keywords
CLEAN_KEYWORDS = [
    "food security", "crop yield", "soil fertility", "irrigation", "climate change", "drought",
    "farmers", "women in agriculture", "sustainable farming", "pesticide use", "nutrition",
    "agricultural finance", "livestock", "seed variety", "organic farming", "soil erosion",
    "farming techniques", "agribusiness", "water conservation", "plant breeding", "genetic engineering",
    "gender equality", "agricultural policy", "technology adoption", "income diversification",
    "agricultural extension", "education", "access to markets", "land ownership", "rural development",
    "crop rotation", "precision agriculture", "food systems", "global trade", "carbon footprint",
    "greenhouse gases", "rainfall patterns", "smallholder farmers", "agroecology", "carbon sequestration",
    "input subsidies", "market prices", "poverty alleviation", "malnutrition", "crop failure",
    "remote sensing", "data collection", "climate adaptation", "weather forecasting", "supply chain",
    "labor", "access to credit", "fertilizer application", "post-harvest loss", "food distribution",
    "income inequality", "water management", "plant health", "youth in agriculture", "land use",
    "crop diversification", "migration", "rural-urban linkages", "resilience", "ecosystem services",
    "public health", "biodiversity", "soil moisture", "animal health", "technology transfer",
    "digital agriculture", "policy reform", "financial literacy", "value chains", "agricultural education",
    "crop insurance", "supply resilience", "biofuels", "economic development", "capacity building",
    "training programs", "green revolution", "pest management", "urban agriculture", "market access",
    "investment", "gender empowerment", "climate mitigation", "crop diseases", "pollution",
    "green technologies", "mobile extension", "transportation", "aquaculture", "seasonal variability",
    "youth migration", "trade policy", "nutrition programs", "healthcare access", "rural finance"
]

def get_best_match(raw_keyword, keyword_list):
    matches = get_close_matches(raw_keyword.lower(), keyword_list, n=1, cutoff=0.4)
    return matches[0] if matches else raw_keyword

def generate_pie_chart(file_path, output_folder):
    df = pd.read_csv(file_path)
    df['Keywords'] = df['Keywords'].astype(str).str.split(';')
    df_exploded = df.explode('Keywords')
    df_exploded['Keywords'] = df_exploded['Keywords'].str.strip().str.lower()
    
    keyword_counts = df_exploded['Keywords'].value_counts().head(20).reset_index()
    keyword_counts.columns = ['RawKeyword', 'Count']

    # Map to best match from clean list
    keyword_counts['CleanedKeyword'] = keyword_counts['RawKeyword'].apply(
        lambda kw: get_best_match(kw, CLEAN_KEYWORDS)
    )

    cleaned_summary = keyword_counts.groupby('CleanedKeyword')['Count'].sum().reset_index()
    cleaned_summary = cleaned_summary.sort_values(by='Count', ascending=False).head(8)

    fig = px.pie(cleaned_summary, values='Count', names='CleanedKeyword',
                 title='Top 8 Keywords by Frequency (Cleaned)')

    vis_folder = os.path.join(output_folder, 'Visualizations')
    os.makedirs(vis_folder, exist_ok=True)
    output_file = os.path.join(vis_folder, f"pie_chart_{os.path.basename(file_path).replace('.csv', '')}.html")
    fig.write_html(output_file)
    print(f"🥧 Pie chart saved to '{output_file}'")
