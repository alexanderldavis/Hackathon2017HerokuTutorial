from flask import Flask, render_template, request, Response, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/exampleMath", methods=["GET", "POST"])
def exampleMath():
    numberOne = request.form['numberOne']
    numberTwo = request.form['numberTwo']
    finalSum = int(numberOne) + int(numberTwo)
    return render_template('add.html', sum=finalSum)
