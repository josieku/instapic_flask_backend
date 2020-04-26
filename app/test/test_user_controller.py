import unittest, json, datetime
from unittest.mock import patch

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
    def test_get_users(self):
        with self.client:
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            auth = data_register['Authorization']
            response = get_users(self, auth)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertTrue(len(data['data']) == 1)
    
    @patch('app.main.model.user.User.encode_auth_token')
    def test_register_user(self, encode_auth_token):
        encode_auth_token.side_effect = Exception('unable to encode token')
        response = register_user(self)
        data_response = json.loads(response.data.decode())
        self.assertTrue(data_response['status'] == 'fail')
        self.assertTrue(data_response['message'] == 'Some error occurred. Please try again.')
        self.assertEqual(response.status_code, 401)


if __name__ == '__main__':
    unittest.main()

