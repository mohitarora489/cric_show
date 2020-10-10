from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'user_email': fields.String(required=False, description='user email address'),
        'user_phone_no': fields.Integer(required=True, description='user mobile number'),
        'user_name': fields.String(required=False, description='user name'),
        'user_id': fields.String(description='user Identifier')
    })

class VideoDto:
    api = Namespace('video', description='video related operations')
    video = api.model('video', {
        'video_id': fields.String(required=True, description='video id'),
        'video_name': fields.String(required=True, description='video name'),
        'video_path': fields.String(required=True, description='video path'),
        'uploaded_date': fields.String(required=True, description='video uploaded date'),
        'user_id': fields.String(description='user Identifier')
    })