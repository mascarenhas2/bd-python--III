from services.usuario_service import UsuarioService
from repositories.usuario_repository import UsuarioRepository
from config.database import Session
import os

def main():
    session = Session()
    repository = UsuarioRepository(session)
    service = UsuarioService(repository)

    # Solicitando dados para o usuário

    # MENU DE OPÇÕES
    def menu():
        print("\t - MENU DE OPÇÕES - ")
        print("""  \t1 - Adicionar usuário. 
            2 - Pesquisar um usuário. 
            3 - Atualizar dados de um usuário.
            4 - Excluir usuário.
            5 - Exibir todos os usuários cadastrados
            0 - Sair.""")
        
    while True:
        menu()
        opcao = int(input("\nDigite a opção desejada: "))

        match(opcao):
            case 1:
                print("\n - Adicionando usuário -")
                nome = input("Digite o seu nome: ")
                email = input("Digite o seu email: ")
                senha = input("Digite o seu senha: ")

                service.criar_usuario(nome=nome, email=email, senha=senha)
                break

            case 2:
                print("\n - Pesquisa por email -")
                email = input("Digite o email desejado: ")
                lista_email = repository.pesquisar_usuario_por_email(email=email)
                for usuario in lista_email:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                break

            case 3:
                print("\n - Atualização de dados -")
                break

            case 4:
                print("\n - Excluir usuário -")
                nome = input("Digite o nome: ")
                email = input("Digite o email: ")
                senha = input("Digite o senha: ")

                repository.excluir_usuario()
                break

            case 5:
                print("\n - Exibir todos os usuários cadastrados -")
                lista_usuarios = service.listar_todos_usuarios()
                for usuario in lista_usuarios:
                    print(f"Nome: {usuario.nome} - Email: {usuario.email} - Senha: {usuario.senha}")
                break

            case 0:
                break

if __name__ == "__main__":
    os.system("cls || clear")
    main()