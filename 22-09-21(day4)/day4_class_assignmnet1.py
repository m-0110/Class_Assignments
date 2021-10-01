'''
PROGRAM DESCRIPTION:

Create three endpoints
'''


#PROGRAMMED BY: Modika Ishwarya
#DATE:21-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None



from flask import Flask
from flask import render_template

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