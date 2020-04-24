import datetime
from app.main import db
from app.main.model.user import User
from app.main.service.post_service import upload_new_post
from app.test.fake_images import image1, image2

def save_changes(data):
    db.session.add(data)
    db.session.commit()

def populate():
    db.drop_all()
    db.create_all()
    db.session.commit()

    ''' Creates 3 users and 3 posts '''
    user1 = User(
        username='Jim Pug',
        password='jimmypuggy',
        registered_on=datetime.datetime.utcnow()
    )
    save_changes(user1)
    post1 = upload_new_post(dict(
        image=image1,
        description='this is my favorite screenshot'
    ), current_user=user1)

    user2 = User(
        username='Alice Dog',
        password='alicedog',
        registered_on=datetime.datetime.utcnow()
    )
    save_changes(user2)
    post2 = upload_new_post(dict(
        image=image2,
        description='what a cool pic'
    ), current_user=user2)

    user3 = User(
        username='Piccolo Schnauzer',
        password='picco',
        registered_on=datetime.datetime.utcnow()
    )
    save_changes(user3)
    post3 = upload_new_post(dict(
        image=image1,
        description='look at this cool shot i took!'
    ), current_user=user3)

