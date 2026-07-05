# api_fastapi.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.predict import load_model, predict_patient

app = FastAPI(
    title="Hepatitis C Prediction API",
    description="API untuk memprediksi penyakit Hepatitis C menggunakan model SVM.",
    version="1.0.0"
)

# Load model saat server menyala
model = load_model('models/best_svm_hepatitis.joblib')

# Skema Validasi Input Data Pasien
class PatientData(BaseModel):
    Age: int
    Sex: str
    ALB: float
    ALP: float
    ALT: float
    AST: float
    BIL: float
    CHE: float
    CHOL: float
    CREA: float
    GGT: float
    PROT: float

    class Config:
        json_schema_extra = {
            "example": {
                "Age": 45, "Sex": "m", "ALB": 39.0, "ALP": 60.0, 
                "ALT": 20.0, "AST": 25.0, "BIL": 10.0, "CHE": 8.0, 
                "CHOL": 5.0, "CREA": 70.0, "GGT": 22.0, "PROT": 70.0
            }
        }

@app.get("/")
def home():
    return {"message": "Selamat datang di API Prediksi Hepatitis C. Kunjungi /docs untuk mencoba API."}

@app.post("/predict")
def get_prediction(data: PatientData):
    if model is None:
        raise HTTPException(status_code=500, detail="Model gagal dimuat di server.")
    
    try:
        # Pydantic v1 menggunakan .dict(), di v2 disarankan .model_dump()
        patient_dict = data.dict() if hasattr(data, 'dict') else data.model_dump()
        
        # Panggil fungsi predict dari predict.py
        hasil = predict_patient(model, patient_dict)
        return {
            "status": "success",
            "prediction": str(hasil),
            "input_data": patient_dict
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Terjadi kesalahan saat memprediksi: {str(e)}")