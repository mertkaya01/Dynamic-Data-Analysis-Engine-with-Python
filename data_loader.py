# data_loader.py

import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame | None:
    """
    Read the CSV file from the path and transform to Pandas Dataframe
    If the file is can not find or have a error for reading turn None
    """
    # Checking the file
    if not os.path.exists(file_path):
        print(f"HATA: Belirtilen dosya bulunamadı: '{file_path}'")
        return None

    try:
        # Uploading the data with read_csv func from Pandas
        df = pd.read_csv(file_path)
        print(f"VERİ YÜKLENDİ: '{file_path}' dosyasında {len(df)} satır ve {len(df.columns)} sütun bulundu.")
        return df
    
    except Exception as e:
        # Catching errors like CSV format mistakes
        print(f"HATA: Dosya okunurken bir sorun oluştu. Detay: {e}")
        return None