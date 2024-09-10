#!/usr/bin/env python3
"""
Flask app with Babel internationalization support and locale parameter.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config:
    """
    Configuration class for Flask-Babel.

    Attributes:
        LANGUAGES (list): Supported languages for the app.
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


@babel.localeselector
def get_locale():
    """
    Select the best matching language based on the client's request
    or the `locale` parameter in the URL.

    Returns:
        str: The best matching language from the supported languages.
    """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the home page with a welcome message.

    Returns:
        str: Rendered HTML for the index page.
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
