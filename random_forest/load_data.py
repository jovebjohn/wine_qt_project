import pandas as pd

def load_dataset(path):
    df = pd.read_csv(path)

    if 'Id' in df.columns:
        df = df.drop('Id', axis=1)

    return df