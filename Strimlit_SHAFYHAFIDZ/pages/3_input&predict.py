import streamlit as st
import pandas as pd
import pickle

# Load model prediksi yang sudah disimpan
with open('Strimlit_SHAFYHAFIDZ/ModelGradientSaf.sav', 'rb') as file:
    model = pickle.load(file)

# Judul halaman
st.title("Prediksi Data (Batch) 📂")

# Header untuk bagian unggah file
st.header("Silahkan Unggah File Anda")

# Penjelasan singkat
st.write("""
Silakan unggah file data Anda untuk analisis. Pastikan file dalam format yang didukung, seperti:
- CSV (Comma-Separated Values)
- Excel (XLSX)

Setelah mengunggah file, aplikasi akan membaca data Anda, dan Anda dapat melanjutkan ke tahap prediksi.
""")

# Komponen untuk mengunggah file
uploaded_file = st.file_uploader(
    label="Pilih file Anda", 
    type=["csv", "xlsx"],  # Format file yang didukung
    help="Unggah file dalam format CSV atau Excel."
)

# Jika file diunggah, tampilkan nama file dan kontennya
if uploaded_file is not None:
    st.success(f"File '{uploaded_file.name}' berhasil diunggah!")
    st.write("Berikut adalah isi file yang Anda unggah:")
    
    # Membaca file berdasarkan format
    try:
        if uploaded_file.name.endswith('.csv'):
            data = pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            data = pd.read_excel(uploaded_file)
        
        st.dataframe(data)  # Menampilkan data dalam tabel
        
        # Pastikan data memiliki kolom yang sesuai untuk prediksi
        required_columns = ['Agency','Agency Type','Distribution Channel','Product Name Bundle','Duration','Net Sales','Commision (in value)','Age','Region']
        if all(col in data.columns for col in required_columns):
            st.success("Data memiliki semua kolom yang diperlukan untuk prediksi.")
            
            # Tombol untuk melanjutkan ke tahap prediksi
            if st.button("Lakukan Prediksi"):
                # Melakukan prediksi
                predictions = model.predict(data[required_columns])
                data['Prediction'] = predictions  # Menambahkan kolom prediksi
                
                st.write("Hasil Prediksi:")
                st.dataframe(data[['Prediction']])  # Menampilkan kolom prediksi
                
                # Simpan hasil prediksi ke file untuk diunduh
                csv = data.to_csv(index=False)
                st.download_button(
                    label="Unduh Hasil Prediksi",
                    data=csv,
                    file_name='predictions.csv',
                    mime='text/csv'
                )
        else:
            st.error(f"File Anda tidak memiliki kolom yang diperlukan: {', '.join(required_columns)}")
    except Exception as e:
        st.error(f"Terjadi kesalahan saat membaca file: {e}")
else:
    st.info("Silakan unggah file untuk memulai.")
