import streamlit as st
import pandas as pd
import os
import main  # Mengimport logik dari main.py

# 1. Konfigurasi Halaman
st.set_page_config(
    page_title="NexusData AI | Analisis Pasaran",
    page_icon="📊",
    layout="wide"
)

# 2. CSS Khas untuk Rupa Kreatif & Profesional
st.markdown("""
    <style>
    /* Latar belakang utama */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    /* Gaya Kad Metrik */
    [data-testid="stMetricValue"] {
        color: #007bff;
        font-size: 30px;
    }
    /* Kad Rumusan AI */
    .ai-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        border-left: 5px solid #6c5ce7;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        color: #2d3436;
        line-height: 1.6;
    }
    /* Butang Gradient */
    div.stButton > button:first-child {
        background: linear-gradient(to right, #6a11cb 0%, #2575fc 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    div.stButton > button:first-child:hover {
        transform: scale(1.02);
        box-shadow: 0 10px 20px rgba(0,0,0,0.15);
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Sidebar Kawalan
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2103/2103633.png", width=80)
    st.title("Kawalan NexusData")
    st.write("---")
    st.markdown("### Tetapan Bot")
    st.caption("Automasikan pengumpulan data dan analisis AI dengan satu klik.")
    
    run_bot = st.button("🚀 JALANKAN ANALISIS LANGSUNG")
    st.write("---")
    st.success("Status Sistem: Aktif")

# 4. Papan Pemuka Utama (Dashboard)
st.title("📊 NexusData: Analisis Pasaran Pintar")
st.markdown("Mentransformasi data web mentah kepada **wawasan perniagaan** secara automatik.")

# Logik apabila butang ditekan
if run_bot:
    with st.spinner("🤖 Bot sedang melayar web & AI sedang menjana wawasan..."):
        try:
            main.run_all()
            st.balloons() 
        except Exception as e:
            st.error(f"Ralat berlaku: {e}")

# Paparan Hasil
if os.path.exists('data_buku_besar.csv'):
    df = pd.read_csv('data_buku_besar.csv')
    
    # Bahagian Metrik Pintar
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Jumlah Produk", len(df), "Langsung")
    with c2:
        df['Harga_Num'] = df['Harga'].str.replace('£', '').astype(float)
        st.metric("Purata Harga", f"£{df['Harga_Num'].mean():.2f}")
    with c3:
        st.metric("Enjin AI", "Llama 3.1", "Groq Cloud")

    st.markdown("---")

    # Susun Atur: Graf dan Jadual Data
    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("📈 Visualisasi Harga Pasaran")
        # Visualisasi data dengan tema ungu moden
        st.bar_chart(data=df, x="Nama Produk", y="Harga_Num", color="#6c5ce7")

    with col_right:
        st.subheader("📋 Suapan Data Mentah")
        st.dataframe(df[['Nama Produk', 'Harga']], height=300)

    # Bahagian Wawasan AI
    st.write("---")
    st.subheader("🧠 Rumusan Eksekutif AI")
    if os.path.exists('laporan_ai.txt'):
        with open('laporan_ai.txt', 'r', encoding='utf-8') as f:
            ai_text = f.read()
        
        st.markdown(f"""
        <div class="ai-card">
            {ai_text}
        </div>
        """, unsafe_allow_html=True)
else:
    st.info("👋 Selamat Datang! Klik butang **JALANKAN ANALISIS LANGSUNG** di sidebar untuk memulakan.")