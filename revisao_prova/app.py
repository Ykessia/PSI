from database.config import start_db, destroy_db, session
from database.models import User, Livros
from flask import Flask, render_template, redirect

start_db()

app = Flask (__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro_livro')
def cadastro_livro():
    return render_template('livros.html')