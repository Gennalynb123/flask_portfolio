# import "packages" from flask
from flask import Flask, request, render_template
from image import image_data

# create a Flask instance
app = Flask(__name__)


# connects default URL to render index.html
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Results/')
def Results():
    return render_template("Results.html")

@app.route('/Song/')
def Song():
    return render_template("Song.html")

@app.route('/Test/')
def Test():
    return render_template("Test.html")

@app.route('/Lorde/')
def Lorde():
    return render_template("Lorde.html")

@app.route('/Gennalyn/')
def Gennalyn():
    return render_template("Gennalyn.html")

@app.route('/BTS/')
def BTS():
    return render_template("BTS.html")


@app.route('/DojaCat/')
def DojaCat():
    return render_template("DojaCat.html")



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


@app.route('/Bimary/')
def Bimary():
    return render_template("Bimary.html")


@app.route('/Home/')
def Home():
    return render_template("Home.html")


@app.route('/LogicGate/')
def LogicGate():
    return render_template("LogicGate.html")


@app.route('/ColorCode/')
def ColorCode():
    return render_template("ColorCode.html")


@app.route('/binaryAddition/')
def binaryAddition():
    return render_template("binaryAddition.html")


@app.route('/binarySignedAddition/')
def binarySignedAddition():
    return render_template("binarySignedAddition.html")


@app.route('/rgb/')
def rgb():
    return render_template("rgb.html", images=image_data())




@app.route('/GENNALYN', methods=['GET', 'POST'])
def GENNALYN():
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
            return render_template("Lucas.html", name=name)
    # starting and empty input default
    return render_template("Lucas.html", name="World")


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


@app.route('/retake', methods=['GET', 'POST'])
def retake():
    # submit button has been pushed
    if request.form:
        name = request.form.get("name")
        return render_template("Test.html", name=name)
    # starting and empty input default


@app.route('/binary/', methods=['GET', 'POST'])
def binary():
    if request.method == "POST":
        if request.form:
            bitNumber = request.form.get("bits")
            if len(bitNumber) != 0:  # input field has content
                return render_template("bimary.html", BITS=int(bitNumber), imageOn="imgBulbOn", imageOff="imgBulbOff")
        # starting and empty input default
        if request.form["bits2"]:
            return render_template("bimary.html", BITS=8, imageOn="imgBulbOn", imageOff="imgBulbOff")
    return render_template("bimary.html", BITS=8, imageOn="imgBulbOn", imageOff="/imgBulbOff")









# runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)

