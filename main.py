from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def hello1():
    return render_template('index.html')

@app.route("/about")
def hello2():
    name= 'Kirti'
    return render_template('about.html',name=name)
app.run(debug=True)
