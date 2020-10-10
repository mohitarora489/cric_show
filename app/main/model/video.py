
from .. import db
from ..config import key


class Video(db.Model):
    """ User Model for storing user related details """
    __tablename__ = "user_video_details"

    video_id = db.Column(db.String(100), primary_key=True)
    video_name = db.Column(db.String(100))
    video_path = db.Column(db.String(100), unique=True)
    uploaded_date = db.Column(db.DateTime)
    user_id = db.Column(db.String(100), unique=True)

    def __init__(self,videoId, videoName, videoPath, uploadedDate, userId):
        self.video_id = videoId
        self.video_name = videoName
        self.video_path = videoPath
        self.uploaded_date = uploadedDate
        self.user_id = userId

    def __repr__(self):
        return "<User '{}'>".format(self.user_name)
