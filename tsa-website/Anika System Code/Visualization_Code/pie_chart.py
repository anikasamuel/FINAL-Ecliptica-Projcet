import pandas as pd
import plotly.express as px
import os

def generate_pie_chart(file_path, output_folder):
    df = pd.read_csv(file_path)
    df['Keywords'] = df['Keywords'].astype(str).str.split(';')
    df_exploded = df.explode('Keywords')
    df_exploded['Keywords'] = df_exploded['Keywords'].str.strip()
    keyword_counts = df_exploded['Keywords'].value_counts().reset_index()
    keyword_counts.columns = ['Keyword', 'Count']

    fig = px.pie(keyword_counts.head(5), values='Count', names='Keyword',
                 title='Top 5 Keywords by Frequency')

    # Save to Visualizations folder inside output folder
    vis_folder = os.path.join(output_folder, 'Visualizations')
    os.makedirs(vis_folder, exist_ok=True)
    output_file = os.path.join(vis_folder, f"pie_chart_{os.path.basename(file_path).replace('.csv', '')}.html")
    fig.write_html(output_file)
    print(f"🥧 Pie chart saved to '{output_file}'")
