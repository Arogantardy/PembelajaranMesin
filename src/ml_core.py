# ml_core.py
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, balanced_accuracy_score, f1_score

def get_base_models():
    """Menginisialisasi algoritma baseline."""
    return {
        "KNN": KNeighborsClassifier(),
        "NaiveBayes": GaussianNB(),
        "SVM": SVC(probability=True) # probability=True dibutuhkan jika ingin melihat persentase probabilitas
    }

def get_hyperparameter_grids():
    """Mengembalikan grid parameter untuk proses tuning."""
    return {
        "KNN": {
            'n_neighbors': [3, 5, 7, 9],
            'weights': ['uniform', 'distance']
        },
        "SVM": {
            'C': [0.1, 1, 10],
            'gamma': [0.01, 0.1, 'scale'],
            'kernel': ['rbf']
        }
    }

def optimize_model(model, param_grid, X_train, y_train, cv=5, scoring='f1_macro'):
    """Melakukan Hyperparameter Tuning menggunakan GridSearchCV."""
    grid = GridSearchCV(model, param_grid, cv=cv, scoring=scoring, n_jobs=-1)
    grid.fit(X_train, y_train)
    return grid.best_estimator_, grid.best_params_

def evaluate_model(model, X_test, y_test, model_name="Model"):
    """Fungsi standar untuk mengevaluasi model dan mencetak metrik utama."""
    y_pred = model.predict(X_test)
    print(f"\n--- Evaluasi {model_name} ---")
    print(f"Accuracy         : {accuracy_score(y_test, y_pred):.4f}")
    print(f"Balanced Accuracy: {balanced_accuracy_score(y_test, y_pred):.4f}")
    print(f"Macro F1-Score   : {f1_score(y_test, y_pred, average='macro'):.4f}")
    print("\nClassification Report:\n", classification_report(y_test, y_pred))