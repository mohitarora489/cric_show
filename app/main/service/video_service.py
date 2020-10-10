import uuid
import datetime
import os
from app.main import db
from app.main.model.video import Video
from werkzeug.utils import secure_filename


def save_new_video(data):

    if 'file' not in data.files:
        response_object = {
        'status': 'pass',
        'message': "File does not exist"
        }
        
        return response_object, 400

    file = data.files['file']
    
    if file.filename == '':
        response_object = {
        'status': 'pass',
        'message': 'No file selected for uploading',
        }
        return response_object, 400
    
    if file :
        filename = secure_filename(file.filename)
        filePath = os.path.join(r'C:/MyProjects/cric_show/videos', filename)
        file.save(filePath)
        new_video = Video(
            uuid.uuid1().hex,
            file.filename,
            filePath,
            datetime.datetime.today(),
            data.form['user_id']
        )
        save_changes(new_video)
        response_object = {
        'status': 'pass',
        'message': 'File successfully uploaded',
        }
        return response_object, 201
    else:
        response_object = {
        'status': 'fail',
        'message': 'No file selected for uploading',
        }
        return response_object, 400
    


def get_all_videos():
    return Video.query.all()


def get_user_videos(public_id):
    return Video.query.filter_by(user_id=public_id).all()


def save_changes(data):
    db.session.add(data)
    update()

def update():
    db.session.commit()

