"""
API приложения.
"""
from flask import request
from flask_restful import Resource, Api
from validators import ValidationError

from yacut import app, db
from yacut.models import URLMap
from yacut.error_handlers import APICustomError
from yacut.validators import (check_for_unallowed_chars,
                              check_for_duplicates, validate_url)
from settings import ORIGINAL_MAX_LENGTH, SHORT_MAX_LENGTH
from yacut.utils import get_unique_short_id

api = Api(app, prefix='/api/')


class NewShortId(Resource):
    """
    Эндпоинт для создания короткой ссылки.
    """
    def post(self):
        """
        Отрабатывает метод post: создает запись в БД.
        """
        if not (data := request.get_json()):
            raise APICustomError('Отсутствует тело запроса')

        elif 'url' not in data:
            raise APICustomError('"url" является обязательным полем!')

        elif len(url := data['url']) > ORIGINAL_MAX_LENGTH:
            raise APICustomError(
                f'Длина url не должна превышать {ORIGINAL_MAX_LENGTH}'
            )

        try:
            validate_url(url)
        except ValidationError:
            raise APICustomError(f'Проверьте правильность url')

        if 'custom_id' in data and (custom_id := data['custom_id']):
            if (not check_for_unallowed_chars(custom_id)
                    or len(custom_id) > SHORT_MAX_LENGTH):
                raise APICustomError(
                    'Указано недопустимое имя для короткой ссылки'
                )
            elif not check_for_duplicates(custom_id):
                raise APICustomError(f'Имя "{custom_id}" уже занято.')
        else:
            custom_id: str = get_unique_short_id()

        urlmap = URLMap(original=url, short=custom_id)
        db.session.add(urlmap)
        db.session.commit()

        return urlmap.original_short_serializer(), 201


api.add_resource(NewShortId, '/id/')


class GetOriginalUrl(Resource):
    """
    Эндпоинт для получения оригинальной ссылки.
    """
    def get(self, short_id):
        """
        Отрабатывает метод get: возвращает оригинальную ссылку.
        """
        urlmap = URLMap.query.filter_by(short=short_id).first()
        if not urlmap:
            raise APICustomError('Указанный id не найден',
                                 status_code=404)
        return urlmap.original_short_serializer(mode='original_only')


api.add_resource(GetOriginalUrl, '/id/<string:short_id>/')
