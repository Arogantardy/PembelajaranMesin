# predict.py
import joblib
import pandas as pd
import warnings

# Mengabaikan warning dari sklearn karena kita tidak memasukkan feature names secara spesifik
warnings.filterwarnings("ignore", category=UserWarning)

def load_model(model_path='best_svm_hepatitis.joblib'):
    """Memuat model yang sudah dilatih dari disk."""
    try:
        return joblib.load(model_path)
    except FileNotFoundError:
        print(f"[ERROR] File {model_path} tidak ditemukan. Jalankan 'train.py' terlebih dahulu.")
        return None

def predict_patient(model, patient_data):
    """Menerima dictionary data pasien, memproses, dan memprediksi."""
    # Konversi dictionary ke DataFrame (1 baris)
    df_patient = pd.DataFrame([patient_data])
    
    # 1. Preprocessing data pasien baru (Sama seperti data_generator)
    # Mapping Sex: 'm' -> 1, 'f' -> 0
    if 'Sex' in df_patient.columns:
        df_patient['Sex'] = df_patient['Sex'].map({'m': 1, 'f': 0})
    
    # Pastikan urutan kolom sesuai dengan saat training (mengacu pada dataset asal)
    kolom_urut = ['Age', 'Sex', 'ALB', 'ALP', 'ALT', 'AST', 'BIL', 'CHE', 'CHOL', 'CREA', 'GGT', 'PROT']
    df_patient = df_patient[kolom_urut]
    
    # 2. Lakukan Prediksi
    prediksi = model.predict(df_patient)
    return prediksi[0]

if __name__ == "__main__":
    # Contoh penggunaan (Simulasi pasien baru dari UGD/Laboratorium)
    print("=== SISTEM PREDIKSI HEPATITIS C ===")
    
    model_svm = load_model()
    
    if model_svm:
        # Contoh data pasien suspek/donor yang perlu diperiksa
        pasien_baru = {
            'Age': 45, 
            'Sex': 'm', 
            'ALB': 39.0, 
            'ALP': 60.0, 
            'ALT': 45.0, 
            'AST': 35.0, 
            'BIL': 10.0, 
            'CHE': 8.0, 
            'CHOL': 5.0, 
            'CREA': 80.0, 
            'GGT': 40.0, 
            'PROT': 70.0
        }
        
        print("\nMemproses data laboratorium pasien...")
        hasil_diagnosis = predict_patient(model_svm, pasien_baru)
        print(f"\n[HASIL DIAGNOSIS] Pasien ini diklasifikasikan sebagai: {hasil_diagnosis.upper()}")