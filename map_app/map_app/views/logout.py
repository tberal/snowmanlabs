from flask import g, session, redirect, url_for
from flask.views import View


class LogoutView(View):
    """
    Invalidates the current session
    """
    def dispatch_request(self):
        if g.user:
            session.pop('user', None)
        return redirect(url_for('index'))

