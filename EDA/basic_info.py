def show_basic_info(df):
    print("Dataset Shape:")
    print(df.shape)

    print("\nColumn Names:")
    print(df.columns)

    print("\nMissing Values:")
    print(df.isnull().sum())