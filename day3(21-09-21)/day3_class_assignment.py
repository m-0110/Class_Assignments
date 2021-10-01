'''
PROGRAM DESCRIPTION:
Write a python program to insert the data present in the JSON file into your
MongoDB collection in form of documents one by one
'''


#PROGRAMMED BY: Modika Ishwarya
# MAIL ID : b18cs002@kitsw.ac.in
#DATE:22-09-2021
#PYTHON VERSION:3.8
#CAVEATS:None
#LICENSE:None

import pymongo
from pymongo import MongoClient
import json



#create class with all methods

class Mongo_test:
    #having connection as a attribute
    def __init__(self):
        self.connection=None

    #establish connection
    def establish_connection(self):
        self.connection=MongoClient("mongodb://localhost:27017/")
        if(self.connection):
            return True
        else:
            return False

    #getting list of databases
    def list_db(self):
        if(self.connection):
            return list(self.connection.list_database_names())

    #creating database
    def create_database(self,db_name):
        if (self.connection):
            db_list=self.list_db()
            if(self.db_exists(db_name)):
                print("database already exists")
            else:
                my_db=self.connection[db_name]
                print(db_name,"created")

    #check db exists or not
    def db_exists(self,db_name):
        if (self.connection):
            db_list = self.list_db()
            if(db_name in db_list):
                return True
            else:
                return False

    #create collection
    def create_new_collection(self, db_name, new_collection):
        if self.connection:
            db_name = self.connection[db_name]
            collection = db_name[new_collection]
            return True
        else:
            return ("error")

    #insert
    def insert_from_jsonfile(self,db_name,collection_name,file):
        if self.connection:
            with open(file, "r") as f:
                file = json.load(f)
            db_name = self.connection[db_name]
            collection = db_name[collection_name]

            #insert one by one document into collection
            for i in file:
                collection.insert_one(i)
        else:
            return "error"

    #display documents in collection
    def display_collection(self,db_name,collection_name):
        if self.connection:

            db_name = self.connection[db_name]
            collection = db_name[collection_name]
            result=collection.find()

            print('documents in collection ',collection_name)
            for i in result:
                print(i)

        else:
            return "error"



#create object
s1=Mongo_test()

s1.establish_connection()

database_name="mydb"
s1.create_database(database_name)

#print(s1.db_exists(database_name))
collection_name="customer"

s1.create_new_collection(database_name,collection_name)

s1.insert_from_jsonfile(database_name,collection_name,"file1.json")

s1.display_collection(database_name,collection_name)



#output on execution

'''


database already exists
documents in collection  customer
{'_id': 1, 'name': 'John', 'address': 'Highway 37'}
{'_id': 2, 'name': 'Peter', 'address': 'Lowstreet 27'}
{'_id': 3, 'name': 'Amy', 'address': 'Apple st 652'}
{'_id': 4, 'name': 'Hannah', 'address': 'Mountain 21'}
{'_id': 5, 'name': 'Michael', 'address': 'Valley 345'}
{'_id': 6, 'name': 'Sandy', 'address': 'Ocean blvd 2'}
{'_id': 7, 'name': 'Betty', 'address': 'Green Grass 1'}
{'_id': 8, 'name': 'Richard', 'address': 'Sky st 331'}
{'_id': 9, 'name': 'Susan', 'address': 'One way 98'}
{'_id': 10, 'name': 'Vicky', 'address': 'Yellow Garden 2'}
{'_id': 11, 'name': 'Ben', 'address': 'Park Lane 38'}
{'_id': 12, 'name': 'William', 'address': 'Central st 954'}
{'_id': 13, 'name': 'Chuck', 'address': 'Main Road 989'}
{'_id': 14, 'name': 'Viola', 'address': 'Sideway 1633'}

'''