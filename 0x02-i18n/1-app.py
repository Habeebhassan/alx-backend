#!/usr/bin/env python3
"""
Basic Flask app setup with Babel for i18n support.
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Configuration class for Flask-Babel.

    Attributes:
        LANGUAGES (list): Available languages for the app.
        BABEL_DEFAULT_LOCALE (str): Default locale for the app.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Apply the configuration to the Flask app
app.config.from_object(Config)

# Initialize Babel with the Flask app
babel = Babel(app)


@app.route('/')
def index():
    """
    Render the home page with a welcome message.

    Returns:
        str: Rendered HTML for the index page.
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
