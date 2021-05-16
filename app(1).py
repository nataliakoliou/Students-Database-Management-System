from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError
from flask import Flask, request, jsonify, redirect, Response
from datetime import date
from bson import json_util
import json
import uuid
import time

# Connect to our local MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Choose database
db = client['InfoSys']

# Choose collections
students = db['Students']
users = db['Users']

# Initiate Flask App
app = Flask(__name__)

users_sessions = {}
yearMinus30 = date.today().year - 30

def create_session(username):
    user_uuid = str(uuid.uuid1())
    users_sessions[user_uuid] = (username, time.time())
    return user_uuid  

def is_session_valid(user_uuid):
    return user_uuid in users_sessions

# ΕΡΩΤΗΜΑ 1: Δημιουργία χρήστη
@app.route('/createUser', methods=['POST'])
def create_user():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "username" in data or not "password" in data:
        return Response("Information incomplete",status=500,mimetype="application/json")

    # if there is no user with such a username in Users collection
    if users.count_documents({"username":data["username"]}) == 0 :  
        # add this user into the Users collection
        user = {"username": data['username'], "password": data['password']} 
        users.insert(user)
        return Response(data['username']+" was added to the MongoDB",status=200,mimetype='application/json') 
    # if there is one user with such a username in Users collection
    else:   
        return Response("A user with the given username already exists",status=400,mimetype='application/json')

# ΕΡΩΤΗΜΑ 2: Login στο σύστημα
@app.route('/login', methods=['POST'])
def login():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "username" in data or not "password" in data:
        return Response("Information incomplete",status=500,mimetype="application/json")

    # if authentication is successful...
    if users.count_documents({"$and":[{"username":data["username"]}, {"password":data["password"]}]}) == 1 :
        user_uuid = create_session(data["username"])
        res = {"uuid": user_uuid, "username": data["username"]}
        return Response(json.dumps(res), status=200, mimetype='application/json')
    # otherwise, if authentication is not successful...
    else:    
        return Response("Wrong username or password",status=400,mimetype="application/json")

# ΕΡΩΤΗΜΑ 3: Επιστροφή φοιτητή βάσει email 
@app.route('/getStudent', methods=['GET'])
def get_student_1():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "email" in data:
        return Response("Information incomplete",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    if is_session_valid(uuid):
        student = students.find_one({"email":data["email"]})
        if student != None:
            if "address" in student:
                student_d1 = {"id":str(student["_id"]), "name":student["name"], "email":student["email"], "yearOfBirth":student["yearOfBirth"], "address":student["address"]}
            else:
                student_d1 = {"id":str(student["_id"]), "name":student["name"], "email":student["email"], "yearOfBirth":student["yearOfBirth"]}
            return Response(json.dumps(student_d1), status=200, mimetype='application/json')
        else:
            return Response("Wrong email",status=404,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier",status=401,mimetype="application/json")
        
# ΕΡΩΤΗΜΑ 4: Επιστροφή όλων των φοιτητών που είναι 30 ετών
@app.route('/getStudents/thirties', methods=['GET'])
def get_students_thirty_1():

    studentsp_exactly30 = students.find({"yearOfBirth":{"$eq":yearMinus30}})  
    uuid = request.headers.get('authorization')
    if is_session_valid(uuid):
        students_exactly30=json.loads(json_util.dumps(studentsp_exactly30))
        if students_exactly30 != None:
            students_l1 = []
            for student in students_exactly30:
                if "address" in student:
                    student_d2 = {"id":str(student["_id"]), "name":student["name"], "email":student["email"], "yearOfBirth":student["yearOfBirth"], "address":student["address"]}
                else:
                    student_d2 = {"id":str(student["_id"]), "name":student["name"], "email":student["email"], "yearOfBirth":student["yearOfBirth"]}
                students_l1.append(student_d2)
            return Response(json.dumps(students_l1), status=200, mimetype='application/json')
        else:
            return Response("There are no such students",status=404,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier",status=401,mimetype="application/json")

# ΕΡΩΤΗΜΑ 5: Επιστροφή όλων των φοιτητών που είναι τουλάχιστον 30 ετών
@app.route('/getStudents/oldies', methods=['GET'])
def get_students_thirty_2():

    studentsp_atleast30 = students.find({"yearOfBirth":{"$lte":yearMinus30}})
    uuid = request.headers.get('authorization')
    if is_session_valid(uuid):
        students_atleast30=json.loads(json_util.dumps(studentsp_atleast30))
        if students_atleast30 != None:
            students_l2 = []
            for student in students_atleast30:
                if "address" in student:
                    student_d3 = {"id":str(student["_id"]), "name":student["name"], "email":student["email"], "yearOfBirth":student["yearOfBirth"], "address":student["address"]}
                else:
                    student_d3 = {"id":str(student["_id"]), "name":student["name"], "email":student["email"], "yearOfBirth":student["yearOfBirth"]}
                students_l2.append(student_d3)
            return Response(json.dumps(students_l2), status=200, mimetype='application/json')
        else:
            return Response("There are no such students",status=404,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier",status=401,mimetype="application/json")

# ΕΡΩΤΗΜΑ 6: Επιστροφή φοιτητή που έχει δηλώσει κατοικία βάσει email 
@app.route('/getStudentAddress', methods=['GET'])
def get_student_2():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "email" in data:
        return Response("Information incomplete",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    if is_session_valid(uuid):
        studentp = students.find_one({"email":data["email"]})
        student=json.loads(json_util.dumps(studentp))
        if student != None:
            if "address" in student:
                student_d4 = {"name":student["name"], "street":student["address"][0]["street"], "postcode":student["address"][0]["postcode"]}
                return Response(json.dumps(student_d4), status=200, mimetype='application/json')
            else:
                return Response("The student you are looking for has not declared his home address",status=400,mimetype="application/json")
        else:
            return Response("You inserted the wrong email, or the student you are looking for has not declared his home address",status=400,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier",status=401,mimetype="application/json")

# ΕΡΩΤΗΜΑ 7: Διαγραφή φοιτητή βάσει email 
@app.route('/deleteStudent', methods=['DELETE'])
def delete_student():
    # Request JSON data
    data = None 
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "email" in data:
        return Response("Information incomplete",status=500,mimetype="application/json")

    student = students.find_one({"email":data["email"]})
    uuid = request.headers.get('authorization')
    if is_session_valid(uuid):
        if student != None:
            students.delete_one({"email":data["email"]})
            return Response("Student deleted successfuly", status=200, mimetype='application/json')
        else:
            return Response("You inserted a non-existent email",status=400,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier",status=401,mimetype="application/json")

# ΕΡΩΤΗΜΑ 8: Εισαγωγή μαθημάτων σε φοιτητή βάσει email 
@app.route('/addCourses', methods=['PATCH'])
def add_courses():
    # Request JSON data
    data = None 
    courses_l=[]
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "email" in data or not "courses" in data:
        return Response("Information incomplete",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization') 
    if is_session_valid(uuid):
        studentp = students.find_one({"email":data["email"]})
        student=json.loads(json_util.dumps(studentp))
        if student != None:
            for course_d in data["courses"]:
                courses_l.append(course_d)
            student.update({"courses":courses_l}) 
            if "address" in student:
                student_d5 = {"id":str(student["_id"]), "name":student["name"], "email":student["email"], "yearOfBirth":student["yearOfBirth"], "address":student["address"], "courses":student["courses"]}
            else:
                student_d5 = {"id":str(student["_id"]), "name":student["name"], "email":student["email"], "yearOfBirth":student["yearOfBirth"], "courses":student["courses"]}
            return Response(json.dumps(student_d5),status=200,mimetype='application/json')
        else:
            return Response("You inserted the wrong email",status=400,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier",status=401,mimetype="application/json")

# ΕΡΩΤΗΜΑ 9: Επιστροφή περασμένων μαθημάτων φοιτητή βάσει email
@app.route('/getPassedCourses', methods=['GET'])
def get_courses():
    # Request JSON data
    data = None 
    passed = {}
    try:
        data = json.loads(request.data)
    except Exception as e:
        return Response("bad json content",status=500,mimetype='application/json')
    if data == None:
        return Response("bad request",status=500,mimetype='application/json')
    if not "email" in data:
        return Response("Information incomplete",status=500,mimetype="application/json")

    uuid = request.headers.get('authorization')
    if is_session_valid(uuid):
        studentp = students.find_one({"email":data["email"]})
        student=json.loads(json_util.dumps(studentp))
        if student != None:
            if "courses" in student:
                for course_d in student["courses"]:
                    course_l = next(iter((course_d.items())))
                    if course_l[1] > 5:
                        passed.update(course_d)
                    else:
                        continue
                if not passed:
                    return Response("This student failed all his courses",status=400,mimetype="application/json")
                else:
                    student_d6 = {"name":student["name"], "courses":passed}
                    return Response(json.dumps(student_d6),status=200,mimetype='application/json')
            else:
                return Response("This student has not attended any course exams",status=400,mimetype="application/json")
        else:
            return Response("You inserted the wrong email",status=400,mimetype="application/json")
    else:
        return Response("Invalid user unique identifier",status=401,mimetype="application/json")
    
# Εκτέλεση flask service σε debug mode, στην port 5000. 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)