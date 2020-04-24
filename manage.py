import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import blueprint
from app.main import create_app, db
from app.main.model import user, blacklist

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)

app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run(PORT):
    app.run(host='0.0.0.0', port=PORT)


@manager.command
def test(test_name=None):
    """Runs the unit tests."""
    if test_name is None:
        tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    else: 
        tests = unittest.TestLoader().loadTestsFromName('app.test.' + test_name)

    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

if __name__ == '__main__':
    manager.run()
