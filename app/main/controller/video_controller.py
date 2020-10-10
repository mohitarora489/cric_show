from flask import request
from flask_restx import Resource

from ..util.dto import VideoDto
from ..service.video_service import get_user_videos, save_new_video, get_all_videos

api = VideoDto.api
_video = VideoDto.video


@api.route('')
class VideoList(Resource):
    @api.doc('list_of_videos_uploaded')
    @api.marshal_list_with(_video, envelope='data')
    def get(self):
        """List all registered users"""
        return get_all_videos()

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request
        return save_new_video(data=data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class UserVideoList(Resource):
    @api.doc('get a user')
    @api.marshal_with(_video)
    def get(self, public_id):
        """get a user given its identifier"""
        user = get_user_videos(public_id)
        if not user:
            api.abort(404)
        else:
            return user

# @api.route('/Profile')
# @api.response(404, 'User not found.')
# class UserProfile(Resource):
#     @api.doc('get a user')
#     def post(self):
#         """get a user given its identifier"""
#         data = request.json
#         return save_user_profile(data = data);



