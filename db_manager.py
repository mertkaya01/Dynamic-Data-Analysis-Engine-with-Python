# db_manager.py

import pandas as pd
import sqlite3
import os

def save_to_db(df: pd.DataFrame, db_name: str = 'analysis_results.db', table_name: str = 'processed_data') -> bool:
    """
    Pandas save Dataframe to stated SQLite database
    """
    print(f"-> Veritabanı Dosyası: {db_name}")
    print(f"-> Kaydedilecek Tablo: {table_name}")

    try:
        # Establish a connection to an SQLite database (create the file if it does not exist)
        conn = sqlite3.connect(db_name)
        
        # Write the DataFrame directly to the SQL table
        # if_exists='replace' deletes the old table and creates a new one.
        df.to_sql(table_name, conn, if_exists='replace', index=False)
        
        # Checking how many lines were recorded
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
        row_count = cursor.fetchone()[0]
        
        conn.close()
        
        print(f"\n✅ BAŞARILI: Toplam {row_count} satır '{db_name}' veritabanına kaydedildi.")
        return True

    except Exception as e:
        print(f"\n❌ HATA: Veritabanına kaydederken bir sorun oluştu. Detay: {e}")
        return False