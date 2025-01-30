from database import db

class Cliente(db.Model):
    __tablename__='Clientes'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]

class Veiculo(db.Model):
    __tablename__='Veiculos'
    id: Mapped[int] = mapped_column (primary_key=True)
    modelo:  Mapped[str]
    placa:  Mapped[str] = mapped_column(unique=True)

class Locacao(db.Model):
    __tablename__ = 'Locacoes'
    id: Mapped[int] = mapped_column(primary_key=True)
    cliente_id: Mapped[int] = mapped_column(db.ForeignKey('Clientes.id'), nullable=False)
    veiculo_id: Mapped[int] = mapped_column(db.ForeignKey('Veiculos.id'), nullable=False)

    cliente = db.relationship('Cliente', backref='locacoes')
    veiculo = db.relationship('Veiculo', backref='locacoes')
