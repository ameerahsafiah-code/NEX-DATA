import pandas as pd
import matplotlib.pyplot as plt

def jana_graf():
    try:
        # 1. Baca data dari CSV yang bot kita buat tadi
        df = pd.read_csv('data_buku_besar.csv')

        # 2. Tukar kolum Harga kepada nombor (float)
        df['Harga (GBP)'] = df['Harga (GBP)'].astype(float)

        # 3. Lukis Graf
        plt.figure(figsize=(10, 6))
        plt.hist(df['Harga (GBP)'], bins=10, color='skyblue', edgecolor='black')
        
        # Tambah tajuk dan label
        plt.title('Taburan Harga Buku - Projek NexusData UKM', fontsize=14)
        plt.xlabel('Harga (GBP)', fontsize=12)
        plt.ylabel('Bilangan Buku', fontsize=12)
        plt.grid(axis='y', alpha=0.75)

        # 4. Simpan graf sebagai gambar
        plt.savefig('analisis_harga.png')
        print("✅ Graf berjaya dijana dan disimpan sebagai 'analisis_harga.png'!")
        plt.show()

    except Exception as e:
        print(f"Ralat semasa menjana graf: {e}")

if __name__ == "__main__":
    jana_graf()