"""
utilizando uma lista ou tupla faça um programa quue faça 5 perguntas para uma pessoa sobre um crime . As perguntas são:
a) "Telefonou para a vitima ? "
b) "Esteve no local do crime ? "
c) "Mora perto da vitima ? "
d) "Devia para a vitima ? "
e) "já trabalhou com a vitima ? "
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime . se a pessoa responder positivamente a2 questoes ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cumplice" e 5 como "Assassino", Caso contrario ele será classificado como "inocente".
"""

lista_perguntas = ("a: Telefonou para a vitima ? ","b: Esteve no local do crime ? ","c: Mora perto da vitima ? ","d: Devia para a vitima ? ","e: já trabalhou com a vitima ? ")
print("faça esse questionario para que possamos te liberar")
positivo = 0
for posicao in lista_perguntas:
    resposta = input(posicao + "sim ou Nao >>> ")
    if resposta.lower() == "sim":
        setpositivo = positivo + 1 
print("="*40)
if posicao == 2

