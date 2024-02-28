#!/bin/python

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html")

#run aplication
if __name__ == '__main__':
    app.run(debug=True)
	#app.run(host="0.0.0.0", port=80)
