# 📊 Web Analytics Monitoring Tool

> Analisis struktur konten dan performa respons website berdasarkan URL.

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-FF4B4B?logo=streamlit&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 🖥️ Demo

![App Screenshot](screenshot.png)

Masukkan URL website → klik **Analisis Sekarang** → dapatkan metrik performa + visualisasi struktur konten secara instan.

---

## ✨ Fitur

- 🔍 **Analisis URL real-time** — cukup masukkan URL, tool akan langsung crawl dan parse kontennya
- ⚡ **Metrik performa** — HTTP Status Code dan load time halaman
- 🔗 **Inventarisasi konten** — deteksi total link dan gambar pada halaman
- 📐 **Struktur heading** — distribusi H1–H3 sebagai indikator SEO
- 📊 **Visualisasi interaktif** — bar chart distribusi heading menggunakan Plotly
- 📝 **Interpretasi otomatis** — analisis langsung ditampilkan dalam bahasa natural

---

## 🛠️ Tech Stack

| Komponen | Library |
|---|---|
| UI / Frontend | [Streamlit](https://streamlit.io/) |
| HTTP Request | [Requests](https://docs.python-requests.org/) |
| HTML Parser | [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) |
| Data Processing | [Pandas](https://pandas.pydata.org/) |
| Visualisasi | [Plotly Express](https://plotly.com/python/plotly-express/) |

---

## 🚀 Cara Menjalankan

### 1. Clone repository ini

```bash
git clone https://github.com/username/web-analytics-tool.git
cd web-analytics-tool
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Jalankan aplikasi

```bash
streamlit run app.py
```

Aplikasi akan terbuka otomatis di browser pada `http://localhost:8501`.

---

## 📦 Requirements

Buat file `requirements.txt` dengan isi berikut:

```
streamlit
requests
beautifulsoup4
pandas
plotly
```

---

## 📋 Cara Pakai

1. Buka aplikasi di browser
2. Masukkan URL website **lengkap dengan `http://` atau `https://`**
   - Contoh: `https://monkeytype.com/`
3. Klik tombol **"Analisis Sekarang"**
4. Hasil analisis akan muncul dalam beberapa detik, meliputi:
   - Status Code & Load Time
   - Jumlah Link & Gambar
   - Distribusi Heading (H1–H3)
   - Interpretasi otomatis

---

## 📊 Contoh Output

Hasil analisis `https://monkeytype.com/`:

| Metrik | Nilai |
|---|---|
| Status Code | 200 (OK) ✅ |
| Load Time | 1.22 detik ✅ |
| Total Link | 12 |
| Total Gambar | 0 ⚠️ |
| Tag H1 | 0 ⚠️ |

> **Catatan:** Monkeytype adalah Single Page Application (SPA) berbasis JavaScript. Elemen dinamis seperti heading dan gambar mungkin tidak terdeteksi oleh scraper statis. Untuk hasil lebih akurat, pertimbangkan integrasi headless browser (Selenium/Playwright).

---

## ⚠️ Keterbatasan

- Tool ini menggunakan `requests` + `BeautifulSoup` (scraper statis), sehingga **konten yang dirender oleh JavaScript tidak akan terdeteksi**
- Beberapa website memblokir request dari scraper (akan muncul error timeout atau connection refused)
- Analisis dibatasi pada halaman utama URL yang dimasukkan, bukan seluruh website

---

## 👤 Penulis

**Ibrahim Gunawan** — 20240801282  
Tugas #01 · Data Mining

---

## 📄 Lisensi

Proyek ini dibuat untuk keperluan akademik.
