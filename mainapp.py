from fastapi import FastAPI
from BankNote import BankNote
import pandas as pd
import pickle
import uvicorn


app = FastAPI()

pickle_in = open('classifier.pkl', 'rb')
model = pickle.load(pickle_in)


@app.get("/")
def index():
    return "Hello"


@app.post('/predict')
def predict(data: BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy = data['entropy']
    prediction_result = model.predict([[variance, skewness, curtosis, entropy]])
    if prediction_result[0] > 0.5:
        prediction= "This is Fake Note"
    else:
        prediction = "This is Bank Note"
    return {"prediction": prediction}


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)

