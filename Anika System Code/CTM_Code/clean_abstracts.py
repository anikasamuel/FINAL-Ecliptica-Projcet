import pandas as pd

def remove_empty_abstracts(input_file, output_file):
    df = pd.read_excel(input_file)  # or pd.read_excel if Excel
    df = df[df['Abstract'].notna()]
    df = df[df['Abstract'].str.strip() != '']
    df.to_csv(output_file, index=False)
    return output_file
