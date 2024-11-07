from flask import Blueprint, url_for, \
    redirect

bp = Blueprint(name='user', 
    import_name=__name__,
    url_prefix='/user')

@bp.route('/')
def index():
    return "blueprint funcionando"

@bp.route('/register')
def register():
    return "cadastrar usuário"

@bp.route('/teste')
def teste():
    return redirect(url_for('index'))