from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import List

#mapeamento declarativo
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(String(50), unique=True)
    lista_recipes:Mapped[List["Livros"]] = relationship('Livros', backref='usuario')

    def __repr__(self) -> str:
        return f"(User={self.name})"
    
class Livros(Base):
    __tablename__='livros'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    user_id:Mapped[int] = mapped_column(ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f"(Livros={self.name})"
    
class Emprestimo(Base):
    __tablename__='emprestimo'