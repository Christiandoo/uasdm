import streamlit as st
import numpy as np
import pickle

# Load model yang sudah disimpan
model = pickle.load(open('model_uas.pkl', 'rb'))

# Judul aplikasi
st.title("Prediksi Premi Asuransi")

# Informasi NIM dan Nama
st.sidebar.write("NIM: 2021230040")
st.sidebar.write("Nama: Christiando Shaday Sihombing")

# Input dari pengguna
st.write("### Masukkan Data Anda")
age = st.number_input("Umur (tahun):", min_value=0, max_value=120, value=25)
sex = st.selectbox("Jenis Kelamin:", options=["Pria", "Wanita"])
bmi = st.number_input("BMI (Berat/Height^2):", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Jumlah Anak:", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Perokok:", options=["Tidak", "Ya"])

# Konversi input menjadi array
sex_encoded = 1 if sex == "Pria" else 0
smoker_encoded = 1 if smoker == "Ya" else 0

input_data = np.array([age, sex_encoded, bmi, children, smoker_encoded]).reshape(1, -1)

# Prediksi
if st.button("Submit"):
    prediction = model.predict(input_data)[0]
    st.write(f"### Prediksi Premi Asuransi: ${prediction:.2f} per bulan")
