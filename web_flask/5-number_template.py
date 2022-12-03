#!/usr/bin/python3
""" script that starts a Flask web application
    listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C <text>”
        /python/<text>: display "Python <text>"
        /number/<n>: display “n is a number”
        /number_template/<n>: display a HTML page
"""
from flask import Flask
from flask import render_template
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


@app.route('/python/', strict_slashes=False)
@app.route('/python/<cleantext>', strict_slashes=False)
def pythonroute(cleantext='is cool'):
    """ display “Python ” followed by the value
        of the text variable
        (replace underscore _ symbols with a space)

    Args:
        cleantext: user's text input
    """
    newtext = cleantext.replace('_', ' ')
    return "Python {}".format(newtext)


@app.route('/number/<int:n>', strict_slashes=False)
def numberroute(n):
    """ display “n is a number” only if n is an integer

    Args:
        n: integer number that user insert in the route.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def templateroute(n):
    """ display a HTML page only if n is an integer:
            H1 tag: “Number: n” inside the tag BODY

    Args:
        n: integer number that user insert in the route.
    """
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
