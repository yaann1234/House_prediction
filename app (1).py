import streamlit as st
import numpy as np
import pandas as pd
import pickle
import os

st.set_page_config(
    page_title="Prediksi Harga Rumah Jakarta",
    page_icon="🏠",
    layout="centered"
)

st.markdown("""
<style>
.main-title {
    text-align: center;
    font-size: 28px;
    font-weight: 600;
    color: #185FA5;
    margin-bottom: 4px;
}
.sub-title {
    text-align: center;
    font-size: 14px;
    color: #6b7280;
    margin-bottom: 2rem;
}
.result-box {
    background: #E6F1FB;
    border-radius: 12px;
    padding: 1.5rem;
    text-align: center;
    margin: 1rem 0;
}
.result-label {
    font-size: 13px;
    color: #185FA5;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 6px;
}
.result-price {
    font-size: 32px;
    font-weight: 700;
    color: #0C447C;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def load_model():
    model_path = "rf_model.pkl"
    if not os.path.exists(model_path):
        st.error("❌ File model tidak ditemukan. Pastikan `model/rf_model.pkl` sudah ada.")
        st.stop()
    import gzip
    with gzip.open(model_path, 'rb') as f:
        return pickle.load(f)

rf = load_model()

def prediksi_harga(bed_rooms, bath_rooms, carport, land_area, building_area, kota):
    rumah = {
        'bed_rooms': bed_rooms,
        'bath_rooms': bath_rooms,
        'carport': carport,
        'land_area': land_area,
        'building_area': building_area,
        'city_Jakarta Pusat': 0,
        'city_Jakarta Selatan': 0,
        'city_Jakarta Timur': 0,
        'city_Jakarta Utara': 0
    }
    if kota == "Jakarta Pusat":
        rumah['city_Jakarta Pusat'] = 1
    elif kota == "Jakarta Selatan":
        rumah['city_Jakarta Selatan'] = 1
    elif kota == "Jakarta Timur":
        rumah['city_Jakarta Timur'] = 1
    elif kota == "Jakarta Utara":
        rumah['city_Jakarta Utara'] = 1

    rumah_df = pd.DataFrame([rumah])
    pred_log = rf.predict(rumah_df)
    return np.exp(pred_log)[0]

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-title">🏠 Prediksi Harga Rumah Jakarta</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Estimasi harga properti berbasis machine learning (Random Forest)</div>', unsafe_allow_html=True)

# ── Form ──────────────────────────────────────────────────────────────────────
with st.container(border=True):
    st.markdown("**Ukuran lahan**")
    col1, col2 = st.columns(2)
    with col1:
        land_area = st.number_input("Luas tanah (m²)", min_value=10, max_value=2000, value=150, step=10)
    with col2:
        building_area = st.number_input("Luas bangunan (m²)", min_value=10, max_value=2000, value=100, step=10)

    st.divider()
    st.markdown("**Fasilitas rumah**")
    col3, col4, col5 = st.columns(3)
    with col3:
        bed_rooms = st.number_input("Kamar tidur", min_value=1, max_value=14, value=3)
    with col4:
        bath_rooms = st.number_input("Kamar mandi", min_value=1, max_value=14, value=2)
    with col5:
        carport = st.number_input("Carport", min_value=0, max_value=4, value=1)

    st.divider()
    st.markdown("**Lokasi**")
    kota = st.selectbox("Kota administrasi", [
        "Jakarta Barat", "Jakarta Pusat", "Jakarta Selatan",
        "Jakarta Timur", "Jakarta Utara"
    ], label_visibility="collapsed")

    st.write("")
    prediksi = st.button("Hitung Estimasi Harga", use_container_width=True, type="primary")

# ── Hasil ─────────────────────────────────────────────────────────────────────
if prediksi:
    harga = prediksi_harga(bed_rooms, bath_rooms, carport, land_area, building_area, kota)

    st.markdown(f"""
    <div class="result-box">
        <div class="result-label">Estimasi Harga Properti · {kota}</div>
        <div class="result-price">Rp {harga:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.metric("Batas bawah (−15%)", f"Rp {harga * 0.85:,.0f}")
    with col_b:
        st.metric("Batas atas (+15%)", f"Rp {harga * 1.15:,.0f}")

    st.info("Prediksi menggunakan Random Forest Regressor. Harga sangat dipengaruhi oleh luas tanah dan luas bangunan.", icon="ℹ️")

st.caption("Model: RandomForestRegressor (n_estimators=100) · Dataset: Jakarta House Listing")
