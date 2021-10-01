'''PROGRAM DESCRIPITON:
	Create API REST server using python flask which:-
	1) displays the entire content of the data which has been deleted
	2) In update function, display which data has been updated to what(data before updation and after updation).
'''

#PROGRAMMED BY: Modika Ishwarya
#email-id:b18cs002@kitsw.ac.in
#DATE:21-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None

import requests
from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:002@localhost/guvi'

app.config['SECRET_KEY'] = 'ishwarya@0110'

db = SQLAlchemy(app)


# create a table inside our database
class APIUserModel(db.Model):
    __tablename__ = 'guvi_data_sciences'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    email = db.Column(db.String(20))


# insert data into database
@app.route('/write', methods=['POST'])
def insert():
    name = request.get_json()["name"]
    email = request.get_json()["email"]
    api_user_model = APIUserModel(name=name, email=email)
    save_to_database = db.session()
    try:
        save_to_database.add(api_user_model)
        save_to_database.commit()
    except:
        save_to_database.rollback()
        save_to_database.flush()

    return jsonify({"message": "success"})

# fetch data from server
@app.route('/', methods=['GET'])
def fetch_all():
    data = APIUserModel.query.all()
    data_all = []
    for data in data:
        data_all.append({"id":data.id, "name":data.name, "email":data.email})
    return jsonify(data_all)


# fetch data based on ID
@app.route('/display/<int:id>', methods=['GET'])
def fetch_by_id(id):
    try:
        data = APIUserModel.query.filter_by(id=id).first()
        return jsonify({"id":data.id, "name":data.name, "email":data.email})
    except:
        return jsonify({"message":"error"})



#update data
@app.route('/update/<int:id>', methods=['PATCH'])
def update(id):
    # update = insert + fetch by id
    name = request.get_json()["name"]
    email = request.get_json()["email"]
    save_to_database = db.session()
    try:


        api_user_model = APIUserModel.query.filter_by(id=id).first()
        old =  {"id":api_user_model.id, "name": api_user_model.name, "email": api_user_model.email}
        api_user_model.name = name
        api_user_model.email = email
        save_to_database.commit()
    except:

        save_to_database.rollback()
        save_to_database.flush()
        return jsonify({"message": "error in updating data"})
    id=api_user_model.id
    #after updating get data
    data=APIUserModel.query.filter_by(id=id).first()

    new={"id":data.id, "name":data.name, "email":data.email}
    return jsonify({"old":old,"new":new})


#delete data
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    try:

        save_to_database = db.session()
        data = APIUserModel.query.filter_by(id=id).first()
        deleted={"id":data.id, "name":data.name, "email":data.email}
        APIUserModel.query.filter_by(id=id).delete()
        save_to_database.commit()

    except:
        return jsonify({"message":"error in deleting data"})
    return jsonify({"deleted data":deleted})



if __name__ == '__main__':
    db.create_all()
    app.run(debug=True, port=5000)