"""
lista = simbolo []
lista -> ED Dinamica
      -> alterar conteudo
      -> adicionar / remover elemento
"""
print("="*40)
#lista removida
lista = [1,4,7,9]
print(lista)
print("="*40)
#remove o elemento da posição 1
del lista [1]
print(lista)
print("="*40)
#e para adicionar o elemento no final use .append 
lista.append(8)
print(lista)
print("="*40)
#para adicionar um elemento na lista escolhendo a posição use insert
lista.insert(1, 3)
print(lista)
print("="*40)
#para tirar um valor de uma variavel para outra use pop
valor = lista.pop(2)
print(valor)
print(lista)
print("="*40)
#o comando sort ordena a lista 
lista.sort()
print(lista)
print("="*40)

"""
tupla

é uma nomeclatura imutavel que serve para definir listas que voce nao quer que o valor seja alterado 

simbulo de criação () 
simbulo de acesso []

"""
print("="*40)
# ex
dias_semana = ("dom","seg","ter","qua","qui","sex","sab")
print(dias_semana)


