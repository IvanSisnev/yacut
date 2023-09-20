"""
Формы приложения.
"""
from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, URL, Optional

from yacut import app
from yacut.validators import (check_for_unallowed_chars,
                              check_for_duplicates, validate_url)


class UrlForm(FlaskForm):
    """
    Формы для главной страницы приложения.
    """
    # поле для оригинального url адреса
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Проверьте правильность url адреса'),
            Length(1, 256,)
        ]
    )
    # необязательное поле для короткой ссылки пользователя
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16),
            Optional()
        ]
    )
    submit = SubmitField('Создать')

    @staticmethod
    def validate_original_link(form, field):
        """
        Проверяет оригинальный url адрес на правильность.
        """
        try:
            validate_url(field.data)
        except ValidationError:
            app.logger.info(f'Переданный url {field.data} не прошел проверку '
                            'на валидность.')
            raise ValidationError(
                message='Проверьте правильность url адреса'
            )

    @staticmethod
    def validate_custom_id(form, field):
        """
        Проверяет короткую ссылку пользователя на недопустимые символы и
        на уникальность в БД.
        """
        if not check_for_unallowed_chars(field.data):
            app.logger.info(f'В короткой ссылке {field.data} обнаружены '
                            'недопустимые символы.')
            raise ValidationError(
                message=('В короткой ссылке можно использовать только '
                         'латинские буквы и цифры')
            )
        elif not check_for_duplicates(field.data):
            app.logger.info(f'Переданная короткая ссылка {field.data} не '
                            'уникальна.')
            raise ValidationError(
                message=f'Имя {field.data} уже занято!'
            )
