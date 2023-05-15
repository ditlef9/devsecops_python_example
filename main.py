"""
Main
File: main.py
Updated: 15.05.203 Ditlefsen
"""
import os
from pathlib import Path

import flask

app = flask.Flask(__name__)


# - Routes -----------------------------------------------------------------------------
# - Index ------------------------------------------------------------------------------
@app.route('/', methods=['GET', 'POST'])
def __index():
    print("__index() :: Init")

    return f"Hello from __index!", 200



if __name__ == '__main__':
    # Home
    home_path = str(Path.home())
    home_name = os.path.basename(os.path.normpath(home_path))

    # Lunch app
    if home_path == "/www-data-home" or home_path == "/home":
        # Lunch app in production
        app.run(debug=False, host="0.0.0.0", port=8080)
    else:
        # Lunch app in development
        app.run(debug=True, host="0.0.0.0", port=8080,
                ssl_context=('src/certificates/cert.pem', 'src/certificates/key.pem'))
