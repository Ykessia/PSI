from sqlalchemy import create_engine, Integer, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from sqlalchemy import select

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__='users'
    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    email: Mapped[str] = mapped_column(unique=True)
    books: Mapped[List['Book']] = relationship

    def __repr__(self):
        return f"(nome={self.nome},email={self.email})"

class Book(Base):
    __tablename__='books'
    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str]
    autor: Mapped[str] = mapped_column(ForeignKey('users.id'))

engine = create_engine('sqlite:///teste.db')
session = Session(bind=engine)

Base.metadata.create_all(engine)

# usuario = User(nome='kessia', email='opa@kessia')
# session.add(usuario)
# session.commit()

# sql = select(User)
# lista = session.execute(sql)
# for user in lista:
#     print(user)

sql2 = select(User).where(User.email == 'kessia@kessia')
resultado = session.execute(sql2)
print(resultado.all())

sql2 = select(User.email).where(User.email == 'kessia@kessia')
resultado = session.execute(sql2)
print(resultado.all())