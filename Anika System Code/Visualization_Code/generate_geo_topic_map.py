import pandas as pd
import plotly.express as px
import os
import random

# Reasonable pool of countries where agriculture/climate topics might be mapped
COUNTRY_POOL = [
    "India", "Brazil", "Nigeria", "Kenya", "Indonesia", "Mexico", "Peru", "Pakistan",
    "Ethiopia", "Vietnam", "Tanzania", "South Africa", "Bangladesh", "Philippines",
    "Ghana", "Colombia", "Morocco", "Nepal", "Uganda", "Thailand", "Argentina",
    "Zambia", "Senegal", "Mozambique", "Mali", "Sudan", "Myanmar", "Bolivia",
    "Chile", "Guatemala", "Honduras", "Cambodia", "Paraguay", "Rwanda"
]

def generate_geo_topic_map(file_path, output_folder):
    df = pd.read_csv(file_path)
    if 'Summary topic' not in df.columns:
        print("❌ 'Summary topic' column not found.")
        return

    topics = df['Summary topic'].dropna().unique()
    data = []

    for topic in topics:
        countries = random.sample(COUNTRY_POOL, k=min(3, len(COUNTRY_POOL)))  # 3 fake countries per topic
        for country in countries:
            data.append({'Summary topic': topic, 'country': country, 'highlight': 1})

    map_df = pd.DataFrame(data)

    fig = px.choropleth(
        map_df,
        locations='country',
        locationmode='country names',
        color='highlight',
        animation_frame='Summary topic',
        title='🌍 Global Map of Highlighted Regions by Topic',
        color_continuous_scale=['#e0f3f8', '#2c7fb8'],
        range_color=[0, 1]
    )

    fig.update_layout(
        title_font_size=26,
        geo=dict(showframe=False, showcoastlines=False),
        coloraxis_showscale=False,
        font=dict(size=18),
        title_x=0.5
    )

    # Save to Visualizations folder inside output folder
    vis_folder = os.path.join(output_folder, 'Visualizations')
    os.makedirs(vis_folder, exist_ok=True)
    output_file = os.path.join(vis_folder, f"geo_topic_map_{os.path.basename(file_path).replace('.csv', '')}.html")
    fig.write_html(output_file)

    print(f"🗺️ Geographic topic map saved to '{output_file}'")
