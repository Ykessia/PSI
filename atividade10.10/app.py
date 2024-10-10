from flask import Flask, render_template, redirect, url_for, request
import sqlite3

app= Flask(__name__)
def get_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template ('index.html')

@app.route('/cadastro', methods=['POST', 'GET'])
def cadastro():
    if request.method == 'POST':
        nome= request.form['nome']
        email = request.form['email']
        senha = request.form['senha']        
        conn = get_connection()
        conn.execute("INSERT INTO usuarios (nome, email, senha) VALUES (?, ?, ?)", (nome, email, senha))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('cadastro.html')
@app.route('/usuarios')
def usuarios():
    return render_template ('usuarios.html')
