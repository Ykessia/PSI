from flask import Flask, request, render_template, redirect, url_for, flash
# Importa os módulos necessários do Flask para criar o aplicativo web, lidar com requisições, renderizar templates e exibir mensagens flash

from flask_mysqldb import MySQL
# Importa a extensão Flask-MySQLdb para conectar o Flask ao MySQL

app = Flask(__name__)
# Cria uma instância da aplicação Flask

# Configuração do MySQL
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_PORT'] = '3306'
# Define o host e a porta do servidor MySQL. As linhas estão comentadas, indicando que essas configurações são padrão ou não necessárias neste caso.

app.config['MYSQL_USER'] = 'root'
# Define o nome de usuário para conectar ao banco de dados MySQL

app.config['MYSQL_PASSWORD'] = 'romerito'
# Define a senha para o usuário MySQL

app.config['MYSQL_DB'] = 'users'
# Define o nome do banco de dados que será utilizado

# Retornar os dados como dicionários
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
# Configura o cursor do MySQL para retornar os resultados das consultas como dicionários, onde as chaves são os nomes das colunas

mysql = MySQL(app)
# Cria uma instância do MySQL, conectando a aplicação Flask à configuração do MySQL

# Habilitar mensagens flash
app.config['SECRET_KEY'] = 'muitodificil'
# Define a chave secreta usada para proteger as sessões e as mensagens flash

@app.route('/')
def index():
    # Rota para a página inicial
    conn = mysql.connection.cursor()
    # Cria um cursor para executar consultas no banco de dados
    conn.execute("""SELECT * FROM users""")
    # Executa uma consulta SQL para selecionar todos os usuários da tabela "users"
    users = conn.fetchall()
    # Obtém todos os resultados da consulta
    conn.close()
    # Fecha o cursor para liberar recursos
    return render_template('pages/index.html', users=users)
    # Renderiza o template 'index.html' e passa a lista de usuários para o template

@app.route('/create', methods=['POST', 'GET'])
def create():
    # Rota para criar um novo usuário
    if request.method == 'POST':
        # Se o método da requisição for POST (submissão de formulário)
        email = request.form['email']
        senha = request.form['password']
        # Obtém os valores do formulário

        if not email:
            # Se o email não for fornecido
            flash('Email é obrigatório')
            # Exibe uma mensagem flash de erro
        else:
            conn = mysql.connection.cursor()
            # Cria um cursor para executar consultas no banco de dados
            conn.execute("INSERT INTO users(email, senha) VALUES (%s,%s)", (email, senha))
            # Executa uma consulta SQL para inserir um novo usuário na tabela "users"
            mysql.connection.commit()
            # Confirma as alterações no banco de dados
            conn.close()
            # Fecha o cursor para liberar recursos
            return redirect(url_for('index'))
            # Redireciona para a página inicial
    
    return render_template('pages/create.html')
    # Renderiza o template 'create.html' quando o método da requisição for GET (exibição do formulário)

@app.route('/<int:id>/edit', methods=['POST', 'GET'])
def edit(id):
    # Rota para editar um usuário específico com base no ID
    conn = mysql.connection.cursor()
    # Cria um cursor para executar consultas no banco de dados
    conn.execute('SELECT id, email, senha FROM users WHERE id = %s', (id,))
    # Executa uma consulta SQL para selecionar o usuário com o ID fornecido
    user = conn.fetchone()
    # Obtém o resultado da consulta (um único usuário)
    
    if user is None:
        # Se o usuário não for encontrado
        return redirect(url_for('error', message='Usuário Inexistente'))
        # Redireciona para a página de erro com uma mensagem
    
    if request.method == 'POST':
        # Se o método da requisição for POST (submissão de formulário)
        email = request.form['email']
        # Obtém o novo email do formulário
        
        conn.execute('UPDATE users SET email=%s WHERE id=%s', (email, id))
        # Executa uma consulta SQL para atualizar o email do usuário com o ID fornecido
        mysql.connection.commit()
        # Confirma as alterações no banco de dados
        conn.close()
        # Fecha o cursor para liberar recursos
        return redirect(url_for('index'))
        # Redireciona para a página inicial
    
    return render_template('pages/edit.html', user=user)
    # Renderiza o template 'edit.html' e passa o usuário para o template quando o método da requisição for GET (exibição do formulário de edição)

@app.route('/error')
def error():
    # Rota para exibir mensagens de erro
    error = request.args.get('message')
    # Obtém a mensagem de erro da URL
    return render_template('errors/error.html', message=error)
    # Renderiza o template 'error.html' e passa a mensagem de erro para o template
