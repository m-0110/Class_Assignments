'''
PROGRAM DESCRIPTION:

Create three endpoints using flask
'''

#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:21-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None



from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

#create object
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/home") # creating url to view
def home(): # function is view
    return "welcome to home page"

@app.route("/index")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True,port=5000)
