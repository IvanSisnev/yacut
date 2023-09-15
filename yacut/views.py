"""
View-функции приложения.
"""
from flask.views import View
from flask import render_template

from yacut import app, db
from yacut.models import URLMap
from yacut.forms import UrlForm


class IndexPage(View):
    methods = ["GET", "POST"]

    def dispatch_request(self):
        form = UrlForm()
        return render_template('index_page.html', form=form)


app.add_url_rule('/', view_func=IndexPage.as_view('index_page'))
