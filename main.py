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
    isbn = input("Digite o ISBN: ").strip()
    titulo = input("Digite o título: ").strip()
    autor = input("Digite o autor: ").strip()
    ano = input("Digite o ano de publicação: ").strip()

    if not isbn or not titulo or not autor or not ano:
        print("Preencha todos os campos.")
        return

    for livro in livros:
        if livro["isbn"] == isbn:
            print("ISBN já cadastrado.")
            return

    try:
        int(ano)
    except ValueError:
        print("O ano deve ser numérico.")
        return

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


def listar_livros():
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros:
        print("-" * 20)
        print("ISBN:", livro["isbn"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Status:", livro["status"])


def buscar_livro():
    termo = input("Digite um título ou autor para buscar: ").strip().lower()

    if not termo:
        print("Digite algo para buscar.")
        return

    encontrados = []
    for livro in livros:
        titulo = livro["titulo"].lower()
        autor = livro["autor"].lower()

        if termo in titulo or termo in autor:
            encontrados.append(livro)

    if not encontrados:
        print("Nenhum livro encontrado.")
        return

    for livro in encontrados:
        print("-" * 20)
        print("ISBN:", livro["isbn"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Status:", livro["status"])


def alterar_status_livro(acao):
    termo = input("Digite o título ou autor do livro: ").strip().lower()

    if not termo:
        print("Digite algo para localizar o livro.")
        return

    encontrado = None
    for livro in livros:
        titulo = livro["titulo"].lower()
        autor = livro["autor"].lower()

        if termo in titulo or termo in autor:
            encontrado = livro
            break

    if encontrado is None:
        print("Livro não encontrado.")
        return

    print("Livro encontrado:")
    print("ISBN:", encontrado["isbn"])
    print("Título:", encontrado["titulo"])
    print("Autor:", encontrado["autor"])
    print("Ano:", encontrado["ano"])
    print("Status:", encontrado["status"])

    if acao == "emprestar":
        if encontrado["status"] == "Disponível":
            encontrado["status"] = "Emprestado"
            salvar_livros()
            print("Empréstimo registrado.")
        else:
            print("Este livro já está emprestado.")
    else:
        if encontrado["status"] == "Emprestado":
            encontrado["status"] = "Disponível"
            salvar_livros()
            print("Devolução registrada.")
        else:
            print("Este livro já está disponível.")


def ordenar_livros():
    print("1. Ordenar por título")
    print("2. Ordenar por autor")
    print("3. Ordenar por ano de publicação")
    criterio = input("Escolha uma opção: ")

    if criterio == "1":
        livros_ordenados = sorted(livros, key=lambda livro: livro["titulo"].lower())
    elif criterio == "2":
        livros_ordenados = sorted(livros, key=lambda livro: livro["autor"].lower())
    elif criterio == "3":
        livros_ordenados = sorted(livros, key=lambda livro: int(livro["ano"]))
    else:
        print("Opção inválida.")
        return

    if not livros:
        print("Nenhum livro cadastrado.")
        return

    for livro in livros_ordenados:
        print("-" * 20)
        print("ISBN:", livro["isbn"])
        print("Título:", livro["titulo"])
        print("Autor:", livro["autor"])
        print("Ano:", livro["ano"])
        print("Status:", livro["status"])


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
        alterar_status_livro("emprestar")
    elif opcao == "3":
        alterar_status_livro("devolver")
    elif opcao == "4":
        listar_livros()
    elif opcao == "5":
        buscar_livro()
    elif opcao == "6":
        ordenar_livros()
    elif opcao == "7":
        break
    else:
        print("Opção inválida.")
