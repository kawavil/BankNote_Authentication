from flask import Flask, request, render_template
from BankNote import BankNote
import pickle

app = Flask("")


pickle_in = open("classifier.pkl", 'rb')
model = pickle.load(pickle_in)


@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/", methods=['POST'])
def predict():
    data = [int(x) for x in request.form.values()]

    variance = data[0]
    skewness = data[1]
    curtosis = data[2]
    entropy = data[3]
    prediction_result = model.predict([[variance, skewness, curtosis, entropy]])
    if prediction_result[0] > 0.5:
        result = "This is fake note"

    else:
        result = "This is Bank Note"
    return render_template('index.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)



