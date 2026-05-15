import os
import subprocess
import pandas as pd
from playwright.sync_api import sync_playwright
from groq import Groq

def install_playwright():
    """Memastikan pelayar Chromium dipasang di server Streamlit"""
    try:
        # Melancarkan arahan pemasangan pelayar secara senyap
        subprocess.run(["playwright", "install", "chromium"], check=True)
    except Exception as e:
        print(f"Nota: Proses pemasangan pelayar: {e}")

def scrape_data():
    """Mengekstrak data dari laman web secara langsung"""
    # Pastikan pelayar tersedia sebelum memulakan
    install_playwright()
    
    with sync_playwright() as p:
        # headless=True adalah WAJIB untuk deployment online
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        
        try:
            # Laman Web Sasaran
            page.goto("http://books.toscrape.com/", timeout=60000)
            
            # Mengambil 10 data pertama
            titles = page.locator("h3 a").all_inner_texts()
            prices = page.locator(".price_color").all_inner_texts()
            
            data = []
            for i in range(min(10, len(titles))):
                data.append({
                    "Nama Produk": titles[i],
                    "Harga": prices[i].replace("Â", ""), # Membersihkan simbol pelik
                })
                
            df = pd.DataFrame(data)
            df.to_csv("data_buku_besar.csv", index=False)
            return data
            
        except Exception as e:
            print(f"Ralat semasa scraping: {e}")
            return []
        finally:
            browser.close()

def analyze_with_ai(data):
    """Menghantar data ke Llama 3.1 untuk analisis perniagaan"""
    # Mengambil API Key dari Secrets Streamlit atau Environment Variable
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        return "⚠️ Ralat: Kunci API Groq tidak dijumpai. Sila tetapkan dalam Secrets."

    client = Groq(api_key=api_key)
    
    # Arahan (Prompt) dalam Bahasa Melayu yang profesional
    prompt = f"""
    Anda adalah Pakar Analisis Data Pasaran profesional. 
    Berdasarkan data harga produk berikut: {str(data)}
    
    Sila berikan dalam Bahasa Melayu:
    1. 🏆 Produk paling mahal dan paling murah.
    2. 📈 Analisis ringkas trend harga (Wawasan Perniagaan).
    3. 💡 Cadangan strategi kompetitif untuk peruncit.
    
    Gunakan format Markdown yang kemas dengan emoji.
    """
    
    try:
        chat = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-70b-versatile",
        )
        
        result = chat.choices[0].message.content
        
        # Simpan laporan untuk dibaca oleh app.py
        with open("laporan_ai.txt", "w", encoding="utf-8") as f:
            f.write(result)
        return result
    except Exception as e:
        return f"⚠️ Ralat AI: {e}"

def run_all():
    """Fungsi utama untuk menyelaraskan keseluruhan proses"""
    data_mentah = scrape_data()
    if data_mentah:
        analyze_with_ai(data_mentah)
        return "Proses Berjaya!"
    else:
        return "Gagal mengumpul data."

if __name__ == "__main__":
    run_all()