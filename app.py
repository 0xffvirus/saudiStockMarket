from flask import Flask, jsonify
import yfinance as yf

app = Flask(__name__)

@app.route('/price/<ticker>')
def get_price(ticker):
    try:
        data = yf.Ticker(ticker).history(period="1d")
        price = round(data["Close"].iloc[-1], 2)
        return jsonify({"ticker": ticker, "price": price})
    except:
        return jsonify({"error": "could not get price"}), 500
