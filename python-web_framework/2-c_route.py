"""here we import the flask module"""
from flask import Flask

"""we intialise the Flask module"""
app = Flask(__name__)


"""we declare the route of the resource"""
@app.route("/", strict_slashes = False)
def main():
    """here is the function that executes when that route is hit"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes = False)
def first():
    """this is the function"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes = False)
def second(text):
    """this is text"""
    modified = "C " + text.replace('_', ' ')
    return modified
if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)
    