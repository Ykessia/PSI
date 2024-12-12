from flask import Flask, render_template, request, make_response, url_for, redirect

app = Flask(__name__)

mensagens = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        resposta = make_response(redirect(url_for('mensagem')))
        resposta.set_cookie('nome', nome, max_age=60 * 60 * 24)
        return resposta
    nome = request.cookies.get('nome')
    return render_template('registrar.html', nome=nome)

@app.route('/mensagem', methods=['GET', 'POST'])
def mensagem():
    if request.method == 'POST':
        mensagem = request.form['mensagem']
        mensagens.append(mensagem) 
        resposta = make_response(redirect(url_for('mensagem')))
        resposta.set_cookie('mensagem', mensagem, max_age=60 * 60 * 24)
        return resposta
    nome = request.cookies.get('nome')
    mensagem = request.cookies.get('mensagem')
    return render_template('mensagem.html', nome=nome, mensagem=mensagem, mensagens=mensagens)
    
    
