import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import plotly.express as px
import time

st.set_page_config(page_title="Web Analytics Tool", layout="wide")
st.title("📊 Web Analytics Monitoring Tool")
st.markdown("Analisis struktur konten dan performa respons website berdasarkan URL.")

# Input User
url_input = st.text_input("Masukkan URL Website (lengkap dengan http/https):", "https://www.example.com")
analyze_button = st.button("Analisis Sekarang")

if analyze_button:
    try:
        with st.spinner('Sedang menganalisis website...'):
            start_time = time.time()
            response = requests.get(url_input, timeout=10)
            end_time = time.time()
            
            # 1. Performa Dasar
            load_time = round(end_time - start_time, 2)
            status_code = response.status_code
            
            # 2. Parsing Konten
            soup = BeautifulSoup(response.text, 'html.parser')
            title = soup.title.string if soup.title else "Tidak ditemukan"
            links = soup.find_all('a')
            images = soup.find_all('img')
            headings = {
                "H1": len(soup.find_all('h1')),
                "H2": len(soup.find_all('h2')),
                "H3": len(soup.find_all('h3'))
            }

            # Menampilkan Metrik Utama
            col1, col2, col3, col4 = st.columns(4)
            col1.metric("Status Code", status_code)
            col2.metric("Load Time", f"{load_time} detik")
            col3.metric("Total Link", len(links))
            col4.metric("Total Gambar", len(images))

            st.divider()

            # Visualisasi Struktur Heading
            st.subheader("Visualisasi Struktur Heading")
            df_headings = pd.DataFrame(list(headings.items()), columns=['Tag', 'Jumlah'])
            fig = px.bar(df_headings, x='Tag', y='Jumlah', color='Tag', title="Distribusi Heading (H1-H3)")
            st.plotly_chart(fig)

            # Interpretasi (Untuk bahan laporan Word)
            st.subheader("📝 Interpretasi Hasil")
            if status_code == 200:
                st.success(f"Website '{title}' berhasil diakses dengan status OK.")
            else:
                st.warning(f"Website merespons dengan kode status {status_code}.")

            st.write(f"- **Kecepatan:** Waktu muat halaman adalah {load_time} detik. (Standar ideal < 2 detik).")
            st.write(f"- **SEO:** Ditemukan {headings['H1']} tag H1. Sebuah halaman idealnya memiliki tepat satu H1.")
            st.write(f"- **Konten:** Terdapat {len(links)} internal/external links dan {len(images)} gambar yang terdeteksi.")

    except Exception as e:
        st.error(f"Gagal menganalisis URL. Pastikan URL benar. Error: {e}")