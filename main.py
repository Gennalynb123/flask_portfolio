# import "packages" from flask
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


# connects /kangaroos path to render kangaroos.html
@app.route('/kangaroos/')
def kangaroos():
    return render_template("kangaroos.html")


@app.route('/walruses/')
def walruses():
    return render_template("walruses.html")


@app.route('/hawkers/')
def hawkers():
    return render_template("hawkers.html")


@app.route('/stub/')
def stub():
    return render_template("stub.html")


@app.route('/Gennalyn/')
def Gennalyn():
    return render_template("Gennalyn.html")


@app.route('/Rithwikh/')
def Rithwikh():
    return render_template("Rithwikh.html")

@app.route('/Jun/')
def Jun():
    return render_template("Jun.html")


@app.route('/Lucas/')
def Lucas():
    return render_template("Lucas.html")


@app.route('/Ali/')
def Ali():
    return render_template("Ali.html")



# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
