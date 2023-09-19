"""
View-функции приложения.
"""
from flask.views import View
from flask import render_template, redirect, abort

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
        Передает на страницу форму, проверяет ее в случае метода POST и
        сохраняет в БД.
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


class RedirectPage(View):
    """
    View-класс страницы редиректа с короткой ссылки на оригинальную.
    """
    methods = ['GET']

    def dispatch_request(self, short_id):
        """
        Перенаправляет с url адреса короткой ссылки на оригинальную ссылку.
        """
        urlmap = URLMap.query.filter_by(short=short_id).first()
        if urlmap:
            return redirect(urlmap.original)
        abort(404)


app.add_url_rule('/<string:short_id>/',
                 view_func=RedirectPage.as_view('redirect_page'))
