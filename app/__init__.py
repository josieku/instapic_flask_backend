import os, json

from flask_restplus import Api
from flask import Blueprint
from flask_cors import CORS


from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.post_controller import api as post_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='InstaPic by Josie',
          version='1.0',
          description='API for the premium photo sharing platform'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns, path='/auth')
api.add_namespace(post_ns, path="/post")

CORS(blueprint, origins=['*'], support_credentials=True, automatic_options=True)

# initialize app
from .main import create_app
from .main import db

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
app.url_map.strict_slashes = False

@app.teardown_request
def teardown_request(exception):
    if exception:
        db.session.rollback()
    db.session.remove()