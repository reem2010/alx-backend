#!/usr/bin/env python3
"""starts a Flask web application"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id) -> Dict:
    """get user function"""
    if (user_id and int(user_id) in users):
        return users[int(user_id)]
    return None


class Config():
    """configure class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """get locale"""
    locale = request.args.get('locale')
    if (locale in Config.LANGUAGES):
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


@app.before_request
def before_request():
    """before request func"""
    id = request.args.get('login_as')
    g.user = get_user(id)


@app.route('/')
def index():
    """route func"""
    name = None
    if (g.user):
        name = g.user["name"]
    return render_template('6-index.html', name=name)


if __name__ == '__main__':
    app.run()
