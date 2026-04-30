import pandas as pd
import numpy as np
from scipy import stats
import os

def clean_dataset(country):
    print(f"--- Processing {country.upper()} ---")
    file_path = f"{country.lower()}.csv"
    
    if not os.path.exists(file_path):
        print(f"File {file_path} not found. Skipping...")
        return

    # Loading with NASA header skip
    df = pd.read_csv(file_path, skiprows=10)
    
    # Feature Engineering
    df['Country'] = country.capitalize()
    df['Date'] = pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format='%Y%j')
    df['Month'] = df['Date'].dt.month
    
    # Cleaning
    df.replace(-999, np.nan, inplace=True)
    df.drop_duplicates(inplace=True)
    
    # Outlier Capping (99th percentile)
    cols = ['T2M', 'T2M_MAX', 'T2M_MIN', 'PRECTOTCORR', 'RH2M', 'WS2M']
    for col in cols:
        limit = df[col].quantile(0.99)
        df[col] = np.where(df[col] > limit, limit, df[col])
    
    # Missing Values: Forward fill then drop remaining gaps
    df[cols] = df[cols].ffill()
    df.dropna(subset=cols, inplace=True)
    
    # Export
    os.makedirs('data', exist_ok=True)
    out_path = f"data/{country.lower()}_clean.csv"
    df.to_csv(out_path, index=False)
    print(f"Success! Saved to {out_path}\n")

if __name__ == "__main__":
    countries = ['ethiopia', 'kenya', 'nigeria', 'sudan', 'tanzania']
    for c in countries:
        clean_dataset(c)
