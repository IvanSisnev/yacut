"""
View-функции приложения.
"""
from flask.views import View
from flask import request, render_template, redirect

from yacut import app, db
from yacut.models import URLMap
from yacut.forms import UrlForm
from yacut.utils import get_unique_short_id


class IndexPage(View):
    """
    View-класс главной страницы.
    """
    methods = ['GET', 'POST']

    def dispatch_request(self):
        """
        View-функция.
        """
        form = UrlForm()
        if form.validate_on_submit():
            short_id = form.custom_id.data
            if not short_id:
                short_id: str = get_unique_short_id()
            urlmap = URLMap(original=form.original_link.data, short=short_id)
            db.session.add(urlmap)
            db.session.commit()
            return render_template('index_page.html',
                                   form=form, urlmap=urlmap), 200
        return render_template('index_page.html',
                               form=form), 200


app.add_url_rule('/', view_func=IndexPage.as_view('index_page'))
