from flask import Flask, render_template
app = Flask(__name__)

# 1) http://localhost:5000 - should display 8 by 8 checkerboard

@app.route('/')
def default():
    return render_template("index.html", boxesX=8, boxesY=8, color1="red", color2="black")

# 2) http://localhost:5000/4 - should display 8 by 4 checkerboard

@app.route('/<int:boxesY>')
def changeY(boxesY):
    return render_template("index.html", boxesX=8, boxesY=boxesY, color1="red", color2="black")

# 3) http://localhost:5000/(x)/(y) - should display x by y checkerboard.  For example, http://localhost:5000/10/10 should display 10 by 10 checkerboard.  Before you pass x or y to Jinja, please remember to convert it to integer first (so that you can use x or y in a for loop)

@app.route('/<int:boxesX>/<int:boxesY>')
def changeXandY(boxesX, boxesY):
    return render_template("index.html", boxesX=boxesX, boxesY=boxesY, color1="red", color2="black")

# SENSEI BONUS: Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render a checkerboard with x rows and y columns, with alternating colors, color1 and color2

@app.route('/<int:boxesX>/<int:boxesY>/<string:color1>/<string:color2>')
def changeXYandColor(boxesX, boxesY, color1, color2):
    return render_template("index.html", boxesX=boxesX, boxesY=boxesY, color1=color1, color2=color2)

# ----------------------------------------------
if __name__=="__main__":
    app.run(debug=True)