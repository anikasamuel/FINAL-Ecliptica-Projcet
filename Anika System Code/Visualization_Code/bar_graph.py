import pandas as pd
import os
import matplotlib
matplotlib.use('Agg')  # <-- This disables GUI stuff that causes those RuntimeErrors
import matplotlib.pyplot as plt


def bar_chart_overview(file_path, output_folder):
    df = pd.read_excel(file_path)
    df = df.dropna(subset=['Year', 'Assigned Topic'])
    df['Year'] = pd.to_numeric(df['Year'], errors='coerce').dropna().astype(int)
    df['Assigned Topic'] = df['Assigned Topic'].str.strip()

    topic_counts = df['Assigned Topic'].value_counts()

    plt.figure(figsize=(10, 6))
    topic_counts.plot(kind='bar')
    plt.title('Count of Publications by Assigned Topic')
    plt.xlabel('Assigned Topic')
    plt.ylabel('Number of Publications')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save to Visualizations folder inside output folder
    vis_folder = os.path.join(output_folder, 'Visualizations')
    os.makedirs(vis_folder, exist_ok=True)
    output_file = os.path.join(vis_folder, 'bar_chart_overview.png')
    plt.savefig(output_file)
    print(f"📊 Bar chart saved to '{output_file}'")
    plt.close()
