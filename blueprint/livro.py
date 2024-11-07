from flask import Blueprint, url_for, \
    redirect, render_template

bp = Blueprint(name='book', import_name=__name__,
    url_prefix='/book', template_folder='templates')

@bp.route('/')
def index():
    return render_template('livro/index.html')

@bp.route('/redirect')
def redirect_():
    return redirect(url_for('user.index'))