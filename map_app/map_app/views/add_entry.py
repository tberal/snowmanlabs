from flask import g, redirect, url_for
from flask.views import View

from map_app.models import TourPoint

from map_app.app import Session

class AddEntryView(View):
    """
    Saves a location added in the add view to the database:
    
    Parameters:
        lat: the location's latitude
        lng: the location's longitude
        name: the location's name
        cat: the location's category
        public: whether this location should be displayed publicly or not
        user: the facebook id of the user who created this entry
    """
    def dispatch_request(self, lat, lng, name, cat, public, user):
        if g.user:
            if public == 'n':
                public = False
            new_point = TourPoint(
                    latitude = lat,
                    longitude = lng,
                    name = name,
                    category = cat,
                    public = public,
                    user = user
                    )
            db_session = Session()
            db_session.add(new_point)
            db_session.commit()
            db_session.close()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))
