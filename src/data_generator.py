# data_generator.py
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE

def load_dataset(filepath='HepatitisCdata.csv'):
    """Memuat data dan menghapus kolom yang berpotensi menyebabkan data leakage."""
    df = pd.read_csv(filepath)
    if 'Unnamed: 0' in df.columns:
        df = df.drop(columns=['Unnamed: 0'])
    return df

def preprocess_data(df):
    """Melakukan imputasi nilai kosong dan pemetaan kategorikal."""
    # 1. Imputasi nilai kosong (Missing Values) dengan Nilai Median tiap Kelas
    for col in df.select_dtypes(include=[np.number]).columns:
        if df[col].isnull().any():
            df[col] = df.groupby('Category')[col].transform(lambda x: x.fillna(x.median()))
            
    # 2. Pemisahan Fitur (X) dan Target (y)
    X = df.drop(columns=['Category'])
    y = df['Category']
    
    # 3. Mapping Fitur Kategorikal (Sex: m=1, f=0)
    if 'Sex' in X.columns:
        X['Sex'] = X['Sex'].map({'m': 1, 'f': 0})
        
    return X, y

def get_train_test_split(X, y, test_size=0.20, random_state=42):
    """Membagi data menggunakan Stratified Split."""
    return train_test_split(X, y, test_size=test_size, stratify=y, random_state=random_state)

def apply_smote(X_train, y_train, random_state=42):
    """Menerapkan teknik SMOTE untuk menyeimbangkan kelas."""
    smote = SMOTE(random_state=random_state)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)
    return X_train_res, y_train_res