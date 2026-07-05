# train.py
import joblib
from src.data_generator import load_dataset, preprocess_data, get_train_test_split, apply_smote
from src.ml_core import get_base_models, get_hyperparameter_grids, optimize_model, evaluate_model

# sisa kode di bawahnya tetap sama...
from src.ml_core import get_base_models, get_hyperparameter_grids, optimize_model, evaluate_model

def main():
    print("[1] Memuat dan memproses data...")
    df = load_dataset('data/HepatitisCdata.csv')
    X, y = preprocess_data(df)
    
    print("[2] Membagi data (Train/Test Split)...")
    X_train, X_test, y_train, y_test = get_train_test_split(X, y)
    
    print("[3] Menyeimbangkan data latih dengan SMOTE...")
    X_train_res, y_train_res = apply_smote(X_train, y_train)
    
    models = get_base_models()
    grids = get_hyperparameter_grids()
    
    print("[4] Memulai proses Pelatihan (Training) dan Tuning...")
    best_svm_model = None
    
    for name, model in models.items():
        if name in grids:
            print(f"\n>> Mengoptimasi {name}...")
            best_model, best_params = optimize_model(model, grids[name], X_train_res, y_train_res)
            print(f"Parameter Terbaik {name}: {best_params}")
        else:
            print(f"\n>> Melatih {name} (Baseline)...")
            best_model = model
            best_model.fit(X_train_res, y_train_res)
        
        # Evaluasi dengan data Uji Asli (bukan data SMOTE)
        evaluate_model(best_model, X_test, y_test, model_name=f"{name} (Optimized)")
        
        # Menyimpan model terbaik berdasarkan analisis kita sebelumnya
        if name == "SVM":
            best_svm_model = best_model
            
    print("\n[5] Menyimpan model SVM terbaik ke disk...")
    print("\n[5] Menyimpan model SVM terbaik ke disk...")
    # Simpan model untuk keperluan deployment/prediksi
    joblib.dump(best_svm_model, 'best_svm_hepatitis.joblib')
    print("[✓] Model berhasil disimpan sebagai 'best_svm_hepatitis.joblib'")

if __name__ == "__main__":
    main()