from crypt import methods
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def Home():
    return "a"

@app.route('/draw', methods= ['GET', 'POST'])
def draw():
    return "k"


if __name__ == '__main__':
    app.run(debug=True)