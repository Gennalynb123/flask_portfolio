# import "packages" from flask
from flask import Flask, request, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Test/')
def Test():
    return render_template("Test.html")


@app.route('/Results/')
def Results():
    return render_template("Results.html")



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


@app.route('/Binary/')
def Binary():
    return render_template("Binary.html")


@app.route('/Home/')
def Home():
    return render_template("Home.html")



@app.route('/Genna', methods=['GET', 'POST'])
def Genna():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Gennalyn.html", name=name)
    # starting and empty input default
    return render_template("Gennalyn.html", name="World")


@app.route('/JUN', methods=['GET', 'POST'])
def JUN():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Jun.html", name=name)
    # starting and empty input default
    return render_template("Jun.html", name="World")


@app.route('/LUCAS', methods=['GET', 'POST'])
def LUCAS():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Jun.html", name=name)
    # starting and empty input default
    return render_template("Jun.html", name="World")


@app.route('/RITHWIKH', methods=['GET', 'POST'])
def RITHWIKH():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Rithwikh.html", name=name)
    # starting and empty input default
    return render_template("Rithwikh.html", name="World")


@app.route('/ALI', methods=['GET', 'POST'])
def ALI():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Ali.html", name=name)
    # starting and empty input default
    return render_template("Ali.html", name="World")



@app.route('/BINARY', methods=['GET', 'POST'])
def BINARY():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        if len(name) != 0:  # input field has content
            return render_template("Binary.html", name=name)
    # starting and empty input default
    return render_template("Binary.html", name="World")







# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

