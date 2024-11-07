from flask import Flask, render_template

from user import bp
from livro import bp as bp_book
from emprestimo.emprestimo import bp_emprestimo

app = Flask(__name__)

app.register_blueprint(bp)
app.register_blueprint(bp_book)
app.register_blueprint(bp_emprestimo)

@app.route('/')
def index():
    return render_template('index.html')