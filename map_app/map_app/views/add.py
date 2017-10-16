from flask import g, request, redirect, url_for, render_template
from flask.views import View

from map_app.app import map_api

from map_app.forms import AddTourPoint


class AddView(View):
    """
    Loads a form to allow users to register new locations. Then save the new location to the database
    The user provides an address string, which is converted to that locations latitude and longitude
    before being saved to the database.
    """
    methods = ['GET', 'POST']

    def dispatch_request(self):
        if g.user:
            form = AddTourPoint(request.form)
            if form.validate_on_submit():
                address = request.form['address']
                location = map_api.geocode(address)[0]['geometry']['location']
                lat = location['lat']
                lng = location['lng']
                return redirect(url_for(
                    'add_entry',
                    lat=lat,
                    lng=lng,
                    name=request.form['name'],
                    cat=request.form['category'],
                    public=request.form.get('public', 'n'),
                    user=g.user['id']
                    )
                )
            return render_template('add.html', form=form)
        else:
            return redirect(url_for('index'))

