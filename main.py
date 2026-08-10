import csv

livros = []


def carregar_livros():
    global livros
    livros = []

    with open("livros.csv", "r", encoding="utf-8", newline="") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            livros.append(
                {
                    "isbn": linha["isbn"],
                    "titulo": linha["titulo"],
                    "autor": linha["autor"],
                    "ano": linha["ano"],
                    "status": linha["status"],
                }
            )


def salvar_livros():
    with open("livros.csv", "w", encoding="utf-8", newline="") as arquivo:
        campos = ["isbn", "titulo", "autor", "ano", "status"]
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()

        for livro in livros:
            escritor.writerow(livro)


def cadastrar_livro():
    isbn = input("Digite o ISBN: ")
    titulo = input("Digite o título: ")
    autor = input("Digite o autor: ")
    ano = input("Digite o ano de publicação: ")

    livro = {
        "isbn": isbn,
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "status": "Disponível",
    }

    livros.append(livro)
    salvar_livros()
    print("Livro cadastrado com sucesso!")


carregar_livros()

while True:
    print("=" * 20)
    print("Sistema de Biblioteca")
    print("1. Cadastrar livro")
    print("2. Registrar empréstimo")
    print("3. Registrar devolução")
    print("4. Listar livros")
    print("5. Buscar livro")
    print("6. Ordenar livros")
    print("7. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_livro()
    elif opcao == "2":
        print("Funcionalidade ainda não implementada.")
    elif opcao == "3":
        print("Funcionalidade ainda não implementada.")
    elif opcao == "4":
        print("Funcionalidade ainda não implementada.")
    elif opcao == "5":
        print("Funcionalidade ainda não implementada.")
    elif opcao == "6":
        print("Funcionalidade ainda não implementada.")
    elif opcao == "7":
        break
    else:
        print("Opção inválida.")
