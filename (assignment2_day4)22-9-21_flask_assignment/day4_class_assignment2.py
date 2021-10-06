'''
PROGRAM DESCRIPTION:
create three end points and add css and javascript
'''



#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:22-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/register')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
