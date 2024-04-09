#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def route():
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
