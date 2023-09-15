"""
Формы приложения.
"""
from flask_wtf import FlaskForm
from wtforms import URLField, StringField, SubmitField
from wtforms.validators import DataRequired, Length, URL, Optional


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
            Length(
                1, 256,
                message='Длина url адреса не должна превышать 256 символов')
        ]
    )
    # необязательное поле для псевдонима
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(
                1, 16,
                message=(
                    'Длина короткой ссылки не должна превышать 16 символов'
                )
            ),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
