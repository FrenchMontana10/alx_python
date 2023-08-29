from flask import Flask, abort

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.errorhandler(404)
def not_found(error):
    return 'Not Found', 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
