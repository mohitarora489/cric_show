from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy
import datetime
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://mohiaror:Zaq12wsx@localhost/cric_show'
db = SQLAlchemy(app)

class user_detail(db.Model):
    user_id = db.Column(db.String(100), primary_key=True)
    user_name= db.Column(db.String(100))
    user_email= db.Column(db.String(30), unique=True)
    user_phone_no = db.Column(db.Integer, unique=True)
    user_status = db.Column(db.Boolean)
    user_created_date = db.Column(db.DateTime)
    device_id = db.Column(db.String(100), unique=True)
    notify_token = db.Column(db.String(100))

    def __init__(self, userPhnNum, createdDate, userId, deviceId):
        self.user_phone_no = userPhnNum
        self.user_created_date = createdDate
        self.user_status = 1
        self.user_id = userId
        self.device_id = deviceId


# @app.route('/Login', methods=['Post'])
# def login_and_sign_up():
#     mobileNum = request.json['mobileNum']
#     otp = request.json['OTP']
#     deviceId= request.json["device_id"]

#     if len(otp) == 0:
#         return { 'userId': '', "otp" :"123456"}, 200

#     # if otp != "123456":
#     #     return 201
    
#     user = user_detail.query.filter_by(user_phone_no=mobileNum).first()

#     if user is None:
#         userid = uuid.uuid1().hex
#         user = user_detail(mobileNum, datetime.date.today(), userid,mobileNum) 
#         db.session.add(user)
#         db.session.commit()

#         user = user_detail.query.filter_by(user_phone_no=mobileNum).first()

#     return { 'userId': user.user_id, "otp" :"123456"}, 200

@app.route('/GetProfile/<string:userId>', methods=['Get'])
def get_user_details(userId):
 
    user = user_detail.query.filter_by(user_id=userId).first()

    if user is None:
        return { 'message': "User does not exists"}, 201

    return { 'user_name': user.user_name, "user_email" :user.user_email}, 200


@app.route('/UpdateProfile', methods=['Post'])
def update_user_details():
    userId = request.json['user_Id']
    userName = request.json['user_name']
    userEmail = request.json['user_email']

    user = user_detail.query.filter_by(user_id=userId).first()

    if user is None:
        return { 'message': "User id "+ userId +" does not exists"}, 201

    user.user_email = userEmail;
    user.user_name = userName;
    db.session.commit()

    return "200"

if __name__ =="__main__":
    app.run(debug=True)

