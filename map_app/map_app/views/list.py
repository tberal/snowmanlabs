from flask import g, render_template, redirect, url_for
from flask.views import View

from map_app.models import TourPoint

from map_app.app import Session

class ListView(View):
    """
    Lists all the locations created by the currently connected user.
    """
    def dispatch_request(self):
        if g.user:
            db_session = Session()
            point_list = db_session.query(TourPoint).filter(TourPoint.user == g.user['id'])
            db_session.close()
            return render_template('list.html', points=point_list)
        else:
            return redirect(url_for('index'))
