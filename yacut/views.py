"""
View-функции приложения.
"""
from flask.views import View
from flask import request, render_template, redirect, flash

from yacut import app, db
from yacut.models import URLMap
from yacut.forms import UrlForm
from yacut.utils import get_unique_short_id, check_for_duplicates


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
        # todo попробовать убрать проверку метода
        if request.method == 'POST' and form.validate_on_submit():
            short_id = form.custom_id.data
            if not short_id:
                short_id: str = get_unique_short_id()
            elif not check_for_duplicates(short_id):
                flash('Такая короткая ссылка уже используется')
                # todo оставить original_link
                return render_template('index_page.html', form=form)
            urlmap = URLMap(original=form.original_link.data, short=short_id)
            db.session.add(urlmap)
            db.session.commit()
            # todo оставить original_link и short_id если было
            # todo вывести готовую ссылку
            return redirect(...)
        return render_template('index_page.html', form=form)


app.add_url_rule('/', view_func=IndexPage.as_view('index_page'))
