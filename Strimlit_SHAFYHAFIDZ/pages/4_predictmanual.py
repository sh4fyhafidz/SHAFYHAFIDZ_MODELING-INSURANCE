import streamlit as st
import pandas as pd
import pickle

# Memuat model (sudah termasuk ColumnTransformer)
with open('ModelGradientSaf.sav', 'rb') as file:
    model = pickle.load(file)

# Judul aplikasi
st.title("Prediksi Default Kredit")

# Input pengguna
st.sidebar.header('Masukkan Informasi Pemegang Polis')
agency = st.sidebar.selectbox("Agency (Agency)", ['C2B', 'EPX', 'JZI', 'CWT', 'LWC', 'ART', 'CSR', 'SSI', 'RAB', 'KML', 'TST', 'TTW', 'JWT', 'ADM', 'CCR', 'CBH'])
agency_type = st.sidebar.selectbox("Tipe Agency (Agency Type)", ['Airlines','Travel Agency'])
channel = st.sidebar.selectbox("Strategi Pemasaran (Distribution Channel)", ['Online', 'Offline'])
product = st.sidebar.selectbox("Nama Produk (Product Name Bundle)", ['Cancellation Plans', 'Comprehensive Plans', 'Other Plans', 'Rental Plans', 'Basic Plans', 'Annual Plans', 'Specialty Plans', 'Single Trip Plans'])
duration = st.sidebar.number_input("Lama Waktu Perjalanan (Duration (dalam jam))", min_value=1.0, max_value=4881.0, value=50.0)
sales = st.sidebar.number_input("Jumlah Pendapatan (Net Sales)", min_value=1.0, max_value=283.5, value=10.0)
comission = st.sidebar.number_input("Jumlah Komisi (Commision (in value))", min_value=0.0, max_value=283.5, value=1.0)
age = st.sidebar.number_input("Umur (Age)", min_value=0.0, max_value=118.0, value=0.5)
region = st.sidebar.selectbox("Destinasi Wisata (Region)", ['ASIA', 'EUROPE', 'AUSTRALIA', 'AMERICA', 'AFRICA'])

# Dataframe input
input_data = pd.DataFrame({
    'Agency': [agency],
    'Agency Type': [agency_type],
    'Distribution Channel': [channel],
    'Product Name Bundle': [product],
    'Duration': [duration],
    'Net Sales': [sales],
    'Commision (in value)': [comission],
    'Age': [age],
    'Region': [region]
})

# Tampilkan data input
st.write("Data yang Anda masukkan:")
st.write(input_data)

# Tombol prediksi
if st.button('Prediksi Default Polis'):
    try:
        # Langsung prediksi tanpa encoding karena sudah termasuk di model
        prediction = model.predict(input_data)

        # Tampilkan hasil prediksi
        if prediction[0] == 1:
            st.success("Prediksi: **Default Polis** (1)")
        else:
            st.success("Prediksi: **Tidak Default Polis** (0)")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat prediksi: {e}")
