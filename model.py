import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Dummy training dataset
data = {
    'month': [1, 2, 3, 4, 5, 6],
    'expenses': [4000, 4200, 4100, 4300, 3900, 4400],
    'income': [7000, 7100, 7050, 7200, 6900, 7300]
}
df = pd.DataFrame(data)

X = df[['month', 'income']]
y = df['expenses']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, 'budget_model.pkl')


