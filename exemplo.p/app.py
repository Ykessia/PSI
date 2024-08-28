from flask import Flask, render_template, request, redirect, url_for, flash, session, make_response

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Necessário para gerenciar sessões

# Dados de usuários em memória (substitua por um banco de dados em produção)
users_db = {}

@app.route('/')
def index():
    username = session.get('username')
    if username:
        return render_template('profile.html', username=username)
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users_db:
            flash('Usuário já existe!')
            return redirect(url_for('register'))
        
        users_db[username] = password
        flash('Registrado com sucesso! Faça login.')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if users_db.get(username) == password:
            session['username'] = username
            resp = make_response(redirect(url_for('index')))
            resp.set_cookie('username', username)
            return resp
        else:
            flash('Credenciais inválidas!')
            return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    resp = make_response(redirect(url_for('index')))
    resp.set_cookie('username', '', expires=0)
    return resp

if __name__ == '__main__':
    app.run(debug=True)