import random

import requests
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/health")
def health():
    return "healthy"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/get_quote")
def quote():
    # quote = requests.get("http://gen:5000/quote").text
    # print("quote - ", quote)

    # return render_template("quote.html", quote=quote)

    r = requests.get('http://week2-devops-nginx_web1-1/quote')
    quote = r.text
    print("quote - ", quote)
    return render_template("quote.html", quote=quote)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5001)
