from flask import g, request, render_template
from flask.views import View
from sqlalchemy import text

from geocoder import freegeoip

from map_app.config import FACEBOOK_API
from map_app.app import engine

class IndexView(View):
    """
    Loads the application home page. Tracks the current user location based on its IP.
    After that, lists all public locations within a 5km radius of the user's current location.
    If no user is logged in, provides an option to connect via facebook(This connection is handled
    by javascript) and display all public restaurants in a 5km radius.
    """
    def dispatch_request(self):
        if request.remote_addr == '127.0.0.1':
            lat = -25.43555700
            lng = -49.27032780
        else:
            location = freegeoip(request.remote_addr).json
            lat = location['lat']
            lng = location['lng']

        if g.user:
            stmt = text("SELECT * FROM tour_points WHERE acos(sin(:lat) * sin(latitude) + cos(:lat) * cos(latitude) * cos(longitude - (:lng))) * 6371 <= 5 AND public IS TRUE")
            nearby = engine.execute(stmt, {'lat': lat, 'lng': lng})

            return render_template(
                    'index.html',
                    app_id=FACEBOOK_API['APP_ID'],
                    app_name=FACEBOOK_API['APP_NAME'],
                    user=g.user,
                    nearby=nearby
                    )

        stmt = text("SELECT * FROM tour_points WHERE acos(sin(:lat) * sin(latitude) + cos(:lat) * cos(latitude) * cos(longitude - (:lng))) * 6371 <= 5 AND public IS TRUE AND category = 'restaurant'")
        nearby = engine.execute(stmt, {'lat': lat, 'lng': lng})

        return render_template(
                'login.html',
                app_id=FACEBOOK_API['APP_ID'],
                app_name=FACEBOOK_API['APP_NAME'],
                nearby=nearby
                )
