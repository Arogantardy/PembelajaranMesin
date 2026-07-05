# app_streamlit.py
import streamlit as st
from src.predict import load_model, predict_patient

# Konfigurasi Halaman
st.set_page_config(page_title="Hepatitis C Predictor", layout="centered")

st.title("Sistem Prediksi Hepatitis C")
st.write("Masukkan parameter biokimia darah pasien di bawah ini untuk melihat hasil prediksi berbasis model SVM.")

# Cache model agar tidak diload berulang kali setiap kali ada interaksi UI
# Cache model agar tidak diload berulang kali setiap kali ada interaksi UI
@st.cache_resource
def get_model():
    # Ubah path di bawah ini dengan menambahkan folder 'model/'
    return load_model('models/best_svm_hepatitis.joblib')

model = get_model()

if model is None:
    st.error("Model tidak ditemukan! Pastikan file 'best_svm_hepatitis.joblib' ada di direktori yang sama.")
else:
    # Form Input User
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age (Tahun)", min_value=1, max_value=120, value=45)
        sex = st.selectbox("Sex", options=["m", "f"], format_func=lambda x: "Laki-laki (m)" if x == "m" else "Perempuan (f)")
        alb = st.number_input("ALB", value=39.0)
        alp = st.number_input("ALP", value=60.0)
        
    with col2:
        alt = st.number_input("ALT", value=20.0)
        ast = st.number_input("AST", value=25.0)
        bil = st.number_input("BIL", value=10.0)
        che = st.number_input("CHE", value=8.0)
        
    with col3:
        chol = st.number_input("CHOL", value=5.0)
        crea = st.number_input("CREA", value=70.0)
        ggt = st.number_input("GGT", value=22.0)
        prot = st.number_input("PROT", value=70.0)

    # Tombol Prediksi
    if st.button("Lakukan Prediksi", type="primary"):
        patient_data = {
            'Age': age, 'Sex': sex, 'ALB': alb, 'ALP': alp, 'ALT': alt,
            'AST': ast, 'BIL': bil, 'CHE': che, 'CHOL': chol, 'CREA': crea,
            'GGT': ggt, 'PROT': prot
        }
        
        with st.spinner("Memproses data..."):
            hasil = predict_patient(model, patient_data)
            
        st.success("Prediksi Berhasil!")
        st.metric(label="Hasil Diagnosis (Kategori)", value=str(hasil))