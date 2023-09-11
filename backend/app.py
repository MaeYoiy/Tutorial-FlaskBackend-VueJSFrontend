from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
from flask_cors import CORS # Consume Api for allow us to fetch / consume Api
import json
import datetime

# Create object of flask
app = Flask(__name__)
CORS(app)

mysql = MySQL(app)

api = Api(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'r@@tmink'
app.config['MYSQL_DB'] = 'test'

# Convert data form MySQL to Python
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

# Create api for students
class Student(Resource):
    def get(self):
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM students")
        data = dictfetchall(cur)
        cur.close()
        print(type(data))
        
        return jsonify({'students':data,'Method':'GET'})
    
    def post(self):
        return jsonify({'Method':'POST'})
    
    def put(self):
        return jsonify({'Method':'PUT'})
    
    def patch(self):
        return jsonify({'Method':'PATCH'})
    
api.add_resource(Student, '/api/students/')

# app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:''@localhost/flask'
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# class Articles(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     title = db.Column(db.String(100))
#     body = db.Column(db.Text())
#     date = db.Column(db.DateTime, default = datetime.datetime.now)

#     def __init__(self, title, body):
#         self.title = title
#         self.body = body



# # Create our route
# @app.route('/get', methods = ['GET'])
# def get_articles():
#     return jsonify({"Hell0":"World"})


# Run flask application
if __name__ == "__main__":
    app.run(debug=True)
