import pandas as pd
import numpy as np

def clean_data(df):
    df = df.copy()

    # Drop duplicate rows
    df.drop_duplicates(inplace=True)

    # Remove rows with missing target values
    df = df[df['Rating'].notna()]

    # Convert Reviews to int
    df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')

    # Convert Installs to numeric
    # Handle cases where 'Free' is incorrectly placed in Installs column
    df['Installs'] = df['Installs'].replace('Free', '0')
    df['Installs'] = df['Installs'].str.replace('[+,]', '', regex=True).astype(float)

    # Convert Price to numeric
    # Handle cases where 'Everyone' is incorrectly placed in Price column
    df['Price'] = df['Price'].replace('Everyone', '0')
    df['Price'] = df['Price'].str.replace('$', '', regex=False).astype(float)

    # Clean Size column
    def size_to_mb(x):
        if 'M' in x:
            return float(x.replace('M', ''))
        elif 'k' in x:
            return float(x.replace('k', '')) / 1024
        else:
            return np.nan

    df['Size'] = df['Size'].replace('Varies with device', np.nan)
    df['Size'] = df['Size'].dropna().map(size_to_mb)

    # Fill missing size with median
    df['Size'].fillna(df['Size'].median(), inplace=True)

    return df
