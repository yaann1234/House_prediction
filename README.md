# 🏠 Prediksi Harga Rumah Jakarta

Aplikasi web prediksi harga rumah di wilayah Jakarta berbasis machine learning menggunakan algoritma **Random Forest Regressor**.

---

## 📌 Tentang Proyek

Proyek ini dibangun sebagai bagian dari penelitian perbandingan algoritma **Regresi Linear** dan **Random Forest** untuk prediksi harga rumah di Jakarta. Berdasarkan hasil evaluasi, model Random Forest dipilih sebagai model terbaik dengan performa:

| Metrik | Nilai |
|--------|-------|
| R² Score | 0.8531 |
| MAE | 0.2495 |
| RMSE | 0.3563 |

---

## ✨ Fitur Aplikasi

- Input spesifikasi properti (luas tanah, luas bangunan, kamar tidur, kamar mandi, carport, lokasi)
- Estimasi harga otomatis berbasis model Random Forest
- Rentang harga batas bawah dan batas atas

---

## 🗂️ Struktur Folder

```
prediksi-harga-jakarta/
├── app.py               # Aplikasi Streamlit
├── requirements.txt     # Library yang dibutuhkan
├── README.md            # Dokumentasi proyek
└── model/
    └── rf_model.pkl     # Model Random Forest yang telah dilatih
```

---

## ⚙️ Cara Menjalankan Secara Lokal

1. Clone repository ini:
   ```bash
   git clone https://github.com/username/prediksi-harga-jakarta.git
   cd prediksi-harga-jakarta
   ```

2. Install library yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

3. Jalankan aplikasi:
   ```bash
   streamlit run app.py
   ```

---

## 📦 Library yang Digunakan

- [Streamlit](https://streamlit.io/) — framework aplikasi web
- [Scikit-learn](https://scikit-learn.org/) — model machine learning
- [Pandas](https://pandas.pydata.org/) — pengolahan data
- [NumPy](https://numpy.org/) — komputasi numerik

---

## 📊 Dataset

Dataset berupa listing rumah di wilayah Jakarta yang diperoleh dari platform properti online, terdiri dari **10.000 data** dengan variabel:

- `price` — harga rumah
- `city` — kota administrasi (Jakarta Barat, Pusat, Selatan, Timur, Utara)
- `bed_rooms` — jumlah kamar tidur
- `bath_rooms` — jumlah kamar mandi
- `carport` — jumlah carport
- `land_area` — luas tanah (m²)
- `building_area` — luas bangunan (m²)

---

## 👤 Author

**Gemma Althaf Hayyan Naqi**  
Sistem Informasi, UIN Syarif Hidayatullah  
gemma.althaf24@mhs.uinjkt.ac.id
