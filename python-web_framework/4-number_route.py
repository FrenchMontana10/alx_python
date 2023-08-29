from flask import Flask, abort  # Import the Flask module and the 'abort' function
from urllib.parse import unquote  # Import the 'unquote' function from the 'urllib.parse' module

app = Flask(__name__)  # Create a Flask web application instance

@app.route('/', strict_slashes=False)  # Define a route for the root URL '/'
def hello_hbnb():
    return 'Hello HBNB!'  # Display "Hello HBNB!" when this route is accessed

@app.route('/hbnb', strict_slashes=False)  # Define a route for '/hbnb'
def hbnb():
    return 'HBNB'  # Display "HBNB" when this route is accessed

@app.route('/c/<text>', strict_slashes=False)  # Define a route with a dynamic 'text' parameter
def c(text):
    text = unquote(text.replace("_", " "))  # Decode and replace underscores with spaces in 'text'
    return 'C {}'.format(text)  # Display "C " followed by the 'text' value

@app.route('/python/', strict_slashes=False)  # Define a route for '/python/' with a default 'text' value
@app.route('/python/<path:text>', strict_slashes=False)  # Define a route for '/python/' with a dynamic 'text' parameter
def python(text='is cool'):
    text = unquote(text.replace("_", " "))  # Decode and replace underscores with spaces in 'text'
    return 'Python {}'.format(text)  # Display "Python " followed by the 'text' value

@app.route('/number/<int:n>', strict_slashes=False)  # Define a route for '/number/' with an integer parameter 'n'
def is_number(n):
    return '{} is a number'.format(n)  # Display "{} is a number" with the value of 'n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Start the Flask application on host 0.0.0.0 and port 5000
