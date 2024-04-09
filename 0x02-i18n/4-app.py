#!/usr/bin/python3
"""starts a Flask web application"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """configure class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.route('/')
def index():
    """route func"""
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
