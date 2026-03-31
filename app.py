from flask import Flask, render_template, request
from model import get_price_details

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/result", methods=["POST"])
def result():

    phone = request.form["model"]

    details = get_price_details(phone)

    return render_template("result.html", details=details)


if __name__ == "__main__":
    app.run()