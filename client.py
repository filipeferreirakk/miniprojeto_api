import requests

BASE_URL = "http://127.0.0.1:5000"


def checar_status():
    resposta = requests.get(f"{BASE_URL}/health")
    print("Status do servidor:", resposta.json())


def listar_livros():
    autor = input("Filtrar por autor (enter para listar todos): ")
    parametros = {}
    if autor:
        parametros["autor"] = autor
    resposta = requests.get(f"{BASE_URL}/books", params=parametros)
    livros = resposta.json()
    if not livros:
        print("Nenhum livro encontrado")
        return
    print("\nLivros:")
    for livro in livros:
        print(f"  [{livro['id']}] {livro['titulo']} - {livro['autor']} ({livro['ano']})")


def buscar_livro():
    book_id = input("Id do livro: ")
    resposta = requests.get(f"{BASE_URL}/books/{book_id}")
    if resposta.status_code == 404:
        print("Livro nao encontrado")
        return
    livro = resposta.json()
    print(f"{livro['titulo']} de {livro['autor']}, {livro['ano']}")


def cadastrar_livro():
    titulo = input("Titulo: ")
    autor = input("Autor: ")
    ano = int(input("Ano: "))
    payload = {"titulo": titulo, "autor": autor, "ano": ano}
    resposta = requests.post(f"{BASE_URL}/books", json=payload)
    print("Cadastrado:", resposta.json())


def atualizar_livro():
    book_id = input("Id do livro a atualizar: ")
    titulo = input("Novo titulo: ")
    autor = input("Novo autor: ")
    ano = int(input("Novo ano: "))
    payload = {"titulo": titulo, "autor": autor, "ano": ano}
    resposta = requests.put(f"{BASE_URL}/books/{book_id}", json=payload)
    if resposta.status_code == 404:
        print("Livro nao encontrado")
        return
    print("Atualizado:", resposta.json())


def remover_livro():
    book_id = input("Id do livro a remover: ")
    resposta = requests.delete(f"{BASE_URL}/books/{book_id}")
    if resposta.status_code == 404:
        print("Livro nao encontrado")
        return
    print("Removido com sucesso")


def menu():
    while True:
        print("\n1 - Listar livros")
        print("2 - Buscar por id")
        print("3 - Cadastrar")
        print("4 - Atualizar")
        print("5 - Remover")
        print("0 - Sair")
        opcao = input("Opcao: ")
        if opcao == "1":
            listar_livros()
        elif opcao == "2":
            buscar_livro()
        elif opcao == "3":
            cadastrar_livro()
        elif opcao == "4":
            atualizar_livro()
        elif opcao == "5":
            remover_livro()
        elif opcao == "0":
            break
        else:
            print("Opcao invalida")


checar_status()
menu()