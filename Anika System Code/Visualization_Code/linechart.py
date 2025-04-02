import pandas as pd
import matplotlib
matplotlib.use('Agg')  # <-- This disables GUI stuff that causes those RuntimeErrors
import matplotlib.pyplot as plt
import os

def line_chart_overview(file_path, output_folder):
    df = pd.read_excel(file_path)
    df = df.dropna(subset=['Year', 'Assigned Topic'])
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').dropna().astype(int)
    df['Assigned Topic'] = df['Assigned Topic'].str.strip()

    topic_trends = df.groupby(['Year', 'Assigned Topic']).size().unstack(fill_value=0)

    plt.figure(figsize=(12, 6))
    topic_trends.plot(marker='o')
    plt.title('Topic Trends Over Time')
    plt.xlabel('Year')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save to Visualizations folder inside output folder
    vis_folder = os.path.join(output_folder, 'Visualizations')
    os.makedirs(vis_folder, exist_ok=True)
    output_file = os.path.join(vis_folder, 'line_chart_overview.png')
    plt.savefig(output_file)
    print(f"📈 Line chart saved to '{output_file}'")
    plt.close()
