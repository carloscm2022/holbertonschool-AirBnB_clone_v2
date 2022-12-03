#!/usr/bin/python3
""" script that starts a Flask web application
    listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C <text>”
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def rootroute():
    """display “Hello HBNB!”
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnbroute():
    """display "HBNB"
    """
    return "HBNB"


@app.route('/c/<cleantext>', strict_slashes=False)
def textroute(cleantext):
    """ display “C ” followed by the value
        of the text variable
        (replace underscore _ symbols with a space)

    Args:
        cleantext: user's text input
    """
    newtext = cleantext.replace('_', ' ')
    return "C {}".format(newtext)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
