#!/usr/bin/env python3
"""
Basic Flask app setup.
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """
    Render the home page with a welcome message.

    Returns:
        str: Rendered HTML for the index page.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)