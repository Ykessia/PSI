# Importa as classes e funções necessárias do Flask e sqlite3
from flask import Flask, url_for, request, render_template, flash, redirect
import sqlite3

# Cria uma instância da aplicação Flask
app = Flask(__name__)

# Função para obter a conexão com o banco de dados SQLite
def get_connection():
    # Conecta ao banco de dados SQLite chamado 'database.db'
    conn = sqlite3.connect('database.db')
    # Define a fábrica de linhas para retornar objetos de linha como dicionários
    conn.row_factory = sqlite3.Row
    return conn

# Rota para a página inicial ('/')
@app.route('/')
def index():
    # Obtém a conexão com o banco de dados
    conn = get_connection()
    # Executa uma consulta SQL para selecionar id e email dos usuários
    users = conn.execute('SELECT id, email FROM users').fetchall()
    # Fecha a conexão com o banco de dados
    conn.close()
    # Renderiza o template 'index.html' e passa a lista de usuários para ele
    return render_template('pages/index.html', users=users)

# Rota para criar um novo usuário ('/create')
@app.route('/create', methods=['GET', 'POST'])
def create():
    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        # Obtém os dados do formulário
        email = request.form['email']
        senha = request.form['password']
        # Verifica se o campo email está vazio
        if not email:
            # Exibe uma mensagem flash se o email não for fornecido
            flash('Email é obrigatório')
        else:
            # Obtém a conexão com o banco de dados
            conn = get_connection()
            # Executa uma consulta SQL para inserir um novo usuário
            conn.execute("INSERT INTO users (email, senha) VALUES (?, ?)", (email, senha))
            # Confirma a transação
            conn.commit()
            # Fecha a conexão com o banco de dados
            conn.close()
            # Redireciona para a página inicial após a inserção
            return redirect(url_for('index'))
    # Renderiza o template 'create.html' para o método GET
    return render_template('pages/create.html')

# Rota para editar um usuário existente ('/<int:id>/edit')
@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    # Define a consulta SQL para selecionar um usuário pelo id
    SELECT = "SELECT * FROM users WHERE id = ?"
    # Obtém a conexão com o banco de dados
    conn = get_connection()
    # Executa a consulta SQL para obter o usuário pelo id
    usuario = conn.execute(SELECT, (id,)).fetchone()
    # Fecha a conexão com o banco de dados
    conn.close()

    # Verifica se o usuário foi encontrado
    if usuario is None:
        # Retorna uma mensagem se o usuário não existir
        return "NÃO EXISTE"

    # Verifica se o método da requisição é POST
    if request.method == 'POST':
        # Obtém o novo email do formulário
        email = request.form['email']
        # Define a consulta SQL para atualizar o email do usuário
        UPDATE = "UPDATE users SET email = ? WHERE id = ?"
        # Obtém a conexão com o banco de dados
        conn = get_connection()
        # Executa a consulta SQL para atualizar o usuário
        conn.execute(UPDATE, (email, id))
        # Confirma a transação
        conn.commit()
        # Fecha a conexão com o banco de dados
        conn.close()
        # Redireciona para a página inicial após a atualização
        return redirect(url_for('index'))
    
    # Renderiza o template 'edit.html' para o método GET, passando o usuário para o template
    return render_template('pages/edit.html', user=usuario)
