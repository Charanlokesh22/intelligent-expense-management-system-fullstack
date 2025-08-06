
import joblib
import numpy as np

model = joblib.load('budget_model.pkl')

def predict_expense(month: int, income: float):
    features = np.array([[month, income]])
    predicted = model.predict(features)
    return round(predicted[0], 2)
