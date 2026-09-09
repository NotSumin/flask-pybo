from flask import Blueprint

bp = Blueprint('main', __name__, url_prefix='/main')

@bp.route('/')
def hello_world():
    return 'Hello Main!'

@bp.route('/hello')
def hello():
    return 'main hello page'