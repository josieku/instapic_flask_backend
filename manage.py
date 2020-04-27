import os
import unittest

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app
from app.main import db
from app.main.model import user, blacklist

from populate_db import populate

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def run():
    app.run(host='0.0.0.0', port=5000)


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

@manager.command
def populate_db():
    populate()

@manager.command
def clear_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    manager.run()
