import uuid
import datetime

from app.main import db
from app.main.model.user import User


def save_new_user(data):
    user = User.query.filter_by(user_phone_no=data['user_phone_no']).first()
    if not user:
        new_user = User(
            uuid.uuid1().hex,
            data['user_phone_no'],
            data['device_id'],
            datetime.date.today()
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'User sucessfully added',
            'user_id': new_user.user_id
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'success',
            'message': 'User sucessfully logged in',
            'user_id': user.user_id
        }
        return response_object, 201


def get_all_users():
    return User.query.all()


def get_a_user(public_id):
    return User.query.filter_by(user_id=public_id).first()

def save_user_profile(data):
    user = User.query.filter_by(user_id=data['user_id']).first()
    if user:
        user.user_name = data['user_name']
        user.user_email = data['user_email']
        update()
        response_object = {
            'status': 'pass',
            'message': 'Profile sucessfully updated',
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'user does not exist',
        }
        return response_object, 409

def save_changes(data):
    db.session.add(data)
    update()

def update():
    db.session.commit()

