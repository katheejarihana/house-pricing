import joblib
import pandas as pd

model = joblib.load("models/house_price_model.pkl")

sample = {
    "area":[4000],
    "bedrooms":[2],
    "bathrooms":[2],
    "stories":[0],
    "mainroad":[1],
    "guestroom":[0],
    "basement":[0],
    "hotwaterheating":[0],
    "airconditioning":[0],
    "parking":[1],
    "prefarea":[1],
    "furnishingstatus":[0]
}

df = pd.DataFrame(sample)

prediction = model.predict(df)

print(f"Predicted House Price: {prediction[0]:.2f}")