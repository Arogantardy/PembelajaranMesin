# app_gradio.py
import gradio as gr
from src.predict import load_model, predict_patient

# Load Model di awal
model = load_model('models/best_svm_hepatitis.joblib')

def predict_gradio(age, sex, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot):
    if model is None:
        return "Error: Model tidak ditemukan."
        
    patient_data = {
        'Age': age, 'Sex': sex, 'ALB': alb, 'ALP': alp, 'ALT': alt,
        'AST': ast, 'BIL': bil, 'CHE': che, 'CHOL': chol, 'CREA': crea,
        'GGT': ggt, 'PROT': prot
    }
    hasil = predict_patient(model, patient_data)
    return str(hasil)

# Desain Antarmuka Gradio
with gr.Blocks(title="Hepatitis C Predictor") as app:
    gr.Markdown("# 🩺 Sistem Prediksi Hepatitis C (SVM Model)")
    gr.Markdown("Aplikasi sederhana untuk memprediksi kategori/stadium hepatitis C berdasarkan data lab pasien.")
    
    with gr.Row():
        with gr.Column():
            age = gr.Number(label="Age", value=45)
            sex = gr.Radio(choices=["m", "f"], label="Sex (m=Male, f=Female)", value="m")
            alb = gr.Number(label="ALB", value=39.0)
            alp = gr.Number(label="ALP", value=60.0)
            alt = gr.Number(label="ALT", value=20.0)
            ast = gr.Number(label="AST", value=25.0)
            
        with gr.Column():
            bil = gr.Number(label="BIL", value=10.0)
            che = gr.Number(label="CHE", value=8.0)
            chol = gr.Number(label="CHOL", value=5.0)
            crea = gr.Number(label="CREA", value=70.0)
            ggt = gr.Number(label="GGT", value=22.0)
            prot = gr.Number(label="PROT", value=70.0)
            
    btn = gr.Button("Prediksi Sekarang", variant="primary")
    output = gr.Textbox(label="Hasil Prediksi Kategori")
    
    btn.click(fn=predict_gradio, 
              inputs=[age, sex, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot], 
              outputs=output)

if __name__ == "__main__":
    app.launch()