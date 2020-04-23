import unittest
import json
import datetime

from app.main import db
from app.test.base import BaseTestCase

def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            username='username',
            password='123456'
        )),
        content_type='application/json'
    )

def get_users(self, jwt):
    return self.client.get(
        '/user/',
        headers=dict(
            Authorization=jwt
        )
    )

class TestUserController(BaseTestCase):
    def test_get_posts(self):
        with self.client:
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            auth = data_register['Authorization']
            response = get_users(self, auth)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(len(data['data']) == 1)


if __name__ == '__main__':
    unittest.main()

