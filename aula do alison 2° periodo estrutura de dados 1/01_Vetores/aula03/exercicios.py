"""
faca um programa que leia o nome de 5 pessoas digitados pelo(a) usuario(a) e armazene em uma lista de nomes , no final imprima na tela uma mensagem de boas vindas para cada armazenado
EX:
nome = ["Turing","Ada","Linus", " Dijkstra","Berners-Lee"]
Seja bem vindo(a) Turing
Seja bem vindo(a) Ada
Seja bem vindo(a) Linus
Seja bem vindo(a) Dijkstra
Seja bem vindo(a) Berners-Lee
"""
nomes = []
total_nomes = 5 

for i in range (total_nomes):
    tmp = input(f"Digite 0 {i+1}° nome: ")
    nomes.append(tmp)
#print(nomes)
print("="*30)
for j in range(len(nomes)):
    print(f"Seja bem vindo(a) {nomes[j].upper()}")