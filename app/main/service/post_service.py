import uuid
import datetime
import base64
import io

from flask import jsonify

from app.main import db
from app.main.model.post import Post
from app.main.service.auth_helper import Auth

def format_post_object(post):
    # converts all images to base64 readable string
    # populates object with username
    post.username = post.user.username
    post.image = base64.b64encode(post.image)
    return post

def get_all_posts():
    raw_posts = Post.query.all()
    return list(map(format_post_object, raw_posts))

# def get_post_by_id(id):
#     return Post.query.filter_by(id=id).first()

# def get_posts_by_user(user_id):
#     return Post.query.filter_by(user_id=user_id)

def upload_new_post(data, current_user):
    file_data = base64.b64decode(data['image']) # converts b64 string to binary
    new_post = Post(
        image=file_data,
        description=data['description'],
        user_id=current_user.id,
        posted_on=datetime.datetime.utcnow()
    )
    save_changes(new_post)
    return format_post_object(new_post)

def delete_post(post_id, user_id):
    post = Post.query.filter_by(user_id=user_id, id=post_id).first_or_404()
    
    db.session.delete(post)
    db.session.commit()

    response_object = {
        'message': 'Post deleted',
        'status': 'success',
    }

    return response_object, 200

def save_changes(data):
    db.session.add(data)
    db.session.commit()

