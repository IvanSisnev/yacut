"""
API приложения.
"""
from flask import request, jsonify
from flask_restful import Resource, Api

from yacut import app, db
from yacut.models import URLMap
from yacut.error_handlers import APICustomError
from yacut.validators import check_for_unallowed_chars, check_for_duplicates
from settings import ORIGINAL_MAX_LENGTH, SHORT_MAX_LENGTH
from yacut.utils import get_unique_short_id

api = Api(app, prefix='/api/')


class NewShortId(Resource):

    def post(self):
        data = request.get_json()
        if 'url' not in data:
            raise APICustomError('Отсутствует обязательное поле url')

        elif len(url := data['url']) > ORIGINAL_MAX_LENGTH:
            raise APICustomError(
                f'Длина url не должна превышать {ORIGINAL_MAX_LENGTH}'
            )
        # todo добавить обработчик ошибки url
        if 'custom_id' in data:
            custom_id = data['custom_id']
            if len(custom_id) > SHORT_MAX_LENGTH:
                raise APICustomError(
                    'Длина custom_id не должна превышать '
                    f'{SHORT_MAX_LENGTH} символов'
                )
            elif not check_for_unallowed_chars(custom_id):
                raise APICustomError(
                    'Поле custom_id должно содержать только латинские буквы и '
                    'цифры'
                )
            elif not check_for_duplicates(custom_id):
                raise APICustomError(
                    'Такой custom_id уже используется.'
                )
        else:
            custom_id = get_unique_short_id()

        urlmap = URLMap(original=url, short=custom_id)
        db.session.add(urlmap)
        db.session.commit()

        return urlmap.to_dict(), 201


api.add_resource(NewShortId, '/id/')
