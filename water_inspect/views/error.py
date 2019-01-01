from flask import Blueprint, render_template

blue_error = Blueprint('blue_error', __name__)


@blue_error.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@blue_error.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
