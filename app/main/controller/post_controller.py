from flask import request
from flask_restplus import Resource

from app.main.util.decorator import token_required
from ..util.dto import PostDto
from ..service.post_service import get_all_posts, upload_new_post, delete_post

api = PostDto.api

@api.route('/')
class Posts(Resource):
    @api.doc('Retrieves all posts')
    @token_required
    @api.marshal_list_with(PostDto.post_details, envelope='data')
    @api.response(200, 'Retrieved posts')
    def get(self, current_user):
        """List all posts"""
        return get_all_posts()

    @api.doc('upload post with image and short description')
    @token_required
    @api.expect(PostDto.post_upload, validate=True)
    @api.marshal_with(PostDto.post_details)
    @api.response(200, 'Post uploaded')
    def post(self, current_user):
        """ Uploads a new post """
        data = request.json
        return upload_new_post(data=data, current_user=current_user)

    @token_required
    @api.expect(PostDto.post_delete, validate=True)
    @api.response(200, 'Post deleted')
    def delete(self, current_user):
        """ Deletes a specific post by current user """
        data = request.json
        return delete_post(data['id'], current_user.id)
