# Sistema de Biblioteca

Projeto simples em Python para controlar o acervo físico de uma biblioteca.

## Objetivo

O sistema ajuda a controlar um acervo físico, registrando livros, seus dados e o status de empréstimo.

## Arquivos do projeto

- main.py: contém o programa principal em Python.
- livros.csv: arquivo com os livros salvos em formato CSV.
- README.md: documentação do projeto.

## Requisitos

É preciso ter Python instalado.

## Como executar

```bash
python main.py
```

## Funcionalidades

- Cadastrar livro
- Listar livros
- Buscar por título ou autor
- Registrar empréstimo
- Registrar devolução
- Ordenar por título, autor ou ano

## Estrutura de um livro

Cada livro possui:

- ISBN
- título
- autor
- ano
- status

## Uso do CSV

Os dados ficam salvos em livros.csv. Quando o programa abre, ele lê esse arquivo. Quando você cadastra, empresta ou devolve um livro, ele salva as alterações de volta no CSV.

## Status dos livros

- Disponível: o livro pode ser emprestado.
- Emprestado: o livro está fora da biblioteca.

## Conceitos de Python usados

O programa usa:

- if, elif e else
- while
- listas
- dicionários
- funções
- leitura e escrita de arquivo com o módulo csv
