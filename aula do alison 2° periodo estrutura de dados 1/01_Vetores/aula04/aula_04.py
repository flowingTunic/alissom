"""
Crie duas listas em python , uma para armazenar  o nome e outra lista para armazenar a idade de 5 pessoas. Posteriormente indique quias pessoas tem 18  anos ou mais e quantas sao menores de idade 
Ex:
jose, 10 anos 
Joaquim, 19 anos
jailton, 30 anos
Juarez, 5 anos
Joao 18 anos
--> sao maiores de idade: Joaquim, Jailton, Joao
--> sao menores de idade: Jose, Juarez
"""
ndp = 5
idade = []
nomes = []

for i in range (ndp):
    nomes.append(input("digite o nome: "))
    tmp = int(input(f"wdigite sua idade {nomes[i]} "))
    idade.append(tmp)

maiores = "--> sao maiores de idade: "
menores = "--> sao menores de idade: "
for j in range(len(idade)):
    if idade[j] >= 18:
        tmp = nomes[j]
        maiores = maiores + tmp + ", "
    else:
        tmp = nomes[j]
        menores = menores + tmp + ", "
print("="*35)
print(maiores[:-2])
print(menores[:-2])
