from flask import Blueprint, render_template, url_for

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/')
def _index():
    return render_template('index.html')


