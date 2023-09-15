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
        'Введите url адрес',
        validators=[
            DataRequired(message='Обязательное поле'),
            Length(
                1, 256,
                message='Длина url адреса не должна превышать 256 символов'),
            URL(message='Проверьте правильность url адреса')
        ]
    )
    # необязательное поле для псевдонима
    custom_id = StringField(
        'Введите псевдоним',
        validators=[
            Length(1, 16),
            Optional()
        ]
    )
    submit = SubmitField('Создать')
