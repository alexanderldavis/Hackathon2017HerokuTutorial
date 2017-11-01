from flask import Flask, render_template, request, Response, jsonify

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route("/exampleMath", methods=['GET'])
def exampleMath():
    numberOne = flask.request.form['numberOne']
    numberTwo = flask.request.form['numberTwo']
    finalSum = int(numberOne) + int(numberTwo)
    return render_template('add.html', sum=finalSum)
