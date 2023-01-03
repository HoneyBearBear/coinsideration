import os
import requests
import json

from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from markupsafe import escape

# setup app for use with filesystem sessions for login, flash
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['TESTING'] = True
app.config['SECRET_KEY'] = '37c2d8dceef6e5d972c9ad0fbb8579527dcabf20862854555d8e7f653df4a006'
Session(app)

# export API_KEY='e035e126-11bf-4b0c-8f30-9f63b4d904e0'
api_key = os.environ.get("API_KEY")
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# coinmarketcap API setup
payload={}
headers = {
    'X-CMC_PRO_API_KEY': api_key,
    'Accept-Encoding': 'deflate, gzip',
    'Accept':'application/json'
}

# defines index with POST and GET methods
@app.route("/", methods=["GET","POST"])
def index():
    # if method is POST store form entry for youtube api search
    if request.method == "POST":

        # store escaped, lower case, stripped user input in the name variable, also formats to replace spaces with dashes to form proper slugs for API
        name = escape(request.form.get("name").lower().strip().replace(" ", "-"))

        # if no name is entered render index page and flash error message
        if not name:
            flash('Please enter a valid cryptocurrency name.')
            return render_template("index.html")


        # construct urls for API price and metadata
        url_meta = f"https://pro-api.coinmarketcap.com/v2/cryptocurrency/info?slug={name}"
        url_quote = f"https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest?slug={name}"

        response_meta = requests.request("GET", url_meta, headers=headers, data=payload)
        response_quote = requests.request("GET", url_quote, headers=headers, data=payload)

        coin = json.loads(response_meta.text)
        coin_quote = json.loads(response_quote.text)

        if coin['status']['error_code'] == 400:
            flash('Please enter a valid cryptocurrency name.')
            return render_template("index.html")
        else:
            return render_template("results.html", metadata=coin, quote=coin_quote, name=name)

    else:
        # else render home search template
        return render_template("index.html")