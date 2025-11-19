# main.py

import argparse
from data_loader import load_data
from processor import process_data
from db_manager import save_to_db # New import

# NOTE: Global setting for Pandas FutureWarnings (Optional but clears output)
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

def main():
    """CLI Argümanlarını yöneten ana fonksiyon ve iş akışını başlatır."""
    parser = argparse.ArgumentParser(
        description="Dinamik Veri İşleme ve Analiz Aracı. CSV dosyasını okur, temizler ve veritabanına kaydeder."
    )
    
    parser.add_argument(
        "file_path", 
        type=str, 
        help="Analiz edilecek CSV dosyasının yolu."
    )
    
    args = parser.parse_args()
    file_path = args.file_path
    
    # STEP 1: DATA LOADING
    print("-" * 30)
    print(f"1. ADIM: Veri Yükleniyor... (Dosya: {file_path})")
    
    data_frame = load_data(file_path)
    
    if data_frame is None:
        print("İşlem Başarısız: Veri yüklenemedi. Program sonlandırılıyor.")
        return

    # STEP 2: DATA PROCESSING AND CLEANING
    print("-" * 30)
    print("2. ADIM: Veri İşleniyor ve Temizleniyor...")
    # NOTE: DataFrame'in bir kopyasını işlemek için .copy() kullanmak FutureWarning'ı çözer.
    processed_df = process_data(data_frame.copy())
    
    print("\nTemizlenmiş DataFrame Başlangıcı:")
    print(processed_df.head(3))
    
    # STEP 3: SAVE TO DATABASE
    print("-" * 30)
    print("3. ADIM: Veritabanına Kaydediliyor...")
    
    db_success = save_to_db(processed_df)
    
    if db_success:
        print("-" * 30)
        print("🎉 İŞLEM TAMAMLANDI: Tüm iş akışı başarıyla sona erdi.")
    else:
        print("-" * 30)
        print("🚨 İŞLEM BAŞARISIZ: Kayıt hatası nedeniyle sonlandırıldı.")

if __name__ == "__main__":
    main()