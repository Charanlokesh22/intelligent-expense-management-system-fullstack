
from fastapi import FastAPI
from pydantic import BaseModel
from predictor import predict_expense

app = FastAPI()

class BudgetRequest(BaseModel):
    month: int
    income: float

@app.post("/predict")
def get_budget_suggestion(data: BudgetRequest):
    suggestion = predict_expense(data.month, data.income)
    return {"suggested_budget": suggestion}
