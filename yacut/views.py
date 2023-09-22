"""
View-функции приложения.
"""
from http import HTTPStatus

from flask.views import View
from flask import render_template, redirect

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

        if not form.validate_on_submit():
            # возвращаю шаблон с формой
            return render_template('index_page.html',
                                   form=form), HTTPStatus.OK

        short_id = form.custom_id.data
        # если short_id не передана, создаю ее
        if not short_id:
            short_id: str = get_unique_short_id()

        urlmap = URLMap(original=form.original_link.data, short=short_id)
        db.session.add(urlmap)
        db.session.commit()
        app.logger.info(f'Новая запись с id {urlmap.id} создана.')
        # возвращаю шаблон с созданной короткой ссылкой
        return render_template('index_page.html',
                               form=form, urlmap=urlmap), HTTPStatus.OK


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
        # да, короче получилось, но если я захочу логировать это исключение,
        # мне придется делать try-except, перехватывать исключение и все равно
        # делать abort(404)?
        urlmap = URLMap.query.filter_by(short=short_id).first_or_404()
        app.logger.info(f'Успешный редирект по короткой ссылке {short_id}.')
        return redirect(urlmap.original)


app.add_url_rule('/<string:short_id>',
                 view_func=RedirectPage.as_view('redirect_page'))
