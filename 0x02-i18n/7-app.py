#!/usr/bin/env python3
"""
Flask app with Babel internationalization and time zone support.
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _
from typing import Optional, Dict
import pytz
from pytz.exceptions import UnknownTimeZoneError

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

# Mock user table
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id: Optional[int]) -> Optional[Dict]:
    """
    Retrieve a user dictionary based on the user ID or None if the user does not exist.

    Args:
        user_id (Optional[int]): The user ID to retrieve.

    Returns:
        Optional[Dict]: A dictionary containing user details or None.
    """
    if user_id is None or user_id not in users:
        return None
    return users.get(user_id)


@app.before_request
def before_request():
    """
    Set the current user before processing each request.
    """
    user_id = request.args.get('login_as')
    g.user = get_user(int(user_id)) if user_id else None


@babel.localeselector
def get_locale():
    """
    Select the best matching language based on the client's request,
    user settings, or the `locale` parameter in the URL.

    Returns:
        str: The best matching language from the supported languages.
    """
    # 1. Locale from URL parameters
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    
    # 2. Locale from user settings
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')

    # 3. Locale from request headers
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone() -> str:
    """
    Select the best matching time zone based on the client's request,
    user settings, or the default.

    Returns:
        str: A valid time zone.
    """
    # 1. Timezone from URL parameters
    timezone = request.args.get('timezone')
    if timezone:
        try:
            # Validate timezone
            pytz.timezone(timezone)
            return timezone
        except UnknownTimeZoneError:
            pass

    # 2. Timezone from user settings
    if g.user and g.user.get('timezone'):
        try:
            # Validate timezone
            pytz.timezone(g.user.get('timezone'))
            return g.user.get('timezone')
        except UnknownTimeZoneError:
            pass

    # 3. Default timezone
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route('/')
def index():
    """
    Render the home page with a welcome message.

    Returns:
        str: Rendered HTML for the index page.
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
