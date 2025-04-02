import pandas as pd                      # For loading and manipulating CSV data
import networkx as nx                    # For building and managing graph structures
import plotly.graph_objects as go        # For creating interactive network visualizations
import os                                # For file operations
from sklearn.feature_extraction.text import TfidfVectorizer  # For converting text to vectors
from sklearn.metrics.pairwise import cosine_similarity       # For comparing text similarity

# A curated list of clean agricultural/development keywords for matching
CLEAN_KEYWORDS = [
    "food security", "crop yield", "soil health", "irrigation", "climate change", "drought resilience",
    "smallholder farming", "women in agriculture", "sustainable farming", "pesticide use", "nutrition access",
    "farm financing", "livestock management", "seed quality", "organic agriculture", "soil erosion",
    "farming practices", "agribusiness growth", "water access", "plant breeding", "GMO crops",
    "gender equity", "agricultural policy", "technology use", "income diversification",
    "agricultural training", "education access", "market access", "land tenure", "rural development",
    "crop rotation", "precision agriculture", "food systems", "international trade", "carbon emissions",
    "greenhouse gases", "rainfall variability", "resilient communities", "agroecology", "carbon sequestration",
    "subsidy reform", "price volatility", "poverty reduction", "malnutrition reduction", "crop loss prevention",
    "remote sensing", "data-driven farming", "climate adaptation", "weather forecasting", "supply chain resilience",
    "farm labor", "access to credit", "fertilizer use", "post-harvest losses", "food distribution systems",
    "income inequality", "water management", "plant health", "youth in farming", "land use efficiency",
    "crop diversification", "migration patterns", "urban-rural linkages", "climate resilience", "ecosystem services",
    "public health", "biodiversity loss", "soil monitoring", "animal health", "technology training",
    "digital agriculture", "policy advocacy", "financial literacy", "value chain development", "agriculture education",
    "insurance schemes", "food access equity", "biofuel production", "economic upliftment", "skills training",
    "capacity building", "crop science", "pest management", "urban agriculture", "market intelligence",
    "investment in ag", "women’s empowerment", "climate mitigation", "crop diseases", "pollution control",
    "clean technologies", "mobile extension", "farm logistics", "aquaculture systems", "seasonal forecasting",
    "youth migration", "trade agreements", "nutrition programs", "healthcare access", "rural banking"
]

# Color palette mapped by thematic category
CATEGORY_COLORS = {
    "climate": "#FDB863", "soil": "#B2ABD2", "tech": "#E66101", "equity": "#5E3C99",
    "water": "#4393C3", "nutrition": "#D6604D", "production": "#4DAC26", "finance": "#762A83",
    "topic": "#FFD700", "default": "#BFBFBF"
}

# Predefined keyword-to-category mapping for color assignment
CATEGORY_MAP = {
    "climate": ["climate change", "climate adaptation", "carbon emissions", "carbon sequestration", "greenhouse gases",
                "rainfall variability", "climate resilience", "climate mitigation", "seasonal forecasting"],
    "soil": ["soil health", "soil erosion", "soil monitoring", "land use efficiency", "land tenure"],
    "tech": ["precision agriculture", "remote sensing", "digital agriculture", "data-driven farming", "mobile extension",
             "technology use", "technology training", "clean technologies"],
    "equity": ["gender equity", "women in agriculture", "education access", "youth in farming", "women’s empowerment"],
    "water": ["irrigation", "water access", "water management"],
    "nutrition": ["nutrition access", "malnutrition reduction", "food access equity", "nutrition programs", "public health"],
    "production": ["crop yield", "crop loss prevention", "seed quality", "fertilizer use", "pesticide use", "crop rotation", "plant breeding", "crop diversification"],
    "finance": ["farm financing", "access to credit", "insurance schemes", "subsidy reform", "rural banking"]
}

# Function to match a raw keyword to the best-fitting clean keyword
def get_best_match(raw_keyword):
    vectorizer = TfidfVectorizer().fit(CLEAN_KEYWORDS + [raw_keyword])  # Fit vectorizer to all known keywords plus input
    vecs = vectorizer.transform([raw_keyword] + CLEAN_KEYWORDS)         # Vectorize the input + all keywords
    sims = cosine_similarity(vecs[0:1], vecs[1:]).flatten()             # Compare input to all others
    best_index = sims.argmax()                                          # Choose the most similar keyword
    return CLEAN_KEYWORDS[best_index]

# Function to return the color category of a given keyword
def get_category(keyword):
    for cat, kws in CATEGORY_MAP.items():
        if keyword in kws:
            return cat
    return "default"  # Return default if keyword not categorized

# Main function to create a network graph and save it as an interactive HTML
def generate_keyword_network(file_path, output_folder):
    df = pd.read_csv(file_path)  # Load CSV file
    df = df.dropna(subset=['Summary topic', 'Keywords'])  # Remove rows missing required fields
    df['Keywords'] = df['Keywords'].astype(str).str.split(';')  # Convert keyword string to list
    df_exploded = df.explode('Keywords')  # Flatten keyword lists so each keyword is a separate row
    df_exploded['Keywords'] = df_exploded['Keywords'].str.strip().str.lower()  # Clean keywords

    # Get the top 5 topics by frequency
    top_topics = df_exploded['Summary topic'].value_counts().head(5).index.tolist()
    df_filtered = df_exploded[df_exploded['Summary topic'].isin(top_topics)]  # Keep only top 5 topics

    # Clean and match each keyword
    df_filtered['Cleaned Keyword'] = df_filtered['Keywords'].apply(get_best_match)

    G = nx.Graph()  # Create a new empty graph
    for _, row in df_filtered.iterrows():
        topic = row['Summary topic']
        keyword = row['Cleaned Keyword']
        G.add_node(topic, type='topic', color=CATEGORY_COLORS['topic'])  # Add topic node
        cat = get_category(keyword)
        G.add_node(keyword, type='keyword', color=CATEGORY_COLORS.get(cat, CATEGORY_COLORS['default']))  # Add keyword node
        G.add_edge(topic, keyword)  # Connect topic and keyword

    # Generate node positions
    pos = nx.spring_layout(G, seed=42)
    edge_x, edge_y = [], []
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])  # X coords of each edge
        edge_y.extend([y0, y1, None])  # Y coords of each edge

    # Define how edges look on the graph
    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=1, color='gray'),
        hoverinfo='none',
        mode='lines'
    )

    node_x, node_y, labels, colors, sizes = [], [], [], [], []
    for node, data in G.nodes(data=True):
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        labels.append(node)
        colors.append(data['color'])                      # Use color based on category
        sizes.append(28 if data['type'] == 'topic' else 16)  # Bigger size for topic nodes

    # Define how nodes appear
    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        text=labels,
        textposition="top center",
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color=colors,
            size=sizes,
            line_width=2
        )
    )

    # Create the full figure with layout and data
    fig = go.Figure(
        data=[edge_trace, node_trace],
        layout=go.Layout(
            title=dict(
                text='🌐 Keyword Network by Topic (Categorized)',
                font=dict(size=22)
            ),
            showlegend=False,
            hovermode='closest',
            margin=dict(b=20, l=5, r=5, t=40),
            xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
            yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
    )

    # Save figure to file
    vis_folder = os.path.join(output_folder, 'Visualizations')
    os.makedirs(vis_folder, exist_ok=True)
    output_file = os.path.join(vis_folder, f"keyword_network_{os.path.basename(file_path).replace('.csv', '')}.html")
    fig.write_html(output_file)
    print(f"🔗 Keyword network saved to '{output_file}'")
    return output_file  # Return the path to the saved HTML file
