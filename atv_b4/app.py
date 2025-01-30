from flask import request, render_template, redirect, url_for
from database import db
from models import Cliente, Veiculo, Locacao

app = Flask(__name__)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cadastrar_cliente', methods=['GET', 'POST'])
def cliente():
    if request.method == 'POST':
        nome = request.form['nome']
        novo_cliente = Cliente(nome=nome)
        db.session.add(novo_cliente)
        db.session.commit()
        return redirect(url_for('index'))
    clientes = Cliente.query.all()
    return render_template('cliente.html', clientes=clientes)

@app.route('/cadastrar_veiculo', methods=['GET', 'POST'])
def veiculo():
    if request.method == 'POST':
        modelo = request.form['modelo']
        placa = request.form['placa']
        novo_veiculo = Veiculo(modelo=modelo, placa=placa)
        db.session.add(novo_veiculo)
        db.session.commit()
        return redirect(url_for('index'))
    veiculos = Veiculo.query.all()
    return render_template('veiculo.html', veiculos=veiculos)

@app.route('/cadastrar_locacao', methods=['GET', 'POST'])
def locacao():
    if request.method == 'POST':
        cliente_id = request.form['cliente_id']
        veiculo_id = request.form['veiculo_id']
        nova_locacao = Locacao(cliente_id=cliente_id, veiculo_id=veiculo_id)
        db.session.add(nova_locacao)
        db.session.commit()
        return redirect(url_for('index'))
    clientes = Cliente.query.all()
    veiculos = Veiculo.query.all()
    locacoes = Locacao.query.all()
    return render_template('locacao.html', clientes=clientes, veiculos=veiculos, locacoes=locacoes)
