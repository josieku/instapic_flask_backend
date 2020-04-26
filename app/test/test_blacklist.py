import unittest
from unittest.mock import patch

from app.test.base import BaseTestCase
from app.main.service.blacklist_service import save_token
from app.main.model.blacklist import BlacklistToken

class TestBlacklist(BaseTestCase):
    def test_blacklist_repr(self):
        new_token = BlacklistToken(token='test token')
        self.assertEqual(repr(new_token), "<id: token: {}>".format(new_token.token))

    @patch('app.main.db.session.commit')
    def test_save_token(self, db_commit):
        db_commit.side_effect = Exception('error')
        self.assertRaises(Exception, save_token('test token'))
        


if __name__ == '__main__':
    unittest.main()