from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello1():
    return "Hello World!"


@app.route("/kirti")
def hello2():
    return "Hello Everyone"
app.run(debug=True)
