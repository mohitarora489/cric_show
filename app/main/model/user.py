
from .. import db
from ..config import key


class User(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user_detail"

    user_id = db.Column(db.String(100), primary_key=True)
    user_name= db.Column(db.String(100))
    user_email= db.Column(db.String(30), unique=True)
    user_phone_no = db.Column(db.Integer, unique=True)
    user_status = db.Column(db.Boolean)
    user_created_date = db.Column(db.DateTime)
    device_id = db.Column(db.String(100), unique=True)
    notify_token = db.Column(db.String(100))

    def __init__(self, userId, userPhnNum, deviceId, createdDate):
        self.user_phone_no = userPhnNum
        self.user_created_date = createdDate
        self.user_status = 1
        self.user_id = userId
        self.device_id = deviceId

    def __repr__(self):
        return "<User '{}'>".format(self.user_name)
