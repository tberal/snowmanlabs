import json

from flask import Flask, session, request, g
from flask_wtf.csrf import CSRFProtect
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from googlemaps import Client
from facebook import get_user_from_cookie, GraphAPI

from map_app.config import APP_CONFIG, DATABASE_CONFIG, FACEBOOK_API, MAPS_API
from map_app.models import User, TourPoint

engine = create_engine(
        '{}://{}:{}@{}/{}'.format(
            DATABASE_CONFIG['ENGINE'],
            DATABASE_CONFIG['ID'],
            DATABASE_CONFIG['PWD'],
            DATABASE_CONFIG['HOST'],
            DATABASE_CONFIG['DB']
            ),
        echo=True
        )

TourPoint.metadata.create_all(engine)
User.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

app = Flask(__name__)
app.config['SECRET_KEY'] = APP_CONFIG['SECRET_KEY']
csrf = CSRFProtect(app)

map_api = Client(MAPS_API['API_KEY'])


@app.before_request
def get_current_user():
    """
    Checks if there's a currently active user session. If there's none,
    it'll then check whether there's an active facebook cookie or not, and then
    use this cookie's data to register or log the user in.
    """
    if session.get('user'):
        g.user = session.get('user')
        return

    result = get_user_from_cookie(
            cookies=request.cookies,
            app_id=FACEBOOK_API['APP_ID'],
            app_secret=FACEBOOK_API['APP_SECRET']
            )

    db_session = Session()
    if result:
        user = db_session.query(User).filter(User.id == result['uid']).first()

        if not user:
            graph = GraphAPI(result['access_token'])
            profile = graph.get_object('me')
            if 'link' not in profile:
                profile['link'] = ''

            user = User(
                    id=str(profile['id']),
                    name=profile['name'],
                    profile_url=profile['link'],
                    access_token=result['access_token']
                    )
            db_session.add(user)

        elif user.access_token != result['access_token']:
            user.access_token = result['access_token']

        session['user'] = dict(
                name=user.name,
                profile_url=user.profile_url,
                id=user.id,
                access_token=user.access_token
                )

    db_session.commit()
    g.user = session.get('user', None)
