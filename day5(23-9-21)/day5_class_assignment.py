'''
PROGRAM DESCRIPTION
using flask_sqlalchemy create tables and columns
'''


#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:21-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None


from flask import Flask
from flask import render_template
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:002@localhost/mydb'

app.config['SECRET_KEY'] = 'ishwarya@0110'

db = SQLAlchemy(app)

# create a table inside our database
class APIUserModel(db.Model):
    __tablename__ = 'guvi_data_sciences'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))

# create a table2 inside our database
class APIUserModel2(db.Model):
    __tablename__ = 'machine_learning'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)
