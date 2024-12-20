from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import declarative_base
from app.config.database import db

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(150))
    email = Column(String(150))
    senha = Column(String(150))

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = self._verificar_nome_usuario(nome)
        self.email = self._verificar_email_usuario(email)
        self.senha = self._verificar_senha_usuario(senha)

    def _verificar_nome_usuario(self, nome):
        self._verificar_nome_invalido(nome)  
        self._verificar_nome_vazio(nome)    
        return nome

    def _verificar_email_usuario(self, email):
        self._verificar_email_invalido(email)
        self._verificar_email_vazio(email)
        return email

    def _verificar_senha_usuario(self, senha):
        self._verificar_senha_vazio(senha)
        self._verificar_senha_invalido(senha)
        return senha

    def _verificar_nome_vazio(self, nome):
        if nome == "":
            raise ValueError("É necessário preencher o NOME para prosseguir.")

    def _verificar_nome_invalido(self, nome):
        if not isinstance(nome, str):
            raise TypeError("ERRO! Nome invalido.")

    def _verificar_email_vazio(self, email):
        if email == "":
            raise ValueError("É necessário preencher o E-MAIL para prosseguir.")

    def _verificar_email_invalido(self, email):
        if not isinstance(email, str):
            raise TypeError("ERRO! E-mail invalido.")

    def _verificar_senha_vazio(self, senha):
        if senha == "":
            raise ValueError("É necessário preencher a senha para prosseguir.")

    def _verificar_senha_invalido(self, senha):
        if not isinstance(senha, str):
            raise TypeError("ERRO! Senha invalida.")

# Criação da tabela no banco de dados
Base.metadata.create_all(bind=db)