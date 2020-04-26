import unittest, json, datetime, base64
from unittest.mock import patch

from app.main import db
from app.test.base import BaseTestCase
from app.test.fake_images import image1, image2
from app.main.model.post import Post

def register_user(self):
    return self.client.post(
        '/user/',
        data=json.dumps(dict(
            username='username',
            password='123456'
        )),
        content_type='application/json'
    )


def login_user(self):
    return self.client.post(
        '/auth/login',
        data=json.dumps(dict(
            username='username',
            password='123456'
        )),
        content_type='application/json'
    )

def make_post(self, jwt):
    return self.client.post(
        '/post/',
        data=json.dumps(dict(
            image=image1,
            description='screenshot test image 1'
        )),
        content_type='application/json',
        headers=dict(
            Authorization=jwt
        )
    )

def get_posts(self, jwt):
    return self.client.get(
        '/post/',
        headers=dict(
            Authorization=jwt
        )
    )

def get_posts_by_page(self, jwt):
    return self.client.get(
        '/post/',
        headers=dict(
            Authorization=jwt
        ),
        query_string=dict(
            pagesize=1
        )
    )

def delete_post(self, post_id, jwt):
    return self.client.delete(
        '/post/',
        data=json.dumps(dict(
            id=post_id
        )),
        content_type='application/json',
        headers=dict(
            Authorization=jwt
        )
    )

class TestPostService(BaseTestCase):
    def test_post_model(self):
        file_data = base64.b64decode(image1)
        new_post = Post(
            image=file_data,
            description='testpost',
            user_id=1,
            posted_on=datetime.datetime.utcnow()
        )
        self.assertEqual(repr(new_post), "<Post '{}'>".format(new_post.id))

    def test_get_posts_without_auth(self):
        with self.client:
            response = get_posts(self, '')
            self.assertEqual(response.status_code, 401)

    def test_get_posts_with_auth(self):
        with self.client:
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            auth = data_register['Authorization']
            response = get_posts(self, auth)
            self.assertEqual(response.status_code, 200)

    def test_get_posts_by_page_with_auth(self):
        with self.client:
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            auth = data_register['Authorization']
            response = get_posts_by_page(self, auth)
            self.assertEqual(response.status_code, 200)

    def test_create_post_without_auth(self):
        with self.client:
            response = make_post(self, '')
            self.assertEqual(response.status_code, 401)

    def test_create_post_with_auth(self):
        with self.client:
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            auth = data_register['Authorization']
            resp_posts = get_posts(self, auth)
            data_posts = json.loads(resp_posts.data.decode())
            self.assertTrue(len(data_posts['data']) == 0)
            response = make_post(self, auth)
            data_response = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            resp_posts = get_posts(self, auth)
            data_posts = json.loads(resp_posts.data.decode())
            # self.assertTrue(len(data_posts['data']) == 1)

    def test_delete_post_without_auth(self):
        with self.client:
            response = delete_post(self, 0, '')
            self.assertEqual(response.status_code, 401)

    def test_delete_post_as_owner(self):
        with self.client:
            resp_register = register_user(self)
            data_register = json.loads(resp_register.data.decode())
            self.assertTrue(data_register['status'] == 'success')
            auth = data_register['Authorization']
            resp_make = make_post(self, auth)
            data_make = json.loads(resp_make.data.decode())
            self.assertEqual(resp_make.status_code, 200)
            resp_delete = delete_post(self, data_make['id'], auth)
            self.assertEqual(resp_delete.status_code, 200)


    def test_delete_post_not_as_owner(self):
        pass


if __name__ == '__main__':
    unittest.main()

