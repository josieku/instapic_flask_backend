from flask import request
from flask_restplus import Resource, reqparse

from app.main.util.decorator import token_required
from ..util.dto import PostDto
from ..service.post_service import get_all_posts, get_posts_by_page, upload_new_post, delete_post

api = PostDto.api

@api.route('/')
class Posts(Resource):
    @api.doc('Retrieves all posts')
    @token_required
    @api.marshal_list_with(PostDto.post_details, envelope='data')
    @api.response(200, 'Retrieved posts')
    def get(self, current_user):
        """List all posts"""
        # parser = reqparse.RequestParser()
        # parser.add_argument('pagesize', type=int, required=False)
        # parser.add_argument('page', type=int, required=False)
        # parser.add_argument('sort', type=int, required=False)
        # args = parser.parse_args()
        pagesize = request.args.get('pagesize', default=0, type=int)
        page = request.args.get('page', default=0, type=int)
        # sort = request.args.get('sort', default=None)

        try:
            if pagesize is not 0:
                page = page or 1
                return get_posts_by_page(pagesize, page)

            return get_all_posts()
        except Exception as e:
            return []


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
