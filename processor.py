# processor.py

import pandas as pd

def process_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Performs data cleaning and basic analysis operations:
    1. Identifies missing (NaN) values.
    2. Fills missing values in the 'Cost' column with the mean.
    3. Fills missing values in the 'Units' column with 0.
    4. Returns the processed DataFrame.
    """
    print("\n[VERİ TEMİZLEME RAPORU]")
    
    # 1. Checking for missing values
    missing_data = df.isnull().sum()
    print("Eksik Değerler (Temizlemeden Önce):")
    print(missing_data[missing_data > 0])
    
    # 2. Filling missing values ​​in the 'Cost' column with average
    cost_mean = df['Cost'].mean()
    df['Cost'].fillna(cost_mean, inplace=True)
    print(f"\n✅ 'Cost' sütunu ortalama ({cost_mean:.2f}) ile dolduruldu.")
    
    # 3. Fill missing values ​​in the 'Units' column with 0
    df['Units'].fillna(0, inplace=True)
    print("✅ 'Units' sütunu 0 ile dolduruldu.")
    
    # Let's add a new column: Total Revenue = Sales - Cost
    df['Profit'] = df['Sales'] - df['Cost']
    print("✅ 'Profit' (Kâr) sütunu hesaplandı.")
    
    return df