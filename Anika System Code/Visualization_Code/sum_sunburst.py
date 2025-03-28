import pandas as pd
import plotly.express as px
import os

def create_sunburst_chart(file_path, output_folder):
    df = pd.read_csv(file_path)
    if 'Summary topic' not in df.columns or 'Keywords' not in df.columns:
        print("The file must contain 'Summary topic' and 'Keywords' columns.")
        return

    df['Keywords'] = df['Keywords'].astype(str).str.split(';')
    df_exploded = df.explode('Keywords')
    df_exploded['Keywords'] = df_exploded['Keywords'].str.strip()

    fig = px.sunburst(
        df_exploded,
        path=['Summary topic', 'Keywords'],
        title="Sunburst Chart of Summary Topics and Keywords"
    )

    fig.update_layout(
        title_font_size=32,
        font=dict(size=24),
        title_x=0.5
    )

    # Save to Visualizations folder inside output folder
    vis_folder = os.path.join(output_folder, 'Visualizations')
    os.makedirs(vis_folder, exist_ok=True)
    output_file = os.path.join(vis_folder, f"sunburst_chart_{os.path.basename(file_path).replace('.csv', '')}.html")
    fig.write_html(output_file)

    print(f"🌞 Sunburst chart saved to '{output_file}'")
