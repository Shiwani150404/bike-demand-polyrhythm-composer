import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    return df

def preprocess_data(df):
    # Convert date
    df['dteday'] = pd.to_datetime(df['dteday'])

    # Drop duplicates
    df = df.drop_duplicates()

    # Feature engineering
    df['year'] = df['dteday'].dt.year
    df['month'] = df['dteday'].dt.month
    df['day'] = df['dteday'].dt.day

    return df