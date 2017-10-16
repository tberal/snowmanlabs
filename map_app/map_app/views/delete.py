from flask import g, redirect, url_for
from flask.views import View

from map_app.models import TourPoint

from map_app.app import Session


class DeleteView(View):
    """
    Removes a location from the database.

    Parameters:
        lat: The location's latitude
        lng: The location's longitude
    """
    def dispatch_request(self, lat, lng):
        if g.user:
            db_session = Session()
            db_session.query(TourPoint).filter(
                    TourPoint.latitude == lat,
                    TourPoint.longitude == lng
                    ).delete()
            db_session.commit()
            db_session.close()
            return redirect(url_for('list'))
        else:
            return redirect(url_for('index'))
