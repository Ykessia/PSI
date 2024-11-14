from flask import Flask, request, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

app.config['SECRET_KEY'] = 'muitodificil'

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    senha: Mapped[str]

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    users = db.session.execute(db.select(User)).scalars()
    return render_template("pages/index.html", users=users)

@app.route('/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        email = request.form['email']
        senha= request.form['password']

        if not email:
            flash('Email é obrigatório')
        else:
            user = User(
            email=email,
            senha=senha,
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
    
    return render_template('pages/create.html')

@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):

    # obter informação do usuário
    user = db.get_or_404(User, id)

    if user == None:
        return redirect(url_for('error', message='Usuário Inexistente'))

    if request.method == 'POST':
        user.email = request.form['email']

        db.session.commit()
        return redirect(url_for('index'))
    
    return render_template('pages/edit.html', user=user)

@app.route('/error')
def error():
    error = request.args.get('message')
    return render_template('errors/error.html', message=error)