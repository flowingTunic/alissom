"""
vamos supor que precisamos criar um programa para cadastrar alunos em uma escola , armazenando informaçoes como nome ,idade e nota. podemos utiliizar um dicionario para representar cada aluno , onde a chave sera o numero de matricula e o valor sera outro dicionario contendo as informações do aluno.
"""
import json

def carregar_produtos():
    try:
        with open('produtos.json', 'r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_produtos(produtos):
    with open('produtos.json', 'w') as arquivo:
        json.dump(produtos, arquivo, indent=4)

def inserir_produto(produtos):
    codigo = input("Digite o código do produto: ")
    if codigo in produtos:
        print("Código de produto já existe.")
    else:
        nome = input("Digite o nome do produto: ")
        preco = float(input("Digite o preço do produto: "))
        disponivel = True  # Por padrão, um novo produto é disponível
        produtos[codigo] = {
            "nome": nome,
            "quantidade": 0,
            "preco": preco,
            "disponivel": disponivel
        }
        print("Produto adicionado com sucesso.")

def consultar_produto(produtos):
    codigo = input("Digite o código do produto: ")
    if codigo in produtos:
        produto = produtos[codigo]
        print(f"Nome: {produto['nome']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: {produto['preco']}")
        print(f"Disponível: {produto['disponivel']}")
    else:
        print("Produto não encontrado.")

def consultar_todos_produtos(produtos):
    if produtos:
        for codigo, produto in produtos.items():
            print(f"Código: {codigo}")
            print(f"Nome: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: {produto['preco']}")
            print(f"Disponível: {produto['disponivel']}")
            print("-" * 30)
    else:
        print("Não há produtos cadastrados.")

def alterar_preco(produtos):
    codigo = input("Digite o código do produto: ")
    if codigo in produtos:
        novo_preco = float(input("Digite o novo preço: "))
        produtos[codigo]['preco'] = novo_preco
        print("Preço do produto atualizado com sucesso.")
    else:
        print("Produto não encontrado.")

def aplicar_acrescimo_desconto(produtos):
    percentual = float(input("Digite o percentual de acréscimo (+) ou desconto (-): "))
    for produto in produtos.values():
        produto['preco'] *= (1 + percentual / 100)
    print("Acréscimo ou desconto aplicado com sucesso.")

def excluir_produto(produtos):
    codigo = input("Digite o código do produto que deseja excluir: ")
    if codigo in produtos:
        del produtos[codigo]
        print("Produto excluído com sucesso.")
    else:
        print("Produto não encontrado.")

def main():
    produtos = carregar_produtos()

    while True:
        print("\n=== Menu de Opções ===")
        print("1. Inserir um novo produto")
        print("2. Consultar um produto por código")
        print("3. Consultar todos os produtos")
        print("4. Alterar o preço de um determinado produto")
        print("5. Aplicar um acréscimo ou desconto em todos os produtos")
        print("6. Excluir um registro de produto")
        print("7. Sair do programa")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_produto(produtos)
        elif opcao == '2':
            consultar_produto(produtos)
        elif opcao == '3':
            consultar_todos_produtos(produtos)
        elif opcao == '4':
            alterar_preco(produtos)
        elif opcao == '5':
            aplicar_acrescimo_desconto(produtos)
        elif opcao == '6':
            excluir_produto(produtos)
        elif opcao == '7':
            salvar_produtos(produtos)
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
