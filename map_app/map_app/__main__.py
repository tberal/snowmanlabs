from sqlalchemy import create_engine

from map_app.app import app
from map_app.views import IndexView, AddView, AddEntryView, ListView, DeleteView, LogoutView

app.add_url_rule('/', view_func=IndexView.as_view('index'))
app.add_url_rule('/add/', view_func=AddView.as_view('add'))
app.add_url_rule('/add/<lat>/<lng>/<name>/<cat>/<public>/<user>/', view_func=AddEntryView.as_view('add_entry'))
app.add_url_rule('/list/', view_func=ListView.as_view('list'))
app.add_url_rule('/delete/<lat>/<lng>/', view_func=DeleteView.as_view('delete'))
app.add_url_rule('/logout/', view_func=LogoutView.as_view('logout'))


if __name__ == '__main__':
    app.run(debug=True)
