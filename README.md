# ⚙️ DataProcessor-CLI: Dinamik Veri Analiz Motoru


Bu proje, Python, Pandas ve SQLite yeteneklerini bir araya getiren, komut satırı tabanlı (CLI) bir veri işleme ve analiz otomasyon aracıdır. Ham CSV verilerini alır, temizler, temel analizleri yapar ve sonuçları kalıcı bir veritabanına kaydeder.

---

## 🚀 Proje Amacı ve Özellikler

Bu araç, **temiz mühendislik kodlamasını, modüler tasarımı ve veri yönetimi becerilerini** sergilemek amacıyla geliştirilmiştir.

| Özellik | Açıklama |
| :--- | :--- |
| **CLI Tabanlı Kullanım** | Kullanıcıdan dosya yolunu doğrudan terminalden alır. |
| **Modüler Tasarım** | Veri yükleme, işleme ve kaydetme modüllerine ayrılmıştır (SOLID prensipleri). |
| **Veri Temizleme (Pandas)** | Kayıp verileri (NaN), sütunun **ortalama** değeri veya **0** gibi mantıksal değerlerle doldurur. |
| **Temel Analiz** | `Sales` ve `Cost` üzerinden yeni bir `Profit` (Kâr) sütunu hesaplar. |
| **Veri Kalıcılığı (SQL)** | İşlenmiş verileri, kolay sorgulanabilmesi için **SQLite** veritabanına kaydeder. |
| **Ufak bir proje olarak yapmak istedim. |
---

## 🛠️ Kullanılan Teknolojiler

| Kategori | Teknoloji | Neden Kullanıldı? |
| :--- | :--- | :--- |
| **Ana Dil** | Python | Hızlı prototipleme ve güçlü veri işleme kütüphanelerine erişim. |
| **Veri Analizi** | Pandas | CSV okuma, DataFrame manipülasyonu ve hızlı istatistiksel işlemler için. |
| **Veritabanı** | SQLite (SQL) | Hafif, sunucusuz ve standart SQL sorgulama yeteneği. |
| **CLI** | `argparse` | Komut satırı argümanlarını profesyonelce yönetmek için. |

---

## 💻 Kurulum ve Çalıştırma

### 1. Kütüphaneleri Yükleme

Bu proje, Python 3 gerektirir. Gerekli kütüphaneleri `requirements.txt` dosyasından kurun:

```bash

# pip install -r requirements.txt
