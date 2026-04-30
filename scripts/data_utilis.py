import pandas as pd
import numpy as np
from scipy import stats

def load_and_initial_clean(file_path, country_name):
    """Handles NASA header, datetime conversion, and sentinel values."""
        # 1. Load (NASA files usually have 10-15 rows of metadata)
            df = pd.read_csv(file_path, skiprows=10)
                
                    # 2. Basic Metadata
                        df['Country'] = country_name
                            df['Date'] = pd.to_datetime(df['YEAR'] * 1000 + df['DOY'], format='%Y%j')
                                df['Month'] = df['Date'].dt.month
                                    
                                        # 3. Sentinel Values
                                            df.replace(-999, np.nan, inplace=True)
                                                
                                                    # 4. Duplicates
                                                        dupe_count = df.duplicated().sum()
                                                            df.drop_duplicates(inplace=True)
                                                                
                                                                    return df, dupe_count

                                                                    def handle_outliers_and_missing(df, cols):
                                                                        """Calculates Z-scores and handles gaps."""
                                                                            # Z-score detection
                                                                                z_scores = np.abs(stats.zscore(df[cols].fillna(df[cols].mean())))
                                                                                    outlier_count = (z_scores > 3).sum()
                                                                                        
                                                                                            # Capping Strategy (Standard for climate extremes)
                                                                                                for col in cols:
                                                                                                        upper = df[col].quantile(0.99)
                                                                                                                lower = df[col].quantile(0.01)
                                                                                                                        df[col] = df[col].clip(lower, upper)
                                                                                                                                
                                                                                                                                    # Forward-fill and row-drop logic
                                                                                                                                        df = df.dropna(thresh=int(len(df.columns) * 0.7))
                                                                                                                                            df[cols] = df[cols].ffill()
                                                                                                                                                
                                                                                                                                                    return df, outlier_count
                                                                                                                                                    