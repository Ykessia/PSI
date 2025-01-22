from sqlalchemy import create_engine, Table, Column, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, relationship
from typing import List

engine = create_engine('sqlite:///exemplo2.db')
session = Session(bind=engine)


class Base(DeclarativeBase):
    pass


#relacionamento 1xN
class Estudante(Base):
    __tablename__='estudantes'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    curso_id: Mapped[int] = mapped_column(ForeignKey('cursos.id'), nullable=True)

    def __repr__(self) -> str:
        return f"Estudante={self.nome}"

class Curso(Base):
    __tablename__='cursos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    #back_populates
    estudantes: Mapped[List['Estudante']] = relationship('Estudante', backref='curso')

    def __repr__(self) -> str:
        return f"Curso={self.nome}"

# CRIAÇÃO DO BANCO
Base.metadata.create_all(bind=engine)

info = Curso (nome='informática')

x = Estudante(nome='evelyn', curso_id = 1)
y = Estudante(nome='marcella', curso_id=1)
z = Estudante(nome='poliana')

# session.add(info)
# session.add_all([x,y,z])
# session.commit ()


#select * from cursos where id = 1
curso = session.query(Curso).get(1)
print(curso)

print(curso.estudantes)

estudante= session.query(Estudante).get(1)
print(str(estudante) + " estuda " + str(estudante.curso))