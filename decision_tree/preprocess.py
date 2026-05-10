def prepare_data(df):
    X = df.drop('quality', axis=1)

    # Convert quality into binary values
    y = (df['quality'] >= 6).astype(int)

    return X, y