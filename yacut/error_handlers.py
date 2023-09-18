"""
Обработчики ошибок приложения.
"""
from flask import jsonify, render_template

from . import app, db

# todo проверить работу обработчиков.
@app.errorhandler(404)
def page_not_found(error):
    """
    Обработчик ошибки 404.
    """
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    """
    Обработчик ошибки 500.
    """
    db.session.rollback()
    return render_template('500.html'), 500

# todo добавить обработчики ошибок API
