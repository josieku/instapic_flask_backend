from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'admin': fields.Boolean(description='admin privilleges')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='The username'),
        'password': fields.String(required=True, description='The user password '),
    })

class PostDto:
    api = Namespace('post', description='post related operations')
    post_upload = api.model('post_upload', {
        'image': fields.String(required=True, description='image in base64'),
        'description': fields.String(required=True, description='short description of the image')
    })
    post_details = api.model('post', {
        'username': fields.String(required=True, description='post owner'),
        'posted_on': fields.DateTime(required=True, description='posted datetime'),
        'image': fields.String(required=True, description='image in base64'),
        'description': fields.String(required=True, description='short description of the image'),
        'id': fields.Integer(required=True, description='post id')
    })
    post_delete = api.model('post_delete', {
        'id': fields.Integer(required=True, description='post id')
    })