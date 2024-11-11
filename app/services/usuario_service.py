from models.usuario_model import Usuario
from repositories.usuario_repository import UsuarioRepository

class UsuarioService:

    def __init__(self, repository: UsuarioRepository):
        self.repository = repository

    def criar_usuario(self, nome : str, email : str, senha : str):
        try:
            usuario = Usuario(nome=nome, email=email, senha=senha)

            novo_usuario = self.repository.pesquisar_usuario_por_email(usuario.email)

            if novo_usuario:
                print("Usuario já cadastrado!")
                return
            
            self.repository.salvar_usuario(usuario)
            print("Usuario cadsatrado com sucesso!")
        except TypeError as erro:
            print(f"Erro ao salvar o usuário: {erro}")
        except Exception as erro: print(f"Ocorreu um erro inesperado: {erro}")

    
    def exibir_todos_usuarios(self):
        return self.repository.exibir_usuario()