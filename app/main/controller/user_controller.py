from flask import request
from flask_restplus import Resource, cors
# from flask_cors import cross_origin

from app.main.util.decorator import token_required
from ..util.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    # def options(self):
    #     print("\n\nin options in user controller\n\n")
    #     return

    @api.doc('list_of_registered_users')
    @token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self, current_user):
        """List all registered users"""
        return get_all_users()

    @api.expect(_user, validate=True)
    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)

    
