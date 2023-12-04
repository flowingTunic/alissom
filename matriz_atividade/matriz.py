dados_pessoas = []

for _ in range(10):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    dados_pessoas.append((nome, idade))
idade_mais_nova = float('inf')
pessoa_mais_nova = None

for nome, idade in dados_pessoas:
    if idade < idade_mais_nova:
        idade_mais_nova = idade
        pessoa_mais_nova = nome
print(f"\nA pessoa mais nova é {pessoa_mais_nova} com {idade_mais_nova} anos.")