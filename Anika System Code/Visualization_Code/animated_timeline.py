import pandas as pd
import plotly.express as px
import os

def animated_topic_timeline(file_path, output_folder):
    df = pd.read_excel(file_path)
    if 'Year' not in df.columns or 'Assigned Topic' not in df.columns:
        raise ValueError("The file must contain 'Year' and 'Assigned Topic' columns.")

    topic_trends = df.groupby(['Year', 'Assigned Topic']).size().reset_index(name='Count')
    fig = px.scatter(
        topic_trends,
        x='Year', y='Count', size='Count', color='Assigned Topic',
        hover_name='Assigned Topic', animation_frame='Year',
        title='Animated Timeline of Topics by Year',
        labels={'Count': 'Number of Publications'}
    )

    # Save to the correct output folder
    vis_folder = os.path.join(output_folder, 'Visualizations')
    os.makedirs(vis_folder, exist_ok=True)
    output_file = os.path.join(vis_folder, 'animated_timeline.html')
    fig.write_html(output_file)
    print(f"📽️ Timeline saved to '{output_file}'")
