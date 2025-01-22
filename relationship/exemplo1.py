from sqlalchemy import create_engine, Table, Column, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, mapped_column, Mapped, relationship
from typing import List

engine = create_engine('sqlite:///exemplo1.db')
session = Session(bind=engine)


class Base(DeclarativeBase):
    pass

estudantes_cursos = Table(
    'estudantes_cursos',
    Base.metadata,
    Column('estudantes_id', ForeignKey('estudantes.id'), primary_key=True),
    Column('cursos_id', ForeignKey('cursos.id'), primary_key=True)
)

#relacionamento NxN
class Estudante(Base):
    __tablename__='estudantes'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    cursos: Mapped[List['Curso']] = relationship('Curso', secondary=estudantes_cursos, back_populates='estudantes')

class Curso(Base):
    __tablename__='cursos'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    estudantes = relationship('Estudante', secondary=estudantes_cursos, back_populates='cursos')

# CRIAÇÃO DO BANCO
Base.metadata.create_all(bind=engine)

info = Curso (nome='informática')

x = Estudante(nome='evelyn')
y = Estudante(nome='marcella')
z = Estudante(nome='poliana')

session.add(info)
session.add_all([x,y,z])
session.commit()

#####

info = session.query(Curso).get(1)
info.estudantes.append(x)
session.commit()

info.estudantes.remove(x)
session.commit()