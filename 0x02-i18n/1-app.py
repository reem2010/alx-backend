#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
app.url_map.strict_slashes = False


class Config(object):
    """configure class"""
    LANGUAGES = ["en", "fr"],
    BABEL_DEFAULT_LOCALE = "en",
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route("/")
def route():
    """route func"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
