import pandas as pd

def load_data(filepath):
    df = pd.read_csv(filepath, sep=';')
    df['y'] = df['y'].map({'yes': 1, 'no': 0})
    df = df.dropna(subset=['y'])
    return df

